# 来源与借鉴边界

检索日期：2026-10-21。以下是维护入口；规则变化时读原页，不能把本文日期当成永久有效保证。

## 官方

- [考试类型](https://ielts.org/take-a-test/test-types)：区分 Academic、General Training 和其他用途。
- [Academic 免费样题](https://ielts.org/take-a-test/preparation-resources/sample-test-questions/academic-test)：可取得题目及配套材料。A/G 听说相同，读写不同。
- [评分解释](https://ielts.org/take-a-test/your-results/ielts-scoring-in-detail)：总分、四维评分、原始分换算的版本差异；页面链接到最新 Band Descriptors。
- [口语结构与评价](https://ielts.org/news-and-insights/demystifying-the-ielts-speaking-test)：三部分及评分维度。
- [Academic 写作](https://ielts.org/take-a-test/test-types/ielts-academic-test/ielts-academic-format-writing)、[General Training 写作](https://ielts.org/take-a-test/test-types/ielts-general-training-test/ielts-general-training-format-writing)：任务、字数、时间及权重。
- [ChatGPT Voice](https://help.openai.com/en/articles/20001274-chatgpt-voice)：语音能力和可用性。此 Skill 不保证特定账户、客户端的入口、额度或文件加载能力。
- [豆包功能说明](https://www.doubao.com/legal/feature_intro)、[豆包记忆说明](https://www.doubao.com/legal/memory_faq)：语音交互及通话文本说明。实际入口以客户端为准，未在本次任务中做真人通话测试。

## 现有 Skill

仅参考公开结构和方法，本文独立编写，没有复制对方实现或打包对方题库。

1. [Shearersxy/IELTS-SpeakingSkill](https://github.com/Shearersxy/IELTS-SpeakingSkill/blob/main/ielts-speaking/SKILL.md)：参考个性化素材、题目状态和间隔复习。没有沿用其固定目标分数，也不把润色答案当作学生实际能力。
2. [KaichenCurry/ielts-speaking-ai](https://github.com/KaichenCurry/ielts-speaking-ai/blob/main/SKILL.md)：参考模考结束后集中反馈、原句纠错记录。未沿用其 Notion 数据库、供应商或固定题数，不把各 Part 分数平均当作官方口语计分；网页还提示 frontmatter 解析错误，因此不直接安装。

两者主要覆盖口语；本 Skill 自行补充听读、写作、备考规划及跨平台续接。后续若直接复用第三方文件，先检查许可证与依赖。

## 扩展调研后的取舍

以下均阅读了仓库说明及相应入口文件，属于源文件调研，未安装和运行其第三方服务。星数与作者提分自述不作为有效性证据。

- [YANZHANLIN/ielts-claude-skills](https://github.com/YANZHANLIN/ielts-claude-skills)：参考按题型定位和同义替换证据；不沿用“阅读不考英语水平”或只凭首尾句定主旨的简化判断。
- [xuchi-0808/ielts-claude-skills](https://github.com/xuchi-0808/ielts-claude-skills)：参考学习记录、错因聚合、词汇复习、诊断计划。它是前者的扩展，不能作为两份独立有效性验证。没有复制 CLI 或承诺模板中的固定进步日期。
- [AaronL725/ielts-writing-review-skills](https://github.com/AaronL725/ielts-writing-review-skills)：参考原稿定位批注与改稿隔离；不强制默认 Word、特定教师身份、四段作文或固定目标分。
- [orzcls/PersonaLingo](https://github.com/orzcls/PersonaLingo)：参考通过问答挖掘真实个人素材与素材来源；不要求 MBTI，不为简单口语练习增加完整画像流水线。
- [Vera-2334/ielts-speaking-tutor](https://github.com/Vera-2334/ielts-speaking-tutor)：参考问题分析和回答展开；不沿用“同一动词不能重复”等机械规则，不给生成的文本评发音，不把示例词数与秒数强绑定。
- [Jobo16/ielts-buddy](https://github.com/Jobo16/ielts-buddy)：参考把材料、原始作答、修订和数据接口分开；它的外部平台能力依赖账号和权限，未接入本 Skill，不把仓库公开等同于题库免费可用。
- [JackLee992/ielts-prep-skill](https://github.com/JackLee992/ielts-prep-skill)：参考诊断/专项/复盘/模拟/恢复分流及续接档案；不替用户猜机构门槛或承诺单科重考可被接收。
- [yuy879143-coder/ielts-claude-skills](https://github.com/yuy879143-coder/ielts-claude-skills)：作为覆盖范围候选查看公开介绍；作者的“两个月7.5”自述未独立核实，不作为学习结果证据，也未直接采用其实现。

由这些取舍补充 intake-planning.md、materials.md、worked-examples.md 和 assets/study-record.md。当前版本仍为教学流程与记录工具；真实声学评分、真人持续训练和官方评分校准尚未验证。
