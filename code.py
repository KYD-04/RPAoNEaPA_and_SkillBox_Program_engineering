import unittest
from datetime import datetime
from app import Course, Meeting

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

    course = next((c for c in courses if c.id == course_id), None)
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

class TestCourseMeeting(unittest.TestCase):
    def setUp(self):
        self.course = register_course(
            student_ids=[1, 2, 3],
            teacher_ids=[1, 2],
            name="Программирование на Python",
            description="Изучение основ Python"
        )

    def test_register_course(self):
        self.assertEqual(self.course.name, "Программирование на Python")
        self.assertEqual(self.course.students, [1, 2, 3])
        self.assertEqual(self.course.teachers, [1, 2])
        print("test_register_course: OK")

    def test_create_meeting(self):
        meeting = create_meeting(
            course_id=self.course.id,
            student_ids=[1, 2, 3],
            teacher_ids=[1],
            name="Введение в Python",
            description="Первая лекция по Python",
            link="https://meet.example.com",
            date_time=datetime(2025, 4, 1, 14, 0)
        )
        self.assertEqual(meeting.name, "Введение в Python")
        self.assertEqual(meeting.invitees, [1, 2, 3])
        self.assertEqual(meeting.organizers, [1])
        print("test_create_meeting: OK")

if __name__ == "__main__":
    unittest.main()