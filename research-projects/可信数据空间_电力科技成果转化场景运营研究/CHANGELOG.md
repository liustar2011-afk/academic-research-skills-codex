# 变更记录

## 2026-05-21 B-004 电力行业科技成果转化痛点研究

### 新增

- 新建 `07_branch_research/电力行业科技成果转化痛点研究/`。
- 形成支线任务单、摘要报告、深研报告、证据表、影响分析和汇入建议。

### 调整

- 将 B-004 结论汇入 `03_outline/论文提纲.md` 第三章。
- 更新 `09_evidence/evidence_pool.md` 和 `09_evidence/source_manifest.md`。
- 更新 `07_branch_research/BRANCH_INDEX.md`、`TASK_BOARD.md`、`PROJECT_INDEX.md`、`CURRENT_STATE.md`、`INTEGRATION_LOG.md` 和 `ARTIFACTS.md`。

### 目的

- 为第三章补充现实案例和痛点证据。
- 将电力科技成果转化断点具体化为成果资产表达、需求场景建模、评价交易采信、工程验证履约和标准扩散复用五类问题。

### 后续影响

- 开题报告草稿可直接吸收第三章现实问题表达。
- 后续应通过访谈核验五类痛点优先级，并选择 2-3 个典型案例进入论文第六章。

## 2026-05-21 v0.1

### 新增

- 建立研究项目目录。
- 固化阶段成果：`02_stage_outputs/阶段成果_v0.1.md`。
- 新建项目说明：`00_project_brief/项目说明.md`。
- 新建研究问题：`00_project_brief/研究问题.md`。
- 新建本地材料索引：`01_source_materials/local_materials_index.md`。
- 新建外部资料清单：`01_source_materials/外部资料清单.md`。
- 新建开题报告提纲：`03_outline/开题报告提纲.md`。
- 新建论文提纲：`03_outline/论文提纲.md`。
- 新建政策依据表占位：`04_literature_policy/政策依据表.md`。
- 新建文献综述笔记占位：`04_literature_policy/文献综述笔记.md`。
- 新建理论分析框架：`05_models/理论分析框架.md`。
- 新建“四化一扩散”运营模式：`05_models/四化一扩散运营模式.md`。
- 新建开题报告草稿入口：`06_drafts/开题报告草稿.md`。
- 新建论文初稿入口：`06_drafts/论文初稿.md`。
- 新建项目管理文件：`PROJECT_INDEX.md`、`CURRENT_STATE.md`、`DEPENDENCY_MAP.md`、`REVISION_QUEUE.md`、`DECISIONS.md`、`研究边界.md`。
- 接入工作区通用 `research-system/` 机制。
- 新建支线研究索引：`07_branch_research/BRANCH_INDEX.md`。
- 规划首批支线研究：可信数据空间政策梳理、科技成果转化政策梳理、行业组织与平台治理文献综述、电力行业科技成果转化痛点研究、科技金融与知识产权运营案例研究、跨行业扩散与产业服务案例研究。
- 新建对话窗口任务板：`TASK_BOARD.md`。
- 新建成果物索引：`ARTIFACTS.md`。
- 接入统一阶段定义：`research-system/PHASES.md`。
- 将当前状态明确为：`P1：材料诊断与框架初建` 已完成，下一步进入 `P2：政策与文献补强`。
- 在 `PROJECT_INDEX.md` 中直接嵌入阶段总览，避免只看到阶段名但看不到阶段体系。

### 当前判断

- 当前阶段成果可作为研究设计基准稿，但不能视为定稿。
- 下一步应优先补充政策与文献依据。

## 2026-05-21 P2 支线：可信数据空间政策梳理

### 新增

- 新建支线目录：`07_branch_research/可信数据空间政策梳理/`。
- 完成支线任务单：`BRANCH_BRIEF.md`。
- 完成支线报告：`branch_report.md`。
- 完成证据表：`evidence_table.md`。
- 完成对主线影响分析：`implications_for_main.md`。
- 完成汇入主线建议：`handoff_to_main.md`。

### 汇入

- 已将可信数据空间、国家数据基础设施、数据二十条、2025 工作要点、数据安全法、个人信息保护法等条目汇入 `04_literature_policy/政策依据表.md`。

### 待处理

- 尚未修订 `05_models/理论分析框架.md`。
- 尚未修订 `03_outline/论文提纲.md` 第四章。
- 等用户确认后，再把支线结论进一步汇入主线模型和提纲。

## 2026-05-21 索引增强

### 新增

- 新建 `PROCESS_ARTIFACTS.md`，登记过程成果物。
- 在 `PROJECT_INDEX.md` 中新增主线任务总表、支线任务总表、成果物总表和前因后果链。

### 调整

- `TASK_BOARD.md` 中的主线任务和支线任务加入编号。
- `ARTIFACTS.md` 增加过程成果物索引和支线影响分析。
- 新增 `MAIN_BRANCH_MAP.md`，建立主线任务与支线任务的明确关联。
- `PROJECT_INDEX.md` 增加“主线-支线关联摘要”。
- 新增 `TASK_ARTIFACT_MAP.md`，建立任务与成果物的双向关系。
- `PROJECT_INDEX.md` 增加“任务-成果物关联摘要”。

### 目的

- 用户打开一张项目控制台表，就能看到主体任务、支线任务、过程成果物、汇入状态和下一步。

## 2026-05-21 项目质量与证据机制增强

### 新增

- 新建 `HEALTH_CHECK.md`。
- 新建 `CLAIM_EVIDENCE_MAP.md`。
- 新建 `INTEGRATION_LOG.md`。
- 新建 `QUESTION_PARKING_LOT.md`。

### 目的

- 定期检查项目健康状态。
- 将核心结论与证据强度绑定。
- 单独记录支线汇入过程。
- 停放暂不处理但可能影响后续研究的问题。

## 2026-05-21 外部技能全面引入

### 新增到通用研究系统

- `research-system/imported-skills/`
- `research-system/evidence/`
- `research-system/methods/`
- `research-system/domain-adapters/`
- `research-system/delivery/`
- `research-system/quality-gates/`
- `research-system/templates/research-asset-template.md`

### 当前项目新增

- `00_project_brief/研究任务书.md`
- `HYPOTHESIS_LOG.md`
- `09_evidence/`
- `10_domain_adapter/domain_selection.md`
- `06_synthesis/research_asset.md`
- `review_log.md`
- `artifact_manifest.md`
- `11_versions/`
- `99_archive/`

### 目的

- 将外部 14 个技能全部转化为本仓库可复用的研究机制、领域适配器和交付转化规范。

## 2026-05-21 B-002 科技成果转化政策梳理

### 新增

- 新建 `07_branch_research/科技成果转化政策梳理/BRANCH_BRIEF.md`。
- 新建 `07_branch_research/科技成果转化政策梳理/branch_report.md`。
- 新建 `07_branch_research/科技成果转化政策梳理/evidence_table.md`。
- 新建 `07_branch_research/科技成果转化政策梳理/implications_for_main.md`。
- 新建 `07_branch_research/科技成果转化政策梳理/handoff_to_main.md`。

### 汇入

- 已将科技成果转化法、实施若干规定、转移转化行动方案、国家技术转移体系、职务成果赋权、成果评价机制、专利转化运用和成果转化工作情况报告等政策条目汇入 `04_literature_policy/政策依据表.md`。

### 同步

- 更新 `PROJECT_INDEX.md`、`TASK_BOARD.md`、`ARTIFACTS.md`、`CURRENT_STATE.md`、`CLAIM_EVIDENCE_MAP.md`、`INTEGRATION_LOG.md`、`09_evidence/evidence_pool.md` 和 `09_evidence/source_manifest.md`。

### 后续影响

- B-002 已完成首轮政策补强，但尚未汇入理论框架、论文提纲和“四化一扩散”模式。

## 2026-05-21 B-003 行业组织与平台治理文献综述

### 新增

- 新建 `07_branch_research/行业组织与平台治理文献综述/BRANCH_BRIEF.md`。
- 新建 `07_branch_research/行业组织与平台治理文献综述/branch_report.md`。
- 新建 `07_branch_research/行业组织与平台治理文献综述/evidence_table.md`。
- 新建 `07_branch_research/行业组织与平台治理文献综述/implications_for_main.md`。
- 新建 `07_branch_research/行业组织与平台治理文献综述/handoff_to_main.md`。

### 汇入

- 已将创新中介、创新经纪、边界组织、平台治理、生态系统治理和行业协会中介作用等理论观点汇入 `04_literature_policy/文献综述笔记.md`。

### 同步

- 更新 `PROJECT_INDEX.md`、`TASK_BOARD.md`、`ARTIFACTS.md`、`CURRENT_STATE.md`、`CLAIM_EVIDENCE_MAP.md`、`INTEGRATION_LOG.md`、`09_evidence/evidence_pool.md` 和 `09_evidence/source_manifest.md`。

### 后续影响

- B-003 已为“中电联为什么可以作为行业级枢纽主体”提供首轮理论支撑，但仍需补充中电联公开资料和中文行业组织治理文献。

## 2026-05-21 B-001/B-002/B-003 主线汇入

### 修改

- 更新 `05_models/理论分析框架.md`。
- 更新 `03_outline/论文提纲.md`。

### 汇入内容

- B-001：可信数据空间的“可信管控、资源交互、价值共创”机制。
- B-002：科技成果转化政策链条和成果资产运营逻辑。
- B-003：中电联作为行业组织型创新中介、技术经纪组织者、边界组织、平台治理者和生态编排者的理论定位。

### 同步

- 更新 `INTEGRATION_LOG.md`，将 B-001、B-002、B-003 状态推进为 integrated。
- 更新 `TASK_BOARD.md`、`PROJECT_INDEX.md`、`CURRENT_STATE.md` 和 `REVISION_QUEUE.md`。

### 后续影响

- 下一步应同步修订 `03_outline/开题报告提纲.md`。
- 之后可进入电力行业政策补强或 B-004 电力行业科技成果转化痛点研究。

## 2026-05-21 开题报告提纲同步修订

### 修改

- 重写 `03_outline/开题报告提纲.md`。

### 调整内容

- 对齐“现实断点-制度基础-数据空间-枢纽治理-运营能力-价值扩散”理论框架。
- 增加科技成果转化制度基础、可信数据空间政策基础、行业组织与平台治理文献、资料缺口与调研计划。
- 将“四化一扩散”运营模式和六类场景应用纳入开题报告结构。

### 同步

- 更新 `TASK_BOARD.md`、`PROJECT_INDEX.md`、`CURRENT_STATE.md` 和 `REVISION_QUEUE.md`。

### 后续影响

- 可进入电力行业政策补强、B-004 痛点研究或开题报告草稿 v0.1 写作。

## 2026-05-21 B-007 电力行业政策梳理

### 新增

- 新建 `07_branch_research/电力行业政策梳理/BRANCH_BRIEF.md`。
- 新建 `07_branch_research/电力行业政策梳理/branch_report.md`。
- 新建 `07_branch_research/电力行业政策梳理/detailed_report.md`。
- 新建 `07_branch_research/电力行业政策梳理/evidence_table.md`。
- 新建 `07_branch_research/电力行业政策梳理/implications_for_main.md`。
- 新建 `07_branch_research/电力行业政策梳理/handoff_to_main.md`。

### 汇入

- 已将现代能源体系、能源科技创新、新型电力系统、电力系统稳定、能源装备示范、能源重点领域设备更新等政策条目汇入 `04_literature_policy/政策依据表.md`。

### 同步

- 更新 `07_branch_research/BRANCH_INDEX.md`、`TASK_BOARD.md`、`PROJECT_INDEX.md`、`ARTIFACTS.md`、`CURRENT_STATE.md`、`INTEGRATION_LOG.md`、`09_evidence/source_manifest.md` 和 `09_evidence/evidence_pool.md`。

### 后续影响

- 后续应将电力行业政策结论吸收到开题提纲、论文提纲和理论框架，并启动 B-004 痛点研究。

## 2026-05-21 支线深研报告机制增强

### 新增

- 新增 `research-system/templates/branch-template/detailed_report.md`。

### 调整

- 更新 `research-system/templates/branch-template/BRANCH_BRIEF.md`。
- 更新 `research-system/workflows/mainline-branch-workflow.md`。
- 将复杂支线的成果包扩展为“摘要报告 + 深研报告 + 证据表 + 影响分析 + 汇入建议”。

### 目的

- 避免支线报告过于提纲化。
- 为后续正文写作沉淀可直接转写的分析段落、材料细读和判断边界。

## 2026-05-21 B-003 深研报告补充

### 新增

- 新建 `07_branch_research/行业组织与平台治理文献综述/detailed_report.md`。

### 调整

- 更新 `07_branch_research/行业组织与平台治理文献综述/BRANCH_BRIEF.md`。
- 更新 `07_branch_research/行业组织与平台治理文献综述/branch_report.md`。
- 更新 `ARTIFACTS.md` 和 `PROJECT_INDEX.md`。

### 目的

- 补厚“为什么中电联可以作为行业级枢纽主体”的理论论证。
- 沉淀可直接转写到论文第二章和第五章的正文段落。

## 2026-05-21 B-001/B-002 深研报告补充

### 新增

- 新建 `07_branch_research/可信数据空间政策梳理/detailed_report.md`。
- 新建 `07_branch_research/科技成果转化政策梳理/detailed_report.md`。

### 调整

- 更新 B-001、B-002 的 `BRANCH_BRIEF.md` 和 `branch_report.md`。
- 更新 `ARTIFACTS.md`、`PROJECT_INDEX.md`、`mkdocs.yml` 和 `scripts/build_research_portal.py`。

### 目的

- 补厚“可信数据空间如何支撑成果转化”和“科技成果转化政策链条如何支撑场景运营模式”的细节论证。
- 为论文第二章、第四章和第五章沉淀可转写正文段落。

## 版本规则

| 版本 | 含义 |
|---|---|
| v0.1 | 初步结构或首版成果 |
| v0.2 | 补充材料后修订 |
| v0.3 | 加入政策、文献或访谈后修订 |
| v1.0 | 阶段确认稿 |
| v1.1 | 阶段确认稿上的小修订 |

## 变更记录规则

重要修改应记录：

1. 修改日期。
2. 修改对象。
3. 修改原因。
4. 影响到的下游文件。
5. 是否已同步下游。
