import begin
import pa
import rooms
import bos
import fighting
import winning
import end
from clas import cls
if __name__ == '__main__':
    trying = "да"
    while trying == "да":
        bossess = ["Тролль" , "Красноглазый волк" , "Бронированный скелет"]
        fight = 1
        luck = 0
        bocc = cls(1,1,1,1)
        import random as r
        name = str(input("Введите имя персонажа: ", ))
        print ("1-Лёгкий", "2-Средний", "3-Сложный")
        difficult = input("Выберите уровень сложности: ", )
        while difficult != "1" and difficult != "3" and difficult != "2":
            print ("1-Лёгкий", "2-Средний", "3-Сложный")
            difficult = input("Выберите уровень сложности: ", )
        cl = input("Выберите героя: 1-крестьянин, 2-рыцарь.")
        while cl != "1" and cl != "2" and cl != "37":
            cl = input("Выберите героя: 1-крестьянин, 2-рыцарь.")
        if cl == "1" :
            character = cls("крестьянин" , 160, "топор", 20)
        elif cl == "2" :
            character = cls("рыцарь", 200, "ржавый меч", 30)
        else:
            character = cls("бог", 100000, "божественная кара", 1000)
        print ("Имя персонажа: " , name , "\nВаш класс: ", character.cl, "\nОружие: ", character.w, "\nУрон: ", character.dm, "\nЗдоровье: ", character.fhp )
        input()
        hp = begin.beg1(character.cl, character.fhp, character.w, name)
        while fight != 4 and hp != 0 and luck != 1:
            hp, luck, character.dm, character.w = pa.path(name, character.cl, character.w, character.dm, hp, luck)
            if hp != 0 and luck != 1:
                room = rooms.ro(name, character.cl)
                bocc.name = r.choice(bossess)
                bossess.remove(bocc.name)
                bocc.name, agr, bocc.dm, bocc.fhp, bocc.w = bos.bos(name, character.cl, room, difficult, fight, bocc.name)
                if agr == 1:
                    choose, hp = fighting.fig(name, character.cl, character.fhp, character.dm, bocc.fhp, bocc.name, bocc.dm, fight)
                    if choose == "нет":
                        break
                fight += 1
                if fight != 4:
                    character.fhp, character.dm, character.w = winning.win(name, character.cl, character.fhp, character.dm, character.w, fight)
                    hp = character.fhp
        trying = end.end(luck, hp)
    print("Возвращайтесь скорее!!!")
