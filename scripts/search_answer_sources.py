"""Search public result pages for CET official-answer provenance.

This is a discovery helper only. A search result is never classified as official
until the linked page is fetched and its publisher/domain is verified.
"""

from __future__ import annotations

import html
import re
import urllib.parse
import urllib.request


QUERIES = [
    "全国大学英语六级考试 官方答案 2025 12月",
    "site:cet.neea.edu.cn 六级 答案",
    "site:neea.edu.cn 大学英语六级 答案",
    "site:chaxun.neea.edu.cn 大学英语六级 答案",
]


def main() -> None:
    for query in QUERIES:
        url = "https://cn.bing.com/search?q=" + urllib.parse.quote(query)
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        raw = urllib.request.urlopen(req, timeout=35).read().decode("utf-8", "replace")
        print(f"QUERY\t{query}")
        for block in re.findall(r'<li class="b_algo".*?</li>', raw, re.S):
            match = re.search(r'<h2[^>]*><a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', block, re.S)
            if not match:
                continue
            title = re.sub(r"<[^>]+>", "", html.unescape(match.group(2)))
            print(f"RESULT\t{html.unescape(match.group(1))}\t{title}")


if __name__ == "__main__":
    main()
