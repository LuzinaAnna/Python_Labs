from Car import Car
from Audi import Audi
from BMW import BMW
from Mersedes import Mersedes
from VAZ import VAZ
c = Car(120, "green", 250)
a = Audi(140, "red", 270, "Q7", 14)
b = BMW(100, "black", 230, "M3", 1998)
m = Mersedes(150, "white", 290, "GLE Coupe I", "S")
v = VAZ(70, "cherry", 130, "пятерка","good")
c.info()
a.info()
b.info()
m.info()
v.info()