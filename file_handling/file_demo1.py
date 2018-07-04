ex_list = ['chaitu',1988,'Febuary','female']

ex_file = open("C:\\Users\\Chaithanya\\Desktop\\samplefile.txt", 'w')

for a in ex_list:
    ex_file.write(str(a) + "\n")

ex_file.close()