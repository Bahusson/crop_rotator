from django import template
from core.snippets import flare

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


# Zipuje listy
@register.filter(name='zip_lists')
def zip_lists(a, b):
    return zip(a, b)

@register.simple_tag(takes_context=True)
def orderlookup(context, **kwargs):
    substeps = context['substeps']
    button = kwargs['button']
    for substep in substeps:
        if button == substep.order:
            return True


@register.simple_tag(takes_context=True)
def fertilizerlookup(context, **kwargs):
    substep = kwargs['substep']
    for item in substep.crop_substep.all():
        if item.id == 118:
            return True

@register.simple_tag(takes_context=True)
def fertilizerlookup2(context, **kwargs):
    substep = kwargs['substep']
    for item in substep.crop_substep.all():
        if item.id == 129:
            return True

@register.simple_tag(takes_context=True)
def nonefamilylookup(context, **kwargs):
    family = kwargs['family']
    if family.id == 29:
        return True

@register.simple_tag(takes_context=True, name='deep_list')
def deep_list(context, **kwargs):
    itemlist = context['efcs']
    itemlist2 = itemlist['e_crops']
    a = int(kwargs['step_no'])
    b = int(kwargs['search_by'])
    c = int(kwargs['search_pos'])
    d = int(kwargs['searched_item'])
    for i in itemlist2:
        if a is i[3][0]:
            if b is i[c]:
                return (i[d], i[d+5], i[8])


@register.simple_tag(takes_context=True, name='error_tab')
def error_tab(context, **kwargs):
    itemlist = context['efcs']
    itemlist2 = itemlist['e_tabs']
    a = int(kwargs['step_no'])
    for i in itemlist2:
        if a is i:
            return True


# Wielofunkcyjny tag do płytkiego przeszukiwania par zmiennych.
@register.simple_tag(name='shallow_list')
def shallow_list(**kwargs):
    from_context = kwargs['from_context']
    order = int(kwargs['step_no'])
    plant = int(kwargs['search_by'])
    a = from_context[3][0]
    b = from_context[1]
    c = from_context[9]
    if a is order and b is plant:
        return c


# Przeróbka powyższego.
@register.simple_tag(name="complex_list")
def complex_list(**kwargs):
    from_context = kwargs['from_context']
    order = int(kwargs['step_no'])
    subject = int(kwargs['search_by'])
    sub_type = int(kwargs['subject_type'])
    mylist = []
    for i in from_context:
        a = i[3][0]
        b = i[sub_type]  # 1 dla rośliny a 2 dla rodziny.
        specimen = i[9]
        i_value = i[10]
        step = i[8]
        if a is order and b is subject:
            mylist.append((specimen, i_value, step))
    return mylist
