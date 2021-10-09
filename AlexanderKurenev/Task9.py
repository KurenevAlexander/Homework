class EvenRange:
    def __iter__(self):
        return self

    def __init__(self, start, end):
        self.__start__ = start + start % 2 - 2  # get the nearest even number on the sequence and decrease it by 2
        self.__end__ = end

    def __next__(self):
        self.__start__ += 2
        if self.__start__ < self.__end__:
            return self.__start__
        else:
            print('Out of Number!')
            raise StopIteration


if __name__ == '__main__':
    er1 = EvenRange(7, 11)
    print(next(er1))
    print(next(er1))
    #print(next(er1))

    print()

    er2 = EvenRange(3, 14)
    for number in er2:
        print(number)
