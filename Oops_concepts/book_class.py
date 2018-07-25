class Book:
    def __init__(self,name):
        self.name = name


art_science = Book("The Art of Science")
Python_programming = Book("THe Python Programm in 100 steps")
art_journals = Book("The Journals")
#
# art_science.name = "The Art of Science"
# Python_programming.name = "THe Python Programm in 100 steps"
# art_journals.name = "The Journals"
#
print(art_journals.name)
print(art_science.name)
print(Python_programming.name)