from pytest_mock.plugin import MockerFixture

from pyutils.globber import glob

base_file_list = [
    "test/test/03_test.py",
    "test/test/01_test.py",
    "test/test/02_test.py",
    "test/test/__init__.py",
]

normal_list = [
    "test/test/03_test.py",
    "test/test/01_test.py",
    "test/test/02_test.py",
    "test/test/__init__.py",
]
sorted_list = [
    "test/test/01_test.py",
    "test/test/02_test.py",
    "test/test/03_test.py",
    "test/test/__init__.py",
]
not_sorted_list = [
    "test/test/03_test.py",
    "test/test/01_test.py",
    "test/test/02_test.py",
    "test/test/__init__.py",
]
exclude_init_list = [
    "test/test/03_test.py",
    "test/test/01_test.py",
    "test/test/02_test.py",
]
not_exclude_init_list = [
    "test/test/03_test.py",
    "test/test/01_test.py",
    "test/test/02_test.py",
    "test/test/__init__.py",
]
set_all_param_list = [
    "test/test/03_test.py",
    "test/test/01_test.py",
    "test/test/02_test.py",
    "test/test/__init__.py",
]


def test_normal(mocker: MockerFixture):
    mocker.patch("glob.glob", return_value=base_file_list)
    assert glob() == normal_list


def test_sorted(mocker: MockerFixture):
    mocker.patch("glob.glob", return_value=base_file_list)
    assert glob(sort=True) == sorted_list


def test_not_sorted(mocker: MockerFixture):
    mocker.patch("glob.glob", return_value=base_file_list)
    assert glob(sort=False) == not_sorted_list


def test_glob_exclude_init(mocker: MockerFixture):
    mocker.patch("glob.glob", return_value=base_file_list)
    assert glob(exclude_init=True) == exclude_init_list


def test_glob_not_exclude_init(mocker: MockerFixture):
    mocker.patch("glob.glob", return_value=base_file_list)
    assert glob(exclude_init=False) == not_exclude_init_list


def test_glob_all_param(mocker: MockerFixture):
    mocker.patch("glob.glob", return_value=base_file_list)
    assert glob(exclude_init=False) == set_all_param_list
