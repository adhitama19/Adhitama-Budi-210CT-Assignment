reversed_list = []

user_input = input("Please enter a sentence: ") #User will input a sentence
lower_word = user_input.lower() #All the words will be in lower_case
sentence_new = lower_word #Assign new variable for lower_word

first_sentence = sentence_new.split() # The words that user have inputted will be in the form of list
final_sentence = first_sentence[::-1] # Dibalik

di_wrap = " ".join(final_sentence) # Digabungin jadi 1
print(di_wrap) #di_wrap ditunjukin di intrepreter


#user_input = input ("Please enter a sentence: ")

#def reversedFunc(user_input):
#    while len(user_input) > 1:
