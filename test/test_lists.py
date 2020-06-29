import pytest
import list_basics


def test_list_created():
    assert isinstance(list_basics.create_list(), list)


def test_append_to_list():
    x = [1, 2, 3]
    y = 4
    len_x = len(x)
    x_1 = list_basics.append_to_list(x, y)
    assert len(x_1) == len_x + 1
    assert x_1[-1] == y


@pytest.mark.parametrize("index", [0, 1, 2])
def test_insert_into_list(index):
    x = [1, 2, 3]
    y = 4
    len_x = len(x)
    x_1 = list_basics.insert_into_list(x, index, y)
    assert len(x_1) == len_x + 1
    assert x_1[index] == y


@pytest.mark.parametrize("multiplier", [0, 1, 2])
def test_multiply_elements(multiplier):
    x = [1, 2, 3]
    assert list_basics.multiply_elements(x, multiplier) == list(
        map(lambda e: e * multiplier, x)
    )


def test_stringify_list():
    x = [1, 2, 3]
    template = "hello {}"
    assert list_basics.stringify_list(x, template) == list(
        map(lambda e: template.format(e), x)
    )


def test_get_list_of_ints():
    x = ["a", 1, 2, "v", 3, "b"]
    assert list_basics.get_list_of_ints(x) == [1, 2, 3]


def test_multiply_and_format():
    x = [2, 4, 5]
    template = "banana {} joe"
    assert list_basics.multiply_and_format(x, 2, template) == list(
        map(lambda e: template.format(e * 2), x)
    )


def test_format_strings_in_list():
    x = ["banana {}", "joe {}", "sallee"]
    y = "xxx"
    assert list_basics.format_strings_in_list(x, y) == ["banana xxx", "joe xxx"]
