from __future__ import annotations

import re as r
from re import Match, Pattern


class Rer:
    def __init__(self, pattern: Pattern | str):
        if isinstance(pattern, str):
            self.pattern = r.compile(pattern)
        else:
            self.pattern: Pattern = pattern
        self.matched: Match[str] | None

    def match_with(self, string: str):
        self.matched = r.match(self.pattern, string)
        return self

    def search_from(self, string: str) -> Rer:
        self.matched = r.search(self.pattern, string)
        return self

    def group(self, index: int) -> str | None:
        return self.matched and self.matched.group(index)
