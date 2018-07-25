class Book:
    def __init__(self,name,copies=0):
        self.name = name
        self.copies = copies

    def increase_copies(self, how_much):
        self.copies += how_much

    def decrease_copies(self, how_much):
        self.copies -= how_much

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

Python_programming.increase_copies(25)
Python_programming.decrease_copies(10)

print(Python_programming.copies)