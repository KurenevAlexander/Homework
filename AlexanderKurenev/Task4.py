def supress_except(fun):
    """Decorator for supressing exceptions. If exception not occure write 'No exceptions!' to console."""
    def wrapper(*args, **kwargs):
        result = None
        try:
            result = fun(*args, **kwargs)
        except:
            pass
        else:
            print('No exceptions!')
        return result

    return wrapper


@supress_except
def fn1():
    print('Function without exceptions')


@supress_except
def fn2():
    print('Function with exceptions')
    raise ValueError


if __name__ == '__main__':
    fn1()
    fn2()
