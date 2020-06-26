a = "abc"
b = "dff"


def concat_with_string_addition(a, b):
    return a + b


def concat_with_format(a, b):
    return "{}{}".format(a, b)


"""
def concat_with_join(*args):
   return "".join(args)


def concat_with_join_and_separator(*args, separator=","):
    return separator.join(args)   
"""


def concat_with_join(*args, separator=""):
    return separator.join(args)


def concat_with_old_style_formatting(a, b):
    return "%s%s" % (a, b)


def concat_with_f_strings(a, b):
    return f"{a}{b}"


def format_with_template_string(template, a, b):
    return template.format(a, b)


def format_with_separator_string(a, b, separator):
    return separator.format(a, b)


def format_with_spacing(a, b, spacing=10):
    return f"{a: >{spacing}}{b: >{spacing}}"


def split(a, separator=None):
    return a.split(separator)


def strip(a):
    return a.strip()


def combine_split_join(a, split_separator=" ", join_separator=","):
    return concat_with_join(
        *split(a, separator=split_separator), separator=join_separator
    )

