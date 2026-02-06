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
    count = len(st) # len counts how many things there are  in a string . googled this 
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


""" service = input("How was the service you recieved today? awful, mediocre, satisfactory, or excellent?")
bill = float(input("Cost of your meal today?:"))
if service == "awful":
    tipv = 0.0 * bill
elif service == "mediocre": 
     tipv = .15 * bill
elif service == "satisfactory":
     tipv =.20 * bill 
elif service == "excellent":
    tipv = .25 * bill 
totb = tipv + bill

def tipcalculator():
     print("Suggested tip is shown first, total bill with that tip second .")
     print(tipv)
     print(totb)
tipcalculator() """

# make a FUNCTION to state all factors of a number

""" listofactor = []
num = int(input("State an integer:"))
def fff():
    for i in range(1, num + 1): 
        remainder = num % i # dividing number by factor, in this case, i 
        if remainder == 0:
            listofactor.append(i) # EVERY ITERATION OF i THAT THIS IS TRUE FOR WILL BE RECORDED IN listofactor. append inputs things in  a list. gooogled how to do this i did not know 
    print("The factors of that integer are..")
    print(listofactor)
fff()
 """
# find the gcf of two numbers via a function 


fac1 = []
fac2 = []
num1 = int(input("State an integer"))
num2 = int(input("State another integer. It can be the same integer:"))
def gcf():
    for i in range(1, num1 + 1): 
        remainder = num1 % i # dividing number by factor, in this case, i 
        if remainder == 0:
            fac1.append(i)
    for i in range(1, num2 + 1): 
         remainder = num2 % i # dividing number by factor, in this case, i 
    if remainder == 0:
            fac2.append(i)
    cf = list ((fac1) & (fac2)) # googled this, the two lists are converted into sets, the & records common items in the set, and then makes a list out of them.  
    print ("The GCF of these two numbers is..")
    print(cf[-1]) # -1 indicates last. 
gcf() 



