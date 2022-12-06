from Car import Car
class Audi(Car):
    def __init__(self, hp, color, max_speed, model, wheel_radius):
        super().__init__(hp, color, max_speed)
        self.name = "Audi"
        self.__model = model
        self.__wheel_radius = wheel_radius
    @property
    def model(self):
        return self.__model
    @property
    def wheel_radius(self):
        return self.__wheel_radius
    @model.setter
    def model(self, m):
        self.__model = m
    @wheel_radius.setter
    def wheel_radius(self, r):
        if r>0:
            self.__wheel_radius = r
        else:
            raise ValueError
    def info(self):
        print(self.name)
        print(f"Hp: {self.hp}")
        print("Color:" + self.color)
        print(f"Max speed: {self.max_speed}")
        print("Model:"+self.__model)
        print(f"Wheel radius: {self.__wheel_radius}")