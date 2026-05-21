# 过程成果物索引

本文件记录过程性成果物，包括任务单、证据表、影响分析、汇入建议、状态更新等。原则：只要对后续理解前因后果有帮助，就应落地。

## 过程成果物总表

| 编号 | 阶段 | 所属任务 | 过程成果物 | 作用 | 状态 | 文件 |
|---|---|---|---|---|---|---|
| PA-001 | P0 | 项目初始化 | 项目控制台 | 说明项目总状态、阶段、基准成果、任务和恢复方式 | active | `PROJECT_INDEX.md` |
| PA-002 | P0 | 项目初始化 | 当前状态 | 用于中断恢复 | active | `CURRENT_STATE.md` |
| PA-003 | P0 | 项目初始化 | 变更记录 | 记录关键修改和阶段推进 | active | `CHANGELOG.md` |
| PA-004 | P0 | 项目初始化 | 研究决策记录 | 记录为什么采用某些研究路径和模型 | active | `DECISIONS.md` |
| PA-005 | P0 | 项目初始化 | 研究边界 | 防止研究跑偏，明确纳入和排除内容 | active | `研究边界.md` |
| PA-006 | P1 | 材料诊断与框架初建 | 阶段成果 v0.1 | 固化材料诊断、研究框架、提纲、模型和调研计划 | baseline | `02_stage_outputs/阶段成果_v0.1.md` |
| PA-007 | P1 | 材料诊断与框架初建 | 理论分析框架 | 固化“问题断点-数据空间-枢纽组织-运营能力-价值扩散”框架 | draft | `05_models/理论分析框架.md` |
| PA-008 | P1 | 材料诊断与框架初建 | “四化一扩散”运营模式 | 固化核心模式 | draft | `05_models/四化一扩散运营模式.md` |
| PA-009 | P2 | 可信数据空间政策梳理 | 支线任务单 | 说明支线目标、边界、输入和输出 | completed | `07_branch_research/可信数据空间政策梳理/BRANCH_BRIEF.md` |
| PA-010 | P2 | 可信数据空间政策梳理 | 支线研究报告 | 梳理可信数据空间政策结论 | completed | `07_branch_research/可信数据空间政策梳理/branch_report.md` |
| PA-011 | P2 | 可信数据空间政策梳理 | 证据表 | 记录政策来源、关键内容、支撑主线观点和限制 | completed | `07_branch_research/可信数据空间政策梳理/evidence_table.md` |
| PA-012 | P2 | 可信数据空间政策梳理 | 对主线影响分析 | 判断支线对研究问题、理论框架、论文提纲的影响 | completed | `07_branch_research/可信数据空间政策梳理/implications_for_main.md` |
| PA-013 | P2 | 可信数据空间政策梳理 | 汇入主线建议 | 说明哪些内容应直接吸收、谨慎吸收或不吸收 | completed | `07_branch_research/可信数据空间政策梳理/handoff_to_main.md` |
| PA-014 | P2 | 政策与文献补强 | 政策依据表 | 汇总政策依据，当前已吸收可信数据空间支线 | in_progress | `04_literature_policy/政策依据表.md` |
| PA-015 | P2 | 主线-支线任务管理 | 主线-支线关联矩阵 | 说明每条支线为什么启动、关联哪个主线任务、输出汇入哪里 | active | `MAIN_BRANCH_MAP.md` |
| PA-016 | P2 | 任务成果物管理 | 任务-成果物关联矩阵 | 建立任务与成果物的双向关系，支持按任务或成果物反查 | active | `TASK_ARTIFACT_MAP.md` |
| PA-017 | P2 | 项目质量管理 | 项目健康检查 | 检查阶段、任务、成果物、支线汇入和证据风险 | active | `HEALTH_CHECK.md` |
| PA-018 | P2 | 证据管理 | 结论-证据映射表 | 将核心结论与证据强度关联，防止弱证据支撑强结论 | active | `CLAIM_EVIDENCE_MAP.md` |
| PA-019 | P2 | 支线汇入管理 | 支线汇入日志 | 记录支线吸收了什么、未吸收什么、后续动作是什么 | active | `INTEGRATION_LOG.md` |
| PA-020 | P2 | 问题管理 | 问题停车场 | 停放有价值但暂不处理的问题，防止打断主线 | active | `QUESTION_PARKING_LOT.md` |
| PA-021 | P0/P1 | 咨询式研究框架 | 研究任务书 | 固化决策问题、SCQ、议题树、关键假设和证据需求 | draft | `00_project_brief/研究任务书.md` |
| PA-022 | P1/P2 | 假设驱动研究 | 假设日志 | 记录核心假设、证据、反驳证据和验证状态 | active | `HYPOTHESIS_LOG.md` |
| PA-023 | P2 | 事实库与证据池 | 来源清单 | 登记本地材料和政策来源 | active | `09_evidence/source_manifest.md` |
| PA-024 | P2 | 事实库与证据池 | 证据缺口 | 登记当前结论的证据缺口 | active | `09_evidence/evidence_gap.md` |
| PA-025 | P2 | 领域适配器 | 领域适配器选择 | 记录主适配器和辅助适配器 | active | `10_domain_adapter/domain_selection.md` |
| PA-026 | P3 | 研究成果资产 | 研究成果资产母本 | 后续 Word/PPT/开题报告转化母本 | pending | `06_synthesis/research_asset.md` |

## 维护规则

每次产生以下内容时，都应登记到本表：

1. 支线任务单。
2. 支线报告。
3. 证据表。
4. 影响分析。
5. 汇入建议。
6. 版本化阶段成果。
7. 重要修改说明。
8. 评审意见和回应。

## 状态说明

| 状态 | 含义 |
|---|---|
| active | 当前有效的管理性成果物 |
| draft | 初稿 |
| baseline | 当前阶段基准稿 |
| in_progress | 正在补充 |
| completed | 已完成但不一定全部汇入主线 |
| integrated | 已完成并汇入主线 |
| superseded | 已被新版本替代 |
