import random as r

def fig(name, c, fhp, dm, bfhp, bname, bdm, fight):
    print ("\'Враг заметил вас! Сражение начинается.\'")
    hp = fhp
    bhp = bfhp
    shift = 0
    while bhp != 0 and shift != 1:
        back = 0
        shift = 0
        choose = input("1-Ударить, 2-Попытаться пробежать к выходу, 3-Отступить. Выбор:", )
        while choose != "1" and choose != "2" and choose != "3":
            choose = input("1-Ударить, 2-Попытаться пробежать к выходу, 3-Отступить. Выбор:", )
        if choose == "1":
            chanse = r.randint(1, fight*3)
            if chanse == 1:
                bhp -= dm
                print ("\'Атака прошла успешно.\'")
            else:
                print ("\'Промах.\'")
        elif choose == "2":
            chanse = r.randint(1, fight*6)
            if chanse == 1:
                shift = 1
                print (name, "смог прорваться к выходу!")
            else:
                print (bname, "не позволил пробежать мимо него.")
        else:
            chanse = r.randint(1, ((fight+1)*5))
            if chanse == 1:
                back = 1
                print (name, "смог убежать от врага!")
            else:
                print ("\'",bname, "не дал герою сбежать.\'")
        if back == 1:
            print ("\"Нужно немного передохнуть, и с новыми силами я точно его одалею!\"")
            hp = fhp
            input()
            print ("\'После отдыха ваше здоровье восстановилось. Здоровье:", hp,"\'")
            print ("\'Вы вновь вступили в сражение с боссом", bname,"\'")
        if bhp <= 0:
            bhp = 0
        if bhp != 0 and shift != 1 and back !=1:
            chanse = r.randint(1, ((fight+1)*2))
            if chanse != 1:
                print ("\'Получен урон:", -bdm, "ед.зд.\'")
                hp -= bdm
            else:
                print ("\'Враг промахнулся\'")
        input()
        if hp <= 0:
            hp = 0
        if shift != 1 and back !=1:
            print ("\'Здоровье персонажа:", hp, "\'")
            print ("\'Здоровье врага:", bhp, "\'")
        if hp == 0:
            print ("\'Вы проиграли. Герой мёртв.\'")
            choose = input("Хотите начать сражение снова?(да/нет): ", )
            while choose != "да" and choose != "нет":
                choose = input("Хотите попробовать снова?(да/нет): ", )
            if choose == "да":
                hp = fhp
                bhp = bfhp
                print ("\'Враг заметил вас! Сражение начинается.\'")
            elif choose == "нет":
                break
    if hp > 0 and shift != 1:
        print ("\'",bname, "был повержен.\'")
    input()
    return choose, hp
