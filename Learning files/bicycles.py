bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print (bicycles)
print (bicycles[0])
print (bicycles[0].title())

#to access the last element in the list use index -1 
print(bicycles[-1])

#to use individual values from the list
message = "My first bike was a " + bicycles[0].title() + "."
print (message)


freinds = ['Sherill', 'Venisha', 'Ann', 'Jami', 'Christina']
print ("Hey " + freinds[0].title() + "!")
print ("Hey " + freinds[1].title() + "!")
print ("Hey " + freinds[2].title() + "!")
print ("Hey " + freinds[3].title() + "!")
print ("Hey " + freinds[4].title() + "!")

motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)

#to add something to the end of the list use append
motorcycles.append('ducati')
print(motorcycles)

#to add manually to an empty list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)


#inserting into a list use position and item
motorcycles.insert(0, 'ducati') #inserts ducati to position 0 in the list
print(motorcycles)

freinds.insert(3, 'Janice')
print(freinds)

#deleting items from a list use the del command. Can be done by position.
motorcycles = ['honda', 'yamaha', 'suzuki']

del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

#removing items from a list using the pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print (motorcycles)
print (popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print("the last motorcyle I owned was a " + last_owned.title() + ".")

#can also be done by position
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop(0)
print("the last motorcyle I owned was a " + last_owned.title() + ".")

#remove by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print (motorcycles)

motorcycles.remove('ducati')
print (motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print (motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print ("\nA " + too_expensive.title() + " is too expensive for me.")

guest_list= ['Venisha', 'Sherill', 'Janice']
print("Hey " + guest_list[0] + " would you like to come to dinner?")
print("Hey " + guest_list[1] + " would you like to come to dinner?")
print("Hey " + guest_list[2] + " would you like to come to dinner?")
print("Oh no! " + guest_list[2] + " cant make it! Who to invite?")
no_go = guest_list.pop(2)
guest_list.append('Christina')
print("Hey " + guest_list[0] + " would you like to come to dinner?")
print("Hey " + guest_list[1] + " would you like to come to dinner?")
print("Hey " + guest_list[2] + " would you like to come to dinner?")
print("Hey everyone I found a bigger table!")
guest_list.insert(2, 'Liz')
guest_list.insert(3, 'Li')
guest_list.append('Sharon')
print("Hey " + guest_list[0] + " would you like to come to dinner?")
print("Hey " + guest_list[1] + " would you like to come to dinner?")
print("Hey " + guest_list[2] + " would you like to come to dinner?")
print("Hey " + guest_list[3] + " would you like to come to dinner?")
print("Hey " + guest_list[4] + " would you like to come to dinner?")
print("Hey " + guest_list[5] + " would you like to come to dinner?")

print("Now I can only have two people for dinner")
uninvited = guest_list.pop(5)
print("sorry " + uninvited + " I can only have two people over")
uninvited = guest_list.pop(4)
print("sorry " + uninvited + " I can only have two people over")
uninvited = guest_list.pop(3)
print("sorry " + uninvited + " I can only have two people over")
uninvited = guest_list.pop(2)
print("sorry " + uninvited + " I can only have two people over")
print("Hey " + guest_list[0] + " we're still on")
print("Hey " + guest_list[1] + " we're still on")
del guest_list[1]
del guest_list[0]
print(guest_list)
