import random

def asign(option):
    if option == 1:
        choice = "Rock"
    elif option == 2:
        choice = "Paper"
    elif option == 3:
        choice = "Scissor"
    else:
        print("Invalid input")
        quit()
    return choice

score = 0

def check_win(choice_list, name):
    global score
    if choice_list == [1, 3]:
        score += 10
        winner = name
    elif choice_list == [3, 2]:
        score += 10
        winner = name
    elif choice_list == [2, 1]:
        score += 10
        winner = name
    elif choice_list[0] == choice_list[1]:
        winner = "It's a tie."
    else:
        winner = "Computer"
    return score, winner

def play(rounds, name):
    for i in range(rounds):
        player_input = int(input("Enter your choice:"))
        comp_input = random.randint(1, 3)

        player_choice = asign(player_input)
        print("Your choice is ", player_choice)
        comp_choice = asign(comp_input)
        print("Computer choice is ", comp_choice)

        choice_list = [player_input, comp_input]
        score, winner = check_win(choice_list, name)
        print(f"Winner of round {i + 1} is {winner}.")
        print(f"Your current score is ", score)
    return score, winner

def win_calc(rounds, score, name):
    if score > ((rounds * 10 / 2)):
        final_win = name
    else:
        final_win = "Computer"
    return final_win

def announce(rounds, score, name):
    if (rounds % 2 != 0):
        final_winner = win_calc(rounds, score, name)
    else:
        if score == ((rounds * 10 / 2)):
            print("Oh no! It's a tie. So lets have a tie breaker round!")
            final_round_score, final_winner = play(1, name)
        else:
            final_winner = win_calc(rounds, score, name)
    return final_winner

if __name__ == "__main__":
    print("Welcome to rock paper scissor game!")
    print("You will be playing with the computer.")
    print("""The input system is as follows:
        - Press '1' for Rock
        - Press '2' for Paper
        - Press '3' for Scissor""")

    name = input("Enter your name:")
    rounds = int(input("Enter the number of rounds you want to play:"))
    score, winner = play(rounds, name)
    win_name = announce(rounds, score, name)
    print("The winner is .... ", win_name)
