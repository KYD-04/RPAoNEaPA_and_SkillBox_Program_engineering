from base_manager import BaseManager
class Notification:
    def __init__(self, id, user_id, message, date_time):
        self.id = id
        self.user_id = user_id
        self.message = message
        self.date_time = date_time

class NotificationManager(BaseManager):
    def add_notification(self, user_id, message, date_time):
        notification_id = len(self.items) + 1
        notification = Notification(notification_id, user_id, message, date_time)
        return self.add_item(notification)