def get_digits(num):
    """Returns a tuple of a given integer's digits"""
    m = map(int, str(num))
    return tuple(m)


if __name__ == '__main__':
    print(get_digits(input()))
