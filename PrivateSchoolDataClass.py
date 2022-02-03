
from datetime import date
from abc import ABC
from statistics import mean
from dataclasses import dataclass, field
from enum import Enum, unique

class EmptyGroupException(Exception):
    pass

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
        return self.__class__.school_fee_sum-(costs+all_students_rewards)

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

    def budget_check(self):
        school_classes_empty = []
        for school_class in self.school_classes.values():
            if len(school_class.students) == 0:
                school_classes_empty.append(school_class.id)
        if len(school_classes_empty) > 0:
            raise EmptyGroupException(
                        f"Unfortunatly {self.name} havn't sufficient number of "
                        f"students in the {[*school_classes_empty]}"
                    )

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

@unique
class Gender(Enum):
    female = "F"
    male = "M"
    non_binary = "NB"

@dataclass
class Human(ABC):
      name: str = field(compare=False)
      surname: str = field(compare=False)
      birth_date: date = field(compare=False)
      gender: Gender = field(compare=False)

      def __post_init__(self):
          if not isinstance(self.birth_date, date):
              raise TypeError(
                  f"Incorrect data type of 'birth_date' parameter: {type(self.birth_date)}. Should be: datetime.date(YYYY-MM-DD)!")

      @property
      def age(self):
        return (date.today() - self.birth_date).days // 365

@dataclass
class PrivateSchoolStaffAudience(Human):
    reward_sum: float

    def __post_init__(self):
        if not isinstance(self.birth_date, date):
            raise TypeError(
                f"Incorrect data type of 'birth_date' parameter: {type(self.birth_date)}. Should be: datetime.date(YYYY-MM-DD)!")


@dataclass
class Headmaster(PrivateSchoolStaffAudience):
    pass

@dataclass
class Headteacher(PrivateSchoolStaffAudience):
    pass

@dataclass
class Teacher(PrivateSchoolStaffAudience):
    pass

@dataclass(order=True)
class Student(PrivateSchoolStaffAudience):
    average_mark: float = field(compare=False)
    sort_index: int = field(init=False, repr=False, compare=True)

    def __post_init__(self):
        if not isinstance(self.birth_date, date):
            raise TypeError(
                f"Incorrect data type of 'birth_date' parameter: {type(self.birth_date)}. Should be: datetime.date(YYYY-MM-DD)!")

        self.sort_index = self.age


school_ranok = PrivateSchool("Ranok")
school_ranok.set_headmaster(Headmaster("Serg", "Penkov", date(1998, 5, 25), Gender.male, 20000))
school_ranok.set_headteacher(Headteacher("Victor", "Kurkin", date(1995, 5, 25), Gender.male, 15000))
teacher1 = Teacher("Ivan", "Tetcher", date(1989, 5, 25), Gender.non_binary, 6000)
teacher2 = Teacher("Zana", "Van zein", date(1989, 5, 25), Gender.female, 6000)
class8a = school_ranok.add_class("8-A", teacher1)
class9a = school_ranok.add_class("9-A", teacher2)
student1 = Student("Vasiliy", "King", date(2011, 5, 25), Gender.non_binary, 500, 12)
student2 = Student("Ivar", "Kozinski", date(2010, 5, 25), Gender.male, 500, 10)
student3 = Student("Yan", "Kozlov", date(2010, 5, 25), Gender.male, 500, 10)
student4 = Student("Yakob", "Nizhynski", date(2010, 5, 25), Gender.male, 500, 5)
student5 = Student("Dirk", "King", date(2011, 5, 25), Gender.non_binary, 500, 12)
student6 = Student("Mathew", "Kozinski", date(2010, 5, 25), Gender.male, 500, 10)
class8a.add_student(student1)
class8a.add_student(student2)
class8a.add_student(student3)
class8a.add_student(student4)
class9a.add_student(student5)
class9a.add_student(student6)
# class8a.remove_student(student4)
class8a.print_student_list()
class9a.print_student_list()
print(f"Class average mark is:{class8a.average_mark()}")
print(f"School average mark is:{school_ranok.average_mark()}")
print(f"We have budget {school_ranok.budget_counting()}")
students = [student1, student2, student3, student4]
students.sort()
for student in students:
    print(f"{student.name} {student.surname}. Age: {student.age}. Gender: {student.gender.name}")
for i in students:
    class8a.remove_student(i)
print(f"We have budget {school_ranok.budget_counting()}")
print(len(class9a.students))
students1 = [student5, student6]
for i in students1:
    class9a.remove_student(i)
school_ranok.budget_check()


