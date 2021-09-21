def get_pairs(lst):
    """Returns a list of tuples containing pairs of elements"""
    out = []
    length = len(lst)
    if length == 1:
        return None
    for i in range(1, length):
        out.append((lst[i - 1], lst[i]))
    return out


if __name__ == '__main__':
    print(get_pairs([1, 2, 3, 8, 9]))
    print(get_pairs(['need', 'to', 'sleep', 'more']))
