'''
This program calculates the final bowling score of a game based on user input.
'''

# --- Functions ---
def get_final_bowling_score(rolls):
    last_roll = penultimate_roll = ''
    score = 0
    return calculate_score(rolls, last_roll, penultimate_roll, score)

def calculate_score(remaining_rolls, last_roll, penultimate_roll, score):
    current_roll = remaining_rolls[0]
    was_strike = False
    was_spare = False
    if current_roll == '-':
        current_roll = 0
    elif current_roll == 'X':
        was_strike = True
        current_roll = 10
    elif current_roll == '/':
        was_spare = True
        current_roll = 10 - last_roll
    else:
        current_roll = int(current_roll)

    score += current_roll

    if penultimate_roll == 'X':
        score += current_roll
    if last_roll == 'X' or last_roll == '/':
        score += current_roll

    if len(remaining_rolls) == 1:
        # Depending on any strikes or spares in the final frame, there may need to be
        # some scoring adjustments
        if penultimate_roll == 'X':
            if last_roll == 'X':
                # The current_roll and last_roll were both added three times to
                # the final score. They should have only been added once and twice,
                # respectively, so subtract accordingly.
                return (score - (current_roll * 2) - 10)
            elif was_spare:
                # Remove the extra 10 points that were added for the final spare
                return (score - 10)
            else:
                # The final two rolls were added twice, but should have only been
                # added once.
                return (score - current_roll - int(last_roll))
        elif last_roll == '/':
            # The current_roll was added twice and should have only been added once
            return (score - current_roll)
        else:
            return score
    else:
        penultimate_roll = last_roll

        if was_spare or was_strike:
            # Reset the current roll to be the correct string
            current_roll = remaining_rolls[0]

        last_roll = current_roll
        remaining_rolls = remaining_rolls[1:]
        return calculate_score(remaining_rolls, last_roll, penultimate_roll, score)

# --- Test Cases ---
assert(get_final_bowling_score('XXXXXXXXXXXX') == 300)
assert(get_final_bowling_score('9-9-9-9-9-9-9-9-9-9-') == 90)
assert(get_final_bowling_score('5/5/5/5/5/5/5/5/5/5/5') == 150)
assert(get_final_bowling_score('X7/9-X-88/-6XXX81') == 167)

# --- Main Program ---
inputted_game = input("Enter a bowling game (with no quotes please!): ")
score = get_final_bowling_score(inputted_game)
print(score)
