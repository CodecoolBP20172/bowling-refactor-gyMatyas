def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - get_value(game[i - 1])
        else:
            result += get_value(game[i])
        # if not in_first_half:
            # frame += 1
        if frame < 10  and get_value(game[i]) == 10:
            if game[i] == '/':
                result += get_value(game[i+1])
            elif game[i] == 'X' or game[i] == 'x':
                result += get_value(game[i+1])
                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        if in_first_half and not game[i].upper() == 'X':
            in_first_half = False
        else:
            in_first_half = True
            frame += 1
    return result

def get_value(char):
    return int(char) if char.isdigit() else 10 if char.upper() in 'X/' else 0 if char == '-' else ValueError
