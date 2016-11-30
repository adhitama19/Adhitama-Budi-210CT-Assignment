""" This is the week 3 task 1 solutions. It ask as to reversed a sentence. """


user_input = input("Please enter a sentence: ")         # (1)

list_append = []

lower_word = user_input.lower()                         # (1)
sentence_new = lower_word                               # (1)

first_sentence = sentence_new.split()                   # (1)

for word in first_sentence:                             # (n)
    list_append.append(word)                            # (n)

final_sentence = list_append[::-1]                      # (1)

combine_sentence = " ".join(final_sentence)                      # (1)
print(combine_sentence)                                          # (1)

# Big O Notation = 2n + 7
# Therefore the Big O = O(n)

"""
PSEUDOCODE:

user_input <- user input a sentence

list_append <- empty list

lower_word <- make all input lower case
sentence_new <- new variable for lower_word

first_sentence <- split the sentence new into list

for word <- FIRST_SENTENCE[0] to FIRST_SENTENCE[end]
    append word to list_append

final_sentence = reverse the list_append

combine_sentence <- join the final_sentence into string
print combine sentence // Output

"""
