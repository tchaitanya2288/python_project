"""
File I/O

Read file ---> .Read()
Read line by line -------> .Readline()
"""

my_file = open("firstfile1.txt", 'r')

print(str(my_file.read()))
my_file.close()

print("================Read line by line=================")

my_file_line = open("firstfile1.txt", 'r')

print(str(my_file_line.readline()))
my_file_line.close()