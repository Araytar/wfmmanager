from tinydb import TinyDB, Query


class Database(object):
    def __init__(self) -> None:
        self.Inventory = TinyDB("./storage/inventory.json")
        self.Item = Query()


    def add(self, item, count) -> bool:
        try:
            self.Inventory.insert({"type": item, "count": count})
            return True
        except:
            return False

    def remove(self, item, count) -> bool:
        try:
            self.Inventory.remove(item)
            return True
        except:
            return False
