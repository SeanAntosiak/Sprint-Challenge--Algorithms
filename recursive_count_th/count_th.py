'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if len(word) < 2:
        return(0)
    elif word == 'th':
        return(1)
    elif word[0:2] == 'th':
        count = 1 + count_th((word[2:len(word)]))
        return(count)
    else:
        count = count_th(word[1:len(word)])
        return(count)
