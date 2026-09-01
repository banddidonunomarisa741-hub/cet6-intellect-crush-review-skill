# 真题清洗与标准化模块

将材料标准化为：`session`、`paper`、`section`、`question_id`、`stem`、`options`、`answer`、`evidence`、`source_url`、`retrieved_at`、`copyright_status`、`answer_status`、`confidence` 和 `revision_log`。统一全角标点、题号、选项标签和段落边界，但保留原文版本哈希。

清洗顺序：结构解析 → 题号连续性 → 选项数量 → 答案键覆盖 → 证据位置 → 版本/来源登记。OCR 只生成候选文本，不得覆盖人工确认内容；任何修订记录旧值、新值、理由和操作者。答案冲突保留多个版本，不能静默择一。
