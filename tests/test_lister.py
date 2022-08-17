import pytest
from pyutils.lister import is_included_all, is_matched


included_test = {
    "test" :["b","c","a", "d", "e"],
    "target" :["a","b","c"],
}

matched_test = {
    "test" :["b","c","a", "b", "a"],
    "target" :["a","b","c"],
}

def test_is_included_all():
    assert is_included_all(included_test["test"], included_test["target"])


def test_is_matched():
    assert is_matched(matched_test["test"], matched_test["target"])
