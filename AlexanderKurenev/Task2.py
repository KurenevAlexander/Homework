import string


def most_common_words(filepath, number_of_words=3):
    """
    Function which search for most common words in the file.
    :param filepath: str - filename
    :param number_of_words: int - count of most common words
    :return: list
    """
    with open(filepath, 'r') as f:
        words = []
        table = str.maketrans('', '', string.punctuation)
        line = f.readline()
        while line:
            s = line.translate(table).lower()
            words.extend(s.split())
            line = f.readline()

    dct = {}
    for word in words:
        dct[word] = dct.get(word, 0) + 1

    sort_words = sorted(dct.items(), key=lambda items: -items[1])
    sort_words = sort_words[:number_of_words]

    common_words = []
    for word in sort_words:
        common_words.append(word[0])
    return common_words


if __name__ == '__main__':
    print(most_common_words('data/lorem_ipsum.txt', 3))
