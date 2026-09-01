# 语料目录说明

本目录预留给合法取得或已授权的题目、答案、评分样本和原创分析元数据。未经核验的网页全文、教辅全文和外刊全文不应复制到这里。

当前可用的本地索引位于工作区的 `research-data/structured-answers.json`，覆盖 2015–2025 年 69 套公开页面答案（2020 年 6 月该站点返回 404）。2015 年是历史对照，2016 年以后是主训练范围，2019 年以后提高近年风格权重。索引状态为 `public_reference`，不是已完成官方来源证明的答案。

用户提供官方答案文件后，登记为 `official_candidate`，先做发布链/版本/哈希检查，再与至少两个独立来源逐题交叉核验；冲突题保留多版本并降置信度。

建议每条记录包含：`session`、`paper`、`section`、`question_id`、`source_url`、`answer_status`、`blind_answer`、`reference_answer`、`evidence`、`taxonomy`、`confidence`、`rights`。
