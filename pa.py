import random as r

def path(n, c, w, d, hp, luck):
    chanse = r.randint(1,41)
    if chanse < 11:
        print ("Пройдя по тёмному коридору,", n, "наткнулся на развилку.")
        choose = input("1-Пойти налево, 2-Пойти направо. Выбор:", )
        while choose != "1" and choose != "2":
            choose = input("1-Пойти налево, 2-Пойти направо. Выбор:", )
        if choose == "1":
            print ("После долгих колебаний", c, "решил пойти налево.")
        if choose == "2":
            print ("\"Мама всегда говорила мне, что налево ходить нельзя, поэтому я пойду направо.\"")
        room = r.randint(1,100)
        if room == 1:
            input()
            print ("Пройдя немного вперёд,", n, "вышел из пещеры, оказавшись недалеко от своего дома.")
            luck = 1
        else:
            room = r.randint(1,5)
            if room == 1:
                print (c, "забрёл в комнату, усыпанную золотом и украшением.\n\"Здесь золота больше, чем в королевской казне! Возьму-ка я пару блестящих камушков, а остальное заберу, когда найду выход из этой пещеры.\"")
                input()
                print (n, "уже собирался уходить, но тут он заметил меч, который стоял в самом углу комнаты. Меч был уже не пригоден к использованию, ведь его кромка уже крошилась от старости.")
                choose = input("1-Взять меч в руки, 2-Уйти. Выбор:", )
                while choose != "1" and choose != "2":
                    choose = input("1-Взять меч в руки, 2-Уйти. Выбор:", )
                if choose == "1":
                    chanse = r.randint(1,10)
                    if chanse == 1:
                        print ("Как только", n, "взял меч в руки, тот засветился, заставив человека закрыть глаза.\nОткрыв глаза,", c, "увидел в своих руках великолепный меч.")
                        input()
                        print ("\'В ваши руки попал священный меч. Урон: 20.")
                        choose = input("1-Взять меч, 2-Не брать меч. Выбор:", )
                        while choose != "1" and choose != "2":
                            choose = input("1-Взять меч, 2-Не брать меч. Выбор:", )
                        if choose == "1":
                            d = 100
                            w = "священный меч"
                            print ("\"Не пропадать же такому добру!\"\n\'Вы взяли", w,". Ваш урон:", d,"\'")
                        if choose == "2":
                            print ("\"Сила зависит не от оружая, а от умения!\"")
                    else:
                        а=1
                        print ("Это оказался самый обычный старый меч.\n\'","Ржавый меч. Урон: 5")
                        choose = input("1-Взять меч, 2-Не брать меч. Выбор:", )
                        while choose != "1" and choose != "2":
                            choose = input("1-Взять меч, 2-Не брать меч. Выбор:", )
                        if choose == "1":
                            d = 30
                            w = "Ржавый меч"
                            print ("\"Не пропадать же такому добру!\"\n\'Вы взяли", w,". Ваш урон: 5\'")
                        if choose == "2":
                            print ("\"Сила зависит не от оружая, а от умения!\"")
                    input()
                print("Вернувшись к развилке,", n, "пошёл в другую сторону.")
                input()
        print ("Всё больше и больше углубляясь в пещеру,", c,"чувствовал тревогу.")




    elif chanse < 21 and chanse > 10:
        print (n, "долго-долго шёл по тёмной пещере.")
        input()
        print ("\"Да сколько можно?! Я иду уже полдня!\"")
        input()
        print (c, "хотел было уже сдаться, но тут...")



    elif chanse < 31 and chanse > 20:
        print ("Немного пройдя вперёд,", n, "наткнулся на тупик.")
        choose = input("1-Вернуться назад, 2-Ударить стену. Выбор: ", )
        while choose != "1" and choose != "2":
            choose = input("1-Вернуться назад, 2-Ударить стену. Выбор: ", )
        if choose == "1":
            print (n, "сидел в яме, ожидая помощи, 3 дня и скончался от голода.")
            hp = 0
        elif choose == "2":
            chanse = r.randint(1,10)
            if chanse != 1:
                print ("После удара стена разрушилась и за ней оказался коридор!")
            else:
                print ("Ничего не случилось...")
                input()
                print ("\"Видимо, придётся вернуться назад и ждать помощи.\"")
                input()
                print (n, "сидел в яме, ожидая помощи, 3 дня и скончался от голода.")
                hp = 0




    elif chanse < 41 and chanse > 30:
        print ("Далее по коридору оказался крутой спуск.")
        choose = input("1-Съехать по спуску, 2-Вернуться назад. Выбор: ", )
        while choose != "1" and choose != "2":
            choose = input("1-Съехать по спуску, 2-Вернуться назад. Выбор: ", )
        if choose == "1":
            chanse = r.randint(1,10)
            if chanse == 1:
                print ("Спускаясь,", n, "сильно разогнался и на высокой скорости влетел в стену...")
                hp = 0
            else:
                print ("После спуска опять оказался длинный коридор.")
        else:
            print (n, "сидел в яме, ожидая помощи, 3 дня и скончался от голода.")
            hp = 0



    else:
        print (c, "долго шёл по пещере, как вдруг...он проснулся.\nОказывается, это был просто сон.\nВсё это время", n,"спал на столе в таверне.")
        pause = input()
        luck = 1
    return hp, luck, d, w