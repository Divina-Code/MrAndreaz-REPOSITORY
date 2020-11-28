from random import randint 



words  = ["австралия", "индия", "джибути", "англия", "филиппины"]

random_index = randint(0, 4) 
word = words[random_index] 

print(word)

game = True 
lives = 10 


letters = []

while game:
    print()
    print()
    print("*"+"___*"*len(word))
    letter = input("Введите букву или слово: ")

    if len(letter)<1: 
        print("Нужно ввести что-нибудь, букву или слово")
        
    elif len(letter) == 1: 
       
        if letter in word:
            if letter not in letters: 
                print("Есть такая буква!")            
                letters.append(letter) 
            else:
                print("Ты уже угадывал такую букву")
                lives = lives - 1 
        else:
            print("такой буквы нет")
            lives = lives - 1    

    else: 
        if letter == word:
            print("ТЫ ПОБЕДИЛ! Игра окончена")
            
        else:
            print("Не угадал! Игра окончена, ТЫ ПРОИГРАЛ")
            
        game = False    
        
          
    
    print("Осталось", lives, "жизней", "Угаданные буквы: ", letters )    
    

    
    if lives == 0:
        print("У тебя кончились жизни, ты проиграл")
        game = False

    
print("Спасибо за игру, приходи ещё!")
