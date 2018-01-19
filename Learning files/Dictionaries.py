###defineing a dictionary
##alien_0 = {'color': 'green', 'points': 5}
##print(alien_0['color'])
##print(alien_0['points'])
##print(alien_0)
##
###adding to a dictionary
##alien_0['x_position'] = 0
##alien_0['y_position'] = 25
##print(alien_0)
##
###Starting witn an empty dictionary
##alien_0 = {}
##
##alien_0['color']  = 'green'
##alien_0['points'] = 5
##print(alien_0)
##
###6-1 Person
##fav_person = {'first_name': 'Venisha', 'last_name':'Kumar', 'age':'22', 'city':'Brooklyn'}
##print(fav_person)
##print(fav_person['first_name'])
##print(fav_person['last_name'])
##print(fav_person['age'])
##print(fav_person['city'])
##
###6-2 Fav Number
##fav_number = {'ven':'14', 'Janice':'12', 'Jami': '10', 'brian': '22', 'sherill':'18'}
##print(fav_number['ven'])
##print(fav_number['Janice'])
##print(fav_number['Jami'])
##print(fav_number['brian'])
##print(fav_number['sherill'])
##
###6-3 Glossary
##words = {'if statement':'conditional', 'for': 'loop',
##         'while':'loop', 'switch':'conditional', 'bool':'true/false',
##         'variable': 'somethign that holds data', 'list':'something that holds varies items',
##         'while': 'another loop', 'int': 'a number', 'string': 'a word'}
##word = 'if statement'
##print("\n" + word.title() + ":" + words['if statement'])
##word = 'for'
##print("\n" + word.title() + ":" + words['for'])
##word = 'while'
##print("\n" + word.title() + ":" + words['while'])
##word = 'switch'
##print("\n" + word.title() + ":" + words['switch'])
##word = 'bool'
##print("\n" + word.title() + ":" + words['bool'])
##
###6-4 Glossary with for loop
##for word in words:
##    print("\n" + word.title() + ":" + words[word])
##
##
###6-5 Rivers
##rivers = {'Nile': 'Egypt', 'Tigres': 'Iraq', 'Missouri':'Iowa'}
##
##for key, value in rivers.items():
##    print("The " + key.title() + " runs through " + value.title())
##
##for river in rivers.keys():
##    print(river.title())
##
##for country in rivers.values():
##    print(country.title())
##
###6-6 Polling
##favorite_languages = {
##    'jen': 'python',
##    'sarah': 'c',
##    'edward': 'ruby',
##    'phil': 'python'
##    }
##friends = ['jen', 'sarah', 'edward', 'phil', 'venisha', 'sherill']
##for name in friends:
##    if name in favorite_languages.keys():
##        print(name.title() + ", Thank you!")
##    else:
##        print(name.title() + " needs to take the poll")

#6-7 People
##fav_people = [] 
##fav_person = {'first_name': 'Venisha', 'last_name':'Kumar',
##                        'age':22, 'city':'Brooklyn'}
##fav_people.append(fav_person)
##fav_person = {'first_name': 'Ann', 'last_name': 'Snuffer',
##                         'age':40, 'city': 'Columbus'}
##fav_people.append(fav_person)
##fav_person = {'first_name': 'Sherill', 'last_name':'Christian',
##                           'age':24, 'city': 'Manhattan'}
##fav_people.append(fav_person)
##
##for fav_person in fav_people:
##    name = fav_person['first_name'].title() + " " + fav_person['last_name'].title()
##    age = str(fav_person['age'])
##    city = fav_person['city'].title()
##
##    print(name + ", of " + city + ", is " + age + " years old.") 
##
#6-8 Pets
##pets = []
##pet = {'name': 'Beasley', 'type': 'cat', 'owner': 'Rebecca'}
##pets.append(pet)
##pet = {'name': 'Bugsley', 'type': 'cat', 'owner': 'Brian'}
##pets.append(pet)
##pet = {'name': 'Bubba', 'type': 'dog', 'owner': 'Sean'}
##pets.append(pet)
##pet = {'name': 'Klipper', 'type': 'bird', 'owner': 'Kellie'}
##pets.append(pet)
##pet = {'name': 'Corgi', 'type': 'dog', 'owner': 'Janice'}
##pets.append(pet)
##pet = {'name': 'Mac', 'type': 'cat', 'owner': 'Chris'}
##pets.append(pet)
##pet = {'name': 'Tommy', 'type': 'cat', 'owner': 'Christina'}
##pets.append(pet)

##for pet in pets:
##    print("\nHere's the following pet: " + pet['name'].title())
##    for key, value in pet.items():
##        print("\t" + key + ": " + str(value))
##        
#6-9 Fav Places
fav_places = {
    'Venisha': ['New York', 'Ohio'],
    'Rebecca': ['New York', 'San Diego'],
    'Ann': ['New Orleans', 'San Antonio'],
    }

for name, cities in fav_places.items():
    print(name.title() + ": ")
    for city in cities:
        print("\t"+city.title())

#6-10 Fav Numbers
#numbers = []
fav_number = {
    'ven':[14, 2],
    'Janice': [12, 24],
    'Jami': [10, 100],
    'brian': [22, 482297593],
    'sherill': [18,500, 5000000],
              }

for name, numbers in fav_number.items():
    print(name.title() + ": ")
    for number in numbers:
        print("\t" + str(number))

#6-11 Cities
cities  = {
     'New York': ['United States', '11 million', 'Gotham'],
     'London': ['England', '7 million', 'The Smoke'],
     'Paris': ['France', '7 million', 'City of Lights'],
     }

for name, facts in cities.items():
    print(name.title() + ": ")
    for fact in facts:
        print("\t" + fact.title())

