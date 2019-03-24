#function called End to display game over screen with score
#inputs  T: number of turns taken to win the game
#outputs C: continue playing boolean 

def End(T):

    print('Congratulations! You have completed this game in',T,'guesses!')
    print('Would you like to play again? (y/n)')

    ui = input()
    ui.lower()
    if ui[0] == "y":
        C = True
    else:
        C = False
    
    return C


