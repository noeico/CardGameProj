from Exercise_student.Course import Course

class Student:
    def __init__(self, ID, name, age, ):


        self.ID = ID
        self.name = name
        self.age = age
        self.sub_grades = {}

    def add_grade(self, subject, grade):
        self.sub_grades.update({subject : grade})


    def __str__(self):
        return f"ID:{self.ID} Name:{self.name} Age:{self.age}Subjects and Grades: {self.sub_grades}"


    def calc_factor(self, subject, factor):
        old_grade = self.sub_grades[subject]
        new_grade = (old_grade + (old_grade/factor))
        if new_grade > 100:
            new_grade = 100
        self.sub_grades[subject] = new_grade

    def average(self):
        dict_length = len(list(dict))
        sum_of_grades = 0
        for subject in range(1, dict_length + 1):
            sum_of_grades += self.sub_grades[subject]
        average = sum_of_grades/(dict_length+1)
        return average


    def __eq__(self, other):
        return self.ID == other.ID

    def __gt__(self, other):
        return self.age > other.age



student1 = Student(123, 'noei', 'co')
student1.add_grade('math' , 85)
print (student1)
student1.calc_factor('math', 10)
print (student1)



