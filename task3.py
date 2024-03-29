'''
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
'''
PACK_MAX_WEIGHT = 2.0

list_of_things = {
    "палатка":0.5,
    "топор":0.3,
    "термос":0.2,
    "котелок":0.1,
    "консервы":0.3,
    "вода":0.5,
    "одежда":0.6,
    "веревка":0.4,
    "нож":0.3
}

def pack_options(things):
    pack_curr_weight = 0
    pack = {}
    for k,v in things.items():
        pack_curr_weight += v
        if pack_curr_weight <= PACK_MAX_WEIGHT:
            pack[k] = v
        else: break
    print(pack)


pack_options(list_of_things)