import re as r
from copy import deepcopy

import pytest

from pyutils.rer import Rer

match_test_cases = [
    {
        "target": "test123",
        "pattern": r"[a-z]+",
        "expected": "test",
    },
    {
        "target": "test123",
        "pattern": r.compile("[a-z]+"),
        "expected": "test",
    },
    {
        "target": "test123",
        "pattern": r"\d+",
        "expected": None,
    },
]

search_test_cases = deepcopy(match_test_cases)
search_test_cases[2]["expected"] = "123"


@pytest.mark.parametrize("test_case", match_test_cases)
def test_rer_match_with(test_case: dict):
    assert (
        Rer(test_case["pattern"]).match_with(test_case["target"]).group(0)
        == test_case["expected"]
    )


@pytest.mark.parametrize("test_case", search_test_cases)
def test_rer_search_from(test_case: dict):
    assert (
        Rer(test_case["pattern"]).search_from(test_case["target"]).group(0)
        == test_case["expected"]
    )
