""" This is the week 3 task 1 solutions. It ask us to reverse a sentence.

    input = This is awesome
    output = awesome is this

"""


#CODE:

def reverse_sent(usr_input):

    inputStr = usr_input                                             # (1)

    list_append = []                                                 # (1)

    lower_word = inputStr.lower()                                    # (1)
    sentence_new = lower_word                                        # (1)

    first_sentence = sentence_new.split()                            # (1)

    for word in first_sentence:                                     # (n)
        list_append.append(word)                                     # (n)

    final_sentence = list_append[::-1]                               # (1)

    combine_sentence = " ".join(final_sentence)                      # (1)
    return (combine_sentence)                              # (1)

user_input = input("Please enter a sentence: ")                      # (1)

func_call = reverse_sent(user_input)
print(func_call)

# Big O Notation = O (2n + 9)

# Therefore the Big O = O(n)


"""

PSEUDOCODE:

REVERSE_SENT(USR_INPUT)

    inputStr <- USR_INPUT

    list_append <- empty list

    lower_word <- make all input lower case
    sentence_new <- new variable for lower_word

    first_sentence <- split the sentence_new into list

    for word <- FIRST_SENTENCE[0] to FIRST_SENTENCE[end]
        append word to list_append

    final_sentence = reverse the list_append

    combine_sentence <- join the final_sentence into string

    return combine sentence // Output
    
user_input <- input("Please enter a sentence: ")
func_call <- reverse_sent (user_input)

print(func_call)


"""
