# Mini Project : Rock Paper Scissors

import random



class Game:
    def __init__(self):
        self.game_items = {
            1: "rock",
            2: "paper",
            3: "scissors"
        }

        self.win_map = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }

    def valid_input(self):
        while True:
            try:
                user_input = int(input("\nWhat do you choose? \n\n1 - for ROCK \n2 - for PAPER \n3 - for SCISSORS \n\n"))
                if user_input in range(1, 4):
                    return user_input
                else:
                    print("=" * 50)
                    print("Number is out of range")
            except ValueError: 
                print("=" * 50)
                print("Not valid number")
        

    def get_user_item(self):
        return self.valid_input()
        
    def get_computer_item(self):
        return random.randint(1, 3)
    
    def get_game_result(self, user_item, computer_item):
        user_item = self.game_items[user_item]
        computer_item = self.game_items[computer_item]
        if user_item == computer_item:
            return "draw"
        elif self.win_map[user_item] == computer_item:
            return "win"
        else:
            return "loss"
        
    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        game_result = self.get_game_result(user_item, computer_item)
        print('=' * 50)
        print(f'You choose: {self.game_items[user_item]}')
        print(f'Computer choose: {self.game_items[computer_item]}')
        print(f"=> Game RESULT: {game_result}")
        print('=' * 50)
        return game_result

# g = Game()


# print(game_items)
# g.get_user_item()

# g.valid_input()
# print(f"\n{g.get_user_item()}")

# print(g.get_game_result(3, 3))

# g.play()

