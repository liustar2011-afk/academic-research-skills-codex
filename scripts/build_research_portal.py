#!/usr/bin/env python3
"""Sync research Markdown files into the MkDocs portal."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PROJECT = ROOT / "research-projects" / "可信数据空间_电力科技成果转化场景运营研究"
PROJECT_DOCS = DOCS / "projects" / "trusted-data-space-power-transfer"


COPIES = {
    ROOT / "RESEARCH_DASHBOARD.md": DOCS / "index.md",
    ROOT / "ACTION_LOG.md": DOCS / "action-log.md",
    ROOT / "research-system" / "README.md": DOCS / "system" / "research-system.md",
    ROOT / "research-system" / "PHASES.md": DOCS / "system" / "phases.md",
    ROOT / "research-system" / "new-project-checklist.md": DOCS / "system" / "new-project-checklist.md",
    ROOT / "research-system" / "external-skill-import-assessment.md": DOCS / "system" / "external-skill-import-assessment.md",
    PROJECT / "PROJECT_INDEX.md": PROJECT_DOCS / "PROJECT_INDEX.md",
    PROJECT / "CURRENT_STATE.md": PROJECT_DOCS / "CURRENT_STATE.md",
    PROJECT / "TASK_BOARD.md": PROJECT_DOCS / "TASK_BOARD.md",
    PROJECT / "ARTIFACTS.md": PROJECT_DOCS / "ARTIFACTS.md",
    PROJECT / "MAIN_BRANCH_MAP.md": PROJECT_DOCS / "MAIN_BRANCH_MAP.md",
    PROJECT / "TASK_ARTIFACT_MAP.md": PROJECT_DOCS / "TASK_ARTIFACT_MAP.md",
    PROJECT / "CLAIM_EVIDENCE_MAP.md": PROJECT_DOCS / "CLAIM_EVIDENCE_MAP.md",
    PROJECT / "HEALTH_CHECK.md": PROJECT_DOCS / "HEALTH_CHECK.md",
    PROJECT / "02_stage_outputs" / "阶段成果_v0.1.md": PROJECT_DOCS / "stage-output-v0.1.md",
    PROJECT / "03_outline" / "论文提纲.md": PROJECT_DOCS / "paper-outline.md",
    PROJECT / "05_models" / "四化一扩散运营模式.md": PROJECT_DOCS / "four-transformations-model.md",
    PROJECT / "07_branch_research" / "科技成果转化政策梳理" / "branch_report.md": PROJECT_DOCS / "branch-b002-report.md",
    PROJECT / "07_branch_research" / "科技成果转化政策梳理" / "evidence_table.md": PROJECT_DOCS / "branch-b002-evidence.md",
    PROJECT / "07_branch_research" / "科技成果转化政策梳理" / "implications_for_main.md": PROJECT_DOCS / "branch-b002-implications.md",
    PROJECT / "07_branch_research" / "科技成果转化政策梳理" / "handoff_to_main.md": PROJECT_DOCS / "branch-b002-handoff.md",
    PROJECT / "07_branch_research" / "行业组织与平台治理文献综述" / "branch_report.md": PROJECT_DOCS / "branch-b003-report.md",
    PROJECT / "07_branch_research" / "行业组织与平台治理文献综述" / "evidence_table.md": PROJECT_DOCS / "branch-b003-evidence.md",
    PROJECT / "07_branch_research" / "行业组织与平台治理文献综述" / "implications_for_main.md": PROJECT_DOCS / "branch-b003-implications.md",
    PROJECT / "07_branch_research" / "行业组织与平台治理文献综述" / "handoff_to_main.md": PROJECT_DOCS / "branch-b003-handoff.md",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def normalize_links(text: str) -> str:
    replacements = {
        "`research-system/PHASES.md`": "`阶段定义`",
        "`research-system/README.md`": "`研究系统说明`",
        "`research-system/workflows/interruption-recovery-workflow.md`": "`中断恢复工作流`",
        "`research-system/workflows/mainline-branch-workflow.md`": "`主线-支线工作流`",
        "`research-system/workflows/branch-integration-checklist.md`": "`支线汇入检查清单`",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def copy_markdown() -> None:
    for source, target in COPIES.items():
        if not source.exists():
            raise FileNotFoundError(source)
        write_text(target, normalize_links(read_text(source)))


def project_landing() -> str:
    return """# 当前项目首页

本页是当前研究项目的网页入口。源文件仍保存在项目目录中，门户页面由 `scripts/build_research_portal.py` 同步生成。

<div class="research-status-grid">
  <div class="research-status-card"><strong>当前阶段</strong><span class="status-warn">P2 政策与文献补强前段</span></div>
  <div class="research-status-card"><strong>已完成</strong><span class="status-ok">P0 项目初始化；P1 材料诊断与框架初建；B-001 可信数据空间政策梳理</span></div>
  <div class="research-status-card"><strong>当前主线</strong><span>M-003 政策依据表补强；M-004 文献综述笔记补强</span></div>
  <div class="research-status-card"><strong>下一步</strong><span>汇入 B-001/B-002/B-003 机制结论；补充电力行业政策；启动 B-004 痛点研究</span></div>
</div>

## 快速入口

| 想看什么 | 入口 |
|---|---|
| 项目全貌 | [项目控制台](PROJECT_INDEX.md) |
| 当前该做什么 | [任务板](TASK_BOARD.md) |
| 已有哪些成果 | [成果物索引](ARTIFACTS.md) |
| 主线和支线怎么关联 | [主线-支线矩阵](MAIN_BRANCH_MAP.md) |
| 任务和成果物怎么关联 | [任务-成果物矩阵](TASK_ARTIFACT_MAP.md) |
| 哪些结论证据强/弱 | [证据状态](CLAIM_EVIDENCE_MAP.md) |
| 项目有什么风险 | [项目健康](HEALTH_CHECK.md) |

## 当前工作流

```mermaid
flowchart LR
  A["P1 材料诊断与框架初建"] --> B["阶段成果 v0.1"]
  B --> C["发现政策与文献缺口"]
  C --> D["B-001 可信数据空间政策梳理"]
  D --> E["部分汇入政策依据表"]
  E --> F["B-002 科技成果转化政策梳理"]
  F --> G["部分汇入政策依据表"]
  G --> H["B-003 行业组织与平台治理文献综述"]
  H --> I["部分汇入文献综述笔记"]
  I --> J["汇入理论框架和论文提纲"]
  I --> K["补充电力行业政策"]
  J --> L["P3 开题报告草稿 v0.1"]
  K --> L
```

## 使用提示

每次主线或支线有新成果后，运行：

```bash
python3 scripts/build_research_portal.py
```

然后刷新本地门户即可看到最新状态。
"""


def main() -> None:
    copy_markdown()
    write_text(PROJECT_DOCS / "index.md", project_landing())
    print(f"Synced {len(COPIES) + 1} portal pages into {DOCS}")


if __name__ == "__main__":
    main()
