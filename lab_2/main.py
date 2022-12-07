import sys
import json
from Car import Car
from Audi import Audi
from BMW import BMW
from Mersedes import Mersedes
from VAZ import VAZ

def write(data):
    jsonstr = json.dumps(data, indent = 4)
    open('./objects.json', 'w').write(jsonstr)
def read_from_json():
    return json.load(open('./objects.json', 'r'))

c = Car(120, "green", 250)
a = Audi(140, "red", 270, "Q7", 14)
b = BMW(100, "black", 230, "M3", 1998)
m = Mersedes(150, "white", 290, "GLE Coupe I", "S")
v = VAZ(70, "cherry", 130, "five", "good")
l = [c, a, b, m, v]
data = {
    'amount' : len(l),
    'obj' : []
}
for elem in l:
    data['obj'].append(elem.__dict__)

write(data)
data.clear()
l.clear()
data = read_from_json()
for elem in data['obj']:
    if elem['name'] == "Car":
        obj = Car(elem['_Car__hp'], elem['_Car__color'], elem['_Car__max_speed'])
    elif elem['name'] == "Audi":
        obj = Audi(elem['_Car__hp'], elem['_Car__color'], elem['_Car__max_speed'], elem['_Audi__model'], elem['_Audi__wheel_radius'])
    elif elem['name'] == "BMW":
        obj = BMW(elem['_Car__hp'], elem['_Car__color'], elem['_Car__max_speed'], elem['_BMW__model'], elem['_BMW__year_realise'])
    elif elem['name'] == "Mersedes":
        obj = Mersedes(elem['_Car__hp'], elem['_Car__color'], elem['_Car__max_speed'], elem['_Mersedes__model'], elem['_Mersedes__clas'])
    elif elem['name'] == "VAZ":
        obj = VAZ(elem['_Car__hp'], elem['_Car__color'], elem['_Car__max_speed'], elem['_VAZ__model'], elem['_VAZ__condition'])
    l.append(obj)
for elem in l:
    elem.info()