# 人工阅卷证据审计

本模块用于 `人工阅卷·证据审计`，也在出现“官方新标准”“阅卷内幕”“固定扣分表”“某年权重变化”“AI 与人工联合阅卷”等主张时启用。目标是判断证据能支持什么，不是收集越多二手经验越好。

## 根锚点

当前根标准是中国教育考试网公开的 CET 英语考试大纲入口、官方 PDF、其中的五档总体印象描述及六级作文/翻译评分样卷。具体页码、文件哈希和许可纪律读取 `human_rubric.md`、`anchor_samples.md`、`official_sources.md` 与 `human-sources.json`。

每次声称“标准已更新”前重新检查官方入口、发布日期、文件版本和哈希。第三方机构使用“新标准”“内部阅卷规则”等措辞，不能替代官方发布链。

## 证据等级

| 等级 | 证据 | 可支持的结论 |
|---|---|---|
| A `official_rubric` | 官方大纲、通知、评分说明、官方样卷及可验证更新 | 正式档次描述、题型要求和官方公开流程 |
| B `cet6_human_anchor` | 来源和许可清楚的 CET-6 人工评分样本，说明评分者培训、盲评/复评协议 | 在该样本范围内校准相邻档和人评一致性 |
| C `external_human_method` | 其他 EFL 人评数据、同行评议评分研究或教学实验 | 评分/训练方法参考，不能直接换算 CET-6 分数 |
| D `secondary_practice` | 高校课程材料、正规培训机构、教师经验、教辅 | 发现候选规律，必须与 A/B 级证据核对 |
| E `unverified_claim` | 匿名帖子、转载、无出处图片、营销文、模型生成总结 | 只能登记为待核验，不能进入评分规则 |

销量、热度、机构名气和多人转发均不能自动提升等级。一个来源可以公开访问，但仍可能没有再分发许可；“能阅读”“能短引分析”“能打包进仓库”必须分开判断。

## 审计字段

每条人类阅卷材料至少登记：

```text
claim_id | claim | publisher | original_url | publication_date | retrieved_at
exam_and_task | sample_year | rater_identity_or_training | rating_protocol
rubric_version | score_scale | double_or_multi_rating | license_status
file_hash_or_version | evidence_level | supported_scope | conflicts | decision
```

缺少评分者身份、评分协议、原始发布页或许可时显式写 `unknown`，不得靠推测补齐。

## 审计步骤与输出

1. 把文章中的事实主张拆开，例如“采用五档总体评分”和“高级词每个加一分”必须分别核验。
2. 追到原始发布者和原文件，记录版本、日期、页码或定位；转载只作线索。
3. 与官方描述和官方样卷对照；冲突时优先 A 级，保留冲突记录而非静默删除。
4. 判断结论是否超出样本：其他考试、四级样本、单一教师批改或模型评分均不能冒充六级全国阅卷。
5. 输出 `accepted`、`partially_supported`、`unverified` 或 `rejected`，说明它能否进入评分、训练提示、产品说明或只能留作候选。

不得把官方总体印象描述改造成未经公布的固定权重或机械扣分公式。公开的人评研究可以帮助设计双评、分歧复核、Kappa/一致率和隐藏测试集，但不能因此宣称 Skill 等同官方阅卷员。
