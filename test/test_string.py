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


def test_concat_with_join():
    a = "abc"
    b = "dff"
    assert string_basics.concat_with_join(a, b) == "abcdff"


def test_concat_with_old_style_formatting():
    a = "abc"
    b = "dff"
    assert string_basics.concat_with_old_style_formatting(a, b) == "abcdff"


def test_concat_f_strings():
    a = "abc"
    b = "dff"
    assert string_basics.concat_with_f_strings(a, b) == "abcdff"


def test_concat_multiple_strings():
    a = "abc"
    b = "dff"
    c = "ddd"
    assert string_basics.concat_with_join(a, b, c) == "abcdffddd"


"""
separator=separator   ????????
"""


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


def test_format_with_separator_string():
    a = "abc"
    b = "dff"
    separator = "{},{}"
    assert string_basics.format_with_separator_string(a, b, separator) == "abc,dff"


def test_format_with_spacing():
    a = "abc"
    b = "dff"
    assert string_basics.format_with_spacing(a, b) == "       abc       dff"


def test_format_with_spacing_with_8spaces():
    a = "abc"
    b = "dff"
    assert string_basics.format_with_spacing(a, b, spacing=8) == "     abc     dff"


def test_split_string():
    a = "a b c"
    assert string_basics.split(a) == ["a", "b", "c"]


def test_split_string_with_separator():
    a = "a,b,c"
    separator = ","
    assert string_basics.split(a, separator=separator) == ["a", "b", "c"]


def test_strip():
    a = "    b   "
    assert string_basics.strip(a) == "b"


def test_combine_split_join():
    a = "abc def xbf"
    assert string_basics.combine_split_join(a) == "abc,def,xbf"


def test_combine_split_join_with_kwargs():
    a = "abc$def$xbf"
    assert (
        string_basics.combine_split_join(a, split_separator="$", join_separator="@")
        == "abc@def@xbf"
    )
