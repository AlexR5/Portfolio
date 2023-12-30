import random

print("Welcome to Hangman.")
print("You have 10 guesses for the word below.")
print("Good luck!")
print("")

word_list = ["batman","door","spiderman","ocean","dad","bottle","liverpool","earth"]
w = random.randint(0,4)
word = word_list[w]

str(word)
a =(len(word))
word_space = a * "_"
print(word_space)
print("There are " + str(a) + " letters.")

found = False
tries = 10
while found == False and tries != 0:
    if "_" not in word_space:
        found = True
    else:
        print("")
        let = input("Enter a letter: ")
        while len(let) != 1:
            print("Please enter just one letter!")
            let = input("Enter a letter: ")
        c = word.count(let)
        if let in word:
            print("Still " + str(tries) + " tries left.")
            if c ==1:
                poflet = word.find(str(let))
                word_space= word_space[:(poflet)] + let + word_space[(poflet+1):]
                print(word_space)
            else:   
                poflet = word.find(str(let))
                word_space= word_space[:(poflet)] + let + word_space[(poflet+1):]
                poflet = word.rfind(str(let))
                word_space= word_space[:(poflet)] + let + word_space[(poflet+1):]
                print(word_space)
        else:
            print("Letter not in word!")
            tries -= 1
            print(str(tries) + " tries left.")
    
if found == True:    
    print("Well done, you have guessed the word!")
else:
    print("You are out of tries, better luck next time!")
    print("The word was: " + word)
    
