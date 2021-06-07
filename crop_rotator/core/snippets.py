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
def list_appending_short(item, vars, rss_list, rss_object):
    length = len(rss_list)
    seasondict = {1: "Summer", 2: None, 3: "Winter",}
    for i in item.crop_substep.all():
        if i.cooldown_min_override:
            cooldown_num = i.cooldown_min_override
        else:
            cooldown_num = i.family.cooldown_min
        vars[0].append(
            [
                cooldown_num,
                i.id,
                i.family,
                [vars[1].order, vars[3], seasondict[item.order]],
                i,
            ]
        )
                # Policz bobowate i strączkowe (tzw. mandatory crops):
        if i.family.is_mandatory_crop:
            vars[2].append(str(vars[1].order))
            is_winter = item.from_step
            winter_sibling = rss_object.objects.filter(from_step=is_winter, order=3)
            if item.order == 1 and length == 1:
                vars[2].append(str(vars[1].order) + "a")
                vars[2].append(str(vars[1].order) + "b")
            elif item.order == 2 and len(winter_sibling) == 0:
                vars[2].append(str(vars[1].order) + "a")
            elif item.order == 1 and len(winter_sibling) == 1 and length == 2:
                vars[2].append(str(vars[1].order) + "b")



def list_appending_long(rss_list,  vars, rss_object):
    if len(rss_list) > 0:
        vars[3] += 1
        list_appending_short(rss_list[0], vars, rss_list, rss_object)
    if len(rss_list) > 1:
        vars[3] += 1
        list_appending_short(rss_list[1], vars, rss_list, rss_object)
    if len(rss_list) > 2:
        vars[3] += 1
        list_appending_short(rss_list[2], vars, rss_list, rss_object)
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


def repack(wrapped_list):
    try:
        wrapped_list1 = wrapped_list[0]
        return wrapped_list1
    except:
        return False


def check_slaves(*args):
    slavedict = {True: 1, False: 0}
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
    return (master_len_1, master_len_2)


def summarize_plans(plans_list, step_class, substep_class):
    summarized_list = []
    for plan in plans_list:
        pe_rs = step_class.objects.filter(from_plan=plan.id)
        pe_rss = substep_class.objects.filter(from_step__from_plan=plan.id)
        listed_pe_rss = list(pe_rss)
        steps_total = len(pe_rs)
        crop_total = 0
        tag_list = []
        for step in listed_pe_rss:
            for crop in step.crop_substep.all():
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
        tag_list3.sort(key=sortSecond, reverse=True)
        summarized_list.append((plan, tag_list3, steps_total, crop_total))
    return summarized_list


def list_crops_to(myitem, crops_query, family_query, tag_query, variant):
    list_appending = []
    item_id = myitem.id
    for crop in crops_query:
        variantdict = {
         "crop": crop.crop_relationships.filter(
           about_crop=item_id, is_server_generated=False),
         "family": crop.crop_relationships.filter(
           about_family=item_id, is_server_generated=False),
         "tag": crop.crop_relationships.filter(
           about_tag=item_id, is_server_generated=False),
        }
        for item in variantdict[variant]:
            list_appending.append((crop, item, variant, myitem))
    for family in family_query:
        variantdict = {
         "crop": family.crop_relationships.filter(
          about_crop=item_id, is_server_generated=False),
         "family": family.crop_relationships.filter(
          about_family=item_id, is_server_generated=False),
         "tag": family.crop_relationships.filter(
          about_tag=item_id, is_server_generated=False),
        }
        for item in variantdict[variant]:
            list_appending.append((family, item, variant, myitem))
    for tag in tag_query:
        variantdict = {
         "crop": tag.crop_relationships.filter(
          about_crop=item_id, is_server_generated=False),
         "family": tag.crop_relationships.filter(
          about_family=item_id, is_server_generated=False),
         "tag": tag.crop_relationships.filter(
          about_tag=item_id, is_server_generated=False),
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


def compare_csv_lists(*args):
    crop_mixes = args[0].objects.all()  # MixCrop
    third_crop_step = args[1].all()  # step.xxxx_xrop
    tcp_listed = []
    for item in third_crop_step:
        temp_list = item.meta_tags_source.split(",")
        for temp_item in temp_list:
            tcp_listed.append(temp_item)
    for mix in crop_mixes:
        mix_list = mix.meta_tags.split(",")
        if(set(mix_list).issubset(set(tcp_listed))):
            args[1].add(mix)
        else:
            args[1].remove(mix)
