import csv
from helpers import Mapper
from helpers import Filter
from helpers import Reduce


"""
Файл phe_healthcare.csv содержит данные о числе пациентов в Лондоне и оставшейся части королевства.
Требуется посчитать максимальное число пациентов в госпитале за все время в остальной части британии(rest of England)
"""

with open("phe_healthcare.csv",mode='r',encoding='UTF-8') as file:
    csv_reader = csv.reader(file)

    #Получаем записи, где часть королевства='Rest of England' и Местонахождение(исправить) пациентов = 'Patients in Hospital'
    #А еще нужно, чтобы последний столбец, где хранятся значения был не пустым
    filtered_rest_of_england = Filter(
        csv_reader, lambda x: x[1] == 'Rest of England' and x[2] == 'Patients in Hospital' and x[-1] != '')

    #Отбрасываем все столбцы, кроме последнего. Конвертируем строки в числа
    #Переход от множества списков из строк к множеству чисел
    mapped_rest_of_england = Mapper(filtered_rest_of_england,lambda x : int(x[-1]))

    #Находим максимальное значение среди последовательности mapped_rest_of_england
    #Получается что-то вроде res=max(x[0],max(x[1],max(x[2]...max(x[n-1],x[n]))))...)
    result = Reduce(mapped_rest_of_england,0,max)

with open("resultaet.txt",'w') as file:
    file.write(str(result))