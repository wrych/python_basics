# what happens after you type python namespace_basics.py
# python reads the file namespace_basiscs.py from the top.
# python sees, that there is a function called main but does not execute it.


def iter_through_array(i):
    arr = [1, 2, 3, 4]
    return arr[i]


def main():
    index = 1
    print(iter_through_array(index + 1))


if __name__ == "__main__":
    main()

