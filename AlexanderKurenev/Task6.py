from Task5 import *


def is_prime(n):
    """Function checks that the number n is prime"""
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    else:
        return True


def goldbach_test(n):
    """Function take number for proving Goldbach's conjecture
    and return tuple of two numbers if conjecture is correct or (0, 0) otherwise"""
    if n == 4:
        return 2, 2
    else:
        for j in range(3, n):
            if is_prime(j) and is_prime(n - j):
                return j, n - j
        return 0, 0


if __name__ == '__main__':
    while True:
        a = input(f'Enter number or "q" for exit: ')
        if a == 'q':
            exit(0)
        try:
            a = int(a)
            if test_num(a):
                res = goldbach_test(a)
                if res != (0, 0):
                    print(f'{res[0]} + {res[1]} = {a}')
                else:
                    print(f'No numbers!')
        except ValueError:
            print(f'Enter number!')
        except NotEvenError:
            print(f'Enter even number!')
        except NotGreatTwoError:
            print(f'Enter number greater than 2')
