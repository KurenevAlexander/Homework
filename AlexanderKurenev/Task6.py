class Sun:
    __instance = None

    @classmethod
    def inst(cls):
        if not cls.__instance:
            cls.__instance = Sun()
        return cls.__instance


p = Sun.inst()
f = Sun.inst()
print(p is f)
