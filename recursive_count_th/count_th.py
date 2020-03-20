'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # Base case: if the length of the word is less than 2, we can assume the string "th" isn't in the word and can return 0
    # Working towards the base case:
    # if the string between indexes 0 and 2 equal "th", add 1 to the cout
    # if not, continue to the next set of indexes

    if len(word) < 2:
        return 0
    elif word[0:2] == "th":
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])
