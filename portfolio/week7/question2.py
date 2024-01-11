# Write and test three functions that each take two words (strings) as parameters and
# return sorted lists (as defined above) representing respectively:
# Letters that appear in at least one of the two words.
# Letters that appear in both words.
# Letters that appear in either word, but not in both.


unique_letters_either_word = lambda word1, word2: sorted(list(set(word1 + word2)))
unique_letters_both_words = lambda word1, word2: sorted(list(set(word1) & set(word2)))
unique_letters_not_both_words = lambda word1, word2: sorted(list(set(word1) ^ set(word2)))

def inps():
    word1= input("Enter first word: ")
    word2= input("Enter second word: ")
    return word1,word2

def getout():
    print("Letters in either word:", unique_letters_either_word(word1, word2))
    print("Letters in both words:", unique_letters_both_words(word1, word2))
    print("Letters in either but not both:", unique_letters_not_both_words(word1, word2))


word1,word2=inps()
getout()

