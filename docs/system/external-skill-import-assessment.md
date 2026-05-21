# 外部技能引入评估报告

来源目录：

`/Volumes/DOC/ChatGPT_Workbench_Research_v0.7/02_skills/`

检查时间：2026-05-21

## 总体判断

该目录下共有 14 个 Markdown 技能说明，适合分三类引入本仓库：

1. **通用研究项目机制**：可直接增强 `research-system/`。
2. **领域适配器/口径库**：适合放入 `research-system/domain-adapters/`，按项目选择启用。
3. **交付转化规范**：适合放入 `research-system/delivery/`，用于研究成果转 Word/PPT/公文。

不建议把这些文件原样注册为 Codex 技能；更适合吸收为本仓库的研究工作台规则、模板、检查清单和领域适配器。

## 引入优先级总表

| 文件 | 类型 | 建议 | 优先级 | 引入位置 |
|---|---|---|---|---|
| `SKILL_科技项目研究与成果物管理.md` | 项目管理机制 | 高度建议引入 | P0 | `research-system/workflows/`、`templates/project-template/` |
| `SKILL_事实库与证据池.md` | 证据管理 | 高度建议引入 | P0 | `research-system/evidence/` |
| `SKILL_假设驱动研究.md` | 研究方法 | 高度建议引入 | P0 | `research-system/methods/` |
| `SKILL_咨询式研究框架.md` | 研究启动方法 | 高度建议引入 | P0 | `research-system/methods/` |
| `SKILL_研究成果资产.md` | 成果资产母本 | 高度建议引入 | P0 | `research-system/templates/research-asset-template.md` |
| `SKILL_Codex_研究闸门执行.md` | 质量闸门 | 建议改造后引入 | P1 | `research-system/quality-gates/` |
| `SKILL_领域适配器选择.md` | 适配器机制 | 建议引入 | P1 | `research-system/domain-adapters/` |
| `SKILL_国家数据局数据要素材料口径.md` | 领域口径 | 建议引入 | P1 | `research-system/domain-adapters/` |
| `SKILL_国家能源局能源政策材料口径.md` | 领域口径 | 建议引入 | P1 | `research-system/domain-adapters/` |
| `SKILL_电力数据基础设施场景研究.md` | 领域研究方法 | 建议引入 | P1 | `research-system/domain-adapters/` |
| `SKILL_中电联行业组织型材料转化.md` | 项目领域口径 | 建议引入，但标注项目适配 | P1 | 当前项目 `domain_adapter/` 或全局 `domain-adapters/` |
| `SKILL_研究成果转Word.md` | 交付转化 | 建议引入 | P2 | `research-system/delivery/word/` |
| `SKILL_研究成果转PPT.md` | 交付转化 | 建议引入 | P2 | `research-system/delivery/ppt/` |
| `SKILL_公文排版_GBT9704_2012.md` | 公文格式 | 谨慎引入 | P2 | `research-system/delivery/official-doc/` |

## 重点可吸收能力

### 1. 科技项目研究与成果物管理

可吸收内容：

- 项目、任务、原始材料、研究过程物、成果资产、交付物、版本、修改意见、review_log、artifact_manifest、handoff 的对象体系。
- 二次修改必须生成新版本，不直接覆盖重要版本。
- 每次修改记录来源、新版本、修改原因、保留内容、删除内容、仍需核验、下一步建议。

与本仓库现有机制的关系：

- 已有 `PROJECT_INDEX.md`、`ARTIFACTS.md`、`PROCESS_ARTIFACTS.md`、`CHANGELOG.md`。
- 还可补强 `review_log` 和 `version archive` 机制。

建议动作：

- 新增通用 `review_log.md` 模板。
- 新增 `11_versions/`、`99_archive/` 目录规则。

### 2. 事实库与证据池

可吸收内容：

- source_manifest。
- fact_cards。
- evidence_pool。
- evidence_gap。
- 待核验清单。
- 事实卡模板。

与本仓库现有机制的关系：

- 已有 `CLAIM_EVIDENCE_MAP.md`。
- 但还缺 `fact_cards/` 和 `evidence_pool.md`。

建议动作：

- 在项目模板中增加 `09_evidence/`。
- 增加 `fact_card_template.md`、`evidence_pool.md`、`evidence_gap.md`。

### 3. 假设驱动研究

可吸收内容：

- 初始假设。
- 假设树。
- 议题优先级。
- 证据需求。
- 验证方式。
- 修正记录。

与本仓库现有机制的关系：

- 当前项目有研究问题和结论证据映射，但还没有“假设日志”。

建议动作：

- 新增 `HYPOTHESIS_LOG.md` 模板。
- 在 P1/P2 阶段强制登记关键假设。

### 4. 咨询式研究框架

可吸收内容：

- 决策问题。
- 研究边界。
- SCQ。
- 议题树。
- 证据需求。
- 关键假设。
- 预期成果物。

与本仓库现有机制的关系：

- 当前项目已有研究边界、问题、成果物，但还缺标准化 `research_brief`。

建议动作：

- 在项目模板中新增 `00_project_brief/研究任务书.md`。

### 5. 研究成果资产

可吸收内容：

研究成果资产必须包含：

- 研究对象。
- 决策问题。
- 研究边界。
- 关键判断。
- 证据映射。
- 价值池。
- 主体责任。
- 战略选项。
- 运营模式。
- 实施路线。
- 风险边界。
- 可转化成果。

与本仓库现有机制的关系：

- 当前项目已经有阶段成果和模型，但还没有专门的 `research_asset.md` 母本。

建议动作：

- 新增 `06_synthesis/research_asset.md` 或 `02_stage_outputs/research_asset_v0.1.md`。
- 后续 Word/PPT 都应从 research_asset 转化，而不是直接从原始材料生成。

### 6. 领域适配器与政策口径

适合引入的适配器：

- 国家数据局数据要素材料口径。
- 国家能源局能源政策材料口径。
- 电力数据基础设施场景研究。
- 中电联行业组织型材料转化。

建议动作：

- 新建 `research-system/domain-adapters/`。
- 每个适配器保留“适用场景、使用边界、输出结构、自检清单”。
- 当前项目可登记选择结果到 `domain_adapter_selection.md`。

### 7. 交付转化规范

适合引入：

- 研究成果转 Word。
- 研究成果转 PPT。
- 公文排版 GB/T 9704-2012。

建议动作：

- 新建 `research-system/delivery/`。
- 明确交付物必须基于 `research_asset.md`。
- 公文排版只作为格式辅助，不替代内容审定、密级、发文程序和印章管理。

## 建议实施路线

### 第一批：立即引入

1. `事实库与证据池`
2. `假设驱动研究`
3. `咨询式研究框架`
4. `研究成果资产`
5. `科技项目研究与成果物管理`

目标：

- 补齐证据池、假设日志、研究任务书、研究成果资产、review_log/版本规则。

### 第二批：领域适配器

1. `领域适配器选择`
2. `国家数据局数据要素材料口径`
3. `国家能源局能源政策材料口径`
4. `电力数据基础设施场景研究`
5. `中电联行业组织型材料转化`

目标：

- 建立“通用研究系统 + 领域口径”的组合机制。

### 第三批：交付转化

1. `研究成果转Word`
2. `研究成果转PPT`
3. `公文排版_GBT9704_2012`

目标：

- 在研究资产足够稳定后，再进入正式 Word/PPT/公文转化。

## 不建议直接引入的方式

1. 不建议原样复制为 Codex 注册技能，因为当前仓库的目标是研究项目工作台，不是扩展 Codex 全局技能。
2. 不建议在研究初期启用 Word/PPT 转化技能，否则容易绕过证据池和研究资产。
3. 不建议把领域口径当成事实来源，领域口径只提供表达规范，事实仍需政策、文献和材料核验。

## 对当前项目的直接影响

当前项目最应优先吸收：

1. `事实库与证据池`：补强 B-002/B-003 后续支线证据组织。
2. `假设驱动研究`：为“四化一扩散”和中电联枢纽主体建立假设验证链。
3. `研究成果资产`：在 P2 结束后形成 `research_asset_v0.1.md`，作为开题报告和后续 PPT/Word 的母本。
4. `中电联行业组织型材料转化`：用于 P3/P4 后的正式表达口径校准。
5. `国家数据局数据要素材料口径`：用于可信数据空间政策表述和场景设计口径校准。
