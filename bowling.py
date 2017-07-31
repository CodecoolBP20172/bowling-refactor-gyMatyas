def score(game):
    """
    # Description: Calculates the total score of the game.
    # Inputs: game - The log of the game.
    # Returns: The game's total score.
    """
    result = 0
    frame = 1
    in_first_half = True
    for current_roll in range(len(game)):
        result = game_logic(current_roll, game, frame, result)
        if in_first_half and not game[current_roll].upper() == 'X':
            in_first_half = False
        else:
            in_first_half = True
            frame += 1
    return result


def game_logic(current_roll, game, frame, result):
    """
    # Description : Adds the current roll's score to total result
    # Inputs: current_roll - The player's current roll
    #         game - The player's every roll
    #         frame - The number of the current frame (round)
    #         result - The total result
    # Returns: The result after adding the current roll
    """
    if game[current_roll] == '/' and frame < 10:
        result += 10 - get_value(game[current_roll - 1]) + get_value(game[current_roll + 1])
    elif game[current_roll].upper() == 'X' and frame < 10:
        result += get_value(game[current_roll]) + get_value(game[current_roll + 1])
        if game[current_roll + 2] == '/':
            result += 10 - get_value(game[current_roll + 1])
        else:
            result += get_value(game[current_roll + 2])
    else:
        result += get_value(game[current_roll])
    return result


def get_value(roll):
    """
    # Description: Returns the current roll's value
    # Inputs: roll - The player's roll
    # Returns: The value of the roll in number
    """
    return int(roll) if roll in '123456789' else 10 if roll.upper() in 'X/' else 0 if roll == '-' else ValueError
