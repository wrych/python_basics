import pytest
import string_basics


def test_concat_with_string_addition():
    a = "abc"
    b = "dff"
    assert string_basics.concat_with_string_addition(a, b) == "abcdff"


def test_concat_with_format():
    a = "abc"
    b = "dff"
    assert string_basics.concat_with_format(a, b) == "abcdff"


def test_concat_f_strings():
    a = "abc"
    b = "dff"
    assert string_basics.concat_with_f_strings(a, b) == "abcdff"


def test_concat_with_join():
    a = "abc"
    b = "dff"
    assert string_basics.concat_with_join(a, b) == "abcdff"


def test_concat_with_old_style_formatting():
    a = "abc"
    b = "dff"
    assert string_basics.concat_with_old_style_formatting(a, b) == "abcdff"


def test_concat_multiple_strings():
    a = "abc"
    b = "dff"
    c = "ddd"
    assert string_basics.concat_with_join(a, b, c) == "abcdffddd"


def test_concat_with_join_and_separator():
    a = "abc"
    b = "dff"
    separator = ","
    assert string_basics.concat_with_join(a, b, separator=separator) == "abc,dff"


def test_format_with_template_string():
    a = "abc"
    b = "dff"
    template = "{}---{}"
    assert string_basics.format_with_template_string(template, a, b) == "abc---dff"

