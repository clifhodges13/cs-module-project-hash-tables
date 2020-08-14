def no_dups(s):
    # Your code here

    # if string is empty
    if s == "":
        # return empty string
        return s

    word_bank = []

    return_string = ""

    # split the string up into a list of words at each empty space
    list_of_words = s.split(' ')

    # for each word
    for w in list_of_words:
        # if the word is not already in the word bank
        if w not in word_bank:
            # add the word to the word bank
            word_bank.append(w)

    # revert list of words back into single string with spaces between words
    for l in word_bank:
        l += ' '
        return_string += l

    # return string with no duplicates and no extra space at the end
    return return_string[:-1]



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))