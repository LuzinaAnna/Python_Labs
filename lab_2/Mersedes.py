from Car import Car
class Mersedes(Car):
    def __init__(self, hp, color, max_speed, model, clas):
        super().__init__(hp, color, max_speed)
        self.__model = model
        self.__clas = clas
    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, m):
        self.__model = m
    @property
    def clas(self):
        return self.__clas
    @clas.setter
    def clas(self, c):
        self.__clas = c
    def info(self):
        print("Mersedes")
        print(f"Hp: {self.hp}")
        print("Color:" + self.color)
        print(f"Max speed: {self.max_speed}")
        print("Model:" + self.__model)
        print("Class: " + self.__clas)