class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        match = False
        if isinstance(lecturer, Lecturer):
            for student_course in self.courses_in_progress:
                for lect_course in lecturer.courses_attached:
                    if student_course == lect_course:
                        match = True
                        break
        else:
            return "ошибка"
        if match == True and 0 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "ошибка"

    def __str__(self):
        if len(self.grades) > 0:
            summ = 0
            for value in self.grades.values():
                summ += sum(value)
            average = summ/len(self.grades)
        else:
            average = 0
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСрденяя оценка за задания: {average}\
    \nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент')
        else:
            if len(self.grades) > 0:
                summ = 0
                for value in self.grades.values():
                    summ += sum(value)
                self_average = summ / len(self.grades)
            else:
                self_average = 0
            if len(other.grades) > 0:
                summ = 0
                for value in other.grades.values():
                    summ += sum(value)
                other_average = summ / len(other.grades)
            else:
                other_average = 0
        return self_average < other_average


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress \
                and hasattr(self, 'reviewing'):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.reviewing = True

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.lecturing = True
        self.grades = {}

    def __str__(self):
        if len(self.grades) > 0:
            summ = 0
            for value in self.grades.values():
                summ += value
            average = summ/len(self.grades)
        else:
            average = 0
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {average}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор')
        else:
            if len(self.grades) > 0:
                summ = 0
                for value in self.grades.values():
                    summ += sum(value)
                self_average = summ / len(self.grades)
            else:
                self_average = 0
            if len(other.grades) > 0:
                summ = 0
                for value in other.grades.values():
                    summ += sum(value)
                other_average = summ / len(other.grades)
            else:
                other_average = 0
            return self_average < other_average


def count_average_by_students(course):
    pass  # Заготовка под функцию подсчета средней оценки за дз по всем студентам в рамках определенного курса


def count_average_by_lecturers(course):
    pass  # Загтовка под функцию подсчета средней оценки студентов преподавателям определенного курса


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
simple_student = Student('Vasiliy', 'Samoylov', 'your_gender')
simple_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

the_reviewer = Reviewer('Pythonist', 'Megalector')
the_reviewer.courses_attached += ['Python']

some_lector = Lecturer('Ivan', 'Petrov')
some_lector.courses_attached += ['Python']
the_lector = Lecturer('Sergey', 'Sidorov')
the_lector.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)  # Вызовы от ментора (только лишь) теперь не работают
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

the_reviewer.rate_hw(best_student, 'Python', 10)

simple_student.rate_lect(some_lector, 'Python', 10)  # Временно можно здесь проверить работу переопределенных оперторов
# сравнения, введя оценку меньше 9ти
best_student.rate_lect(the_lector, 'Python', 9)


print(best_student.grades)
print(the_reviewer)
print(best_student)
print(some_lector < the_lector)
print(simple_student < best_student)
