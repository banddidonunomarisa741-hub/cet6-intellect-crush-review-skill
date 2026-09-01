# GitHub 相关 CET Skill 与题库检索记录

检索日期：2026-09-01。以下只登记公开仓库的元数据、能力摘要和入口，不复制仓库内的整套真题或音频。

## 高相关仓库

### 1. [Liuxiangjian-ai/cet-skill](https://github.com/Liuxiangjian-ai/cet-skill)

- 133 stars、9 forks（检索时 GitHub 返回值）。
- MIT 许可；仓库描述为基于 2015–2025 年四六级趋势的 Codex Skill。
- `SKILL.md` 约 30 KB，覆盖写作、翻译、阅读、听力、错因诊断和学习规划。
- 明确要求选词填空采用 15 选 10、仔细阅读两篇各 5 题，并延迟揭示答案。
- 对我们最有价值的是完整的格式与长度约束；它没有提供可核验的人类标注评测，因此不能直接证明评分达到官方阅卷水平。

### 2. [qingzhou-hub/cet6-tutor](https://github.com/qingzhou-hub/cet6-tutor)

- Hermes Agent Skill，带阅读、听力和艾宾浩斯词汇引擎。
- README 声称包含 2018–2025 年 96 篇阅读、27 套听力和 44 套答案。
- 仓库有 `data/CET6_Perfect_Fixed.json`、`data/CET6_Answer.json` 和听力题库文件，可作为“候选题库入口”研究其字段设计。
- GitHub 仓库元数据没有返回明确许可证；不得把这些数据直接复制进本项目。若要使用，应先获得作者和真题权利人的许可，或让用户在本地自行提供材料。

### 3. [Leonhard-Euler271/cet6-writing-translation-skills](https://github.com/Leonhard-Euler271/cet6-writing-translation-skills)

- 拆成 `cet6-essay-coach` 与 `cet6-translation-coach` 两个 Skill。
- 优点是把五档总体印象评分、意群对齐、最小改译、二稿训练写得很清楚。
- 是我们作文/翻译模块的流程对照，不替代官方评分标准；仓库是否允许再分发需单独核验。

### 4. [tong666-bit/liu-xiaoyan-skill](https://github.com/tong666-bit/liu-xiaoyan-skill)

- MIT 许可；四六级、考研英语和教师风格教学 Skill。
- 含长难句、阅读干扰项、选词填空和 2026 年 6 月六级校准材料的路由示例。
- 适合作为交互语气和短命令设计参考；“教师风格”不能当作命题事实。

### 5. [raisuny-384/cet6-ai-assistant](https://github.com/raisuny-384/cet6-ai-assistant)

- 面向英语六级刷题助手的前端网页项目。
- 可作为 UI/题目提交流程参考；仓库元数据没有明确许可证，不能直接复制其数据或代码。

### 6. [ZhangNingYA/tend](https://github.com/ZhangNingYA/tend)

- GitHub 代码搜索可见 2015–2025 多场 CET6 阅读页面，包含选词填空、段落匹配和仔细阅读的结构化前端内容。
- 可研究按年份/场次组织题目的数据结构和阅读练习交互。
- 代码搜索结果不等于题目版权许可；不直接复制正文、选项或答案到本 Skill。

### 7. [HCLEMINI/CET6-Full-Process-Learning](https://github.com/HCLEMINI/CET6-Full-Process-Learning)

- 覆盖听力、写作、仔细阅读、长篇阅读和选词填空，并有 DeepSeek 接入示例。
- 可作为“全流程产品”和模型调用边界的对照；不把其题库或代码当作本项目数据。

### 8. [Affordan/cet6word-agent](https://github.com/Affordan/cet6word-agent)

- 以词汇 Agent、记忆库和 DeepSeek V4 Flash 配置为主，可参考词汇路由与持久化结构。
- 其模型配置和数据仍需按仓库许可证、版本和第三方词表权利单独核验。

### 9. [opus456/English_assistant](https://github.com/opus456/English_assistant)

- 包含 CET6 材料生成脚本和可切换 DeepSeek 的提示模板，说明“模型 API + 题型模板”路线已有公开实现。
- 没有看到足以证明官方命题等效性的独立评测；仅作实现参考。

## 与本 Skill 的差异

现有项目已经覆盖“题库 + 基础解析 + 生成模拟题”。本 Skill 的差异化不应再宣称“市场上没有类似产品”，而应集中在：

1. 词表驱动的 15 选 10 原创生成，强制独立求解和唯一性审计；
2. 中文式阅读，把题干、选项和逻辑断点压缩后仍回到英文证据；
3. 将可观察的定位成本、干扰项变换、时间负荷和反事实测试记录成命题逆向卡片；
4. 外刊溯源找不到可靠匹配时自动关闭，不让来源猜测污染答案证据；
5. 将“训练性评分器”与“官方阅卷器”明确区分，并保留人工复核队列。

## 题库接入策略

可以研究上述仓库的字段和流程，但不要把其 JSON、PDF、音频或完整真题全文直接打包进本项目。推荐顺序：

1. 先记录公开仓库 URL、提交 SHA、文件路径和许可证；
2. 只提取结构元数据和必要的短引文；
3. 真题全文由用户自有/已授权文件或运行时合法获取；
4. 任何答案先标记 `public_reference`，完成来源链核验后再升权。
