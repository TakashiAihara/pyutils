from typing import Any, Type


def class_attributes(cls: type[Any] | object) -> list[str]:
    return [
        attr
        for attr in dir(cls)
        if not callable(getattr(cls, attr)) and not attr.startswith("_")
    ]
