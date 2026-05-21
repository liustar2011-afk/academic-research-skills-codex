# 研究项目总看板

本文件是对话窗口中的总控面板。以后可以通过“显示研究总看板”快速恢复全局状态。

## 本地可视化门户

已引入 MkDocs 本地门户。当前服务地址：

- http://127.0.0.1:8010/

如服务未运行，可在仓库根目录执行：

```bash
python3 scripts/build_research_portal.py
.venv/bin/mkdocs serve -a 127.0.0.1:8010
```

## 项目列表

| 项目 | 当前阶段 | 当前任务 | 状态 | 入口 |
|---|---|---|---|---|
| 可信数据空间_电力科技成果转化场景运营研究 | P1：材料诊断与框架初建已完成，正在进入 P2：政策与文献补强 | B-003 已完成，下一步汇入理论框架和论文提纲，并补电力行业政策 | active | `research-projects/可信数据空间_电力科技成果转化场景运营研究/PROJECT_INDEX.md` |

## 当前推荐动作

1. 将 B-001、B-002、B-003 的机制结论汇入 `05_models/理论分析框架.md` 和 `03_outline/论文提纲.md`。
2. 补充电力行业科技创新与成果转化政策，继续补强 `04_literature_policy/政策依据表.md`。
3. 启动 B-004“电力行业科技成果转化痛点研究”支线。
4. 基于政策与文献补充结果，生成开题报告草稿 v0.1。

## 最近成果

| 时间 | 项目 | 成果 | 文件 |
|---|---|---|---|
| 2026-05-21 | 全局机制 | 外部技能引入评估 | `research-system/external-skill-import-assessment.md` |
| 2026-05-21 | 全局机制 | 外部技能全量引入 | `research-system/imported-skills/README.md` |
| 2026-05-21 | 全局机制 | 外部技能模块化入口固化 | `research-system/README.md` |
| 2026-05-21 | 全局机制 | MkDocs 本地研究门户 | `mkdocs.yml`、`docs/`、`scripts/build_research_portal.py` |
| 2026-05-21 | 可信数据空间_电力科技成果转化场景运营研究 | B-002 科技成果转化政策梳理 | `research-projects/可信数据空间_电力科技成果转化场景运营研究/07_branch_research/科技成果转化政策梳理/branch_report.md` |
| 2026-05-21 | 可信数据空间_电力科技成果转化场景运营研究 | B-003 行业组织与平台治理文献综述 | `research-projects/可信数据空间_电力科技成果转化场景运营研究/07_branch_research/行业组织与平台治理文献综述/branch_report.md` |
| 2026-05-21 | 可信数据空间_电力科技成果转化场景运营研究 | 阶段成果 v0.1 | `research-projects/可信数据空间_电力科技成果转化场景运营研究/02_stage_outputs/阶段成果_v0.1.md` |
| 2026-05-21 | 全局机制 | 研究项目工作机制 | `research-system/README.md` |
| 2026-05-21 | 全局机制 | 主线-支线研究工作流 | `research-system/workflows/mainline-branch-workflow.md` |

## 对话指令

可以直接使用以下指令：

```text
显示研究总看板
```

```text
显示当前项目任务板
```

```text
列出当前项目成果物
```

```text
继续当前项目
```

```text
启动一个支线研究
```

```text
把这个支线结论汇入主线
```

```text
修改研究问题，并检查影响范围
```

```text
生成本阶段摘要
```

## 维护规则

每次项目阶段性推进后，应同步检查是否需要更新：

1. 本文件。
2. 项目 `TASK_BOARD.md`。
3. 项目 `ARTIFACTS.md`。
4. 项目 `CURRENT_STATE.md`。
5. 项目 `CHANGELOG.md`。
6. 顶层 `ACTION_LOG.md`。
