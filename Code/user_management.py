from base_manager import BaseManager

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

class UserManager(BaseManager):
    def register_user(self, username, password, email, role):
        user_id = len(self.items) + 1
        user = User(user_id, username, password, email, role)
        return self.add_item(user)

    def authenticate_user(self, username, password):
        for user in self.items:
            if user.authenticate(username, password):
                return user
        return None