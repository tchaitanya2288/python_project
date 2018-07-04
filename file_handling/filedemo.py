"""
File I/O

'w'  --> Write-Only mode
'r'  --> Read-Only mode
'r+' --> Read and Write mode
'a'  --> Append mode
"""

my_list = [1,'chaitu',2,'praveen',3]

my_file = open("firstfile.txt", 'w')

for item in my_list:
    my_file.write(str(item) + "\n")

my_file.close()

