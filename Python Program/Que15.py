'''Create 1 CSV file with (,) separated and read that file using Python and print in
Dictionary.
The output should be in sorted order by Roll_no
'''

import csv

with open('students.csv', mode='r') as file:
    reader = csv.DictReader(file)
    rows = list(reader)

sorted_rows = sorted(rows, key=lambda x: int(x['Roll_no']))

for row in sorted_rows:
    print(f"{{roll_no:{row['Roll_no']}, first_name:{row['first_name']}, last_name:{row['last_name']}, gender:{row['gender']}, dob:{row['dob']}}}")

'''Output
roll_no:10, first_name:aaa, last_name:asd, gender:male, dob:20/07/1992}
{roll_no:11, first_name:abc, last_name:xyz, gender:male, dob:12/12/2000}
{roll_no:12, first_name:xya, last_name:asd, gender:female, dob:15/07/1992}
'''
     