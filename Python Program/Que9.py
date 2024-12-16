'''Python has many built-in functions, and if you do not know how to use it, you can read
document online or find some books. But Python has a built-in document function for
every built-in functions.
Please write a program to print some Python built-in functions documents, such as
abs(), int(), raw_input()
And add document for your own function'''


def custom_function(first_name, last_name):
    """
    This function accepts a first name and a last name as input.
    It then returns a formatted string combining the first and last names.

    Parameters:
    first_name (str): The first name of the user.
    last_name (str): The last name of the user.

    Returns:
    str: A formatted full name.
    """
    return f"Full name: {first_name} {last_name}"

# Print documentation for built-in functions
print("Documentation for abs():")
print(abs.__doc__)
print()

print("Documentation for int():")
print(int.__doc__)
print()

print("Documentation for input():")
print(input.__doc__)
print()

# Print documentation for the custom function
print("Documentation for custom_function():")
print(custom_function.__doc__)


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(custom_function(first_name, last_name))
