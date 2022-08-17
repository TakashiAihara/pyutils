from os.path import sep, splitext

from git.repo.base import Repo


def convert_module_format(file_path: str) -> str:
    return splitext(file_path)[0].replace(sep, ".")


def get_git_root() -> str:
    return Repo(".", search_parent_directories=True).git.rev_parse("--show-toplevel")
