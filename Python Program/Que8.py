'''Write a program to compute the frequency of the words from the input. The output
should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python
3.'''

sentance = input("Enter the line you want to compute the frequency = ")
sentance.lower()

words = sentance.split()

word_count = {}

for word in words:
     if word in word_count:
          word_count[word] += 1
     else:
          word_count[word] = 1

sorted_word = sorted(word_count.items())

for word, count in sorted_word:
     print(f"{word}: {count}")
     
'''Output
Enter the line you want to compute the frequency = New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python
2: 2
3?: 1
New: 1
Python: 5
Read: 1
and: 1
between: 1
choosing: 1
or: 2
to: 1
'''