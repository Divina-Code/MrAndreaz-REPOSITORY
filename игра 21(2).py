from random import randint


print("добро пожаловать в игру 21")
n = int(input("Сколько игроков будет?\t"))
print()


players = []  
points = [] 
playORnot = []  

for i in range(n):  
   
    name = input("Введите имя " + str(i + 1) + "-го игрока:\t")
    players.append(name) 

   
    random_points = randint(1, 10) 
    points.append(random_points) 

    
    playORnot.append(True)

for i in range(n):  
    print(players[i], "У вас очков:", points[i])



while playORnot.count(True) > 0:
    print("\n \t\t\tROUND")

    for i in range(n):
        print()
        if playORnot[i] == True:
            answer = input(players[i] + ' будете брать карту? [ДА\НЕТ]')

            answer = answer.upper()  
            answer = answer.strip() 

            if answer == "ДА":
                random_points = randint(1, 10)
                points[i] += random_points
                print(players[i], "Вам выпало:", random_points)

                if points[i] >= 21:
                    playORnot[i] = False
                   

            elif answer == "НЕТ":
                print("Вы ответили ", answer)
                playORnot[i] = False
            else:
                print("Не понял твоего ответа, принимаю только 'ДА' или 'НЕТ' ")

    print("\n____________________________")
    for i in range(n):  
        print(players[i], "У вас очков:", points[i])
