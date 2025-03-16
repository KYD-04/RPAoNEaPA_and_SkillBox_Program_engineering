class BaseManager:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        return item

    def get_item_by_id(self, item_id):
        for item in self.items:
            if item.id == item_id:
                return item
        return None