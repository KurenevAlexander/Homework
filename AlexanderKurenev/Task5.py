from functools import wraps


def remember_result(func):
    """
    Decorator remembers last result of function it decorates and prints it before next call.
    """
    result = None

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal result
        print(f"Last result = '{result}'")
        result = func(*args, **kwargs)
        return result

    return wrapper


@remember_result
def sum_list(*args):
    """
    Function adds the values
    :param args: string or integer values
    :return: concatenation or sum of values
    """
    result = 0
    for a in args:
        if isinstance(a, str):
            args = tuple(map(str, args))
            result = ""

    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result


if __name__ == '__main__':
    sum_list("a", "b")
    sum_list("abc", "cde")
    sum_list(3, 4, 5)
