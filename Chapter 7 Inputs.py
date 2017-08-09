#7-1 Car rental
##print("what kind of car do you want to drive?")
##car = input("Please tell me the car: ")
##print(car)

#7-2 Resturant
##party = input("how many people are in your party this evening? ")
##party = int(party)
##if party <= 8:
##    print("Please follow me")
##else:
##    print("You will have to wait")  

#7-3 Multiples of ten
##number = input(" please enter a number to see if it is a multiple of 10 ")
##number = int(number)
##if number % 10 == 0:
##    print("\nthe number " + str(number) + " is a multiple of 10.")
##else:
##    print("\nThe number " + str(number) + " is not a multiple of 10")

#7-4 Pizza toppings
##active = True
##prompt = "\nWhat do you want on your pizza?"
##prompt+= "\nEnter quit to end "
##while active:
##    message = input(prompt)
##
##    if message == 'quit':
##        active = False
##
##    else:
##        print(message)

#7-5 Movie tickets
prompt = "\nPlease enter your age "
prompt += "\nEnter quit to end "

while True:
    age = input(prompt)

    if age == 'quit':
        break
    age = int(age)
    
    if age < 3:
        print("free")
    elif age >= 3 and age <= 12:
        print("$10")
    elif age > 12:
        print("$15")


