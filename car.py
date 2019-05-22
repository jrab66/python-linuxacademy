
class Car:
    """
    Docstring describing the class
    """
    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires

        # pass omit def
        # pass

    def description(self):
        print(f"A car with an {self.engine} and  {self.tires}")

    def wheel_circumference(self):
        if len(self.tires) > 0:
            return self.tires[0].circumference()
        else:
            return 0