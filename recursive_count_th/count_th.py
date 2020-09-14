'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base case:
    # if the length of the word is below 2 then
    # return 0
    if len(word) < 2:
        return 0
    #
    # also if the first letter of the word is "t" and
    # the second letter is "h" then count that as "1" plus
    # the rest occurences starting the 3rd letter of the
    # word going up
    elif word[0] == "t" and word[1] == "h":
        return 1 + count_th(word[2:])
    # and if not then progress the recursion starting
    # the 2nd letter of the word going up
    else:
        return count_th(word[1:])
