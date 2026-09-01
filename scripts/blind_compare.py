"""Schema helper for blind-answer records.

This intentionally does not solve or score questions. A caller supplies a blind
answer file and a separately protected answer file; the script reports agreement,
disagreement, and missing evidence without rewriting the blind record.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("blind", type=Path)
    parser.add_argument("key", type=Path)
    args = parser.parse_args()
    blind = json.loads(args.blind.read_text(encoding="utf-8"))
    raw_key = json.loads(args.key.read_text(encoding="utf-8"))
    if isinstance(raw_key, list):
        key = {
            f"{row['session']}-{row['paper']}": {
                **row.get("listening", {}),
                **row.get("careful_reading", {}),
            }
            for row in raw_key
        }
    else:
        key = raw_key
    rows = []
    for item in blind:
        ident = (item["session"], item["paper"], str(item["question_id"]))
        correct = key.get(f"{ident[0]}-{ident[1]}", {}).get(ident[2])
        predicted = item.get("answer")
        rows.append({
            "session": ident[0],
            "paper": ident[1],
            "question_id": ident[2],
            "blind_answer": predicted,
            "reference_answer": correct,
            "agreement": predicted == correct if correct else None,
            "evidence": item.get("evidence"),
            "confidence": item.get("confidence"),
        })
    print(json.dumps(rows, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
