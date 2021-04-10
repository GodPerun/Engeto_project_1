# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import hashlib
import re
from task_template import TEXTS

def authenticate(uzivatele):
    user = input("zadej jmeno: ")
    password = input("zadej heslo: ")
    hash_password = hashlib.md5()
    hash_password.update(password.encode('utf-8'))
    # print(hash_password.digest())
    if uzivatele.get(user) != hash_password.digest():
        print("spatne uzivatelske jmeno nebo heslo")
        return 5
    else:
        choice = 0
        print("Hello ", user)

        while choice not in [1, 2, 3]:
            choice = int(input("Pleache choose text 1 or 2 or 3: "))

        return choice


# Press the green button in the gutter to run the script.

def analyza_pocet(veta) -> list:
    seznam = re.split('\. |; |, |\*| \n|\n | ', veta)

    # delka = delka[29].replace('.', '')
    i = 0
    list_updated = []
    for i in range(len(seznam)):
        list_updated.append(seznam[i].replace('.', ''))
        i = i + 1
    # list_updated - list slov bez punctuations
    # asik lepsi cele resit pres regex na alfanum znaky
    print(list_updated)
    return list_updated

def cap_words(seznam) -> int:
    pocet_cap = 0
    for i in range(len(seznam)):
        if seznam[i].istitle() == True:
            pocet_cap = pocet_cap + 1
        i = i + 1
    return pocet_cap

def lower_case(seznam) -> int:
    pocet_lower = 0
    for i in range(len(seznam)):
        if seznam[i].islower() == True:
            pocet_lower = pocet_lower + 1
        i = i + 1
    return pocet_lower

def upper_case(seznam) -> int:
    pocet_upper = 0
    for i in range(len(seznam)):
        if seznam[i].isupper() == True:
            pocet_upper = pocet_upper + 1
        i = i + 1
    return pocet_upper

def numbers(seznam) -> int:
    pocet_numbers = 0
    test = ["test"]
    value = 0
    for i in range(len(seznam)):
        if seznam[i].isnumeric() == True:
            pocet_numbers = pocet_numbers + 1
            value = value + int(seznam[i])
        i = i + 1
    return pocet_numbers, value

def letter_counts(seznam):
    i = 0
    counts = []
    max_pocet_pismen = 0
    for i in range(len(seznam)):
        if max_pocet_pismen < int(len(seznam[i])):
            max_pocet_pismen = int(len(seznam[i]))

        i = i + 1

    i = 1
    # print(counts)
    # print(type(counts))
    for i in range(max_pocet_pismen + 1):  # declarace pole integeru pro pocty characteru ve slovech
        counts.append(int(0))
        i = i + 1
    # print(len(counts))
    # print(counts)
    # print(f"pocet pismen: ", max_pocet_pismen)
    i = 1
    for i in range(len(seznam)):
        i = i + 1
        counts[len(seznam[i-1])] = counts[len(seznam[i-1])] + 1
        # print(seznam[i-1])
    # print(counts)
    return counts


if __name__ == '__main__':

    user_db = {"roman": b"\t\x8fk\xcdF!\xd3s\xca\xdeN\x83&'\xb4\xf6",
               "bob": b" ,\xb9b\xacY\x07[\x96K\x07\x15-#Kp",
               "ann": b"2%\x01p\xa0\xdc\xa9-S\xec\x96$\xf36\xca$",
               "mike": b'H,\x81\x1d\xa5\xd5\xb4\xbcmI\x7f\xfa\x98I\x1e8',
               "liz": b"2%\x01p\xa0\xdc\xa9-S\xec\x96$\xf36\xca$"}
    vystup = authenticate(user_db)

    if vystup == 5:
        # print("neproslo")
        exit(1)
    # veta = input(f"Zadej libovolne dlouho vetu: ")   odebrrane pro testovaci ucely
    veta = TEXTS
    #veta = ["Na Velký pátek budou muset mít všechny obchody zavřeno, běžně nesmějí být prodejny nad 200 metrů čtverečních podle zákona o prodejní době v maloobchodě v provozu jen na Velikonoční pondělí.",
    #      "The monument contains 8198 acres and protects a portion of the largest deposit of freshwater fish fossils in the world. The richest fossil fish deposits are found in multiple limestone layers, which lie some 100 feet below the top of the butte. The fossils represet several varieties of perch, as well as other freshwater genera and herring similar to those in modern oceans. Other fish such as paddlefish, garpike and stingray are also present.",
    #        "treti veta EEE 300 32"]

    seznam_slov = analyza_pocet(veta[vystup-1])
    counts = letter_counts(seznam_slov)
    capitals = cap_words(seznam_slov)
    lowers = lower_case(seznam_slov)
    uppers = upper_case(seznam_slov)
    numbers, value = numbers(seznam_slov)
    print("")
    print(f"---------STATS-----------")
    print(f"pocet title slov:       = {capitals}")
    print(f"pocet lowercase slov:   = {lowers}")
    print(f"pocet cisel:            = {numbers}")
    print(f"soucet cisel:           = {value}")
    print(f"pocet uppercase slov:   = {uppers}")
    print(f"celkovy pocet slof:     = {len(seznam_slov)}")
    print("")
    # print(f"-------------------------")

    print(f"--------HISTOGRAM-----------")
    j = 0
    for i in range(len(counts)):
        if j == 0:
            j += 1
            continue
        pocet_mezer = len(counts) - counts[i]
        print(f"{i}|", '{}'.format(counts[i] * '*'), '{}'.format(pocet_mezer * ' '), f"|{counts[i]}")
    print(f"----------------------------")


    # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
