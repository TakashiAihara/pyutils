import glob as g


def glob(
    path: str = ".",
    sort: bool = False,
    recursive: bool = True,
    exclude_init: bool = False,
) -> list:
    globed: list[str] = [
        p
        for p in g.glob(path, recursive=recursive)
        if not (exclude_init and "__init__.py" in p)
    ]
    return sorted(globed) if sort else globed
