'''Write a program that accepts a sequence of whitespace separated words as input and
prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''

str = input("Enter a separated  words =")

words = str.split()

unique_words = sorted(set(words))

print(" ".join(unique_words))

'''Output
Enter a separated  words =hello world and practice make perfect and hello world agin

agin and hello make perfect practice world
'''
