# 操作日志

本文件记录工作区层面的重要操作，方便用户在对话窗口中追踪“刚才做了什么”。

## 2026-05-21

### 建立电力科技成果转化研究项目

操作：

- 新建 `research-projects/可信数据空间_电力科技成果转化场景运营研究/`。
- 固化阶段成果 v0.1。
- 建立项目说明、研究问题、本地材料索引、外部资料清单。
- 建立开题报告提纲、论文提纲、理论分析框架和“四化一扩散”运营模式。

影响：

- 当前研究从一次性对话整理升级为独立项目。

### 建立项目管理文件

操作：

- 新增 `PROJECT_INDEX.md`。
- 新增 `CURRENT_STATE.md`。
- 新增 `CHANGELOG.md`。
- 新增 `DEPENDENCY_MAP.md`。
- 新增 `REVISION_QUEUE.md`。
- 新增 `DECISIONS.md`。
- 新增 `研究边界.md`。

影响：

- 支持中断恢复、版本留存、依赖追踪和修订管理。

### 建立全局研究系统

操作：

- 新增 `research-system/README.md`。
- 新增主线-支线研究工作流。
- 新增中断恢复工作流。
- 新增支线汇入主线检查清单。
- 新增项目模板和支线模板。

影响：

- 工作区具备可复用的通用研究项目机制，不再只服务单一项目。

### 当前项目接入支线机制

操作：

- 新增 `07_branch_research/BRANCH_INDEX.md`。
- 规划 6 条支线研究。
- 新增 `08_review_revision/`。

影响：

- 当前项目可以通过支线深度研究支撑主线推进。

### 建立对话窗口可见工作台

操作：

- 新增 `RESEARCH_DASHBOARD.md`。
- 新增顶层 `ACTION_LOG.md`。
- 新增当前项目 `TASK_BOARD.md`。
- 新增当前项目 `ARTIFACTS.md`。

影响：

- 用户不需要直接浏览文件系统，也可以通过对话查看项目、任务、成果物和最近操作。

### 明确研究项目阶段体系

操作：

- 新增 `research-system/PHASES.md`。
- 将当前项目状态从临时描述改为统一阶段表达：`P1：材料诊断与框架初建` 已完成，下一步进入 `P2：政策与文献补强`。
- 更新 `PROJECT_INDEX.md`、`CURRENT_STATE.md`、`TASK_BOARD.md` 和 `RESEARCH_DASHBOARD.md`。

影响：

- 以后项目状态必须引用已定义阶段，避免出现用户在上下文中找不到的阶段名。

### 在项目控制台嵌入阶段总览

操作：

- 更新当前项目 `PROJECT_INDEX.md`，直接展示 P0-P6 阶段表。
- 更新 `research-system/templates/project-template/PROJECT_INDEX.md`，让未来项目默认包含阶段总览。

影响：

- 用户查看项目控制台时，不需要再跳转到 `PHASES.md` 才能理解当前阶段体系。

### 启动并完成“可信数据空间政策梳理”支线

操作：

- 创建支线目录：`07_branch_research/可信数据空间政策梳理/`。
- 完成支线成果包：任务单、支线报告、证据表、对主线影响、汇入建议。
- 将政策依据首轮汇入主线 `04_literature_policy/政策依据表.md`。
- 更新支线状态为 completed。

影响：

- P2“政策与文献补强”阶段已完成首条支线。
- 主线第四章“可信数据空间赋能机制”获得政策依据支撑。

### 增强项目总索引和过程成果物留存

操作：

- 新建当前项目 `PROCESS_ARTIFACTS.md`。
- 在 `PROJECT_INDEX.md` 中加入主线任务总表、支线任务总表、成果物总表和前因后果链。
- 更新 `TASK_BOARD.md`，为主线任务和支线任务增加编号。
- 更新 `ARTIFACTS.md`，加入过程成果物索引和支线影响分析。

影响：

- 过程成果物也被显式登记。
- 用户从 `PROJECT_INDEX.md` 一张表即可看到任务、成果、支线、状态和前因后果。

### 建立主线-支线关联矩阵

操作：

- 新增 `MAIN_BRANCH_MAP.md`。
- 在 `PROJECT_INDEX.md` 中加入主线-支线关联摘要。
- 在 `TASK_BOARD.md`、`ARTIFACTS.md`、`PROCESS_ARTIFACTS.md` 中登记该关联矩阵。

影响：

- 每条支线都能追溯到对应主线任务、主线缺口、输入、输出、汇入成果和汇入条件。

### 建立任务-成果物关联矩阵

操作：

- 新增 `TASK_ARTIFACT_MAP.md`。
- 在 `PROJECT_INDEX.md` 中加入任务-成果物关联摘要。
- 在 `ARTIFACTS.md` 和 `PROCESS_ARTIFACTS.md` 中登记该矩阵。

影响：

- 任务和成果物之间建立双向关系：从任务可看到输入/过程/输出，从成果物可反查产生任务和服务任务。

### 建立项目质量与证据管理机制

操作：

- 新增 `HEALTH_CHECK.md`。
- 新增 `CLAIM_EVIDENCE_MAP.md`。
- 新增 `INTEGRATION_LOG.md`。
- 新增 `QUESTION_PARKING_LOT.md`。
- 更新 `PROJECT_INDEX.md`、`ARTIFACTS.md`、`PROCESS_ARTIFACTS.md`、`CHANGELOG.md`。

影响：

- 项目可以定期做健康检查。
- 核心结论可以追踪证据强度。
- 支线汇入有专门日志。
- 暂不处理的问题不会丢失，也不会打断主线。

### 检查外部技能目录并形成引入评估

操作：

- 检查 `/Volumes/DOC/ChatGPT_Workbench_Research_v0.7/02_skills/` 下 14 个技能说明。
- 形成 `research-system/external-skill-import-assessment.md`。

影响：

- 明确哪些外部技能可引入为通用研究机制、领域适配器和交付转化规范。
- 建议优先引入事实库与证据池、假设驱动研究、咨询式研究框架、研究成果资产、科技项目研究与成果物管理。

### 全量引入外部技能为研究系统能力

操作：

- 将 14 个外部技能原文归档到 `research-system/imported-skills/`。
- 新增证据系统：`research-system/evidence/`。
- 新增研究方法：`research-system/methods/`。
- 新增领域适配器：`research-system/domain-adapters/`。
- 新增交付转化规范：`research-system/delivery/`。
- 新增质量闸门：`research-system/quality-gates/`。
- 更新项目模板，加入研究任务书、假设日志、证据目录、领域适配器、研究成果资产、review_log、artifact_manifest、版本和归档目录。
- 将当前项目接入上述新能力。

影响：

- 外部技能已全部引入，但以研究系统模块形式存在，而不是原样注册为 Codex 技能。
- 当前项目具备证据池、假设日志、研究任务书、领域适配器选择、研究成果资产和交付转化闸门。

### 固化外部技能模块入口

操作：

- 更新 `research-system/README.md`，加入证据系统、研究方法、领域适配器、交付转化、质量闸门和原始技能归档的入口说明。
- 更新 `research-system/new-project-checklist.md`，把证据池、假设日志、领域适配器、研究成果资产、版本归档和质量闸门纳入新项目创建动作。
- 更新 `research-system/templates/project-template/README.md`，补齐 `06_synthesis/`、`09_evidence/`、`10_domain_adapter/`、`11_versions/`、`99_archive/` 等目录说明。
- 更新 `RESEARCH_DASHBOARD.md`，将当前推荐动作切换为 B-002“科技成果转化政策梳理”和 B-003“行业组织与平台治理文献综述”。

影响：

- 外部技能不只是被复制进仓库，而是进入通用研究机制和新项目模板。
- 后续新建研究项目时，可以直接复用这些能力。
- 当前项目的下一步动作更清晰：从已完成的可信数据空间政策支线，转向成果转化政策和组织治理文献补强。

### 引入 MkDocs 本地研究门户

操作：

- 新增 `mkdocs.yml`。
- 新增 `requirements-docs.txt`。
- 新增门户目录 `docs/`。
- 新增门户样式 `docs/assets/research-portal.css`。
- 新增同步脚本 `scripts/build_research_portal.py`。
- 建立本地虚拟环境 `.venv/` 并安装 MkDocs、Material for MkDocs 和 pymdown-extensions。
- 已执行 `mkdocs build --strict` 验证通过。
- 已启动本地服务：`http://127.0.0.1:8010/`。

影响：

- 项目状态可以通过网页侧边栏、搜索、目录和关系图查看。
- 现有 Markdown 成果物仍然是源文件，门户页面由同步脚本生成。
- 后续主线或支线成果更新后，运行 `python3 scripts/build_research_portal.py` 即可刷新门户内容。

### 启动并完成 B-002 科技成果转化政策梳理

操作：

- 新建支线目录 `research-projects/可信数据空间_电力科技成果转化场景运营研究/07_branch_research/科技成果转化政策梳理/`。
- 形成支线任务单、支线报告、证据表、对主线影响分析和汇入建议。
- 检索并引用国家层面科技成果转化相关政策来源。
- 将首轮政策条目汇入 `04_literature_policy/政策依据表.md`。
- 同步更新项目控制台、任务板、支线索引、成果物索引、证据池、结论-证据映射表、汇入日志和当前状态。

影响：

- M-003 政策依据表已完成可信数据空间政策和科技成果转化政策两轮补强。
- 后续需要补充电力行业政策，并将 B-001、B-002 的机制结论汇入理论框架和论文提纲。

### 启动并完成 B-003 行业组织与平台治理文献综述

操作：

- 新建支线目录 `research-projects/可信数据空间_电力科技成果转化场景运营研究/07_branch_research/行业组织与平台治理文献综述/`。
- 形成支线任务单、支线报告、证据表、对主线影响分析和汇入建议。
- 梳理创新中介、创新经纪、边界组织、平台治理、生态系统治理和行业协会中介作用文献。
- 将首轮综述结论汇入 `04_literature_policy/文献综述笔记.md`。
- 同步更新项目控制台、任务板、支线索引、成果物索引、证据池、结论-证据映射表、汇入日志和当前状态。

影响：

- M-004 文献综述笔记已获得首轮理论支撑。
- “中电联作为行业级枢纽主体”的表述可由行业组织型创新中介、边界组织、平台治理者和生态编排者四类理论共同支撑。
