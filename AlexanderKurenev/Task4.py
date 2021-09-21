def split_by_index(s, indexes):
    """Function splits the string by indexes specified in indexes. Wrong indexes are ignored."""
    len_s = len(s)

    index_list = []  # create new list with good indexes and sort it
    for i in range(len(indexes)):
        if -len_s < indexes[i] < 0 and indexes[i] + len_s not in index_list:
            index_list.append(indexes[i] + len_s)
        elif 0 < indexes[i] < len_s and indexes[i] not in index_list:
            index_list.append(indexes[i])

    sorted_indexes = sorted(index_list)  # good and sort indexes, and all positive

    out = []  # create list for parts of string
    pos = 0
    for index in sorted_indexes:
        out.append(s[pos: index])
        pos = index
    out.append(s[pos:])
    return out


if __name__ == '__main__':
    s = input('Enter string: ')
    k = list(map(int, input('Enter indexes separated by space: ').split()))
    print(split_by_index(s, k))
