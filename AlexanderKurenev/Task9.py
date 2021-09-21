import string


def test_1_1(*args):
    """Function returns characters that appear in all strings"""
    out = set(args[0])
    for s in args:
        out.intersection_update(set(s))
    return out


def test_1_2(*args):
    """characters that appear in at least one string"""
    out = set()
    for s in args:
        out.update(set(s))
    return out


def test_1_3(*args):
    """Function returns characters that appear at least in two strings"""
    out = set()
    for i in range(len(args) - 1):
        for j in range(i + 1, len(args)):
            out.update(set(args[i]) & set(args[j]))
    return out


def test_1_4(*args):
    """Function returns characters of alphabet, that were not used in any string"""
    out = set()
    letters = test_1_2(*args)
    for i in string.ascii_lowercase:
        if i not in letters:
            out.add(i)
    return out


if __name__ == '__main__':
    test_strings = ["hello", "world", "python", ]
    print(test_1_1(*test_strings))
    print(test_1_2(*test_strings))
    print(test_1_3(*test_strings))
    print(test_1_4(*test_strings), ss == test_1_4(*test_strings))

