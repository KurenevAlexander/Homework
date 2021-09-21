import string


def my_split(s, sep=None, maxsplit=-1):
    """Function works the same as str.split method"""
    separ = []  # create list with separators
    if sep is None:
        separ.extend(string.whitespace)
    else:
        separ.append(sep)

    out = []  # result list
    num_split = 0  # split counter

    while True:
        no_find_count = 0  # counter of unsuccessful delimiter lookups
        if num_split == maxsplit:
            break
        for sp in separ:
            pos = s.find(sp)
            if pos >= 0:
                out.append(s[:pos])
                s = s[pos + len(sp):]
                num_split += 1
            else:
                no_find_count += 1
        if no_find_count == len(separ):
            break
    out.append(s)
    return out


if __name__ == '__main__':
    a = 'hello velo pela good'
    print(my_split(a, ' ', 0))
    print(a.split(' ', 0))
    print(my_split(a))
    print(a.split())
    print(my_split(a, ' '))
    print(a.split(' '))
    print(my_split(a, 'o'))
    print(a.split('o'))
    print(my_split(a, 'el'))
    print(a.split('el'))
    print(my_split(a, 'el', 2))
    print(a.split('el', 2))
