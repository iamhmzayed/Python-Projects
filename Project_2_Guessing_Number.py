#Project_2(GUESSING THE NUMBER)

import random
randomnumber = random.randint(1, 50)                 #min_value , max_value

a = input("What is your name ? ")
print (f"Welcome {a} to Guessing The Number Game")
print("...........................................")
userinput = int(input("\nGuess The Number Between 1 to 50 : "))

if userinput > randomnumber:
    print(f"\nThe Random Number is {randomnumber}")
    print(f"Your Guessed Number is {userinput}")
    print("The Number is Too high")
    print(f"\n:) TRY AGAIN BEST OF LUCK {a} ;)")

elif userinput < randomnumber:
    print(f"\nThe Random Number is {randomnumber}")
    print(f"Your Guessed Number is {userinput}")
    print("The Number is Too low")
    print(f"\n:) TRY AGAIN BEST OF LUCK {a} ;)")

else:
    print(f"The Random Number is {randomnumber}")
    print(f"Your Guessed Number is {userinput}")
    print("Correct")
    print(f"\n:) BINGO CONGRATULATIONS {a} ;)")

