
from datetime import date
from abc import ABC, abstractmethod
from statistics import mean
from math import ceil


class PrivateSchool():
    school_fee_sum = 25000
    def __init__(self, name):
        self.school_classes = {}
        self.headmaster = None
        self.headteacher = None
        self.teachers = []
        self.name = name
        self.school_budget = 0

    def set_headmaster(self, headmaster):
        self.headmaster = headmaster

    def set_headteacher(self, headteacher):
        self.headteacher = headteacher

    def average_mark(self):
        return mean([school_class.average_mark() for school_class in self.school_classes.values()]) #unpacking
    # list.comprehension on dict.values

    def budget_counting(self):
        all_teachers_rewards_sum = sum(teacher.reward_sum for teacher in self.teachers)
        costs = self.headmaster.reward_sum + self.headteacher.reward_sum + all_teachers_rewards_sum
        all_students_rewards = 0
        for school_class in self.school_classes.values():#loop for classes like values of dict
            all_students_rewards += sum(student.reward_sum for student in school_class.students)
        return ceil((costs+all_students_rewards)/self.__class__.school_fee_sum)

    def add_class(self, id, teacher):
        new_class = SchoolClass(id, teacher)
        self.school_classes[id] = new_class #assign new object on the key id to the new_class
        self.teachers.append(teacher)
        return new_class

    def total_remove_class(self, id):
        del self.school_classes[id]

    def remove_class_to_other(self, id, new_id):
        self.school_classes[new_id].students += self.school_classes[id].students
        del self.school_classes[id]

class SchoolClass():
    def __init__(self, id, teacher):
        self.id = id
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def print_student_list(self):
        print(f"{self.id} contains the following students:")
        for student in self.students:
            print(f"{student.name}, {student.surname}")

    def average_mark(self):
        return mean([student.average_mark for student in self.students])


class Human(ABC):
    def __init__(self,
                 name: str,
                 surname: str,
                 birth_date: date
                 ):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date

@property
def age(self):
    age = (date.today() - self.birth_date).days // 365
    return (f"This person  is {age} years old")


class PrivateSchoolStaffAudience(Human):
    def __init__(self,
                 name: str,
                 surname: str,
                 birth_date: date,
                 reward_sum: float):
        Human.__init__(self, name, surname, birth_date)
        self.reward_sum = reward_sum

    @abstractmethod
    def reward_type(self):
        pass

    @abstractmethod
    def position(self):
        pass

    def get_reward_type(self):
        return f'{self.position()}:It\'s so amazing get my {self.reward_type()}'

class Headmaster(PrivateSchoolStaffAudience):
    def reward_type(self):
        return 'salary'

    def position(self):
        return 'Headmaster'

class Headteacher(PrivateSchoolStaffAudience):
    def reward_type(self):
        return 'salary'

    def position(self):
        return 'Headteacher'

class Teacher(PrivateSchoolStaffAudience):
    def reward_type(self):
        return 'salary'

    def position(self):
        return 'Teacher'

class Student(PrivateSchoolStaffAudience):
    def __init__(self,
                 name: str,
                 surname: str,
                 birth_date: date,
                 reward_sum: float,
                 average_mark: float,
                 ):
        PrivateSchoolStaffAudience.__init__(self, name, surname, birth_date, reward_sum)
        self.average_mark = average_mark

    def reward_type(self):
        return 'reward for excellent marks'

    def position(self):
        return 'Student'

reward_type_selection = input("Enter position of the staff or audience (Headmaster, Headteacher, Teacher, Student):")
#@param ["Headmaster", "Headteacher", "Teacher", "Student"]

person = None

if reward_type_selection == "Headmaster":
    person = Headmaster("Serg", "Penkov", date(1998, 5, 25), 20000)
elif reward_type_selection == "Headteacher":
    person = Headteacher("Victor", "Kurkin", date(1995, 5, 25), 15000)
elif reward_type_selection == "Teacher":
    person = Teacher("Ivan", "Tetcher", date(1989, 5, 25), 6000)
else:
    person = Student("Vasiliy", "King", date(2010, 5, 25), 500, 12)

print(person.get_reward_type())

school_ranok = PrivateSchool("Ranok")
school_ranok.set_headmaster(Headmaster("Serg", "Penkov", date(1998, 5, 25), 20000))
school_ranok.set_headteacher(Headteacher("Victor", "Kurkin", date(1995, 5, 25), 15000))
teacher1 = Teacher("Ivan", "Tetcher", date(1989, 5, 25), 6000)
class8a = school_ranok.add_class("8-A", teacher1)
student1 = Student("Vasiliy", "King", date(2010, 5, 25), 500, 12)
student2 = Student("Ivar", "Kozinski", date(2010, 5, 25), 500, 10)
student3 = Student("Yan", "Kozlov", date(2010, 5, 25), 500, 10)
student4 = Student("Yakob", "Nizhynski", date(2010, 5, 25), 500, 5)
class8a.add_student(student1)
class8a.add_student(student2)
class8a.add_student(student3)
class8a.add_student(student4)
class8a.remove_student(student4)
class8a.print_student_list()
print(f"Class average mark is:{class8a.average_mark()}")
print(f"School average mark is:{school_ranok.average_mark()}")
print(f"We need {school_ranok.budget_counting()} two students to pay back the budget")
