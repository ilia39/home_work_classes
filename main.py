class Student:
    student_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list += [self]

    def rate_lecturer(self, lecturer, course, grade):
        match = False
        if isinstance(lecturer, Lecturer):
            for student_course in self.courses_in_progress:
                for lecturer_course in lecturer.courses_attached:
                    if student_course == lecturer_course:
                        match = True
                        break
        else:
            return "ошибка: не лектор"
        if match is False:
            return "ошибка: курсы студента и лектора не соответствуют"
        if 0 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "ошибка: можно ставить оценку в пределах от 0 до 10"

    def __str__(self):
        average = get_average(self)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСрденяя оценка за \
задания: {average}\nКурсы в процессе изучения: {self.courses_in_progress}\
\nЗавершенные курсы: {self.finished_courses}\n'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент')
        else:
            self_average = get_average(self)
            other_average = get_average(other)
            return self_average < other_average


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.reviewing = True

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'


class Lecturer(Mentor):
    lecturer_list = []

    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}
        Lecturer.lecturer_list += [self]

    def __str__(self):
        average = get_average(self)
        return f'Имя: {self.name}\nФамилия: {self.surname}\
\nСредняя оценка: {average}\n'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('ошибка: не лектор')
        else:
            self_average = get_average(self)
            other_average = get_average(other)
            return self_average < other_average


def count_average_by_students(students, course):
    res_students = []
    full_list_accepted = True
    for student in students:
        if isinstance(student, Student) and (course in student.courses_in_progress
                                             or course in student.finished_courses):
            res_students += [student]
        else:
            full_list_accepted = False
    if full_list_accepted is False:
        print('Среднее значение будет посчитано только для тех студентов\
, кто учился или учится на заданном курсе\n')
    summa = 0
    count = 0
    for student in res_students:
        if len(student.grades) == 0:
            continue
        else:
            summa += sum(student.grades[course])
            count += len(student.grades[course])
    if summa == 0:
        return 0
    else:
        average = summa / count
        # print(summa, count) # Так проверить легче
        return average


def count_average_by_lecturers(lecturers, course):
    res_lecturers = []
    full_list_accepted = True
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            res_lecturers += [lecturer]
        else:
            full_list_accepted = False
    if full_list_accepted is False:
        print('Среднее значение будет посчитано только для тех лекторов\
, кому прикреплен заданный курс\n')
    summa = 0
    count = 0
    for lecturer in res_lecturers:
        if len(lecturer.grades) == 0:
            continue
        else:
            summa += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    if summa == 0:
        return 0
    else:
        average = summa / count
        # print(summa, count) # Так проверить легче
        return average


def get_average(graded_class):
    if len(graded_class.grades) > 0:
        summa = 0
        count = 0
        for key in graded_class.grades.keys():
            summa += sum(graded_class.grades[key])
            count += len(graded_class.grades[key])
    else:
        return 0
    average = summa / count
    return average


best_student = Student('Ruy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
simple_student = Student('Vasiliy', 'Samoylov', 'your_gender')
simple_student.courses_in_progress += ['JavaScript']
third_sudent = Student('Third', 'One', 'your_gender')
third_sudent.finished_courses += ['Python']
third_sudent.grades = {'Python': [7, 10]}

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
some_mentor = Mentor('Vasiliy', 'Sergeev')
cool_mentor.courses_attached += ['Python']

the_reviewer = Reviewer('Pythonist', 'Megalector')
the_reviewer.courses_attached += ['Python']
some_reviewer = Reviewer('NonPythonist', 'Lectorov')
some_reviewer.courses_attached += ['Marketing']
more_reviewer = Reviewer('One', 'More')
more_reviewer.courses_attached += ['Python']

some_lector = Lecturer('Ivan', 'Petrov')
some_lector.courses_attached += ['Python']
the_lector = Lecturer('Sergey', 'Sidorov')
the_lector.courses_attached += ['JavaScript', 'Python']

print(the_reviewer.rate_hw(simple_student, 'Python', 10))
print(simple_student.rate_lecturer(some_lector, 'Python', 10))
best_student.rate_lecturer(the_lector, 'Python', 9)
simple_student.rate_lecturer(the_lector, 'JavaScript', 10)
the_reviewer.rate_hw(best_student, 'Python', 10)
more_reviewer.rate_hw(best_student, 'Python', 8)

print(best_student.grades)
print(best_student)
print(the_reviewer)
print(the_lector)
print(the_lector.__dict__)
print(some_lector > the_lector)
print(simple_student < best_student)

print(f"Средняя оценка по студентам: "
      f"{count_average_by_students(Student.student_list, 'Python')}\n")
print(f"Средняя оценка по лекторам: "
      f"{count_average_by_lecturers(Lecturer.lecturer_list, 'Python')}\n")
