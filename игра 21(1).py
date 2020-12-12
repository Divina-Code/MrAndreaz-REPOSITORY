from random import randint



#####
print("добро пожаловать в игру 21")
n = int(input("Сколько игроков будет?\t"))  
print()


players = [] #Список имён игроков
for i in range(n):  #НОВЫЙ ЦИКЛ FOR
    name = input("Введите имя " +str(i+1)+"-го игрока:\t" )
    players.append(name)

print("\nИГРОКИ: ", players)

points = [] #Сколько очков набрал каждый игрок
for j in range(n):
    random_points = randint(1, 10)
    points.append(random_points)
    print(players[j], "Ваш счёт:", random_points)

print("\nОЧКИ: ",points)

game = True #Игра продолжается или закончена
while game:
    for a in range(n):
        answer = input(players[a] + ' будете брать карту? [ДА\НЕТ]')

        answer = answer.upper() #Делаем все буквы ЗАГЛАВНЫМИ
        answer = answer.strip()  #УБираем лишние пробелы, если они есть

        if answer == "ДА":
            print("Вы ответили ", answer)
        elif answer == "НЕТ":
            print("Вы ответили ", answer)
        else:
            print("Не понял твоего ответа, принимаю только 'ДА' или 'НЕТ' ")
