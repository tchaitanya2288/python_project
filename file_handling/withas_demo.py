# print("Normal write starts")
#
# my_write = open("withas.txt", "w")
# my_write.write("TRying to write to the file")
# my_write.close()
#
# print("Normal read starts")
# my_read = open("withas.txt", "r")
# print(str(my_read.read()))

print("with as write starts")
with open("withas.txt","w")as with_as_write:
    with_as_write.write("This is an example of with as write/read")

print()
with open("withas.txt","r")as with_as_read:
    print(str(with_as_read.read()))

