a = "abc"
b = "dff"


def concat_with_string_addition(a, b):
    return a + b


def concat_with_format(a, b):
    return "{}{}".format(a, b)


def concat_with_join(*args, separator=""):
    return "".join(args)


def concat_with_old_style_formatting(a, b):
    return "%s%s" % (a, b)


def concat_with_f_strings(a, b):
    return f"{a}{b}"
