####



class Car:
    def __init__(self, marka, model, rok):
        self.marka = marka
        self.model = model
        self.rok = rok

    def show_data(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"rok: {self.rok}")
        print("koniec show metody")



my_car = Car("Fiat", "126p", 1980)

print(my_car.rok)
my_car.show_data()





lista = [123, 123]
lista.append(7)

sorted(lista)





