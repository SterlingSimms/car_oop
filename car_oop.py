class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = "12%"
        else:
            self.tax = "15%"
        self.display_all()

    def display_all(self):
        print "Price:", self.price
        print "Speed:", self.speed
        if self.fuel == 100:
            print "Fuel: full"
        if self.fuel in range(75,99):
            print "Fuel: mostly full"
        if self.fuel in range(50,74):
            print "Fuel: kind of full"
        if self.fuel in range(25,49):
            print "Fuel: less than half full"
        if self.fuel == 0:
            print "Fuel: empty"
        print "Mileage:", self.mileage
        print "Tax:", self.tax
        return self

car1 = Car(10000, 120, 50, 30)
car2 = Car(50000, 160, 25, 15)
car3 = Car(30000, 140, 0, 20)
car4 = Car(5000, 90, 100, 15)
car5 = Car(40000, 130, 75, 18)
car6 = Car(35000, 160, 40, 12)

