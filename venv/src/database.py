from tinydb import TinyDB, Query
import warframemarket
from cfgparser import loadcfg

class Database(object):
    def __init__(self) -> None:
        self.Inventory = TinyDB("./storage/inventory.json")
        self.Item = Query()

    def __checkforitem(self, TargetItem):
        config = loadcfg()
        wfm = warframemarket.api(config["jwt"])
        ignItems = wfm.getAllItems()
        itemcheck = any(item["item_name"] == TargetItem for item in ignItems)
        if itemcheck:
            return True
        else:
            return False

    def add(self, item, count):
        if self.__checkforitem(item):
            itemexists = self.Inventory.get(self.Item.name == str(item))
            print(itemexists)
            if itemexists != None:
                ucount = itemexists["count"] + count
                self.Inventory.update({"count": ucount,})
            else:
                self.Inventory.insert({"name": item, "count": count})
                return True
        else:
            return False


    def remove(self, item, count):
        target = self.Inventory.get(self.Item.name == str(item))
        if target == None:
            return False
            raise IndexError("target not found")
        elif count <= 0 or target["count"] < count:
            raise IndexError("target out of bounds")
            return False
        else:
            ucount = target["count"] - count
            if ucount == 0:
                self.Inventory.remove(self.Item.name == str(item))
                return True
            else:
                self.Inventory.update({"count": ucount}, self.Item.name == str(item))
                return True


    def get(self, item):
        target = self.Inventory.get(self.Item.name == str(item))
        if target == None:
            return False
        else:
            return target