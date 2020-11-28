from random import randint
words = ["АВСТРАЛИЯ","ИНДИЯ","КИТАЙ","АНГЛИЯ","ГЕРМАНИЯ"]
random_index = randint (0, 4) 
word = words [random_index]
lives = 10
game = True
letters = []
while game:
    print (" "+"__ "*len(word))
    letter = input ("Введите букву или слово: ")
    if letter == word:
        print ("ТЫ ПОБЕДИЛ! Игра окончена.")
        game = False
    elif letter in word:
        print ("Есть такая буква!")
        letters.append(letter)
        print ("Угаданные буквы: ", letters)
    else:
        print ("Не подходит.")
        lives = lives - 1
        print ("Осталось", lives, "жизней")
        print ("Угаданные буквы: ", letters)
    if lives == 0:
        print ("Ты проиграл...")
        print ("Слово было", word)
        game = False
