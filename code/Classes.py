class Car:
    def __init__(self, name, year, ps): # self (this in C++/Java)
        self.name = name
        self.year = year
        self.ps = ps

    def print_car(self):
        print("Car: ", self.name)

    def print_ps(self):
        print("Leistung: ", self.ps, " PS")


my_car = Car("Audi A1 Sportback 40 TFSI", "2020", "200")
my_car.print_car()
my_car.print_ps()

my_car2 = Car("Opel Insignia", "2020", "120")
my_car2.print_car()
my_car2.print_ps()

print("")
