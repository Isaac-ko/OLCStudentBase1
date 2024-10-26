import random

with open("/workspaces/OLCStudentBase1/Listof5LetterWords.txt", "r") as f:
    words = f.readlines()
#    cword - random.choice(words).strip().upper()

#clen up the list
cleanlist = []
for w in words:
    cleanlist.append(w.strip())#remove the /n

current_word = random.choice(cleanlist)
print(current_word)
for i in range(6):
    #ask for the person to guess
    while True:
        guess = input("Guess the 5 letter word: ")

        if len(guess) != 5:
            print("You must enter a 5-letter word")
        elif guess not in cleanlist:
            print("You must enter a proper word")
        else:
            break
    #use ? to denote correct letter but wrong place
    #use # to denote wrong letter

    display = "" # use to build the # ?

    for c in range(len(current_word)):

        if guess[c] == current_word[c]:# # if it matches
            display = display + guess[c]
        elif guess[c] in current_word:
            display = display + "?"

        else:
            display = display +"#"
    print(display.upper())
    print("# means the ;etter dpes not exist in the word")
    print("? means the word exist but in wrong position") 

    if guess == current_word:
        print("You guessed correctly.")
        break
    else:
        print("Try again")
