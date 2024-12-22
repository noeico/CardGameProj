from Exercise_student.Student import Student


class Course:
    def __init__(self, course_num, course_name, max_capacity):
        if course_num  < 0:
            raise TypeError("Course number must be more than 0 !!")
        if type(course_num) != int:
            raise TypeError("Course number must be an integer !!")
        self.course_num = course_num
        if type(course_name) != str:
            raise TypeError("course name has to be a String !!")
        self.course_name = course_name
        if max_capacity  < 0:
            raise TypeError("max capacity for the course has to be more than 0 !!")
        self.max_capacity = max_capacity
        self.subject_teachers ={}
        self.students_list=[]



    def __str__(self):
        return f"course number: {self.course_num}course name: {self.course_name}max capacity: {self.max_capacity}"

    def students(self):
        return self.max_capacity

   # def add_factor(self,subject, factor_percent):
        #for student in self.students_list:


    def add_student(self,student):
        if len(self.students_list) < self.max_capacity:
            self.students_list.append(student)

    def del_student(self, student):
        if student in self.students_list:
            self.students_list.remove(student)

    def average(self):
        return {stu.ID: stu.average() for stu in self.students_list}

    def weak_students(self):
        stupid_students = []
        averages = self.average()
        minn = min(averages.values())
        for id, grade in averages:
            if grade == minn:
                stupid_students.append(id)
        return stupid_students



course1 = Course(34,"Math", 150)

course1.add_student()
