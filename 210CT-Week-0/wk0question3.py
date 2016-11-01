user_input = input("Please enter a value for x: ")
user_input_float = float(user_input)

equation_One = (user_input_float**2) + (4 * user_input_float) + 4
equation_Two = 0
equation_Three = (user_input_float ** 2) + (user_input_float * 5)

if user_input_float < -2:
    print(equation_One)

elif user_input_float == 0:
    print (equation_Two)

elif user_input_float > -2:
    print (equation_Three)

else:
    None
