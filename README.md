# CET-6 Review Skill

面向 Codex 的大学英语六级深度复盘 Skill。它不是商业产品，也不承诺替代教师或官方阅卷；重点是把一道题复盘成可复核的证据链、逻辑断点、干扰项机制和可迁移训练。

## 快速使用

```text
阅读·出题人视角分析·中文背景
阅读·中文极简
阅读·溯源
语篇填词
作文·评分
翻译·训练
复盘
```

如果用户只提交六级试卷、文章或某一道题，Skill 自动进入“深度训练”闭环：答案隔离分析 → 答案核对 → 原文证据 → 题型/逻辑断点 → 命题行为 → 碎片化变式题 → 错误复盘。用户不必重复说明学习背景；短命令只用于选择增强模式。答案隔离仅用于内部降低锚定偏差，不向用户展示模型盲答选项；中文式刷题只有在用户明确调用时才放到最后输出。

当前目录是第一版骨架，详细规则按需加载。它不包含未经授权的真题、教辅或外刊全文。

工作区当前已有 `research-data` 中 2015–2025 年 69 套公开页面答案索引和选项分布分析（2020 年 6 月该站点未提供页面）。2015 年只作历史对照；2016 年以后是主训练范围，2019 年以后提高近年风格权重。2014 年及更早的候选站点已记录，但尚未通过完整性、答案来源和许可核验，详见 [corpus/2016年前材料检索记录.md](corpus/2016年前材料检索记录.md)。该索引标记为公开参考答案，不自动视为官方答案。若用户提供官方答案文件，将按“官方候选 → 发布链/版本/哈希 → 至少两个独立来源逐题交叉核验”的流程升权。

内部答案隔离校验记录见 [corpus/blind-sample-2025-12.md](corpus/blind-sample-2025-12.md)。普通用户输出不展示模型的盲答选项；这些记录只用于发现证据分歧和校准 Skill，不构成官方能力认证。

随机实测与语篇填词压力测试见 [corpus/演示-2021-12-2-阅读47.md](corpus/演示-2021-12-2-阅读47.md) 和 [corpus/演示-语篇填词-用户词表-001.md](corpus/演示-语篇填词-用户词表-001.md)。

GitHub 同类项目检索见 [corpus/GitHub相关Skill检索记录.md](corpus/GitHub相关Skill检索记录.md)。模型能否运行与能否稳定达到目标质量是两件事，评估门槛见 [modules/model_compatibility.md](modules/model_compatibility.md)。

已经确认 GitHub 上存在同类 Skill、题库和 DeepSeek 接入项目；本项目的定位是个人开源的深度复盘流程，而不是宣称“市场首个”。模型/API 价格口径见 [modules/cost_comparison.md](modules/cost_comparison.md)。

逐项功能状态见 [corpus/功能实现审计.md](corpus/功能实现审计.md)。当前最主要的未完成项是三方同配置实测、大规模语篇填词唯一性回测、作文/翻译多人标注校准，以及第三方题库再分发授权。

竞争不能靠宣传保证；比较方法见 [corpus/竞争基准方案.md](corpus/竞争基准方案.md)。在完成冻结测试集和同模型对照前，本项目不声称击败任何 GitHub Skill。

蒙题策略不会默认插入每次讲解。只有用户说出“蒙题/选项分布/熵”，或题目被识别为高难、低得分率、争议题时，才展示统计弱决策和低权重小策略；复杂题自动进入三次训练。

官方来源和版本判断见 [modules/official_sources.md](modules/official_sources.md)。写作/翻译的人类评分标准、官方图片样卷页码与校准协议见 [modules/human_rubric.md](modules/human_rubric.md)、[modules/anchor_samples.md](modules/anchor_samples.md)、[modules/writing_calibration.md](modules/writing_calibration.md) 和 [modules/translation_calibration.md](modules/translation_calibration.md)。

官方 2016 修订版大纲同时公开了五档总体印象评分标准和六级作文、翻译评分样卷；Skill 只登记来源 URL、页码、哈希和分析元数据，不把整套图片或受版权保护的题目全文打包再分发。公开 GitHub 项目可作为实现对照，但没有经过官方背书或可核验的人评校准时，不得当成有效性证明。

评分资料索引见 [human-sources.json](human-sources.json)。它区分“可公开访问”“可引用/分析”和“可再分发”三种权限：网页或 PDF 能打开，不等于允许把整套图片、作文或数据集复制进另一个仓库。公开论文只作为方法参考，非 CET-6 证据时会明确标注。

## 许可状态

当前仓库附带明确的开源许可证文件。无论采用何种许可证，第三方真题、教辅、外刊和音频的版权都不随 Skill 一并获得。
