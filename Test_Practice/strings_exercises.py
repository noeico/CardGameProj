

# word = str(input("please insert a word"))
# word_length = len(word)
# first_letter = word[0]
# last_letter = word[word_length-1]
# for x in range(word_length):
#     print(first_letter,last_letter)

def find_letter():
    word = str(input("please insert a word"))
    letter = str(input("please insert a letter"))
    word_length = len(word)
    for x in range (word_length):
        if word[x] == letter:
            return x
    return -1


print(find_letter())
