from types import ModuleType
from typing import Iterable
from pyutils.pather import convert_module_format
from importlib import import_module as im


def import_module(path: str) -> ModuleType:
    return im(convert_module_format(path))


def import_modules_gen(paths: list[str]) -> Iterable[ModuleType]:
    for file_path in paths:
        yield import_module(file_path)


def import_modules(paths: list[str]) -> list[ModuleType]:
    return list(import_modules_gen(paths))
