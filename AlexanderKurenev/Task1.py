class OpenFile:
    """Class-based context manager for opening and working with file"""
    def __init__(self, file, mode='r'):
        self.file = file
        self.mode = mode
        self.file_obj = None

    def __enter__(self):
        try:
            self.file_obj = open(self.file, self.mode)
        except FileNotFoundError as no_file_err:
            print(f'File not found - {no_file_err}')
        except ValueError as mode_err:
            print(f'Error mode - {mode_err}')
        else:
            return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_obj:
            self.file_obj.close()
        if exc_type is not None:
            print(f'Exception: {exc_type} - {exc_val} - {exc_tb}\n')


if __name__ == '__main__':
    with OpenFile('test_task1.txt', 'r') as res:
        print(res.read())
