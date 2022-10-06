course = 'Python for Beginners'
# Now to calculate the number of characters in this string, you can use a built-in function called len().
print(len(course))
# This is particularly useful when you receive input from the user.
# For example, you have noticed that when you fill out a form online, each input field often has a limit.
# For example, you might have 50 characters for your name, so using this len() function we can enforce a limit on -
# -the number of characters in an input field. if the user types in more characters than we allow them,
# -We can display an error.
# So this len() function it's a general purpose function, so it's not limited to count the number of characters in -
# -a string.

# We have functions for converting all these characters to upper case or lower case. To access these functions we use -
# -the dot operator:
course.upper()
# Because this function is specific to a string, we refer to this as a method. In contrast, len() and print() are -
# -general purpose functions, they don't belong to strings or numbers or other kinds of objects.
# So this is the difference between functions and methods.
print(course.upper())
# Note: This method doesn't change or modify our original string, In fact it creates a new string and returns it.
# So if we print(course) right after we call the upper method, we can see that our course variable still has it's -
# -original form.
print(course)  # It's not modified.


# Converting a string into lower case:
print(course.lower())

# Converting the first letter of each word into upper case (like a title):
print(course.title())

# There are times that you want to find a character or a sequence of characters in a string.
# In those situations you can use find() method:
print(course.find('P'))
# And this will return the index of the first occurrence of that character.
# NOTE: The find() method is case-sensitive, so it's sensitive to lower case or upper case characters.

# We can also pass a sequence of characters:
print(course.find('Beginners'))
# And we get 11 because the Beginners starts with index 11.


# Now we also have method for replacing a character or a sequence of characters, and that is called replace().
print(course.replace('Beginners', 'Absolute Beginners'))
print(course.replace('P', 'J'))

# There are times that you want to check the existence of a character or a sequence of characters in your string.
# In those situations you use the "in" operator. So we refer to this expression as a boolean expression.
print('Python' in course)

# RECAP:
# len()
# course.upper()
# course.lower()
# course.title()
# course.find()
# course.replace()
# in operator => '...' in course
