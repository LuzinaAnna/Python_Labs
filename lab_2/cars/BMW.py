from Car import Car
class BMW(Car):
    def __init__(self, hp, color, max_speed, model, year_release):
        super().__init__(hp, color, max_speed)
        self.__model = model
        self.__year_realise = year_release
    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, m):
        self.__model = m
    @property
    def year_release(self):
        return self.__year_realise
    @year_release.setter
    def year_realease(self, y):
        if y>1927:
            self.__year_realise = y
        else:
            raise ValueError
    def info(self):
        print("BMW")
        print(f"Hp: {self.hp}")
        print("Color:" + self.color)
        print(f"Max speed: {self.max_speed}")
        print("Model:"+self.__model)
        print(f"Year of realease: {self.__year_realise}")