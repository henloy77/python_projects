from random import randrange,choice
import time
def logic(num):
    # human player turn
    computer_number = randrange(1,num)
    print("\nComputer is selecting a number")
    time.sleep(1)
    print("")
    player_count = 0
    player_guess = 0
    print("Its your turn \n")
    while True:
        try:
            player_guess =int(input(f"Guess a number between 0 and {num}: \n"))
            while True:
                if player_guess<1 or player_guess>=5:
                    player_guess =int(input(f"Please enter a valid number between 0 and {num}: \n"))
                    
                else:
                    break
            break
            
        except ValueError:
            print("Please input a valid number\n")
            continue
        
         
    
    player_count+=1
    while player_guess != computer_number:
        player_guess =int(input(f"\nSorry try again \n Guess a number between 0 and {num}: \n"))
        
        player_count+=1
        
        #

    print(f"\nYou got it right !\nIt took you {player_count} tries\n")

    # computers turn
    print("\nChoosing a number for computer to guess")
    time.sleep(2)
    rand_num = randrange(1,num)
    print(rand_num)
    choice_list=[]
    computer_count = 0
    computer_guess = choice(range(1,num))
    choice_list.append(computer_guess)
   
    while True:
        computer_guess = choice(range(1,num))
           
        if computer_guess in choice_list:
            continue
            
        if computer_guess not in choice_list:
            
            print(f"\nComputer guessing a number between 0 and {num}: ")
            time.sleep(1)
            choice_list.append(computer_guess)
            print(f"Computer chose {computer_guess}. ")
            time.sleep(1)
        if computer_guess != rand_num:
            print(f"\nComputer got it wrong, trying again")
            computer_count += 1
            choice_list.append(computer_guess)
            time.sleep(1)
        else:
            
            time.sleep(1)
            
            break
    print(f"\nComputer got it right !\nIt took {computer_count+1} tries")

    if player_count < computer_count+1:
        return ("\nCongratulations, you win !!!")
    elif player_count == computer_count+1:
        return ("\nIts a Tie !!!")
    return "\nSorry, you lost! "
    



print("Hello Gamer.. Welcome to the guessing game !")
time.sleep(1)

while True:
    response = input("\nWould you like to play.\nType Y for yes and N for no\n")
    if response.lower() == "y" or response.lower() == "n":
        if response.lower() == "y":
            print("Starting game..")
            time.sleep(1)
            break
        
        elif response.lower() == "n":
            print("Goodbye !")
    else:
        print("\n---Invalid response---\n")
        print
    
print(logic(5))
