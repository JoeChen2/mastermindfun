""" 
Mastermind Game
Version 0.91
Part by Vincent, Connor, Clemson
last updated(2019/3/3)
"""

import Game_Over
import generate_rand #Change with actual generator
import userinput_processing#userinput processing
import Game_Value_Check

def titlescreen():
    """Prints titlescreen"""
    title_seperator = "*" * 20
    print(title_seperator)
    print()
    print("Mastermind Game")
    print()
    print(title_seperator)
    print()

def rules():
    """Prints the rules"""
    print("Placeholder Rules")
    print()

def start_options():
    """Player chooses if they want to start the game"""
    while True:
        print("Type 1 to start the game")
        print("Type 2 to show the rules")
        print("Type 3 to quit the game")
    
        while True:#check if the input can be turn into interger
            try:
                start_option = int(input("Type your option: "))
                break
            except:
                print("please enter a number from 1-3.")
        print()

        
        if start_option == 1: #Starts game
            game_options()
        elif start_option == 2: #Shows rules
            rules()
        elif start_option == 3: #Quits game
            quit()
        else:
            print("please enter a number from 1-3.")




def game_options():#the acutal game start
    """Player chooses game options"""

    
    try:
        code_length = int(input("How long do you want the code to be? "))
    except:
        print("Invalid input")
        print()


        
    while True:#this is for obtaining weather the user wants repeats in the code
        repeats_input = input("Do you want repeats [y/n]? ")
        repeats = bool()#the variable to store weather the user wants repeats or not

        if repeats_input == "y":
            repeats = True
            break
        elif repeats_input == "n":
            repeats = False
            break
        else:
            print("Invalid input.\n")
    
    game_loop(code_length,repeats)#start the guessing part




def random_code(code_length, repeats):
    """Generates random code"""
    code = generate_rand.generate_random_nunmber(repeats, code_length) #change with actual generator
    return code
    
def game_loop(code_length,repeats):#generate a code abased on setting and start the guessing
    start_again = True#used when the game is won, to indicate the player like to play again with the same setting
    
    """Generates the code and initilise the variables"""
    while start_again == True:#if its false, it will return to the main menu
        code = random_code(code_length,repeats)
        win = False
        tries=0
        
        while(win==False):#make a guess and the program responds
            uinput=userinput_processing.processinput(code)
            CP,CN = Game_Value_Check.Compare(code,uinput)
            
            if CP == len(code):#the user wins
                start_again=Game_Over.End(tries)
                win=True
                
            else:#the user havent win
                print(CP,"in correct place and number;",CN,"correct number but incorrect place.")
                tries += 1

        
        

def main():
    """Starts program"""
    titlescreen()
    start_options()

main()
