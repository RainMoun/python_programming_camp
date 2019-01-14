class Course:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_message(self):
        print("Course name: {},  price: {}.".format(self.name, self.price))


class People:
    def __init__(self, name):
        self.name = name
        self.course = []

    def print_message(self):
        for i in self.course:
            i.print_message()


class Teacher(People):
    def __init__(self, name):
        super().__init__(name)

    def print_message(self):
        if not self.course:
            print("Teacher {} doesn't teach any course".format(self.name))
        else:
            print("Teacher {} teaches following courses".format(self.name))
            super().print_message()


class Student(People):
    def __init__(self, name):
        super().__init__(name)

    def print_message(self):
        if not self.course:
            print("Student {} doesn't learn any course".format(self.name))
        else:
            print("Student {} learns following courses".format(self.name))
            super().print_message()


if __name__ == '__main__':
    course1 = Course("人工智能", 500)
    course1.print_message()
    course2 = Course("机器学习", 200)
    course3 = Course("数据挖掘", 300)
    course4 = Course("python", 1000)
    student1 = Student("Kobe")
    teacher1 = Teacher("Albert")
    student1.course.append(course1)
    student1.course.append(course3)
    teacher1.course.append(course2)
    teacher1.course.append(course4)
    student1.print_message()
    teacher1.print_message()