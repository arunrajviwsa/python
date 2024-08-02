class Vehicle:
    def __init__(self,maxspeed,mileage,seatingCapacity):
        self._seatingCapacity = int(seatingCapacity)
        self._maxspeed = maxspeed
        self._mileage = mileage
    def farecharge1(self):
        v= float(self._seatingCapacity * 100)
        return v

    def speed(self):
        print("max speed", self._maxspeed)
    def mileage(self):
        print("Mileage", self._mileage)

class Bus(Vehicle):
    def __init__(self,seatingCapacity):
        self._seatingCapacity=int(seatingCapacity)

    def totalfare(self):
        self._maintainCharge = float(0.1 * super().farecharge1())
        self._totalfare = self._maintainCharge + (self._seatingCapacity * 100)
        print("Total fare for bus",self._totalfare)


e1 = Vehicle(56,5,50)
e1.speed()
e1.mileage()
e1.farecharge1()
e2 = Bus(34)
e2.totalfare()