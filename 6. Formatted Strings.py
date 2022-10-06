# Formatted strings are particularly useful in situations where you dynamically generate some text with your variables.
first_name = 'John'
last_name = 'Smith'
# We want to print this on terminal: " John [Smith] is a coder "
message = first_name + ' [' + last_name + '] is a coder. '
print(message)
# Perfectly works, but IT'S NOT IDEAL because as our text gets more complicated it becomes harder to visualize the -
# -output. So someone else reading this code,they have to visualize all the string concatenations in their head.
# This is where we use formatted strings, they make it easier for us to visualize the output:
# A formatted string is one that is prefixed with an f. so f,quotes. Now in between the quotes,
# First we want to add the value of the first name variable , so, we add curly braces and here we type "first_name".
# Next we add space, we add our square brackets, in between the square brackets, we want to display the last name so -
# -once again we add curly braces, and type "last_name", and finally here we type "is a coder"
msg = f'{first_name} [{last_name}] is a coder.'
print(msg)
# We use curly braces{} to dynamically insert values into your strings.
