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
