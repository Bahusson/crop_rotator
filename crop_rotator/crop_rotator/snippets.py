import random
from datetime import date


def menu_switcher(*args):
    # Podajesz listy argumentów w formacie:
    # [numer menu, menu_item, link_item]
    # Kolejność dowolna. Klucz ma ten numer menu który podałeś/aś w liście.
    menusdict = {}
    x = 0
    for arg in args:
        menusdict['menu'+str(args[x][0])] = args[x]
        x = x + 1
    return menusdict


# Generator mnemotechnicznych loginów losowych do przekazywania innym userom,
# bo nicki nie muszą być unikalne a jakoś trzeba się banować, polecać,
# wyszukiwać itp.
def gen_login():
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    consonants = [
     'b', 'c', 'd', 'f', 'g', 'h', 'j',
     'k', 'l', 'm', 'n', 'p', 'r', 's',
     't', 'w', 'z']

    L1 = random.choice(consonants).capitalize()
    L2 = random.choice(vowels)
    L3 = random.choice(consonants)
    L4 = random.choice(vowels)
    L5 = random.choice(consonants)
    L6 = random.choice(vowels)
    L7 = random.choice(consonants)
    L8 = random.choice(vowels)
    L9 = str(random.randint(100, 999))

    fulllogin = L1 + L2 + L3 + L4 + L5 + L6 + L7 + L8 + L9
    return fulllogin


# Wyciąga nazwy wszystkich atrybutów modelu
# i zamyka je w tupli do użycia w translatorze.
def all_names(classname):
    itemlist = []
    for item in classname.__dict__:
        itemlist.append(item)
    itemlist2 = itemlist[5:-2]
    itemtuple = tuple(itemlist2)
    return itemtuple


# Python3 code to  calculate age in years
def calculateAge(born):
    today = date.today()
    try:
        birthday = born.replace(year=today.year)

    # raised when birth date is February 29
    # and the current year is not a leap year
    except ValueError:
        birthday = born.replace(year=today.year, month=born.month+1, day=1)

    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year


# Zmienia Stringi True/False w Booleany
def booleanate(mystring):
    if mystring == 'True':
        mystring = True
    else:
        mystring = False
    return mystring


# Flara debugująca
def flare(keyword):
    print("")
    print("")
    print("")
    print("THIS IS A DEBUGGING FLARE " + str(keyword))
    print("")
    print("")
    print("")
