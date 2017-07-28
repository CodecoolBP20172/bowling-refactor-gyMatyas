def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for current_roll in range(len(game)):
        if game[current_roll] == '/' and frame < 10:
            result += 10 - get_value(game[current_roll - 1]) + get_value(game[current_roll + 1])
        elif game[current_roll].upper() == 'X' and frame < 10:
            result += get_value(game[current_roll]) + get_value(game[current_roll + 1])
            if game[current_roll + 2] == '/':
                result += 10 - get_value(game[current_roll + 1])
            else:
                result += get_value(game[current_roll + 2])
        if in_first_half and not game[current_roll].upper() == 'X':
            in_first_half = False
        else:
            in_first_half = True
            frame += 1
    return result

def get_value(roll):
    #######
    # Description: Returns the current roll's score
    # Inputs: roll - player's current roll
    # Returns: the value of the roll in number
    #######
    return int(roll) if roll.isdigit() else 10 if roll.upper() in 'X/' else 0 if roll == '-' else ValueError
