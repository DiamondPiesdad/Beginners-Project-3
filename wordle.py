#delete the 12th row
store=["apple","world","throw","games","point","guess","begin","start","think","china","happy","about","draft","heavy","faith","dream","false","extra","dance","shirt","shift"]
import random
print("Welcome to Wordle!")
print("You have 6 chances to guess a 5-letter word.")
state_all=False
score=0
while state_all==False:
        
    answer=store[random.randint(0,len(store)-1)]

    print(answer)#delete it

    store.remove(answer)
    state_oneplay=False
    count=0
    while state_oneplay==False:
        state_win=False
        guess=str(input("guess a 5-letter word."))
        if len(guess)>5:
            print("too many letters")
        elif len(guess)<5:
            print("not enough letters")
        else:
            output=["⬛️","⬛️","⬛️","⬛️","⬛️"]
            for i in range(5):
                for x in answer:
                    if guess[i]==x:
                        output[i]=("🟨")
                if guess[i]==answer[i]:
                    output[i]=("🟩")
            if guess==answer:
                print("corret! the word is",answer)
                state_oneplay=True
                print(output)
                state_win=True
            else:
                count+=1
                print(output)
            if count==6:
                print("you lose")
                print("the answer is",answer)
                state_oneplay=True
    if  state_win==True:
        score_get=random.randint(1,5)
        print("you get",score_get,"points")
        score+=score_get
        print("you have",score,"points now")
    else:
        print("you have",score,"points now")
    check_continue=input("do you want to continue?(please answer 'yes' or 'no')")
    if check_continue=="no":
        state_all=True
    else:
        if score>=20:
            print("you win!")
            state_all=True

            