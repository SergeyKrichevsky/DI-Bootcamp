from game import Game


def get_user_menu_choice():
    while True:
            try:
                user_input = int(input("\nGAME MENU - What do you choose? \n\n1 - Play a new game \n2 - Show scores \n3 - Quit \n\n"))
                if user_input in range(1, 4):
                    return user_input
                else:
                    print("=" * 50)
                    print("Number is out of range")
            except ValueError: 
                print("=" * 50)
                print("Not valid number")   

results = {"win": 0, "loss": 0, "draw": 0}    

def print_results(results):
    print("=" * 50)
    print('RESULTS:\n')
    for key, value in results.items():
          print(f"{key.capitalize()}s: {value}")
    print("=" * 50)

def main():
     while True:
            user_choice = get_user_menu_choice()
            if user_choice == 3:
                 print_results(results)
                 break
            elif user_choice == 2:
                 print_results(results)
            else: # Game Choice
                 new_game = Game()
                 score = new_game.play()
                 results[score] += 1
                 
            
        
          
main()               