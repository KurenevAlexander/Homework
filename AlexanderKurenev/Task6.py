from functools import wraps


def call_once(func):
    """
    Decorator runs a function or method once and caches the result.
    All consecutive calls to this function should return cached result no matter the arguments.
    """
    result = None

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal result
        if result is None:
            result = func(*args, *kwargs)
        return result

    return wrapper


@call_once
def sum_of_numbers(a, b):
    """
    Function adds two values
    :param a: value
    :param b: value
    :return: a + b
    """
    return a + b


print(sum_of_numbers(13, 42))
print(sum_of_numbers(999, 100))
print(sum_of_numbers(134, 412))
print(sum_of_numbers(856, 232))
