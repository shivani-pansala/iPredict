'''You are required to write a program to sort the (name, age, height) tuples by ascending
order where name is string, age and height are numbers. The tuples are input by
console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name &gt; age &gt; score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[(&#39;John&#39;, &#39;20&#39;, &#39;90&#39;), (&#39;Jony&#39;, &#39;17&#39;, &#39;91&#39;), (&#39;Jony&#39;, &#39;17&#39;, &#39;93&#39;), (&#39;Json&#39;, &#39;21&#39;, &#39;85&#39;), (&#39;Tom&#39;,
&#39;19&#39;, &#39;80&#39;)]'''

data = []
num = int(input("Enter the number of students = "))

print("Enter student details = ")

for i in range(num):
     name, age, height = input().split(",")
     data.append((name, int(age), int(height)))

data.sort(key=lambda x: (x[0], x[1], x[2]))
       
print(data)
          
'''Output
Enter the number of students = 5
Enter student details = 
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
[('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85), ('Tom', 19, 80)]
  '''   