""" This is the solution for coursework question 8. The question ask us to remove the vowels in a word. The method
    used for this solution is by using recursive function. The function will be defined as recursive_vowel with
    string as its parameter. further explaination will be explained through comments on the code """

vowels = ["A", "I", "U", "E", "O", "a", "i", "u", "e", "o"] 

def recursive_vowel(string):    

    if string == "":            
        return string           
    
    elif string[0] in vowels:   # The conditions check if the first letter is a vowel or not
        return recursive_vowel(string[1:])  # first letter skipped, and do the same for other letters. 
    
    return string[0] + recursive_vowel(string[1:]) # first letter returned and do the same to other elements




print (recursive_vowel("Adhitama Budi"))


"""
PSEUDOCODE:

RECURSIVE_VOWEL(STRING)

    if STRING = empty string
        RETURN STRING

    elif STRING[0] in VOWELS				      //base case

        RETURN RECURSIVE_VOWEL(STRING[1:])
		
// first letter skipped and do the same to other string

    return STRING[0] + 

// first letter is skipped and do the same to other string

"""
