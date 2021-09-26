# Task 5.7*
# 1) Run the module `modules/mod_a.py`. Check its result. Explain why does this happen.

# Result: 5

# This result was obtained because:
# 1. the program is executed line by line.
# In the first line, module C was imported and the interpreter executed the code inside it.
# "X = 5" appeared in the namespace of module C.
# 2. After that, the import of the module B was carried out.
# When the code was executed inside this module, the repeated import of the module C was not
# performed (the import of the module is done once). But the code mod_c.x = 5 was executed.
# 3. the output of mod_c.x was executed. There was obviously 5.


# 2) Try to change x to a list `[1,2,3]`. Explain the result.

# Result: 5

# If in module C we replace x with the list `[1,2,3]` and execute module A,
# then when module B is imported and its code mod_c.x = 5 is executed,
# the value of x will be overwritten with "x = 5".

# 3) Try to change import to `from x import *` where x - module names. Explain the result.
#
# Result: 5

# All variables of modules C and B will fall into the namespace of module A.
# The value of the variable x of module C will be overwritten when importing and executing the code of module B.
