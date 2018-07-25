class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_number_of_marks(self):
        return len(self.marks)

    def total_sum_of_marks(self):
        return sum(self.marks)

    def determine_max_marks(self):
        return max(self.marks)

    def determine_min_of_marks(self):
        return min(self.marks)

    def determine_avg_marks(self):
        return self.total_sum_of_marks()/self.get_number_of_marks()

    def add_new_mark(self,new_mark):
        self.marks.append(new_mark)

    def remove_mark(self,index):
        del self.marks[index]

student = Student('chaitu',[25,24,25,22,21,20])
number = student.get_number_of_marks()
maximun_mark = student.determine_max_marks()
minimum_mark = student.determine_min_of_marks()
avg_marks = student.determine_avg_marks()
student.add_new_mark(26)
student.remove_mark(3)

print(student.marks)
print(f"""Student[
      number_of_marks-{number}
      max_of_mark -{maximun_mark}
      min_of_mark- {minimum_mark}
      avg -{avg_marks}
""")