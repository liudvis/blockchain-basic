class Food:
    def __init__(self, name, kind):
        self.name=name
        self.kind=kind
    def describe(self):
        print('{}, {}'.format(self.name, self.kind))

food = Food("banana", "fruit")
food.describe()