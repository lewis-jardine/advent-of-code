total = 0

with open("input.txt", "r", encoding="utf-8") as f:
    rounds = f.readlines()

    # Loop through each round, find my and opponents plays in int form
    # 0 is rock, 1 is paper, 2 is scissors
    for round in rounds:
        opponent = ord(round[0]) - 65
        player = ord(round[2]) - 88
        
        # Find game outcome, calculate score
        # To win, the opponents choice must be one below the players. 
        # Modulo ensures it loops to be no greater than 3.
        if (opponent + 1) % 3 == player:

            # 6 points for a win
            total += 6 + player + 1

        # To draw, both choices must be equal
        elif opponent == player:
            
            # 3 points for a draw
            total += 3 + player + 1

        # The other outcome then must be a loss
        else:
            # 0 points for a loss
            total += player + 1

print(total)