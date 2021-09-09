import random

conv_dict = {'rock':['rock',0],
             'Spock':['Spock',1],
             'paper':['paper', 2],
             'lizard':['lizard', 3],
             'scissors':['scissors',4]}


def name_to_number(name):
    return conv_dict[name][1]

def number_to_name(number):
    for x in conv_dict:
        if conv_dict[x][1] == number:
            return conv_dict[x][0]


def rpsls(player_choice):
    print('')
    print('Your choice is', player_choice)
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(5)
    comp_choice = number_to_name(comp_number)
    print('Computer choice is', comp_choice)
    diff = (player_number - comp_number) % 5
    if diff == 1 or diff == 2:
        print('Congratulations, you win.')
    elif diff == 3 or diff == 4:
        print('Sad days, beaten by some recurring ones and zeroes.')
    else:
        print("It's a tie!")


def run():
    print("Let's play a game, see if you can beat the computer.")
    print("\n-- Rock, Paper, Spock, Lizard, Scissors -- \n")
    print("""Rocks beast lizard and scissors,
    paper beats rocks and scissors,
    Spock beats paper and rock,
    lizard beats Spock and paperm
    scissors beats lizard and Spock.""")
    print('Make your choice and see if you can beat the computer.')

    while True:
        print('')
        player_choice = input('Guess! - ')
        if player_choice not in conv_dict:
            print('Try again!')
            continue
        rpsls(player_choice)
        end = input('Another round? - y/n - ')
        if end == 'n':
            break