def endless_generator():
    n = 1
    while True:
        yield n
        n += 2


if __name__ == '__main__':
    gen = endless_generator()
    while True:
        print(next(gen))
