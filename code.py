import unittest
from datetime import datetime

# Управление пользователями (плохая структура)
class User:
    def __init__(self, id, username, password, email, role):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.role = role
        self.notifications = []
        self.courses = []

    def add_notification(self, message):
        self.notifications.append(message)

    def add_course(self, course_id):
        self.courses.append(course_id)

    def authenticate(self, username, password):
        return self.username == username and self.password == password

class UserManager:
    def __init__(self):
        self.users = []

    def register_user(self, username, password, email, role):
        user_id = len(self.users) + 1
        user = User(user_id, username, password, email, role)
        self.users.append(user)
        return user

    def authenticate_user(self, username, password):
        for u in self.users:
            if u.username == username and u.password == password:
                return u
        return None

# Управление уведомлениями (дублирование и плохая структура)
class Notification:
    def __init__(self, id, user_id, message, date_time):
        self.id = id
        self.user_id = user_id
        self.message = message
        self.date_time = date_time

class NotificationManager:
    def __init__(self):
        self.notifications = []

    def add_notification(self, user_id, message, date_time):
        notification_id = len(self.notifications) + 1
        notification = Notification(notification_id, user_id, message, date_time)
        self.notifications.append(notification)
        return notification

# Управление отчетами (дублирование и плохая структура)
class Report:
    def __init__(self, id, user_id, content, date_time):
        self.id = id
        self.user_id = user_id
        self.content = content
        self.date_time = date_time

class ReportManager:
    def __init__(self):
        self.reports = []

    def generate_report(self, user_id, content, date_time):
        report_id = len(self.reports) + 1
        report = Report(report_id, user_id, content, date_time)
        self.reports.append(report)
        return report

# Интеграция с социальными сетями (плохая читаемость)
class SocialMediaIntegration:
    def __init__(self, user_id, social_media_type, access_token):
        self.user_id = user_id
        self.social_media_type = social_media_type
        self.access_token = access_token

    def share_progress(self, message):
        print(f"Sharing progress to {self.social_media_type}: {message}")

# Управление обратной связью (дублирование и плохая структура)
class Feedback:
    def __init__(self, id, user_id, course_id, message, date_time):
        self.id = id
        self.user_id = user_id
        self.course_id = course_id
        self.message = message
        self.date_time = date_time

class FeedbackManager:
    def __init__(self):
        self.feedbacks = []

    def add_feedback(self, user_id, course_id, message, date_time):
        feedback_id = len(self.feedbacks) + 1
        feedback = Feedback(feedback_id, user_id, course_id, message, date_time)
        self.feedbacks.append(feedback)
        return feedback

# Управление курсами и встречами (плохая структура и дублирование)
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

# Функции для регистрации курсов и создания встреч (плохая структура)
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

# Тесты (плохая читаемость и дублирование)
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

class TestUserManagement(unittest.TestCase):
    def setUp(self):
        self.user_manager = UserManager()
        self.user = self.user_manager.register_user(
            username="testuser",
            password="testpass",
            email="test@example.com",
            role="student"
        )

    def test_register_user(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.role, "student")
        print("test_register_user: OK")

    def test_authenticate_user(self):
        authenticated_user = self.user_manager.authenticate_user("testuser", "testpass")
        self.assertIsNotNone(authenticated_user)
        self.assertEqual(authenticated_user.username, "testuser")
        print("test_authenticate_user: OK")

class TestNotificationManagement(unittest.TestCase):
    def setUp(self):
        self.notification_manager = NotificationManager()
        self.notification = self.notification_manager.add_notification(
            user_id=1,
            message="New assignment available",
            date_time=datetime.now()
        )

    def test_add_notification(self):
        self.assertEqual(self.notification.message, "New assignment available")
        print("test_add_notification: OK")

class TestReportManagement(unittest.TestCase):
    def setUp(self):
        self.report_manager = ReportManager()
        self.report = self.report_manager.generate_report(
            user_id=1,
            content="Your progress report",
            date_time=datetime.now()
        )

    def test_generate_report(self):
        self.assertEqual(self.report.content, "Your progress report")
        print("test_generate_report: OK")

class TestSocialMediaIntegration(unittest.TestCase):
    def setUp(self):
        self.social_media = SocialMediaIntegration(
            user_id=1,
            social_media_type="facebook",
            access_token="dummy_token"
        )

    def test_share_progress(self):
        self.social_media.share_progress("I completed a new course!")
        print("test_share_progress: OK")

class TestFeedbackManagement(unittest.TestCase):
    def setUp(self):
        self.feedback_manager = FeedbackManager()
        self.feedback = self.feedback_manager.add_feedback(
            user_id=1,
            course_id=1,
            message="Great course!",
            date_time=datetime.now()
        )

    def test_add_feedback(self):
        self.assertEqual(self.feedback.message, "Great course!")
        print("test_add_feedback: OK")

if __name__ == "__main__":
    unittest.main()