from Car import Car
class VAZ(Car):
    def __init__(self, hp, color, max_speed, model, condition):
        super().__init__(hp, color, max_speed)
        self.name = "VAZ"
        self.__model = model
        self.__condition = condition
    @property
    def model(self):
        return self.__model
    @property
    def condition(self):
        return self.__condition
    @model.setter
    def model(self, m):
        self.__model = m
    @condition.setter
    def condition(self, c):
        self.__condition = c
    def info(self):
        print(self.name)
        print(f"Hp: {self.hp}")
        print("Color:" + self.color)
        print(f"Max speed: {self.max_speed}")
        print("Model:" + self.__model)
        print("Condition: " + self.__condition)