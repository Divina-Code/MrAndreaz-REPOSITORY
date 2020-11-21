from random import randint
word = ("австралия")
dedant = 10
game = True
while game:
    letter = input ("Введите букву или слово: ")
    if letter in word:
        print ("Есть такая буква!")
    else:
        print ("Не подходит.")
        dedant = dedant - 1
        print ("Жизни: " + str(dedant))

    if letter == word:
        print ("ТЫ ПОБЕДИЛ! Игра окончена")
        game = False
