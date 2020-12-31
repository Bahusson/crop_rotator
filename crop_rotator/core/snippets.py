import random


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


# Zmienia Stringi True/False w Booleany
def booleanate(mystring):
    if mystring == 'True':
        mystring = True
    else:
        mystring = False
    return mystring


# Flara debugująca
def flare(keyword, **kwargs):
    if "order" in kwargs:
        num = " # " + str(kwargs['order'])
    else:
        num = ''
    print("")
    print("")
    print("")
    print("THIS IS A DEBUGGING FLARE" + num + ' - ' + str(keyword))
    print("")
    print("")
    print("")

# Skraca powtarzający się kawałek kodu na widokach.
def list_appending_short(items, letter, vars):
    for i in items[0]:
        vars[0].append(
         [i.family.cooldown_min, i.id, i.family, vars[1].order, i])
        if i.family.is_mandatory_crop:
            vars[2].append(str(vars[1].order) + letter)

# Skraca usuwanie niepoprawnego numeru cropstepu.
def level_off(top_tier, a, b):
    if a[3] > top_tier:
        a[3] = a[3] - top_tier
        if b[3] > top_tier:
            b[3] = b[3] - top_tier
