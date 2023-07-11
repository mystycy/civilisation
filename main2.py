import json #to allow persistent storage
from time import time as unix #timer in latter parts of the game



class Player:
    """
    Player class used to instantiate a player object.
    """

    def __init__(self, player_name: str, lives: int, points: int, inventory=None):
        """
        Player Class Constructor
        :param player_name:
        :param lives:
        :param points:
        :param inventory:
        """
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
        self.name = player_name
        self.lives = lives
        self.points = points

    def contains_item(self, item: str):
        if item in self.inventory:
            return True
        return False


class Path:
    """
    Path class used to instantiate a path object
    """

    def __init__(self, path_number: int, collectable_item: str, hint: str, solution=None):
        """
        Path Class Constructor
        :param path_number:
        :param collectable_item:
        :param hint:
        :param solution:
        """
        self.number = path_number
        self.hint = hint
        self.item = collectable_item
        if solution is None:
            self.solution = []
        else:
            self.solution = solution


def save_progress(path_number: int, save_player: Player):  # function for saving the data into file
    """
    :param path_number:
    :param save_player:
    :return:
    """
    myDict = dict()  # making a dictionary
    myDict['path_number'] = path_number
    myDict['player'] = {}
    myDict['player']['lives'] = save_player.lives
    myDict['player']['name'] = save_player.name
    myDict['player']['points'] = save_player.points
    myDict['player'][
        'inventory'] = save_player.inventory  # once the data in dictionary is populated, write dictionary into progress.json file
    with open("progress.json", "w") as outfile:
        json.dump(myDict, outfile)


def play(path_number, game_map, player: Player):
    """
    Function which asks the user to save the progress first, if they don't want to, the function starts based on the
    path number given and acts based on that path functionality.
    :param path_number:
    :param game_map:
    :param player:
    :returns True False
    """
    prog = input(
        "\nEnter s/S to save your progress, or enter another key to continue\n>> ")  # prompting the user to save the progress
    if prog in ['S', 's']:
        save_progress(path_number, player)
        return False
    if player.lives > 0:  # checking the lives
        if path_number == 0:  # if the path is the first one
            print('Fresh fruits fallen from trees in this path can be eaten,\n'
            'as well as water from freshwater lake, so health is retained. ')
            print('Hint:', game_map[path_number].hint)  # program shows the hint of that path
            solution = input('Input Solution: ')  # user inputs the solution of the puzzle
            if solution in game_map[0].solution:  # if the solution is correct
                player.lives += 2
                player.points += 10
                print('\nCorrect answer! You have been rewarded with an axe, +2 lives and +10 points!')
                player.inventory.append(game_map[path_number].item)
                return True
            else:  # if the solution is incorrect
                print("\nWrong answer! You have lost a life, " + player_name + ".")
                player.lives -= 1
                return False
        elif path_number == 1:  # if the path is the second one
            print("The next path cannot be entered directly, as it is covered by twigs.")
            command = input("Enter action: ")  # user enters the command to clear the path
            command = command.strip('\n').split()
            if command[0] == 'u' and command[1] == 'axe' and command[
                1] in player.inventory:  # if the command is correct, does the same as path 1
                print("\nTwigs chopped of with axe. Path 2 cleared.\nSo, you thought this would be the end of challenge? \n"
                "Unfortunately, you do not get to be spoonfed for the rest of your life. On the bright side, \n"
                'you can still eat the apples fallen from trees in this path and water from nearby freshwater lake, \n'
                "to retain health. Now, moving on.\n ")
                
                print('Hint:', game_map[path_number].hint)
                solution = input('Input Solution: ')
                if solution in game_map[path_number].solution:
                    player.lives += 2
                    player.points += 10
                    print('\nCorrect answer! You have been rewarded with a flamethrower, +2 lives and +10 points!')
                    player.inventory.append(game_map[path_number].item)
                    return True
                else:
                    print("\nWrong answer! You have lost a life, " + player_name + ".")
                    player.lives -= 1
                    return False
            else:
                print('\nUnknown Input. Seems that this is already playing with your mind, ' + player_name + '.\n'
                'Remember to press the u key, followed by a space character and the appropriate item name.\n '
                'Lower case only!')
                return False

        elif path_number == 2:
            print("\nThe next path cannot be entered directly as it is blocked by the ice crystals.")
            command = input("Enter action: ")
            command = command.strip('\n').split()
            if command[0] == 'u' and command[1] == 'flamethrower' and command[1] in player.inventory:
                print("\nIce crystals melted by use of flamethrower. Path 3 cleared.\n"
                "WARNING: No fruits or freshwater present, from here onwards,\n"
                "so life is lost regularly due to hunger and thirst. Also, \n"
                "The longer it takes to answer ther riddle, the more lives will be lost.\n"
                )
                print('\nHint:', game_map[path_number].hint)
                start = unix()  # as in path 3 we will be looking at the time as well so we are starting the timer here
                solution = input('Input Solution: ')
                end = unix() - start
                end = end // 15  # checking the total time taken by the user to answer the riddle and dividing it by 15
                player.lives -= end  # subtracting that value from lives
                if solution in game_map[path_number].solution:
                    player.lives += 2
                    player.points += 10
                    print('\nCorrect answer! You have been rewarded with a torch, +2 lives and +10 points!')
                    player.inventory.append(game_map[path_number].item)
                    return True
                else:
                    print("\nWrong answer! You have lost a life, " + player_name + ".")
                    player.lives -= 1
                    return False
            else:
                print('\nWrong Input!')
                return False

        elif path_number == 3:  # if the path is fourth, everything is same except the time duration will be 10 seconds per life
            print("\nThe next path cannot be seen, let alone, accessed, due to the complete darkness. \n")
            command = input("Enter action: ")
            command = command.strip('\n').split()
            if command[0] == 'u' and command[1] == 'torch' and command[1] in player.inventory:
                print("\nPath 4 can now be seen and entered. \n"
                "WARNING: wildfire started in this path. Due to the obliterating heat, lives are lost\n"
                "during path and during answering the puzzle, at a higher rate!")
                print('Hint:', game_map[path_number].hint)
                start = unix()
                solution = input('Input Solution: ')
                end = unix() - start
                end = end // 10
                player.lives -= end
                if solution in game_map[path_number].solution:
                    player.lives += 2
                    player.points += 10
                    print('\nCorrect answer! You have been rewarded with an iceblaster, +2 lives and +10 points!')
                    player.inventory.append(game_map[path_number].item)
                    return True
                else:
                    print("\nWrong answer! You have lost a life, " + player_name + ".")
                    player.lives -= 1
                    return False
            else:
                print('Wrong Input!')
                return False
        elif path_number == 4:  # when the user at the last path
            print(game_map[path_number].hint)
            print('So, you have overcome your hunger, tiredness and the excruciating heat from the wildfire. \n'
            'Impressive! And you have, by instinct, managed to use the iceblaster to cool down your surroundings \n'
            'in Path 4. But you are not finished yet, you can do even better. Now, for the final challenge: Path 5. \n'
            'You have chosen to enter an abandoned gas/petrol station to search for the final clue.  \n'
            'You find an item that helps you find civilisation. Due to the challenges faced, you are not able to \n'
            'Easily pick or use this item. It may take time and effort. To pick and use this item, this time, \n'
            'press p or "pick", followed by a space character. Now, think hard about of the name of that item \n'
            'you have found, and enter the name. Good luck! \n')
            command = input("Enter action: ")
            if command in ['pick Map', 'Pick Map', 'p Map', 'p map']:  # if the user types pick map the game ends
                print(player_name + "uses the map and is going through the final part of Path 5, into civilisation.\n")
                print("Game finished. Congratulations! You have successfully entered civilisation. \n"
                'You have, and will become stronger, physically and mentally. Well done! Enjoy your day.')
                return True
            else:  # else if the user types wrong command
                print("\nWrong decision! You have lost a life. You must not let yourself become \n"
                'so easily overwhelmed and weak, ' + player_name + ".")
                player.lives -= 1
                return False
        else:
            print('\nWrong Input!')
            return False


def load_map():
    """
    Function to make a map of the game and return the map
    :returns Path[]
    """
    map_of_game = list()
    map_of_game.append(Path(1, 'axe', "A note which state 'the year the Fall of the Berlin wall has taken place' ", ['1989']))
    map_of_game.append(Path(2, 'flamethrower', "An old photograph of Aston Villa players lifting the Champions League Trophy", ['1982']))
    map_of_game.append(Path(3, 'torch', "A map of Yugoslavia and its countries, referring to the Breakup of Yugoslavia", ['1991', '1992']))
    map_of_game.append(Path(4, 'iceblaster', "Item in nearby abandoned lorry: photograph of the Great Fire of London", ['1666']))
    map_of_game.append(Path(5, 'map',
                            "Player drives in abandoned lorry obtained from Path 4, further enough to keep away from wildfire. \n"
                            'Fuel runs out, eventually. Player has to walk to an abandoned petrol station. ',
                            ['MAP', 'map']))
    return map_of_game


if __name__ == '__main__':
    """
    Player and MAP is initialized.
    The game starts here and runs.
    """
    player = Player('Player', 3, 0, [])  # player object
    game_map = load_map()  # map of the game
    player_name = input("\nEnter your name: ")
    print("\nGreetings, " + player_name + '. ifs1 presents.....')
    print("\n---CIVILISATION---")
    print(
        """
    You have woken up in the woods, hidden in the dark, away from all. 
    Confused and dazed, you do not know how or why you ended up here. 
    Nevertheless, dwelling isn't the way. To return to civilisaiton, 
    you must complete a series of puzzles, but it is not as easy as it
    may seem. There are obstructions and challenges you must face in the path. 

    - Look for a hint and proceed to the puzzle box, by pressing any key.
    - Enter the correct answer on the puzzle box. Use the hint to help you.
    - Upon entering the correct answer, you will be rewarded with an item.
    - Use the item to clear the way for your next destination by press the u key,
       followed by the space character and the appropriate item name, and see what awaits you.
    - Good luck!
    """)
    i = 0
    saved_progress = input("Enter S to load your saved progress, or enter another key to continue\n>> ")
    if saved_progress in ['s', 'S']:  # if user wants to reload its progress they will type S
        print('Loading of saved progress requested.\n')
        try:
            with open('progress.json', 'r') as f:  # initializing the player object based on data in file
                saved_dict = json.load(f)
                player = Player(saved_dict['player']['name'], int(saved_dict['player']['lives']),
                                int(saved_dict['player']['points']), saved_dict['player']['inventory'])
                i = saved_dict['path_number']  # getting the path number from file
        except FileNotFoundError:
            print("Path could not be found.\nStarting from path 0 .....")


    while i < 5:  # running a loop for paths
        #automatic deduction of a life - Path 3: -10s, Path 4: -15s 
        print('\nPlayer lives:', player.lives)
        print('Player points: ', player.points)
        print('Player inventory', player.inventory)
        print('Path ' + str(i + 1) + ' : ')
        #calling function of play
        #print player stats before calling function
        if play(i, game_map, player):
            i += 1
        
             
        elif player.lives == 1:
                print('No no no! Only one life left.' + player_name + ', What are you doing?!' 
                'You were almost history, you can do better! Pull your socks up and try harder!')

                 
        else:
            if player.lives <= 0:
                print('Shame on you! ' + player_name + ', it seems that your journey for\n' 
            'civilisation has ended before it even started. Is this the best you can do?\n' 
            'You are adisgrace to civilisation. Good riddance! Please, have a seat and\n'
            're-evaulate your life. You cannot end like this. Come back when you are prepared,\n' 
            'unless you want your disgrace of a half-shoddy attempt to haunt you for life!')
                exit(1)

            exit_input = input("To quit, enter Q, or press another key to continue.\n"
            'When reloading the game, you can load your progress if saved. '
            " \n >> ")
            if exit_input in ['q', 'Q']:
                exit(1)
