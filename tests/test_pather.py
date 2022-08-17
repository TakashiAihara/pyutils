from pyutils.pather import convert_module_format


test_case = {
    "data": "path/to/module.py",
    "expected": "path.to.module",
}


def test_convert_module_format():
    assert convert_module_format(test_case["data"]) == test_case["expected"]
