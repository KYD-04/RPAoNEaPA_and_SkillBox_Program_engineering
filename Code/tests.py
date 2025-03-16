import unittest
from datetime import datetime
from user_management import UserManager, User
from notification import NotificationManager, Notification
from report import ReportManager, Report
from feedback import FeedbackManager, Feedback
from cource import register_course, create_meeting, Course, Meeting
from social_media import SocialMediaIntegration

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
        self.social_media.share_progress("Progress shared on Facebook...")
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