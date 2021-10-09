from contextlib import contextmanager


@contextmanager
def open_file(file, mode='r'):
    """Context manager for opening and working with file,
    including handling exceptions with @contextmanager decorator"""
    file_obj = open(file, mode)
    try:
        yield file_obj
    except IOError:
        print(f'IOError!!!')
    finally:
        file_obj.close()


with open_file('test_task1.txt', 'r') as res:
    print(res.read())
