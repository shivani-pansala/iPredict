'''Please write a program which count and print the numbers of each character in a string
input by console.'''

line = input("Please enter a string = ")
line.lower()

for i in range(0, len(line)):
     count = 0
     for j in range(0, len(line)):
          if(line[i] == line[j]):
                count += 1
     print(f" '{line[i]}' = {count} times")
     

'''Output
Please enter a string = helloo
 'h' = 1 times
 'e' = 1 times
 'l' = 2 times
 'l' = 2 times
 'o' = 2 times
 'o' = 2 times
'''
     


