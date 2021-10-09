class CustomBaseException(Exception):
    pass


class NotNumError(CustomBaseException):
    pass


class NotEvenError(CustomBaseException):
    pass


class NotGreatTwoError(CustomBaseException):
    pass


def test_num(n):
    if not isinstance(n, int):
        raise NotNumError
    if n <= 2:
        raise NotGreatTwoError
    if n % 2 != 0:
        raise NotEvenError
    return True


if __name__ == '__main__':
    print(test_num(6))
