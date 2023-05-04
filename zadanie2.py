from operator import attrgetter

class Movie:

    def __init__(self, tytuł, rok, ocena_filmu):
        self.tytuł = tytuł
        self.rok = rok
        self.ocena_filmu = ocena_filmu


    def __lt__(self, other):
        return (self.ocena_filmu > other.ocena_filmu)


    def __repr__(self):
        return f"{self.tytuł} {self.rok} {self.ocena_filmu}"


m1 = Movie('Johny', 2022, 9)
m2 = Movie('Filip', 2022, 8)
m3 = Movie('Aida', 2020, 9)
m4 = Movie('Generał_Nil', 2009, 8)
m5 = Movie('Diuna', 2021, 8)
m6 = Movie('Teściowie', 2021, 7)
m7 = Movie('Dawno temu w Ameryce', 1984, 9)
m8 = Movie('Gran Torino', 2008, 9)
m9 = Movie('Chłopiec w pasiastej piżamie', 2008, 9)
m10 = Movie('Chłopcy z ferajny', 1990, 9)

lista = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]


lista.sort(reverse = True)
print(lista)
# # sortowanie odwrotnw wg. oceny  rosnąco
lista.sort(reverse = False)
print(lista)
# # sortowanie odwrotnw wg. oceny  malejąco
lista.sort(key=attrgetter('rok'))
print(lista)
# sortowanie rosnące wg.roku
lista.sort(key=attrgetter('ocena_filmu','rok'))
print(lista)
# sortowanie rosnące wg. klucza najpierw ocena filmu nastepnie rok.
lista.sort()
print(lista)
# sortowanie wg. oceny filmu malejąco