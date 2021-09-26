# Look through file `modules/legb.py`.
# 1) Find a way to call `inner_function` without moving it from inside of `enclosed_function`.
# 2.1) Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope.
# 2.2) Modify ONE LINE in `inner_function` to make it print variable 'a' form enclosing function.

a = "I am global variable!"

# 1)
def enclosing_function():
    """A way to call `inner_function` without moving it from inside of `enclosed_function`."""
    a = "I am variable from enclosed function!"

    def inner_function():
        a = "I am local variable!"
        print(a)

    return inner_function


# 2.1)
def enclosing_function1():
    """Modifed ONE LINE in `inner_function` to make it print variable 'a' from global scope."""
    a = "I am variable from enclosed function!"

    def inner_function():
        global a
        print(a)

    return inner_function


# 2.2)
def enclosing_function2():
    """Modifed ONE LINE in `inner_function` to make it print variable 'a' form enclosing function."""
    a = "I am variable from enclosed function!"

    def inner_function():
        print(a)

    return inner_function


if __name__ == '__main__':
    f = enclosing_function()
    f1 = enclosing_function1()
    f2 = enclosing_function2()
    f()
    f1()
    f2()
