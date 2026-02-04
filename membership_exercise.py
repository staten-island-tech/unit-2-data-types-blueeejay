def discount(isMember, age, isResident):
    if (isMember == True or isResident == True) or (age <12 or age > 65) :
        print("Discount applicable")
    else :
       print("No Discount")

discount(False, False, 2)