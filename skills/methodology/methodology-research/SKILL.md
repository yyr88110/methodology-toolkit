---
name: methodology-research
description: "外部调研工具箱——GitHub项目、Skill、开源工具、API/SDK的5W1H结构化分析。触发：调研/分析/评估外部项目、看GitHub仓库、评估Skill是否值得用。"
version: 1.0.0
author: Methodology Toolkit Contributors
license: MIT
metadata:
  hermes:
    tags: [research, evaluation, 5W1H, github-analysis]
    related_skills: [methodology-toolkit, methodology-create, methodology-decide]
---

# 外部调研工具箱

对外部项目、GitHub仓库、Skill、工具链进行结构化分析，输出「值不值得用」的明确结论。

## 核心框架：5W1H

每次调研按此框架输出，不得跳过任何维度：

| 维度 | 回答 |
|------|------|
| (1) What | 这个项目/工具是干什么的？核心功能一句话 |
| (2) Who | 谁做的？作者/组织、Stars/Forks、活跃度（最近提交时间）、社区规模 |
| (3) Where | 拿回来之后，我们可以用在哪？针对我们的具体场景分析，不是泛用途 |
| (4) When | 什么时候上线的？更新频率如何？版本标签多不多？维护是否活跃？ |
| (5) Why | 为什么值得用？解决我们什么具体问题？带来什么价值？不想要「可能有用」的理由 |
| (6) How | 如果值得用，怎么安装、怎么集成、怎么设计使用流程？ |

## 输出规范

- **先给原始数据，再给分析判断**
- 对比/列表类信息优先用飞书卡片组件
- ⚠️ **飞书输出时，必须同步加载 `feishu-messaging` skill**——卡片 JSON 格式（无 msg_type 外壳、无 Markdown 表格、column_set 替代）由 feishu-messaging 定义，本 skill 不重复描述
- 最后必须给明确结论：装 / 不装 / 关注但暂不急
- 如果「不装」，简短说明原因
- 如果「关注但暂不急」，说明触发条件（什么情况下该装）

## 判断标准

| 结论 | 标准 |
|------|------|
| 装 | 直接解决当前痛点，无冗余，无竞品覆盖 |
| 不装 | 被现有工具完全覆盖，或解决不存在的问题 |
| 关注但不急 | 有价值但当前场景未触发，或需等待成熟 |
| 暂不装，退路 | 有价值但不是首选，可作为方案B |

## 调研优先级

1. 先查我们已有的能力（内置工具、现有skill、已安装软件）→ 避免装重复
2. 再查项目原始数据（GitHub API、README）→ 不凭记忆判断
3. 做 5W1H 分析 → 输出结论
4. 涉及最新状态（版本、价格、兼容性）→ 必须外部搜索核实

## 反模式

- ❌ 只描述项目功能，不分析对我们的价值
- ❌ 不给结论，列一堆选项让用户自己选
- ❌ 凭记忆判断而不核实数据
- ❌ 看到 Stars 多就推荐，不考虑实际匹配度
- ❌ **直接开写代码，不先查已有的 skill/项目/API** — 2026-05-29 奥娃脸项目教训：花 2 小时自建 bridge server，最后发现 Hermes 自带 dashboard + 插件系统 + SSE 事件流 + hook 系统，完全不需要中间层。**任何动手前，先问三个问题：① Hermes 自带什么？② 社区有什么？③ 现有方案能不能直接用？**
- ❌ **拍脑壳设计方案，不调研已有方案** — 2026-05-30 教训：老板问「铁律怎么保证执行到位」，奥娃直接自己设计"代码拦截/检查清单"方案，没有先搜 GitHub/论文。老板训斥："不要自己在那里拍脑壳，多用用方法论里面说的那些东西"。正确做法：搜 GitHub（guardrails/constraint enforcement/policy engine）→ 提取关键项目 → 用 MECE/系统思维分析 → 给一套融合方案。**设计系统/方案时，NEVER 从零设计。**

## Pitfalls

- **Agent 常见翻车**：用户问「这个是干啥的」「星级如何」「装上试试」后，Agent 没加载本 Skill 就直接答了，跳过了 5W1H 框架。**所有外部项目/工具/Skill 调研必须加载本 Skill**——哪怕问题是简单一句「星级和评价如何」，也要先加载再用框架回复。
- **GitHub 页面抓取策略**：大仓库页面（README+文件树+commits）可达 85K+ 字符，`web_extract` 会超时。正确优先级：① `mcp_github_get_file_contents` 直接读仓库结构和文件内容（最快最可靠）② `mcp_github_list_commits` 拿提交历史 ③ `mcp_github_search_repositories` 搜仓库元数据 ④ `web_extract` 只用于小 README 页面 ⑤ browser 是最后手段。**NEVER** 对大型 GitHub 仓库页面用 `web_extract`——2026-06-05 实测 CAI 仓库页面 85K 字符导致 30 分钟超时中断。
- **不要用 README 片段代替完整调研**：README 只覆盖 What，Who/When 需要看 Insights/Commits，Where/Why/How 需要结合实际场景分析。
- **Where 维度必须具体**：必须结合用户实际场景（技术管理/育儿/知识管理/团队工具），不能泛泛而谈「可以用在我们的项目中」。
- **How 给可执行命令**：不是概念描述，是能直接复制粘贴运行的步骤。
- **调研结果必须走飞书卡片**：5W1H 分析天然包含多个维度+对比表格+结论，满足飞书卡片路由条件（>200字、含表格/列表）。**完成 5W1H 分析后，直接构造卡片 JSON → send_card.sh → [SILENT]，不要先发文字再补卡片。** 2026-06-07 spec-kit 调研完成后直接甩了长 Markdown 文本，用户再次指出"为啥又不是卡片格式"——说明调研类输出的卡片路由仍然没有成为肌肉记忆。正确流程：① 完成 5W1H 分析 ② 立即构造卡片 JSON ③ send_card.sh 发送 ④ final response 为 [SILENT]。
