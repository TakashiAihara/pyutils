from datetime import datetime as dt

DATE_FORMAT = "%Y%m%d"
DATETIME_FORMAT = "%Y%m%dT%H%M%S"


def date(date: str) -> dt:
    return dt.strptime(convert_basic(date), DATE_FORMAT)


def datetime(date: str) -> dt:
    return dt.strptime(convert_basic(date), DATETIME_FORMAT)


def convert_basic(date: str) -> str:
    return date.replace("-", "").replace(":", "").replace("/", "")
