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
