# Nasledovanie

class Point:
    def __init__(self, x = 0, y =0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"{self.__x}, {self.__y}" # pereopredelenie vuvoda str

class Prop:
    def __init__(self, sp:Point, ep:Point, color:str="red", width:int = 1):  # dvoetochie tolko rekomenduet ispolzovat ukazanuy class no nikak bolshe ne vliyaet
        self._sp = sp
        self._ep = ep
        self._color = color
        self.__width = width  # Privatnaia peremennaya, ispolzuetsia tolko v etom clase

    def getWidth(self):
        return self.__width   # metod dlia ispolzovaniya peremennoy v drugom clase ili iz vne

class Line(Prop):

    def __init__(self, *args):          # constructor classa Line, *args dobavlaem esli est super clas
        print("Konstructor base class")
        super().__init__(*args)         # constructor super classa Prop, vsegda dobavlaem *args

    def drawLine(self):
        print(f"Risuem liniu: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}")


class Rect(Prop):

    def drawRect(self):
        print(f"Risuem Rect: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}")

l = Line(Point(1, 2), Point(10, 20))
l.drawLine()
print(l.getWidth())

# -----------------------------------------------------------------------------------
# PRACTICS:

class PC:

    def __init__(self, ram=1, disk=2, model=3, cpu=4):
        self._ram = ram
        self._disk = disk
        self._model = model
        self._cpu = cpu


class PCordinair(PC):

    def __init__(self, monitor:str = "mon", clavier:str="clav", sourie:str="sour", *args):
        super().__init__(*args)
        self._monitor = monitor
        self._clavier = clavier
        self._sourie = sourie


    def afiche(self):
        print(f"Details: {self._ram}, {self._disk}, {self._model}, {self._cpu}, {self._monitor}, {self._clavier}, {self._sourie}")

class Laptop(PC):
    def __init__(self, gabarit:list, diagonal:float, *args):
        super().__init__(*args)
        self._gabarit = gabarit
        self._diagonal = diagonal


    def afiche(self):
        print(f"Details: {self._ram},{self._disk}, {self._model}, {self._cpu}, {self._gabarit}, {self._diagonal}")


pc = PCordinair("red1", "red2", "red3", 99, 55, 101, 102)
lap = Laptop([1, 2, 10], 2.99, "red3", 99, 55, 101)

l = [pc, lap]

for i in l:
   print(i.afiche())

print(pc._ram)