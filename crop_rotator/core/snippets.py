import random

# Generator mnemotechnicznych loginów losowych do przekazywania innym userom,
# bo nicki nie muszą być unikalne a jakoś trzeba się banować, polecać,
# wyszukiwać itp.
def gen_login():
    vowels = ["a", "e", "i", "o", "u", "y"]
    consonants = [
        "b",
        "c",
        "d",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        "m",
        "n",
        "p",
        "r",
        "s",
        "t",
        "w",
        "z",
    ]

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

def sortSecond(val):
    return val[1]

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
    if mystring == "True":
        mystring = True
    else:
        mystring = False
    return mystring


# Flara debugująca...  :3
def flare(debugged_content, **kwargs):
    if "name" in kwargs:
        num = " # " + str(kwargs["name"])
    else:
        num = ""
    print("")
    print("")
    print("")
    print("THIS IS A DEBUGGING FLARE" + num + " - " + str(debugged_content))
    print("")
    print("")
    print("")


# Skraca powtarzający się kawałek kodu na widokach.
def list_appending_short(items, vars, season, *args):
    for i in items:
        vars[0].append(
            [
                i.family.cooldown_min,
                i.id,
                i.family,
                [vars[1].order, vars[3], season],
                i,
            ]
        )
        # Policz bobowate i strączkowe (tzw. mandatory crops):
        if i.family.is_mandatory_crop:
            vars[2].append(str(vars[1].order))
            if args[0] and len(args[0]) == 0:
                pass
                if args [1] and len(args[1]) == 0:
                    pass

def list_appending_long(a,b,c, vars):
    if len(a) > 0:
        vars[3] += 1
        list_appending_short(a, vars, "Summer", b, c)
    if len(b) > 0:
        vars[3] += 1
        list_appending_short(b, vars, None, c)
    if len(c) > 0:
        vars[3] += 1
        list_appending_short(c, vars, "Winter")
    return vars[3]

# Skraca usuwanie niepoprawnego numeru cropstepu.
def level_off(top_tier, a, b):
    if a[3][0] > top_tier:
        a[3][0] = a[3][0] - top_tier
    if b[3][0] > top_tier:
        b[3][0] = b[3][0] - top_tier


# usuwa powtarzające się elementy na liście i zwraca nową listę
def remove_repeating(new_list, old_list):
    [new_list.append(x) for x in old_list if x not in new_list]


def remove_repeating_2(list):
    [k for k, g in itertools.groupby(sorted(family_interaction_list))]


def repack(wrapped_list):
    try:
        wrapped_list1 = wrapped_list[0]
        return wrapped_list1
    except:
        return False


def check_slaves(*args):
    slavedict = {True: 1, False: 0,}
    master_id = args[slavedict[args[2]]]
    family_slav_list = [master_id]
    if master_id.family_slaves.exists():
        for i in master_id.family_slaves.all():
            family_slav_list.append(i)
    return family_slav_list


def check_ownership(request, user_model, checked_model):
    try:
        userdata = user_model.objects.get(
        id=request.user.id)
        user_id = userdata.id
    except:
        user_id = -1
    owner_id = checked_model.owner.id
    return user_id is owner_id


def slice_list_3(list):
    master_len = len(list)
    master_len_1 = round(master_len/3)
    master_len_2 = master_len_1*2
    return (master_len_1,master_len_2)


def summarize_plans(plans_list, step_class):
    summarized_list = []
    for plan in plans_list:
        pe_rs = step_class.objects.filter(from_plan=plan.id)
        listed_pe_rs = list(pe_rs)
        steps_total = len(listed_pe_rs)
        crop_total = 0
        tag_list = []
        for step in listed_pe_rs:
            for crop in step.early_crop.all():
                crop_total += 1
                for tag in crop.tags.all():
                    if tag.is_featured:
                        tag_list.append(tag)
            for crop in step.middle_crop.all():
                crop_total += 1
                for tag in crop.tags.all():
                    if tag.is_featured:
                        tag_list.append(tag)
            for crop in step.late_crop.all():
                crop_total += 1
                for tag in crop.tags.all():
                    if tag.is_featured:
                        tag_list.append(tag)
        tag_list2 = []
        remove_repeating(tag_list2, tag_list)
        tag_list3 = []
        for item in tag_list2:
            num = tag_list.count(item)
            mychunk = (item, round(num/crop_total*100))
            tag_list3.append(mychunk)
        tag_list3.sort(key = sortSecond, reverse=True)
        summarized_list.append((plan, tag_list3, steps_total, crop_total))
    return summarized_list


def list_crops_to(myitem ,crops_query, family_query, tag_query, variant):
    list_appending = []
    item_id = myitem.id
    for crop in crops_query:
        variantdict={
        "crop": crop.crop_relationships.filter(about_crop=item_id),
        "family": crop.crop_relationships.filter(about_family=item_id),
        "tag": crop.crop_relationships.filter(about_tag=item_id),
        }
        for item in variantdict[variant]:
            list_appending.append((crop, item, variant, myitem))
    for family in family_query:
        variantdict={
        "crop": family.family_relationships.filter(about_crop=item_id),
        "family": family.family_relationships.filter(about_family=item_id),
        "tag": family.family_relationships.filter(about_tag=item_id),
        }
        for item in variantdict[variant]:
            list_appending.append((family, item, variant, myitem))
    for tag in tag_query:
        variantdict={
        "crop": tag.crop_relationships.filter(about_crop=item_id),
        "family": tag.crop_relationships.filter(about_family=item_id),
        "tag": tag.crop_relationships.filter(about_tag=item_id),
        }
        for item in variantdict[variant]:
            list_appending.append((tag, item, variant, myitem))
    return list_appending


# Tworzy nową tuplę z "None" na pierwszyn miejscu.
# Do standaryzacji wzorników.
def none_ify(query):
    mylist = []
    for element in query:
        item = (None, element)
        mylist.append(item)
    return mylist
