class Student:
    def __init__(self, id, first_name, last_name, middle_name, age):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.age = age
        self.courses = []

    def add_course(self, course_id):
        self.courses.append(course_id)

class Teacher:
    def __init__(self, id, first_name, last_name, middle_name, age):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.age = age
        self.courses = []

    def add_course(self, course_id):
        self.courses.append(course_id)

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