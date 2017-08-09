my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]



my_foods.append('cannoli')
friend_foods.append('biryani')


print("My favorite foods are: ")
print(my_foods)

print("\nMy favorite foods are: ")
print(friend_foods)

friends = ['Venisha', 'Sherill', 'Janice', 'Christina', 'Ashley', 'Jami', 'Stephanie', 'Amanda', 'Britney']
print("the first three items in the list are: " + str(friends[0:3]))
print("The middle of the list is: " + str(friends[3:6]))
print("The end of the list is: " + str(friends[-3:]))
print(friends[6:9])

pizza = ['sausage', 'pepperoni', 'olive']

friend_pizzas = pizza[:]
friend_pizzas.append('meatball')

print("My favorite pizzas are ")
for flavors in pizza:
	print(flavors)

print("\nMy friend's favirites are ")
for friend_flavors in friend_pizzas:
	print(friend_flavors)