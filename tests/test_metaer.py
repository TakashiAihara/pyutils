from pyutils.metaer import class_attributes

expected = ["bool143", "bool2", "blah", "foo", "foobar2000"]


class Example:
    bool143 = True
    bool2 = True
    blah = False
    foo = True
    foobar2000 = False


def test_class_attributes():

    assert sorted(class_attributes(Example)) == sorted(expected)
