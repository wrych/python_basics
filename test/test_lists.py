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
