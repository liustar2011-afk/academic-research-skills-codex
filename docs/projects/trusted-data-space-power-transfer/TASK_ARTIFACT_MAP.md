# 任务-成果物关联矩阵

本文件用于建立任务与成果物的双向关系。目标是：看到任务就知道有哪些成果物，看到成果物就知道它来自哪个任务、服务哪个任务、下一步如何使用。

## 主线任务-成果物关系

| 主线任务 | 任务名称 | 输入成果物 | 过程成果物 | 输出成果物 | 下游使用 |
|---|---|---|---|---|---|
| M-001 | 项目初始化 | 用户关于项目隔离、成果目录、恢复机制的要求 | `PROJECT_INDEX.md`、`CURRENT_STATE.md`、`CHANGELOG.md`、`DECISIONS.md`、`研究边界.md` | 项目工作台和管理机制 | 支撑所有后续任务恢复、修订、追踪 |
| M-002 | 材料诊断与框架初建 | 本地 Word/PPT/Excel 材料索引；用户研究方向 | `01_source_materials/local_materials_index.md`、`01_source_materials/外部资料清单.md` | `02_stage_outputs/阶段成果_v0.1.md`、`03_outline/开题报告提纲.md`、`03_outline/论文提纲.md`、`05_models/理论分析框架.md`、`05_models/四化一扩散运营模式.md` | 为 M-003、M-004、M-005 提供基准框架 |
| M-003 | 政策依据表补强 | `02_stage_outputs/阶段成果_v0.1.md`、B-001/B-002 支线成果包 | `07_branch_research/可信数据空间政策梳理/evidence_table.md`、`07_branch_research/可信数据空间政策梳理/handoff_to_main.md` | `04_literature_policy/政策依据表.md` | 支撑 M-005 开题报告草稿、论文第二章和政策基础 |
| M-004 | 文献综述笔记补强 | `02_stage_outputs/阶段成果_v0.1.md`、B-003 支线成果包 | 待 B-003 形成 | `04_literature_policy/文献综述笔记.md` | 支撑 M-005 开题报告草稿、理论框架修订 |
| M-005 | 开题报告草稿 v0.1 | `03_outline/开题报告提纲.md`、`04_literature_policy/政策依据表.md`、`04_literature_policy/文献综述笔记.md`、`05_models/理论分析框架.md`、`05_models/四化一扩散运营模式.md` | 待形成开题写作过程稿 | `06_drafts/开题报告草稿_v0.1.md` | 支撑 P3 阶段评审和后续论文初稿 |

## 支线任务-成果物关系

| 支线任务 | 任务名称 | 输入成果物 | 过程成果物 | 输出成果物 | 汇入主线成果 |
|---|---|---|---|---|---|
| B-001 | 可信数据空间政策梳理 | `02_stage_outputs/阶段成果_v0.1.md`、主线研究问题、政策检索来源 | `BRANCH_BRIEF.md`、`evidence_table.md`、`implications_for_main.md`、`handoff_to_main.md` | `branch_report.md` | 已汇入 `04_literature_policy/政策依据表.md`；待汇入 `05_models/理论分析框架.md`、`03_outline/论文提纲.md` |
| B-002 | 科技成果转化政策梳理 | `02_stage_outputs/阶段成果_v0.1.md`、场景材料、成果转化政策 | 待形成 | 待形成 | 计划汇入 `04_literature_policy/政策依据表.md`、论文第二/三章 |
| B-003 | 行业组织与平台治理文献综述 | `00_project_brief/项目说明.md`、`00_project_brief/研究问题.md`、行业组织/平台治理文献 | 待形成 | 待形成 | 计划汇入 `04_literature_policy/文献综述笔记.md`、`05_models/理论分析框架.md` |
| B-004 | 电力行业科技成果转化痛点研究 | 本地 PPT/Excel、行业政策、公开案例、访谈线索 | 待形成 | 待形成 | 计划汇入 `02_stage_outputs/阶段成果_v0.2.md`、论文第三章 |
| B-005 | 科技金融与知识产权运营案例研究 | `04_literature_policy/政策依据表.md`、案例资料、场景设计材料 | 待形成 | 待形成 | 计划汇入论文第六/七章、`05_models/四化一扩散运营模式.md` |
| B-006 | 跨行业扩散与产业服务案例研究 | 绿色供应链、碳足迹、装备制造、能源相邻行业案例 | 待形成 | 待形成 | 计划汇入 `05_models/四化一扩散运营模式.md`、论文第六章 |

## 成果物-任务反查表

| 成果物编号 | 成果物 | 产生任务 | 作为输入服务的任务 | 当前状态 |
|---|---|---|---|---|
| A-001 | `02_stage_outputs/阶段成果_v0.1.md` | M-002 | M-003、M-004、M-005、B-001、B-002、B-004 | baseline |
| A-002 | `03_outline/开题报告提纲.md` | M-002 | M-005 | draft |
| A-003 | `03_outline/论文提纲.md` | M-002 | M-005、B-001 汇入后修订 | draft |
| A-004 | `05_models/理论分析框架.md` | M-002 | M-005、B-001/B-003 汇入后修订 | draft |
| A-005 | `05_models/四化一扩散运营模式.md` | M-002 | M-005、B-005、B-006 | draft |
| A-006 | `07_branch_research/可信数据空间政策梳理/branch_report.md` | B-001 | M-003、后续 M-005 | completed |
| A-007 | `07_branch_research/可信数据空间政策梳理/evidence_table.md` | B-001 | M-003 | completed |
| A-008 | `07_branch_research/可信数据空间政策梳理/implications_for_main.md` | B-001 | M-003、理论框架修订、论文提纲修订 | completed |
| A-009 | `07_branch_research/可信数据空间政策梳理/handoff_to_main.md` | B-001 | M-003、理论框架修订、论文提纲修订 | completed |
| A-010 | `04_literature_policy/政策依据表.md` | M-003 | M-005、论文第二章、论文第四章 | in_progress |
| A-011 | `04_literature_policy/文献综述笔记.md` | M-004 | M-005、理论框架修订 | pending |
| A-012 | `06_drafts/开题报告草稿.md` | M-005 | 后续 P3/P5 修订 | pending |
| A-013 | `MAIN_BRANCH_MAP.md` | 项目管理 | 所有支线启动和汇入判断 | active |
| A-014 | `TASK_ARTIFACT_MAP.md` | 项目管理 | 所有任务推进和成果物反查 | active |

## 维护规则

1. 新增任务时，必须在本表登记它将产生哪些成果物。
2. 新增成果物时，必须登记产生任务和服务任务。
3. 支线成果汇入主线后，必须更新“汇入主线成果”列。
4. 成果物状态变化时，同步更新 `PROJECT_INDEX.md`、`ARTIFACTS.md` 和本文件。
