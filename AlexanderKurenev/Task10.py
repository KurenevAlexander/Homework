def generate_squares(num):
    """Function takes a number as an argument and returns a dictionary,
    where the key is a number and the value is the square of that number"""
    d = {k: k * k for k in range(1, num + 1)}
    return d


if __name__ == '__main__':
    print(generate_squares(int(input())))
