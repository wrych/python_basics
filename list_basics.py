# fix the tests here


def create_list():
    return list()


def append_to_list(x, y):
    x.append(y)
    return x


def insert_into_list(x, index, y):
    x.insert(index, y)
    return x


def multiply_elements(x, multiplier):
    return [e * multiplier for e in x]


def stringify_list(x, template):
    return [template.format(e) for e in x]


def get_list_of_ints(x):
    ints_in_x = [i for i in x if isinstance(i, int)]
    return ints_in_x


def multiply_and_format(x, y, template):
    multiplyed_elements_list = [e * y for e in x]
    return [template.format(e) for e in multiplyed_elements_list]


def format_strings_in_list(x, y):
    return [e.format(y) for e in x if e.find("{}") >= 0]
