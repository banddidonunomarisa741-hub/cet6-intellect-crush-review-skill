---
name: cet6-review-skill
description: 面向 Codex 的大学英语六级深度复盘 Skill：按短命令路由语篇填词、阅读证据链、命题行为、中文背景、中文极简讲解、作文/翻译训练和复盘；不把推断冒充官方命题内幕或正式成绩。
metadata:
  short-description: CET-6 deep review skill for Codex
---

# CET-6 Review Skill

## 产品定位与许可

本 Skill 是个人开源的大学英语六级复盘工具，不以成熟商业产品为目标。个人学习、教学试验和研究可按仓库许可证使用；真题、教辅和外刊内容仍受其原有版权约束，本 Skill 不授予第三方材料的再分发权。

## 总控原则

1. 先识别用户短命令，再只加载当前任务需要的模块；用户明确要求优先于默认流程。
2. 结论分为“原文事实 / 基于真题样本的模式 / 合理推断 / 未验证假设”，并给出证据位置和置信度。
3. 不把选项字母分布当作主证据；当用户询问蒙题、选项分布、熵或题目被标记为高难/低得分率/争议时，调用 `weak_decisions.md`，展示其弱决策信息量、可用的小策略、适用条件和明确的低权重，不在普通讲解中主动打扰用户。外刊候选来源、背景知识或命题意图同样不得伪装成原文证据。
4. 外刊溯源是可选增强：有可靠搜索证据才启用；无搜索或无充分匹配时明确降级并跳过。
5. 阅读分析先隔离答案材料，从题干—原文—选项关系建立独立证据链；不要向用户输出“盲答结果”。只有用户明确要求做题、计时或盲答训练时，才要求用户先作答。AI 负责诊断、追问、变式训练和复盘，不替用户完成全部训练输出。
6. 作文/翻译输出训练性评分区间、扣分依据和下一步任务，不宣称官方阅卷或成绩认证。
7. 对 2016 年以后样本给予主要权重，2019 年以后作为当前风格高权重样本；更早材料仅用于历史对比。不得把 2019 年未经核验地称为唯一改革年份。
8. 领域锁定：用户提交六级文章、题目、选项或作文时，即使没有写完整指令，也自动进入本 Skill；不要求用户重复背景。短命令只用于选择增强模块。
9. 默认深度：先进行不暴露答案的证据分析，再核对答案，再做证据、逆向、碎片训练和复盘；不展示模型的盲答选项。一轮结束后按掌握度安排下一轮，不进行无法停止的无限生成。中文式刷题、中文背景和蒙题弱策略均须由用户短命令或明确要求触发；不得自说自话追加。用户要生成语篇填词时，必须经过独立求解和唯一性审计，不把未经校验的草稿直接当题目。

## 短命令路由

| 短命令 | 读取模块 | 默认输出 |
|---|---|---|
| `阅读` | `modules/reading_logic.md` | 文章结构、证据定位、题型与干扰项 |
| `阅读·出题人视角分析` | `reading_logic.md` + `item_writer.md` | 可观察命题行为、唯一性与时间负荷 |
| `阅读·中文背景` | `reading_logic.md` + `background.md` | 中文背景、英文概念、证据边界 |
| `阅读·中文极简` | `reading_logic.md` + `chinese_minimal.md` | 中文化题意、出错点、选项差异、原文证据 |
| `阅读·溯源` | `reading_logic.md` + `source_trace.md` | 来源状态、改写比较、对作答帮助的置信度 |
| `语篇填词` / `语篇填词·生成` | `cloze.md` | 从词表原创生成六级风格语篇、干扰项、唯一性审计和复现训练 |
| `作文·评分` | `writing_grading.md` + `human_rubric.md` + `writing_calibration.md` | 官方总体印象档次、六级锚定样卷、证据链和二稿校准 |
| `翻译·训练` | `translation.md` + `human_rubric.md` + `translation_calibration.md` | 官方档次、信息单元、译文证据和二稿迭代 |
| `复盘` | `review_loop.md` | 错误归因、迁移题、下次任务 |
| `六级训练` / `深度训练` | `deep_drill.md` | 自动执行答案隔离分析→校正→逆向→碎片题→复盘闭环 |
| `蒙题·选项分布·熵` | `weak_decisions.md` | 仅在用户需要时解释统计弱策略 |
| `争议题·三练` / `高难题` | `triple_drill.md` | 复杂、低得分率或争议题三阶段复现 |
| `高难题·天花板` / `争议题·深度复盘` / `高错误率题型` | `high_error_ceiling.md` + `triple_drill.md` | 对有公开错误率证据或多来源实质争议的题目执行最高审查档，并压缩成可检索天花板卡片 |
| `成本·模型比较` | `cost_comparison.md` | 按 token、缓存、订阅和人工复核成本比较模型 |

可组合多个短命令，例如：`阅读·出题人视角分析·中文背景`。若用户指定题号、字数、难度或中文比例，只处理指定范围。

## 数据与“预训练”说明

Skill 不会改变模型权重；“预训练”在本项目中指将合法取得、用户提供或已授权的题目/答案/评分样本按结构加载，建立可检索、可比较、可复核的分析资料。默认采用 AI 原生工作流：教辅不是必需输入；若用户提供教辅，只作为待核验的对照观点，须与原题、官方说明和其他版本交叉核验，不得把销量或网络好评当作正确性的证明。

推荐数据层：题目、选项、答案、证据句、考点标签、干扰项机制、来源、版本、人工置信度。优先使用 2016 年至今的现行题型样本，2019 年至今用于近年风格分析。受版权保护的全文不得未经授权打包进仓库或商业产品；可保存用户自有材料、授权材料和必要的短引文/分析元数据。

## 深度工作流目录

| 阶段 | 模块 | 作用 |
|---|---|---|
| 资料进入 | `modules/corpus_acquisition.md` | 合法来源发现、来源登记、版本和版权状态 |
| 资料清洗 | `modules/corpus_normalization.md` | 统一场次、卷号、题号、段落、选项和答案格式 |
| 答案隔离校正 | `modules/blind_calibration.md` | 先隐藏答案建立证据链，再核对答案；不展示盲答选项 |
| 题目建模 | `modules/question_taxonomy.md` | 题型、考点、证据距离、推理操作和难度 |
| 逻辑断点 | `modules/logic_breakpoints.md` | 找出读者可能在哪一步误判，以及需要的最小证据 |
| 命题逆向 | `modules/item_writer.md` | 信息定位、干扰项、时间负荷、唯一性和跨卷模式 |
| 高错误率/争议天花板 | `modules/high_error_ceiling.md` | 证据分级、候选筛选、完整复盘、机制压缩和三次迁移训练 |
| 原文溯源 | `modules/source_trace.md` | 候选来源、删改比较和命题影响；找不到即降级 |
| 中文背景 | `modules/background.md` | 主题知识压缩、概念预览和证据边界 |
| 碎片训练 | `modules/question_fragmentation.md` | 将考点拆成最小训练单元和同机制变式题 |
| 语篇填词 | `modules/cloze.md` | 词性、搭配、语境约束和复现训练 |
| 作文评分 | `modules/writing_grading.md` | 训练性评分、锚定样本、区间和人工复核 |
| 翻译训练 | `modules/translation.md` | 信息、句法、搭配和二次改写 |
| 用户复盘 | `modules/review_loop.md` | 错误画像、迁移训练和长期记忆 |
| 质量审计 | `modules/evaluation_protocol.md` | 跨年份隐藏答案评测、失败案例、回归和版本发布门槛 |
| 人类评分标准 | `modules/human_rubric.md` | 官方 2016 修订版评分描述、证据层级和能力边界 |
| 人工锚点 | `modules/anchor_samples.md` | 官方图片样卷页码、许可登记、OCR 与公开项目对照 |
| 作文校准 | `modules/writing_calibration.md` | 标准→锚点→个案证据、交叉人评和二稿闭环 |
| 翻译校准 | `modules/translation_calibration.md` | 信息单元、错误优先级、参考译文和人工复核 |

详细模块仅在路由命中时读取：

- `modules/reading_logic.md`
- `modules/item_writer.md`
- `modules/high_error_ceiling.md`
- `modules/corpus_acquisition.md`
- `modules/corpus_normalization.md`
- `modules/blind_calibration.md`
- `modules/corpus_quality.md`
- `modules/official_sources.md`
- `modules/question_taxonomy.md`
- `modules/logic_breakpoints.md`
- `modules/background.md`
- `modules/chinese_minimal.md`
- `modules/source_trace.md`
- `modules/question_fragmentation.md`
- `modules/cloze.md`
- `modules/writing_grading.md`
- `modules/translation.md`
- `modules/human_rubric.md`
- `modules/anchor_samples.md`
- `modules/writing_calibration.md`
- `modules/translation_calibration.md`
- `modules/review_loop.md`
- `modules/evaluation_protocol.md`
- `modules/deep_drill.md`
- `modules/weak_decisions.md`
- `modules/triple_drill.md`
- `modules/cost_comparison.md`
