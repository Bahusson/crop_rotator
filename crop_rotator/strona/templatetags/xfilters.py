from django import template

register = template.Library()


# Wyszukuje po liście -1 (Nieużywany?)
@register.filter(name='action')
def action(d, key):
    return d[key-1]


# Wyszukuje po liście
@register.filter(name='lookup')
def lookup(d, key):
    return d[key]


# Wyszukuje po atrybucie
@register.filter(name='lookupdict')
def lookupdict(d, key):
    return d.__getattribute__(key)

# Wyszukuje po liście bezwzględny integer
@register.filter(name='lookupint')
def lookupint(d, key):
    return d[int(key)]


# Wyszukuje po liście bezwzględny integer
@register.filter(name='actionint')
def actionint(d, key):
    return d[int(key)-1]


# Zwraca wartość do filtrowania malejąco
@register.filter(name='negator')
def negator(var):
    neg = '-' + str(var)
    return neg


# Podnosi wartość samego siebie o 1 za każdym razem. (Dla Menu)
@register.filter(name='zip_lists')
def zip_lists(a, b):
    return zip(a, b)


@register.simple_tag(takes_context=True, name='deep_list')
def deep_list(context, **kwargs):
    itemlist = context['efcs']
    itemlist2 = itemlist['e_crops']
    a = int(kwargs['step_no'])
    b = int(kwargs['search_by'])
    c = int(kwargs['search_pos'])
    d = int(kwargs['searched_item'])
    for i in itemlist2:
        if a is i[3] or a is i[8]: #można zrobić do dobrania z +5
            if b is i[c]:
                print(i[d])
                return i[d]
