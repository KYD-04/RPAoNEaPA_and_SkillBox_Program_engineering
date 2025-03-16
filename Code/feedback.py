from base_manager import BaseManager

class Feedback:
    def __init__(self, id, user_id, course_id, message, date_time):
        self.id = id
        self.user_id = user_id
        self.course_id = course_id
        self.message = message
        self.date_time = date_time

class FeedbackManager(BaseManager):
    def add_feedback(self, user_id, course_id, message, date_time):
        feedback_id = len(self.items) + 1
        feedback = Feedback(feedback_id, user_id, course_id, message, date_time)
        return self.add_item(feedback)