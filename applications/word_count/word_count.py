def word_count(s):
    # Your code here
    word_dict = {}

    # split the string into words
    s_list = s.split()

    # for each word
    for word in s_list:
        # remove all special characters and punctuation, except apostrophe and make lowercase
        word = ''.join(e.lower() for e in word if (e.isalnum() or e == "\'"))
        # if word string comes out empty, i.e. the previous line does not find any valid characters,
        if word == '':
            # return the empty dictionary
            return word_dict
        # if the word is not already in the dictionary
        if word not in word_dict:
            # give it a count of 1
            word_dict[word] = 1
        # if the word _is_ in the dictionary
        else:
            # add 1 to the count
            word_dict[word] += 1
    # return the dictionary
    return word_dict



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))