from datetime import datetime as dt

import pytest

from pyutils.datetimer import (
    convert_basic,
    date,
    datetime,
    generate_range_datetime,
    generate_range_strftime,
)

mock_date = "2019-01-01"
mock_datetime = "2019-02-02T01:02:03"

mock_date_case = [
    {
        "params": {
            "start": dt(year=2019, month=1, day=1),
            "end": dt(year=2019, month=1, day=5),
            "reverse": False,
        },
        "expected": [
            dt(year=2019, month=1, day=1),
            dt(year=2019, month=1, day=2),
            dt(year=2019, month=1, day=3),
            dt(year=2019, month=1, day=4),
            dt(year=2019, month=1, day=5),
        ],
    },
    {
        "params": {
            "start": dt(year=2019, month=1, day=1),
            "end": dt(year=2019, month=1, day=5),
            "reverse": True,
        },
        "expected": [
            dt(year=2019, month=1, day=5),
            dt(year=2019, month=1, day=4),
            dt(year=2019, month=1, day=3),
            dt(year=2019, month=1, day=2),
            dt(year=2019, month=1, day=1),
        ],
    },
]

mock_str_case = [
    {
        "params": {
            "start": dt(year=2019, month=1, day=1),
            "end": dt(year=2019, month=1, day=5),
            "reverse": False,
            "format": "%Y%m%d",
        },
        "expected": [
            "20190101",
            "20190102",
            "20190103",
            "20190104",
            "20190105",
        ],
    },
    {
        "params": {
            "start": dt(year=2019, month=1, day=1),
            "end": dt(year=2019, month=1, day=5),
            "reverse": True,
            "format": "%Y%m%d",
        },
        "expected": [
            "20190105",
            "20190104",
            "20190103",
            "20190102",
            "20190101",
        ],
    },
]


def test_date():
    assert date(mock_date) == dt(year=2019, month=1, day=1)


def test_datetime():
    assert datetime(mock_datetime) == dt(
        year=2019, month=2, day=2, hour=1, minute=2, second=3
    )


def test_convert_basic():
    assert convert_basic("2019-01-01") == "20190101"


@pytest.mark.parametrize("test_case", mock_date_case)
def test_generate_range_datetime(test_case: dict):
    assert generate_range_datetime(**test_case["params"]) == test_case["expected"]


@pytest.mark.parametrize("test_case", mock_str_case)
def test_generate_range_strftime(test_case: dict):
    assert generate_range_strftime(**test_case["params"]) == test_case["expected"]
