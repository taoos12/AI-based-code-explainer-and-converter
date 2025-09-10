import random

def play():
    user = input("What's your choice?? 'r' for rock, 'p' for paper and 's' for scissor: ").lower()
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'
    
def is_win(player, opponent):
    if (player == 's' and player == 'p') or (player == 'p' and opponent == 'r') or (player == 'r' and opponent == 's'):
        return True
    
print(play())