class MyNumberCollection:
    """Custom collection of numbers"""
    def __init__(self, start, end=0, step=1):
        self.__collection = []

        if isinstance(start, (list, tuple)):
            for item in start:
                if not isinstance(item, (float, int)):
                    raise TypeError(f'MyNumberCollection supports only numbers!')
            self.__collection = list(start)
        else:
            self.__collection = [item for item in range(start, end, step)]
            self.__collection.append(end)

        self.__iterator = iter(self.__collection)

    def append(self, item):
        if not isinstance(item, (float, int)):
            raise TypeError(f"'{item}' - object is not a number!")
        self.__collection.append(item)

    def __add__(self, other):
        return self.__collection + other.__collection

    def __getitem__(self, index):
        return self.__collection[index] ** 2

    def __iter__(self):
        return self.__iterator

    def __next__(self):
        next(self.__iterator)

    def __repr__(self):
        return str(self.__collection)


if __name__ == '__main__':
    col1 = MyNumberCollection(0, 5, 2)
    print(col1)

    col2 = MyNumberCollection((1, 2, 3, 4, 5))
    print(col2)

    #col3 = MyNumberCollection((1, 2, 3, "4", 5))

    col1.append(7)
    print(col1)

    #col2.append("string")

    print(col1 + col2)

    print(col1)
    print(col2)
    print(col2[4])

    for item in col1:
        print(item)
