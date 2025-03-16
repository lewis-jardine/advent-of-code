total = 0

with open("input.txt", "r", encoding="utf-8") as f:
    rounds = f.readlines()

    # Loop through each round, find opponents plays in int form
    # 0 is rock, 1 is paper, 2 is scissors
    for round in rounds:
        opponent = ord(round[0]) - 65
        player = round[2]

        print(opponent, player)
        
        # 'Z' means a win is required. requires play one greater than opponents
        # Modulo ensures it loops to be no greater than 3.
        if  player == 'Z':
            play = (opponent + 1) % 3 

            # 6 points for a win
            total += 6 + play + 1

        # To draw, both choices must be equal, play is equivalent to opponents
        elif player == 'Y':
            
            # 3 points for a draw
            total += 3 + opponent + 1

        # Loss requires a play one less than opponents
        else:
            # 0 points for a loss
            play = (opponent - 1) % 3 
            total += play + 1


print(total)