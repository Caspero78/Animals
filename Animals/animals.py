# Definiujemy klasę Zwierze, która będzie bazową klasą dla innych klas zwierząt
class Zwierze:
    # Metoda __init__ jest specjalną metodą, która jest wywoływana przy tworzeniu nowego obiektu klasy
    # Przyjmuje ona dwa parametry: imie i waga, które są przypisywane do atrybutów self.imie i self.waga
    # Atrybut self oznacza bieżący obiekt klasy i jest wymagany w każdej metodzie klasy
    def __init__(self, imie, waga):
        self.imie = imie
        self.waga = waga

    # Metoda przedstaw_sie jest zwykłą metodą klasy, która wyświetla informację o wadze zwierzęcia
    # Używa ona f-stringa, czyli specjalnego rodzaju łańcucha znaków, który pozwala na wstawianie wartości zmiennych wewnątrz nawiasów klamrowych
    def przedstaw_sie(self):
        print(f"Waże {self.waga} kg.")

    # Metoda zmien_miejsce jest kolejną metodą klasy, która przyjmuje jeden parametr: miejsce
    # Przypisuje ona wartość tego parametru do atrybutu self.miejsce i wyświetla informację o zmianie miejsca zwierzęcia
    def zmien_miejsce(self, miejsce):
        self.miejsce = miejsce
        print(f"{self.imie} poszedł do {miejsce}.")


# Definiujemy klasę Pies, która dziedziczy po klasie Zwierze
# Oznacza to, że klasa Pies ma dostęp do wszystkich metod i atrybutów klasy Zwierze, ale może je również nadpisywać lub dodawać nowe
class Pies(Zwierze):
    # Metoda przedstaw_sie jest nadpisana w klasie Pies, co oznacza, że zastępuje ona metodę o tej samej nazwie z klasy Zwierze
    # W tej metodzie wyświetlamy informację o imieniu i gatunku zwierzęcia, a następnie wywołujemy metodę przedstaw_sie z klasy Zwierze za pomocą funkcji super()
    # Funkcja super() pozwala na odwołanie się do klasy nadrzędnej, czyli klasy Zwierze w tym przypadku
    def przedstaw_sie(self):
        print(f"Jestem psem o imieniu {self.imie}.")
        super().przedstaw_sie()
        
    # Metoda szczekaj jest nową metodą, która jest specyficzna dla klasy Pies
    # Wyświetla ona dźwięk, który wydaje pies
    def szczekaj(self):
        print("Hau!")


# Definiujemy klasę Kot, która również dziedziczy po klasie Zwierze i nadpisuje metodę przedstaw_sie
# W tej metodzie wyświetlamy informację o imieniu i gatunku zwierzęcia, a następnie wywołujemy metodę przedstaw_sie z klasy Zwierze za pomocą funkcji super()
class Kot(Zwierze):
    def przedstaw_sie(self):
        print(f"Jestem kotem o imieniu {self.imie}.")
        super().przedstaw_sie()

    # Metoda mrucz jest nową metodą, która jest specyficzna dla klasy Kot
    # Wyświetla ona dźwięk, który wydaje kot
    def mrucz(self):
        print("Miau!")


# Definiujemy klasę Kura, która również dziedziczy po klasie Zwierze i nadpisuje metodę przedstaw_sie
# W tej metodzie wyświetlamy informację o imieniu i gatunku zwierzęcia, a następnie wywołujemy metodę przedstaw_sie z klasy Zwierze za pomocą funkcji super()
class Kura(Zwierze):
    def przedstaw_sie(self):
        print(f"Jestem kurą o imieniu {self.imie}.")
        super().przedstaw_sie()

    # Metoda gdakaj jest nową metodą, która jest specyficzna dla klasy Kura
    # Wyświetla ona dźwięk, który wydaje kura
    def gdakaj(self):
        print("Gda!")


# Tworzymy trzy obiekty klasy Pies, Kot i Kura, podając im imiona i wagi jako argumenty
# Argumenty te są przekazywane do metody __init__ klasy Zwierze i przypisywane do atrybutów self.imie i self.waga
pies = Pies("Miki", 10,)
kot = Kot("Czosnek", 5,)
kurczak = Kura("Nugget", 2,)

print()

# Wywołujemy metodę przedstaw_sie dla każdego obiektu, która wyświetla informację o imieniu, gatunku i wadze zwierzęcia
# Metoda ta jest nadpisana w każdej klasie potomnej, ale wywołuje również metodę z klasy nadrzędnej za pomocą funkcji super()
pies.przedstaw_sie()
kot.przedstaw_sie()
kurczak.przedstaw_sie()

print()

# Wywołujemy metodę zmien_miejsce dla każdego obiektu, podając jako argument miejsce, do którego zwierzę się przenosi
# Metoda ta jest dziedziczona z klasy Zwierze i nie jest nadpisana w klasach potomnych
# Przypisuje ona wartość argumentu do atrybutu self.miejsce i wyświetla informację o zmianie miejsca zwierzęcia
pies.zmien_miejsce("salonu")
kot.zmien_miejsce("sypialni")
kurczak.zmien_miejsce("kurnika")

print()

# Wywołujemy metodę szczekaj, mrucz lub gdakaj dla każdego obiektu, która wyświetla dźwięk, który wydaje zwierzę
# Metoda ta jest specyficzna dla każdej klasy potomnej i nie jest dziedziczona z klasy Zwierze
pies.szczekaj()
kot.mrucz()
kurczak.gdakaj()