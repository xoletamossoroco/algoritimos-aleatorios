def scrabble_score(word):
    score = 0
    for letter in word:
        letter = letter.lower( )
        if letter in ['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't']:
            score += 1
        elif letter in ['d', 'g']:
            score += 2
        elif letter in ['b', 'c', 'm', 'p']:
            score += 3
        elif letter in ['f', 'h', 'v', 'w', 'y']:
            score += 4
        elif letter in ['k']:
            score += 5
        elif letter in ['j', 'x']:
            score += 8
        elif letter in ['q', 'z']:
            score += 10
    return score