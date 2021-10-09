from contextlib import ContextDecorator
from time import time, sleep


class TimeLog(ContextDecorator):
    """Decorator with context manager support for writing execution time to log-file"""
    def __enter__(self):
        self.start_time = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time()
        with open('logfile.log', 'a') as f:
            f.write(f'Time = {self.end_time - self.start_time}\n')
        return False


@TimeLog()
def fn():
    sleep(2)


if __name__ == '__main__':
    fn()
