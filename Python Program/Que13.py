'''Please write a binary search function which searches an item in a sorted list. The
function should return the index of element to be searched in the list.'''

numbers = [50,30,10,60,80,40,90]
numbers.sort()
print(numbers)

low = 0
high = len(numbers)-1

num = int(input("Enter a  number to search : "))

while low <= high:
     mid = (low + high) // 2
     
     if numbers[mid] == num:
           print(f"The number {num} is present in the {mid}")
           break
     elif numbers[mid] < num:
          low = mid + 1
          
     else:
          high = mid - 1
        
else:
    print(f"The number {num} is not present in the list.")

'''Output
[10, 30, 40, 50, 60, 80, 90]
Enter a  number to search : 60
The number 60 is present in the 4
'''