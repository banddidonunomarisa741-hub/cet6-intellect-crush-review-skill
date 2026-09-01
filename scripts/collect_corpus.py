"""Collect public CET-6 page metadata without bundling copyrighted full text.

Usage (network required):
  python collect_corpus.py --output corpus-manifest.json

The default output is metadata only: URL, title, section labels, question counts,
retrieval timestamp, content hash, and source status. Keep full page text outside
the repository unless it is user-owned or licensed.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from lxml import html as lhtml


SESSIONS = [
    # 2015–2019 are historical comparison material; 2016 onward is the
    # primary current-format corpus.  2020-06 is omitted because the public
    # source tested on 2026-09-01 returned 404.
    "2015-06", "2015-12", "2016-06", "2016-12", "2017-06", "2017-12",
    "2018-06", "2018-12", "2019-06", "2019-12", "2020-12",
    "2021-06", "2021-12", "2022-06", "2022-09", "2022-12",
    "2023-03", "2023-06", "2023-12", "2024-06", "2024-12",
    "2025-06", "2025-12",
]
BASE = "https://english-exam.lazynote.cn/cet6/paper/{session}-{paper}/"


def clean_text(raw: bytes) -> str:
    tree = lhtml.fromstring(raw)
    for node in tree.xpath("//script|//style|//noscript"):
        node.drop_tree()
    text = " ".join(tree.xpath("//text()"))
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def counts(text: str) -> dict[str, int]:
    return {
        "writing": int("Part I" in text and "Writing" in text),
        "listening": len(re.findall(r"Questions\s+\d+\s+to\s+\d+", text)),
        "reading_questions": len(re.findall(r"\b(?:4[6-9]|5[0-5])\.", text)),
        "translation": int("Translation" in text),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--delay", type=float, default=0.2)
    args = parser.parse_args()
    records = []
    for session in SESSIONS:
        for paper in range(1, 4):
            url = BASE.format(session=session, paper=paper)
            req = urllib.request.Request(url, headers={"User-Agent": "CET6-Codex-Coach/0.1"})
            row = {
                "session": session,
                "paper": paper,
                "url": url,
                "retrieved_at": datetime.now(timezone.utc).isoformat(),
                "source_status": "unverified_public_reference",
            }
            try:
                raw = urllib.request.urlopen(req, timeout=35).read()
                text = clean_text(raw)
                row.update({
                    "http_status": 200,
                    "content_sha256": hashlib.sha256(raw).hexdigest(),
                    "text_characters": len(text),
                    "sections": counts(text),
                })
            except Exception as exc:  # network and parser errors are data status
                row.update({"http_status": None, "error": str(exc)})
            records.append(row)
            time.sleep(args.delay)
    args.output.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {args.output} ({len(records)} records)")


if __name__ == "__main__":
    main()
