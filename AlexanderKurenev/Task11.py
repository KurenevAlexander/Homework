def endless_fib_generator():
    n1 = 0
    n2 = 1
    while True:
        n1, n2 = n2, n1 + n2
        yield n1


if __name__ == '__main__':
    gen = endless_fib_generator()
    while True:
        print(next(gen))
