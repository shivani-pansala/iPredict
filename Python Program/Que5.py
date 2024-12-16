'''Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3'''

sentence = input("Enter a sentence =")

sentence = sentence.split()

letters = 0
digits = 0

for word in sentence:
    for ch in word:
         if ch.isalpha():
            letters += 1
         elif ch.isdigit():
            digits += 1

print("LETTERS = ", letters)

print("DIGITS = ", digits)

''' Output
Enter a sentence =hello world! 123
LETTERS =  10
DIGITS =  3'''