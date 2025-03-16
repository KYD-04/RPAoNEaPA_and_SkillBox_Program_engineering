from datetime import datetime
class Person:
    def __init__(self, id, first_name, last_name, middle_name, age):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.age = age
        self.courses = []

    def add_course(self, course_id):
        self.courses.append(course_id)

class Student(Person):
    pass

class Teacher(Person):
    pass

class Course:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
        self.students = []
        self.teachers = []
        self.meetings = []

    def add_student(self, student_id):
        self.students.append(student_id)

    def add_teacher(self, teacher_id):
        self.teachers.append(teacher_id)

    def add_meeting(self, meeting_id):
        self.meetings.append(meeting_id)

class Meeting:
    def __init__(self, id, name, description, organizers, invitees, link, date_time):
        self.id = id
        self.name = name
        self.description = description
        self.organizers = organizers
        self.invitees = invitees
        self.link = link
        self.date_time = date_time

courses = []
meetings = []

def register_course(student_ids, teacher_ids, name, description):
    course_id = len(courses) + 1
    course = Course(course_id, name, description)
    
    for student_id in student_ids:
        course.add_student(student_id)
    
    for teacher_id in teacher_ids:
        course.add_teacher(teacher_id)
    
    courses.append(course)
    return course

def create_meeting(course_id, student_ids, teacher_ids, name, description, link, date_time):
    course = None
    for c in courses:
        if c.id == course_id:
            course = c
            break
    if not course:
        raise ValueError("Курс с указанным id не найден")
    
    for student_id in student_ids:
        if student_id not in course.students:
            raise ValueError(f"Студент с id {student_id} не зарегистрирован на курс")
    
    for teacher_id in teacher_ids:
        if teacher_id not in course.teachers:
            raise ValueError(f"Преподаватель с id {teacher_id} не зарегистрирован на курс")

    if date_time < datetime.now():
        raise ValueError("Дата встречи уже прошла")

    meeting_id = len(meetings) + 1
    meeting = Meeting(meeting_id, name, description, teacher_ids, student_ids, link, date_time)
    
    course.add_meeting(meeting.id)
    meetings.append(meeting)
    return meeting