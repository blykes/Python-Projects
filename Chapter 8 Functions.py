#8-1 Message
def display_message():
    """displays a message"""
    print("Welcome!")

display_message()

#8-2 Favorite Book
def favorite_book(title):
    print("My favorite book is " + title.title())

favorite_book('brave new world')

#8-3 T-Shirt
def make_shirt(shirt_size, shirt_print):
    print("My sirt size is " + shirt_size + ".")
    print("The shirt should say " + shirt_print + ".")

make_shirt('M', 'WELCOME HOME VEN!')
make_shirt(shirt_size='M', shirt_print='I MISSED YOU!')

#8-4 Large Shirts
def make_shirt(shirt_size='large', shirt_print='I love Python'):
    print("My sirt size is " + shirt_size + ".")
    print("The shirt should say " + shirt_print + ".")

#make_shirt('M', 'WELCOME HOME VEN!')
make_shirt()
make_shirt(shirt_size='Medium')
make_shirt(shirt_size='Small')
make_shirt(shirt_size='XS', shirt_print='Word')

#8-5 Cities
def describe_city(city, country='France'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('Paris')
describe_city('reykjavik', 'iceland')
describe_city('Cannes')

#8-6 City names
def city_country(city, country):
    """return a city and a coutry"""
    return (city.title() + ", " + country.title())

city = city_country('Paris', 'France')
print(city)

city = city_country('London', 'England')
print(city)

city = city_country('Berlin', 'Germany')
print(city)

#8-7
def make_album(artist, title):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict

album = make_album('metallica', 'master of pupptes')
print(album)
album = make_album('social distortion', 'white heat, white light, white trash')
print(album)
album = make_album('halestorm', 'the strange case of')
print(album)

#8-7b
def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

album = make_album('metallica', 'master of pupptes')
print(album)
album = make_album('social distortion', 'white heat, white light, white trash')
print(album)
album = make_album('halestorm', 'the strange case of')
print(album)
album = make_album('megadeth', 'rust in peace', tracks = 8)
print(album)

#8-8 User Albums
def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

#prepare prompts
title_prompt = "\nWhat album are you listening to? "
artist_prompt = "\nWho is it by? "

#escape clause
print("Enter quit at any time to stop. ")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break

    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for playing!")
