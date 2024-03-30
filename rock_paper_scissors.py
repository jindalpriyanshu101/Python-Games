import random
import time


print("<==== Welcome to Rock Paper Scissors Game ====>\n")
print('!! Winning rules of the game ROCK PAPER SCISSORS are: !!\n'
	+ "Rock vs Paper -> Paper wins\n"
	+ "Rock vs scissors -> Rock wins\n"
	+ "Paper vs scissors -> scissor wins\n")

List = ['Rock','Paper','Scissors']

while True:

    print("Enter your choice:\n 0 - Rock \n 1 - Paper \n 2 - scissors \n")

    choice=int(input("Enter your choice: "))
    # looping AS LONG AS user enters invalid input
    while choice > 2 or choice < 0:
        choice =int(input('Enter a valid choice please '))
    
    choice_name = List[choice]
    
    print(f'User choice is: {choice_name} \n')
    time.sleep(1)
    print('Now its Computers Turn....')
    time.sleep(1)

    
    comp_choice = random.randint(0,2)
    comp_choice_name = List[comp_choice]

    print(f"Computer choice is: {comp_choice_name} \n")
    time.sleep(1)
    print(choice_name,'Vs',comp_choice_name)

    if choice == comp_choice:
        result="DRAW"
    
    if (choice==0 and comp_choice==1):
        print('<= paper wins =>\n')
        result='papeR'
    elif (choice==1 and comp_choice==0):
        print('<= paper wins =>\n')
        result='Paper'

    if (choice==0 and comp_choice==2):
        print('<= Rock wins =>\n')
        result='Rock'
    elif (choice==2 and comp_choice==0):
        print('<= Rock wins =>\n')
        result='rocK'

    if (choice==1 and comp_choice==2):
        print('<= scissors wins =>\n')
        result='scissorS'
    elif (choice==2 and comp_choice==1):
        print('<= scissors wins =>\n')
        result='Scissors'

    if result == 'DRAW':
        print("\033[33m<== Its a tie ==>\033[0m\n")         # Yellow coloured output
    elif result == choice_name:
        print("\033[32m<== YOU WON ==>\033[0m\n")       # Green coloured output
    else:
        print("\033[31m<== Computer wins ==>\033[0m\n")         # Red coloured output
    time.sleep(1)

    stop = input("Do you want to play again? (Y/N): ")
    if stop.lower() == 'n':
        break


print("<== Game Ended ==>")
