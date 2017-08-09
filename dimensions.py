dimensions = (200, 50)
#print(dimensions[0])
#print(dimensions[1])

#dimensions[0] = 250

for dimension in dimensions:
    print(dimension)

print("Original: ")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified ")
for dimension in dimensions:
    print(dimension)

buffet = ('chicken', 'wings', 'burgers', 'dogs')
for food in buffet:
    print ("this is the old menu" + food)

#buffet[0] = 'buffalo'

buffet = ('beef', 'wings', 'burgers', 'dogs')
for food in buffet:
    print("This is the first change "+ food)

buffet = ('beef', 'fries', 'burgers', 'dogs')
for food in buffet:
    print("this is the second change " + food)
