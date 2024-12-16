'''Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the
value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106'''

a = input("Enter a digit: ")

str_a = str(a)

a1 = str_a*1
a2 = str_a*2
a3 = str_a*3
a4 = str_a*4

total = int(a1) + int(a2) + int(a3) + int(a4)

print(total)

'''Output
Enter a digit: 9
11106
'''
