from datetime import datetime as dt

from pyutils.datetimer import convert_basic, date, datetime

mock_date = "2019-01-01"
mock_datetime = "2019-02-02T01:02:03"


def test_date():
    assert date(mock_date) == dt(year=2019, month=1, day=1)


def test_datetime():
    assert datetime(mock_datetime) == dt(
        year=2019, month=2, day=2, hour=1, minute=2, second=3
    )


def test_convert_basic():
    assert convert_basic("2019-01-01") == "20190101"
