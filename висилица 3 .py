from random import randint
words = ["АВСТРАЛИЯ","ИНДИЯ","ДЖУБУТИ","АНГЛИЯ","ФИЛИППИНЫ"]
random_index = randint (0, 4) 
word = words [random_index]
lives = 10
game = True
while game:
    print (" "+"__ "*len(word))
    letter = input ("Введите букву или слово: ")
    if letter in word:
        print ("Есть такая буква!")
    else:
        print ("Не подходит.")
        lives = lives - 1
        print ("Жизни: " + str(lives))

    if letter == word:
        print ("ТЫ ПОБЕДИЛ! Игра окончена")
        game = False
    if lives == 0:
        print ("Ты проиграл...")
        game = False
