# So far we learn two built-in functions: print() and input()
# We have a few more functions for converting values into different types. So we have:
# int() for converting a string to an integer.
# We also have float() for converting a string into a float, or a number with a decimal point.
# And we also have bool() for converting a string into a boolean value.

# In python, we have a useful function for getting the type of variables: type()
birth_year = input('Birth year: ')
print(type(birth_year))
age = 2022 - int(birth_year)
print(type(age))
print(age)
