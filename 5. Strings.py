# you could use both single and double quotes to define a string, but there are times you have to use a specific form,
# otherwise you're going to run into issues. Here's an example:
course_1 = 'Python for Beginners'
course_2 = "Python's course for Beginners"
course_3 = 'Python for "Beginners"'

# Triple quotes:
course_4 = '''
Hi John,
Here is our first email to you.

Thank you,
The support team

'''

# We're going to use square brackets[] to get a character and a given index in this string:
course_5 = 'Python for Beginners'
#           012345
print(course_5[0])


# We can also use a negative index here. so with a negative index we can get the characters started from the end;
# -1 is the index of the last character:
course_6 = 'Python for Beginners'
print(course_6[-1])
print(course_6[-2])


# We can also use a similar syntax to extract a few characters instead of just 1 character.
# For example, if we type 0, colon 3, Python interpreter will return all the characters starting with first index all -
# -the way to the second index, but it does not return the character at index 3.
# In other words, back to these indexes you have 0, 1, 2, 3, and so on. When you run this program; Pyton interpreter -
# -will return the characters staring from the index 0 all the way to index 3, but excludes the character and index 3.
course_7 = 'Python for Beginners'
#           012345
print(course_7[0:3])


# So if we don't supply the end index, Python will return all the characters to the end of the string.
course_8 = 'Python for Beginners'
#           012345
print(course_8[0:])
print(course_8[1:])  # so "P" is removed.

# So if we don't apply the first index but add an end index like 5. Python interpreter will assume 0 as the start index.
course_8 = 'Python for Beginners'
#           012345
print(course_8[:5])

# What if we leave both the start and end index? Now in this case 0 will be assumed as the start index,
# and the length of the string will assume as the end index. so with this syntax,
# you can basically copy or clone a string.
course_8 = 'Python for Beginners'
#           012345
another = course_8[:]
print(another)
