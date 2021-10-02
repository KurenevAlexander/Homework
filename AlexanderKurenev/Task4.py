class Bird:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name} can walk and fly'

    def fly(self):
        return f'{self.name} bird can fly'

    def walk(self):
        return f'{self.name} bird can walk'


class FlyingBird(Bird):
    def __init__(self, name, ration='grains'):
        super().__init__(name)
        self.ration = ration

    def __str__(self):
        return f'{self.name} can walk and fly'

    def eat(self):
        return f'It eats mostly {self.ration}'


class NonFlyingBird(Bird):
    def __init__(self, name, ration='fish'):
        super().__init__(name)
        self.ration = ration

    def __str__(self):
        return f'{self.name} can walk, swim, but cannot fly'

    def eat(self):
        return f'It eats mostly {self.ration}'

    def fly(self):
        raise AttributeError(f'{self.name} has no attribute fly')

    def swim(self):
        return f'{self.name} bird can swim'


class SuperBird(FlyingBird, NonFlyingBird):
    def __init__(self, name, ration="fish"):
        super().__init__(name, ration)

    def __str__(self):
        return f'{self.name} bird can walk, swim and fly'

    def eat(self):
        return f'It eats {self.ration}'

    def fly(self):
        FlyingBird.fly(self)


if __name__ == '__main__':
    b = Bird("Any")
    print(b.walk())

    p = NonFlyingBird('Penguin', 'fish')
    print(p.swim())
    #print(p.fly())
    print(p.eat())

    c = FlyingBird('Canary')
    print(str(c))
    print(c.eat())

    s = SuperBird('Gull')
    print(str(s))
    print(s.eat())

