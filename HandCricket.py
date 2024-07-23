import random

def toss():
    computer_choice = random.choice(['odd', 'even'])
    print(f"Computer chose {computer_choice}.")
    
    player_choice = int(input("Enter your choice (1, 2, 3, 4, 5, 6): "))
    if player_choice not in [1, 2, 3, 4, 5, 6]:
        print("Invalid choice, please choose a number between 1 and 6.")
        return toss()
    
    computer_num = random.choice([1, 2, 3, 4, 5, 6])
    print(f"Computer chose {computer_num}.")
    
    total = player_choice + computer_num
    if total % 2 == 0:
        winner = 'even'
    else:
        winner = 'odd'
    
    if winner == computer_choice:
        print("Computer won the toss.")
        return 'computer'
    else:
        print("Player won the toss.")
        return 'player'

def play_inning(is_player_batting):
    score = 0
    while True:
        player_choice = int(input("Enter your choice (1, 2, 3, 4, 5, 6): "))
        if player_choice not in [1, 2, 3, 4, 5, 6]:
            print("Invalid choice, please choose a number between 1 and 6.")
            continue
        
        computer_choice = random.choice([1, 2, 3, 4, 5, 6])
        print(f"Computer chose {computer_choice}.")
        
        if player_choice == computer_choice:
            print("Out!")
            break
        else:
            if is_player_batting:
                score += player_choice
            else:
                score += computer_choice
        
        print(f"Score: {score}")
    
    return score

def main():
    toss_winner = toss()
    if toss_winner == 'player':
        decision = input("You won the toss! Choose 'bat' or 'ball': ").lower()
        if decision not in ['bat', 'ball']:
            print("Invalid choice, please choose 'bat' or 'ball'.")
            return main()
        player_bats_first = (decision == 'bat')
    else:
        decision = random.choice(['bat', 'ball'])
        print(f"Computer won the toss and chose to {decision}.")
        player_bats_first = (decision == 'ball')
    
    if player_bats_first:
        print("Player is batting first.")
        player_score = play_inning(True)
        print(f"Player scored: {player_score}")
        
        print("Computer is batting now. Target: ", player_score + 1)
        computer_score = play_inning(False)
        
        if computer_score >= player_score + 1:
            print("Computer won!")
        else:
            print("Player won!")
    else:
        print("Computer is batting first.")
        computer_score = play_inning(False)
        print(f"Computer scored: {computer_score}")
        
        print("Player is batting now. Target: ", computer_score + 1)
        player_score = play_inning(True)
        
        if player_score >= computer_score + 1:
            print("Player won!")
        else:
            print("Computer won!")

if __name__ == "__main__":
    main()
    
