from __future__ import annotations

import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).with_name("check_spec_consistency.py")
SPEC = importlib.util.spec_from_file_location("check_spec_consistency", SCRIPT)
assert SPEC is not None
assert SPEC.loader is not None
check_spec_consistency = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(check_spec_consistency)


def test_check_claude_md_skips_when_file_missing(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    monkeypatch.setattr(check_spec_consistency, "ROOT", tmp_path)
    check_spec_consistency.ERRORS.clear()

    check_spec_consistency.check_claude_md()

    assert check_spec_consistency.ERRORS == []
    assert (
        "Skipping .claude/CLAUDE.md checks: file not present in this distribution."
        in capsys.readouterr().out
    )
