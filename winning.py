import random as r

def win(name, c, fhp, dm, w, fight):
    path = r.randint(1, 3)
    if path == 1:
        print ("Пройдя немного по туннелю,", name, "обнаружил сундук. \n", c, "открыл сундук и забрал все вещи оттуда.")
    elif path == 2:
        print ("\"Что это такое блестит в темноте?\"")
        input()
        print (name, "пошёл на блеск и обнаружил какие-то вещи...")
    else:
        print ("В проходе", c, "наткнулся на чей-то труп. У умершего человека были различные предметы, которые", name, "решил взять себе.")
    input()
    fhp = fhp + fight * 250
    dm = dm + fight * 40
    if fight == 2:
        w = "стальной меч"
        pr = "кольчуга"
    elif fight == 3:
        w = "чёрная рапира"
        pr = "стальной нагрудник"
    print("\'Вы обнаружили предметы:", w, "и", pr ,".\'\n\'Ваш урон и запас здоровья увеличен.\'\n\'Здоровье: ", fhp,"\'\n\'Урон: ", dm,"\'")
    hp = fhp
    return fhp, dm, w