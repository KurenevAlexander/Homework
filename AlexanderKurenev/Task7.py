def foo(lst):
    """Function returns a new list such that each element at index i
    of the new list is the product of all the numbers in the original array except the one at i"""
    p = 1
    out_lst = []
    for i in lst:
        p *= i
    for i in lst:
        out_lst.append(p // i)
    return out_lst


if __name__ == '__main__':
    k = list(map(int, input('Enter numbers separated by space: ').split()))
    print(foo(k))
