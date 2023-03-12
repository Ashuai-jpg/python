
import random

def get_choices():
    player_choice = input('Enter a choice(rock, paper, scissors):')
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {"player":player_choice, "computer":computer_choice }

    return choices


def check_win(player,computer):
    if(player=='rock'):
        if(computer=='scissors'):
            print(f'You chose {player}, computer chose {computer} \n You Win!')
        elif(computer=='paper'):
            print(f'You chose {player}, computer chose {computer} \n You Lose!')
        elif(computer=='rock'):
            print(f'You chose {player}, computer chose {computer} \n I\'t a Tie!')
    elif(player=='paper'):
        if(computer=='scissors'):
            print(f'You chose {player}, computer chose {computer} \n You Lose!')
        elif(computer=='paper'):
            print(f'You chose {player}, computer chose {computer} \n I\'t a Tie!')
        elif(computer=='rock'):
            print(f'You chose {player}, computer chose {computer} \n You Win!')
    elif(player=='scissors'):
        if(computer=='scissors'):
            print(f'You chose {player}, computer chose {computer} \n I\'t a Tie!')
        elif(computer=='paper'):
            print(f'You chose {player}, computer chose {computer} \n You Win!')
        elif(computer=='rock'):
            print(f'You chose {player}, computer chose {computer} \n You Lose!')


choice = get_choices()

check_win(choice["player"],choice["computer"])