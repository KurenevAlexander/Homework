class HistoryDict(dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__last_keys = []

    def set_value(self, key, value):
        if key in self and id(self[key]) == id(value):
            return
        self[key] = value
        if key in self.__last_keys:
            self.__last_keys.remove(key)
        self.__last_keys.append(key)
        if len(self.__last_keys) > 10:
            self.__last_keys.pop(0)

    def get_history(self):
        return self.__last_keys


d = HistoryDict({"foo": 42})
print(d)
d.set_value("bar", 43)
print(d.get_history())

d.set_value("bar1", 1)
d.set_value("bar2", 2)
d.set_value("bar3", 3)
d.set_value("bar4", 4)
d.set_value("bar5", 5)
d.set_value("bar6", 6)
d.set_value("bar7", 7)
d.set_value("bar8", 8)
d.set_value("bar9", 9)
d.set_value("bar10", 10)

d.set_value("bar1", 11)

print(d.get_history())

print("In dictionary: ", d)