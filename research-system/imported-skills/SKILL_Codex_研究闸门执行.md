# SKILL｜Codex 研究闸门执行

## 适用场景

Codex 在本地项目中执行文件生成、整理、质检、归档或交付物生成。

## 执行要求

1. 先运行 `check_research_gate.py`。
2. 再运行 `check_method_quality.py`。
3. 研究不充分时，创建待补研究清单，不生成交付物。
4. 研究充分时，进入交付转化。
5. 完成后更新 `artifact_manifest.md` 和 `review_log.md`。

## 输出

```text
研究闸门结果
方法质量问题
修改文件清单
下一步建议
```
