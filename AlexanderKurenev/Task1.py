class Counter:
    """We can used negative start and stop numbers"""
    def __init__(self, start=0, stop=None):
        self.count = start
        self.stop = stop

    def get(self):
        return self.count

    def increment(self):
        if self.stop is not None and self.count >= self.stop:
            raise ValueError("Maximal value is reached.")
        self.count += 1


c = Counter(start=42)
c.increment()
print(c.get())

c = Counter()
c.increment()
print(c.get())
c.increment()
print(c.get())

c = Counter(start=42, stop=43)
c.increment()
print(c.get())

c = Counter(start=-2, stop=3)
c.increment()
print(c.get())
c.increment()
print(c.get())
