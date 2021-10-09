class MySquareIterator:
    def __iter__(self):
        return self

    def __init__(self, lst_itr):
        self.itr = lst_itr

    def __next__(self):
        if self.itr:
            return self.itr.pop(0)**2
        else:
            raise StopIteration


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    itr = MySquareIterator(lst)
    for item in itr:
        print(item)