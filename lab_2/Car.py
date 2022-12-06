class Car:
    def __init__(self, hp, color, max_speed):
        self.name = "Car"
        self.__hp = hp
        self.__color = color
        self.__max_speed = max_speed
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp (self, h):
        if h>0:
          self.__hp = h
        else:
          raise ValueError
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, c):
        self.__color = c
    @property
    def max_speed(self):
        return self.__max_speed
    @max_speed.setter
    def max_speed(self, s):
        if s>0:
          self.__max_speed = s
        else:
          raise ValueError
    def info(self):
        print(self.name)
        print(f"Hp: {self.__hp}")
        print("Color:" + self.__color)
        print(f"Max speed: {self.__max_speed}")