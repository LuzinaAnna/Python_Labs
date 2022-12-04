class Car:
    def __init__(self, hp, color, max_speed):
        self.__hp = hp
        self.__color = color
        self.__max_speed = max_speed
    def hp(self):
        return self.__hp
    def hp (self, h):
        self.__hp = h
    def color(self):
        return self.__color
    def color(self, c):
        self.__color = c
    def max_speed(self):
        return self.__max_speed

    def max_speed(self, s):
        self.__max_speed = s

    def max_speed(self):
        return self.__max_speed

    def max_speed(self, s):
        self.__max_speed = s

    def info(self):
        print("Car")
        print(f"Hp: {self.__hp}")
        print("Color:" + self.__color)
        print(f"Max speed: {self.__max_speed}")