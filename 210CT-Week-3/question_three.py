""" This is the solution for coursework question 8. The question ask us to remove the vowels in a word. The method
    used for this solution is by using recursive function. The function will be defined as recursive_vowel with
    string as its parameter. further explaination will be explained through comments on the code """

vowels = ["A", "I", "U", "E", "O", "a", "i", "u", "e", "o"] # List of vowels consisting both lower and upper letter

def recursive_vowel(string):    # function is defined with recursive_vowel as its name and "string" as the parameter

    if string == "":            # The condition check if string input is an empty string or not
        return string           # If it is an empty list, the string will then be returned
    
    elif string[0] in vowels:   # The conditions check if the first letter is a vowel or not
        return recursive_vowel(string[1:])
    
    return string[0] + recursive_vowel(string[1:])




print (recursive_vowel("Adhitama Budi"))
