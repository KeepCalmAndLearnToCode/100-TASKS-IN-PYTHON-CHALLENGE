print("-------------PRINT THE JOKE---------------")

import json
import urllib.request as urllib

import os, glob


def print_joke():
    url = "http://api.icndb.com/jokes/random"
    urlOpened = urllib.urlopen(url)
    data = json.load(urlOpened)

    print(data)
    print(data['value'])
    print("\t" + data['value']['joke'])


# wypisanie domyslnie jednego zartu
print_joke()


def work():
    decision = "t"
    while decision == "t":
        print_joke()
        print("czy chcesz przeczytac kolejny zart? (t/n)")
        decision = input()


print("nie to nie")

work()

print("-------------COUNT CHARACTERS IN WORD---------------")


def count_letter(word):
    letter_occur = {}
    for letter in word:
        if letter_occur.get(
                letter) == None:  # get returns value under the key. I want to check if a letter is the key. If it's not, return.
            letter_occur[letter] = 1  # new character which occurs once
        else:
            letter_occur[letter] += 1
        print(letter_occur)

    return letter_occur


print("-------CEZAR'S CIPHER-------")


def cezar_encrypt(text):
    encrypted = ""
    for letter in text:
        nowy_znak = ord(letter) + 3
        if nowy_znak > ord('z'):
            nowy_znak -= 26  # count of signs in English alphabet
        encrypted = encrypted + chr(
            nowy_znak)  # ord changes the sign into the letter, but we've got } so it's out of ASCII

    return encrypted


print(cezar_encrypt("zebra"))

print("-------BUBBLE SORT-------")

list = [9, 2, 5, 7, 3, 7, 1]


def bubble_sort(list):
    sorted = False
    while sorted == False:
        sorted = True

        for i in range(len(list) - 1):
            # print(i)
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
                sorted = False


print(list)
bubble_sort(list)
print(list)

print("--------SUMA LICZB LISTY---------")

list2 = [2, 2, 7, 1]
list3 = [2, 1, 1, 1]


def suma_liczb(list2):
    start = 0
    for i in list2:
        start = start + i
    return start


wynik = suma_liczb(list2)
print(wynik)

print("--------SUMA LICZB PARZYSTYCH LISTY---------")

list4 = [2, 2, 7, 1, 6, 7, 2, 4]


def suma_parz(list4):
    start = 0  # to znaczy ze 0 jest przypisane do zmiennej start?
    for i in list4:
        if i % 2 == 0:
            start = start + 1
    return start


wynik = suma_parz(list4)
print(wynik)

print("--------GENEROWANIE LISTY---------")


def generuj_liste(n):
    lista = []
    for x in range(n):
        lista.append(x)
    return lista


wynik = generuj_liste(12)
print(wynik)
wynik.append(33)
print(wynik)
print(len(wynik))
print(wynik.sort())

generuj_liste(15)

print("-------LIST OF FIRST FIBONACCI NUMBERS-------")

n = 6


def fibonacci(n):
    # first character of chain
    if n == 0:
        return n
    if n < 2:
        return n
    if n >= 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(n))


def fibonacci_sequence(n):
    lista = []
    for i in range(n):
        print(str(i) + ": " + str(fibonacci(i)))


fibonacci_sequence(10)

print("---------------SQUARE POWER/POTEGA----------------")


# REKURENCJA -POTĘGA a^3 = a * a^2

def potega(a, n):
    if n == 1:
        return a
    else:
        return a * potega(a, n - 1)


print(potega(2, 3))

print("-------------FIZZBUZZ---------------")

for num in range(1, 101):
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Fizz")
    elif num % 3 == 0:
        print("Buzz")
    else:
        print(num)

result = count_letter("DOMINI__KANA")
print(result)

print("-------------KOSMETYCZKA---------------")


class Kosmetyczka:
    def __init__(self):
        print("Jestem w klasie Kosmetyczka")
        self.lista_kosmetykow = []

    def list_cosmetics(self):
        for i in range(len(
                self.lista_kosmetykow)):  # tu sie zwieksza intex 0, 1, 2 - w ktorym elemencie sie znajduje w razie czego

            print(self.lista_kosmetykow[i])

    def find_cosmetics(self,
                       nazwa):  # chcemy znajezc kosmetyk po nazwie, trerzja po liscie koemstykow, szukanie elementu z listy; kosmetyk bedzie przyjmowal kolejne wartosci argumentu; kolejne elementy
        for kosmetyk in self.lista_kosmetykow:
            print(kosmetyk)

            if nazwa == kosmetyk.name:
                print("znaleziono: " + str(kosmetyk))
                return kosmetyk

        raise Exception("Kosmetyk o nazwie: " + nazwa + " nie zostal znaleziony")

    def add_cosmetic(self, kosmetyk):
        self.lista_kosmetykow.append(kosmetyk)


class Kosmetyk():
    def __init__(self, name):
        self.name = name
        print("Jestem w klasie Kosmetyk, nazwa: " + name)

    def __str__(self):
        return "Nazwa: " + self.name


class Puder(Kosmetyk):
    def __init__(self):
        print("Jestem w konsrtuktorze Puder")
        super().__init__("Puder Dior")
        print("Jestem w klasie Puder")


class Szminka(Kosmetyk):
    def __init__(self):
        super().__init__("Szminka Head'n Shoulders")
        print("Jestem w klasie Szminka")


kosmetyczka = Kosmetyczka()
kosmetyczka.list_cosmetics()

kosmetyk = Kosmetyk("Abstrakt")
kosmetyczka.add_cosmetic(kosmetyk)

puder = Puder()
kosmetyczka.add_cosmetic(puder)
szminka = Szminka()
kosmetyczka.add_cosmetic(szminka)
kosmetyczka.list_cosmetics()

odszukany_kosmetyk = kosmetyczka.find_cosmetics("Puder Dior")
print(str(odszukany_kosmetyk))

try:
    odszukany_kosmetyk = kosmetyczka.find_cosmetics("Puder")
except Exception as e:
    print("wyjatek typu Exception, wiadoimosc: " + str(e))

print("-------------PCC 2-7.STRIPPING NAMES---------------")
# Page 29. Store a pearson's name...

name = "\tDaria\n"
print("Without function")
print(name)

print(name.lstrip())
print(name.rstrip())
print(name.strip())

print("-------------PCC 2-9.FAVORITE NUMBERS---------------")
# Page 33. Store youe favourite number in a variable...

# NOPE:
favourite_number = "33"
print("My favourite number is " + favourite_number + ".")

# BETTER:
favourite_num = 33
msg = "My favourite number is " + str(favourite_num) + "."
print(msg)