# API 与 Codex 成本比较（截至 2026-09-01 记录）

价格会变动；发布时重新打开官方价格页核对。以下按美元/百万 token 记录，不把 Codex 订阅额度和 API 账单混为一种计费。

## 记录的官方价目

| 服务 | 输入未命中 | 缓存输入命中 | 输出 | 备注 |
|---|---:|---:|---:|---|
| GPT-5.6 Sol API（短上下文） | $4.00 | $0.40 | $20.00 | 长上下文档为 $8/$0.80/$30 |
| GPT-5.6 Terra API（短上下文） | $2.00 | $0.20 | $12.00 | 长上下文档为 $4/$0.40/$18 |
| GPT-5.6 Luna API（短上下文） | $0.20 | $0.02 | $1.20 | 长上下文档为 $0.40/$0.04/$1.80 |
| DeepSeek V4 Flash API（非高峰） | $0.22 | $0.007 | $0.66 | 高峰为 $0.44/$0.014/$1.32 |

来源：

- [OpenAI API Pricing](https://developers.openai.com/api/docs/pricing)
- [Codex/ChatGPT Pricing](https://learn.chatgpt.com/docs/pricing)
- [DeepSeek API Pricing](https://api-docs.deepseek.com/quick_start/pricing/)

## 同一工作量的示例

假设一次长任务使用 1M 输入 token + 100K 输出 token，且不计算缓存：

- GPT-5.6 Sol 短上下文约 `$4 + $2 = $6`；长上下文约 `$8 + $3 = $11`。
- DeepSeek V4 Flash 非高峰约 `$0.22 + $0.066 = $0.286`；高峰约 `$0.44 + $0.132 = $0.572`。
- GPT-5.6 Luna 短上下文约 `$0.20 + $0.12 = $0.32`。

因此商业 API 场景下，DeepSeek V4 Flash 通常显著便宜；GPT-5.6 Luna 已接近低价档；GPT-5.6 Sol 购买的是更高的能力/工具生态和额度形态，不能只拿单价推断最终学习效果。

## Codex 订阅不能直接换算成每 token

Codex/ChatGPT 订阅按月和共享使用额度工作（页面记录：Free $0、Go $8、Plus $20、Pro 起价 $100/月），实际消耗取决于模型、上下文、推理、工具、检索和缓存。个人已经拥有 Plus/Pro 时，边际成本可能低于另开 API；商业 SaaS 或批量调用则应按 API token、并发、缓存命中、重试和人工复核成本核算。

用户常说的“1 人民币等于 10 美金”方向反了；若想表达约 1 美元 = 10 人民币，应明确写成该假设。比较时先保留美元口径，再按结算日汇率换算。
