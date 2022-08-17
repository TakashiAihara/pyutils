import pytest

from pyutils.dictor import generate_dict

base_dict = {
    "user": "postgres",
    "password": "postgres",
    "port": 5432,
    "driver": "psycopg2",
    "rdbms": "postgres",
    "database": "postgres",
}

test_cases: list[dict] = [
    {  # remove only
        "args": {
            "remove_keys": ["user", "password", "port"],
        },
        "expected": {
            "driver": "psycopg2",
            "rdbms": "postgres",
            "database": "postgres",
        },
    },
    {  # add only
        "args": {
            "add_dict": {"optional": "test=true"},
        },
        "expected": {
            "user": "postgres",
            "password": "postgres",
            "port": 5432,
            "driver": "psycopg2",
            "rdbms": "postgres",
            "database": "postgres",
            "optional": "test=true",
        },
    },
    {  # add and remove
        "args": {
            "add_dict": {"optional": "test=true"},
            "remove_keys": ["user", "password", "port"],
        },
        "expected": {
            "driver": "psycopg2",
            "rdbms": "postgres",
            "database": "postgres",
            "optional": "test=true",
        },
    },
]


@pytest.mark.parametrize("test_case", test_cases)
def test_dictor(test_case):
    generated_dict = generate_dict(base_dict, **test_case["args"])
    assert generated_dict == test_case["expected"]
    assert generated_dict is not base_dict
