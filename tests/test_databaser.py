import pytest

from pyutils.databaser import make_url
from pyutils.dictor import generate_dict

base_postgres_dict = {
    "user": "test_user",
    "password": "test_password",
    "port": 5432,
    "driver": "psycopg2",
    "rdbms": "postgresql",
    "database": "test_database",
    "host": "test_host",
    "optional": "test=true",
}

base_sqlite_dict = {
    "driver": "pysqlite",
    "rdbms": "sqlite",
    "database": ":memory:",
    "optional": "test=true",
}


test_cases = [
    {
        "data": base_postgres_dict,
        "expected": "postgresql+psycopg2://test_user:test_password@test_host:5432/test_database?test=true",
    },
    {
        "data": generate_dict(base_postgres_dict, remove_keys=["password"]),
        "expected": "postgresql+psycopg2://test_user@test_host:5432/test_database?test=true",
    },
    {
        "data": generate_dict(base_postgres_dict, remove_keys=["password", "user"]),
        "expected": "postgresql+psycopg2://test_host:5432/test_database?test=true",
    },
    {
        "data": generate_dict(
            base_postgres_dict, remove_keys=["password", "user", "port"]
        ),
        "expected": "postgresql+psycopg2://test_host/test_database?test=true",
    },
    {
        "data": generate_dict(base_postgres_dict, remove_keys=["host"]),
        "expected": "postgresql+psycopg2://test_user:test_password@localhost:5432/test_database?test=true",
    },
    {
        "data": generate_dict(base_postgres_dict, remove_keys=["driver"]),
        "expected": "postgresql://test_user:test_password@test_host:5432/test_database?test=true",
    },
    {
        "data": generate_dict(base_postgres_dict, remove_keys=["optional"]),
        "expected": "postgresql+psycopg2://test_user:test_password@test_host:5432/test_database",
    },
    {
        "data": base_sqlite_dict,
        "expected": "sqlite+pysqlite:///:memory:?test=true",
    },
    {
        "data": generate_dict(base_sqlite_dict, remove_keys=["driver"]),
        "expected": "sqlite:///:memory:?test=true",
    },
    {
        "data": generate_dict(
            base_sqlite_dict,
            remove_keys=["driver", "optional"],
            add_dict={"database": "./dev.db"},
        ),
        "expected": "sqlite:///./dev.db",
    },
]


@pytest.mark.parametrize("test_case", test_cases)
def test_databaser(test_case: dict):
    assert make_url(**(test_case["data"])) == test_case["expected"]
