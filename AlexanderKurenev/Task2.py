import string


def polindrom(s):
    """Function returns True if "s" is a polyindrome, otherwise false"""
    table = str.maketrans('', '', string.punctuation + ' ')
    s = s.translate(table).lower()
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True


if __name__ == '__main__':
    print(polindrom(input()))
