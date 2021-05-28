import random
choices = ["Rock","Paper","Scissors"]
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock,Paper or Scissors?").capitalize()
    print("Computer choice is",computer)
    if player == computer:
        print("Tie")
    elif player == "Rock":
        if computer == "Paper":
            print("You loose!",computer, "Covers",player)
            cpu_score+=1
        else:
            print("You win", player,"Smashes",computer)
            player_score+=1
    elif player == "Scissor":
        if computer == "Rock":
            print("You loose", computer,"Smashes",player)
            cpu_score+=1
        else:
            print("You Win", player,"Cuts",computer)
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You loose", computer,"Cuts",player)
            cpu_score+=1
        else:
            print("You win",player,"Covers",computer)
            player_score+=1
    elif player == 'End':
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Player:{player_score}")
        break
