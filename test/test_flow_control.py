import pytest
import flow_control


def test_if_case_1():
    assert flow_control.if_case(True) == "yes"


def test_if_case_2():
    assert flow_control.if_case(False) == "no"


def test_elif_case_1():
    assert flow_control.elif_case(0) == "it's a zero"


def test_elif_case_2():
    assert flow_control.elif_case(1) == "it's a one"


@pytest.mark.parametrize("foo", [-1, 2, 3])
def test_elif_case_3(foo):
    assert flow_control.elif_case(foo) == "something else"


def test_for_loop():
    assert flow_control.for_loop([[1, 2], [1, 2, 3], [1, 2, 3, 4]]) == 9


def test_sum_numbers():
    assert flow_control.sum_numbers([1, 2, 3, 4, "abc", 10]) == 20
