def end(luck, hp,):
    if luck == 1 or hp != 0:
        print ("\'Персонаж выбрался из пещеры живым! Игра пройдена. Поздравляем!\'")
    elif hp == 0:
        print ("Игра окончена. Ваш персонаж мёртв.")
    trying = input("Хотите начать снова?(да/нет): ", )
    while trying != "да" and trying !="нет":
        trying = input("Хотите начать снова?(да/нет): ", )
    return trying
