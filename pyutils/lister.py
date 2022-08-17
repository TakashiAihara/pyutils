def is_included_all(lst: list, sublst: list) -> bool:
    """
    Returns True if all elements of sublst are in lst.
    """
    return all([key in lst for key in sublst])


def is_matched(lst: list, sublst: list) -> bool:
    """
    Returns True if all elements are matched.
    """
    return set(lst) == set(sublst)
