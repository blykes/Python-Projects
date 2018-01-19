for value in range (1,6):
	print (value)
	
numbers  = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares= []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)

print("These are squares")
squares = [value**2 for value in range(1,11)]
print(squares)

for value in range(1,21):
	print (value)
	
#for value in range(1,1000000):
	#print(value)
	
#pizza = list(range(1,1000001))
#print(pizza)
#print(min(pizza))
#print(max(pizza))
#print(sum(pizza))

odd=[]
for value in range(1,21,2):
	#new_nums = odd
	odd.append(value)
	print(value)

multiples = list(range(3,31,3))
for threes in multiples:
	print(threes)
print(multiples)


#list of cubes using list comprehension
print("these are cubes")
cubes = [value**3 for value in range(1,11)]
print(cubes)

