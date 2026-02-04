# integers and floats: tip calculator
""" 
values = [1,2.23,5,7,2,30,15] """
""" print(values)
for i in values:
    print(i) """
""" 
print(values[0])
print(values[6]) """

""" x = "this is a thing"
y = x.split( )
z = y[0]
print(y)
print(z) """

#CHALLENGE 1: 
""" 
Using the "input" method in Python, 
ask a user to input a sentence. 
 develop a function that accepts a the user input 
 will tell you how many words are in that string.
 First write out your plan in Pseudo-code using comments.
 Then craft the function. """

# i will use the input method, and then take the inputted sentance, find a way
# define function
# in function: prompt user to write somethingS
# split sentance into words
# assign a value of 1 to each words
# find total value of sentance 
# print total value as wordcount


""" def wordcount():
    sentence = input(" Write a sentence: ") 
    st = sentence.split( )
    count = len(st)
    print(count)
wordcount() """
# booleans and control flow
""" day_of_week = input( " State the day of the Week:")
if day_of_week == "FriYAY":
    print("correct")
else:
    print("incorrect") """

""" x = "man"
print(f"hey {x}")
 """
""" 
temp = 75
if temp > 68:
    print("warm")
elif temp == 68:
    print("perfect!")
else:
    print("cold") """
# ans to q: it will print warm. 
# challenge 2: even calculator 

""" def even_or_odd():
    number = int(input("State any integer:"))
    remainder = number % 2
    if remainder == 0:
        print("Even")
    else:
        print("Odd")
even_or_odd()
 """

# for tip calc: take bill and service value, convert bill to intg 