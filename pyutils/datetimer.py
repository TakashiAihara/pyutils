from collections.abc import Iterable
from datetime import datetime as dt
from datetime import timedelta as td

from pytz import timezone

DATE_FORMAT = "%Y%m%d"
DATETIME_FORMAT = "%Y%m%dT%H%M%S"


def date(date: str) -> dt:
    return dt.strptime(convert_basic(date), DATE_FORMAT)


def datetime(date: str) -> dt:
    return dt.strptime(convert_basic(date), DATETIME_FORMAT)


def convert_basic(date: str) -> str:
    return date.replace("-", "").replace(":", "").replace("/", "")


def generate_range_datetime(
    start: dt,
    end: dt,
    reverse: bool = False,
) -> list[dt]:
    days_num = (end - start).days + 1
    days_list = [start + td(days=x) for x in range(days_num)]
    return list(reversed(days_list)) if reverse else sorted(days_list)


def generate_range_strftime(
    start: dt,
    end: dt,
    format: str,
    reverse: bool = False,
) -> list[str]:
    return [
        dt.strftime(x, format)
        for x in generate_range_datetime(start, end, reverse=reverse)
    ]
