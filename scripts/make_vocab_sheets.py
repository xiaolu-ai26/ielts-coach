#!/usr/bin/env python3
"""Render paired four-column A4 vocabulary sheets from verified JSON records."""
import argparse
import json
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor

def render(data, out):
    items=data['items']
    if not items:
        raise ValueError('items must not be empty')
    ids=set()
    for item in items:
        if type(item.get('id')) is not int or item['id'] in ids:
            raise ValueError('id must be a unique integer')
        ids.add(item['id'])
        for key in ('word','hint'):
            if not isinstance(item.get(key),str) or not item[key].strip() or '\n' in item[key]:
                raise ValueError(f'{key} must be non-empty single-line text')
        if pdfmetrics.stringWidth(f"{item['id']:02d}  {item['word']}",'Helvetica',10.5)>135:
            raise ValueError(f"word too wide at id {item['id']}; use a shorter display form or adapt layout")
        if pdfmetrics.stringWidth(item['hint'],'Helvetica',8)>135:
            raise ValueError(f"hint too wide at id {item['id']}; shorten it before rendering")
    title=data.get('title','词汇手写表')
    source=data.get('source','用户提供材料；提示为AI补充')
    pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
    if pdfmetrics.stringWidth(title,'STSong-Light',19)>400 or pdfmetrics.stringWidth(source,'STSong-Light',8)>535:
        raise ValueError('title or source is too wide; shorten display labels')
    out.mkdir(parents=True,exist_ok=True)
    W,H=A4; margin=30; total=W-60; widths=[147,total/2-147,147,total/2-147]
    paths=[]
    for hints,label,name in [(False,'基础版','vocabulary-basic.pdf'),(True,'AI提示版','vocabulary-hints.pdf')]:
        path=out/name;c=canvas.Canvas(str(path),pagesize=A4);c.setTitle(title+' / '+label)
        for start in range(0,len(items),50):
            batch=items[start:start+50];left=min(25,len(batch))
            c.setFont('STSong-Light',19);c.drawString(margin,H-37,title+' / '+label)
            c.setFont('STSong-Light',10);c.drawString(margin,H-59,'日期：____________  批次：____________  昨日复习 / 今日新词')
            c.setFont('STSong-Light',9);c.drawString(margin,H-77,'看英文，手写中文；先左后右。'+('小字为AI提示，不含中文答案。' if hints else '只做英译中，意思正确即可。'))
            top=H-96;c.setFillColor(HexColor('#E9EDF2'));c.rect(margin,top-25,total,25,fill=1,stroke=0)
            x=margin
            for header,width in zip(['英文','中文意思','英文','中文意思'],widths):
                c.setFillColor(HexColor('#101820'));c.setFont('STSong-Light',11);c.drawString(x+7,top-17,header);x+=width
            y=top-25
            for i in range(25):
                x=margin
                for j,width in enumerate(widths):
                    c.setStrokeColor(HexColor('#A6AFBA'));c.setLineWidth(.45);c.rect(x,y-25.5,width,25.5,stroke=1,fill=0)
                    if j in (0,2):
                        k=i+(25 if j==2 else 0)
                        if k<len(batch):
                            item=batch[k];c.setFillColor(HexColor('#111111'));c.setFont('Helvetica',10.5)
                            c.drawString(x+6,y-(11 if hints else 16),f"{item['id']:02d}  {item['word']}")
                            if hints:
                                c.setFont('Helvetica',8);c.setFillColor(HexColor('#555555'));c.drawString(x+6,y-21,item['hint'])
                    x+=width
                y-=25.5
            c.setFillColor(HexColor('#444444'));c.setFont('STSong-Light',8)
            c.drawString(margin,42,source)
            c.drawString(margin,28,f'第 {start//50+1} 页 / 本页 {len(batch)} 词 / A4竖向，实际大小打印；提示回忆与独立回忆分开记录。')
            c.showPage()
        c.save();paths.append(str(path))
    return paths

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input',required=True,type=Path);p.add_argument('--output-dir',required=True,type=Path)
    args=p.parse_args();data=json.loads(args.input.read_text(encoding='utf-8'))
    print(json.dumps({'files':render(data,args.output_dir),'word_count':len(data['items'])},ensure_ascii=False))
if __name__=='__main__':main()
