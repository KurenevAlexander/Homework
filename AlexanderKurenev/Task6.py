def get_shortest_word(s):
    """Returns the longest word in the given string.
    The word can contain any symbols except whitespaces"""
    return max(s.split(), key=lambda x: len(x))


if __name__ == '__main__':
    print(get_shortest_word(input()))
