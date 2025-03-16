from base_manager import BaseManager
class Report:
    def __init__(self, id, user_id, content, date_time):
        self.id = id
        self.user_id = user_id
        self.content = content
        self.date_time = date_time

class ReportManager(BaseManager):
    def generate_report(self, user_id, content, date_time):
        report_id = len(self.items) + 1
        report = Report(report_id, user_id, content, date_time)
        return self.add_item(report)