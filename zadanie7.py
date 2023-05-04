class Car():

    def __init__(self, marka, model,rok_produkcji, przebieg):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg


    def __repr__(self):
        return f"Car: {self.marka},{self.model},{self.rok_produkcji},{self.przebieg}km"

    def __lt__(self, other):
        return (self.przebieg > other.przebieg)
    # metoda porównująca przebieg wybranych samochodów


os1 = Car('Mazda', '3', 1997, 10000)
os2 = Car('Toyota', 'Corolla', 1998, 11000)
os3 = Car('Opel', 'Meriva', 2009, 123000)
os4 = Car('Fiat', '126', 1989, 112000)
os5 = Car('Toyota', 'Corolla', 2000, 128000)
os6 = Car('Opel', 'Astra', 1999, 11093)

lista = [os1, os2, os3, os4, os5, os6]

print(lista)
print(os3 > os1)
print(os1 > os3)


