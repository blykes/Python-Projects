###9-1 Resturants
##class Restaurant():
##    """A class representing a restaurant."""
##
##    def __init__(self, name, cuisine_type):
##        """Initialize the restaurant."""
##        self.name = name.title()
##        self.cuisine_type = cuisine_type
##
##    def describe_restaurant(self):
##        """Display a summary of the restaurant."""
##        msg = self.name + " serves wonderful " + self.cuisine_type + "."
##        print("\n" + msg)
##
##    def open_restaurant(self):
##        """Display a message that the restaurant is open."""
##        msg = self.name + " is open. Come on in!"
##        print("\n" + msg)
##
##restaurant = Restaurant('the mean queen', 'pizza')
##print(restaurant.name)
##print(restaurant.cuisine_type)
##
##restaurant.describe_restaurant()
##restaurant.open_restaurant()
##
###9-2 Three resutrants
##class Restaurant():
##    """A class representing a restaurant."""
##
##    def __init__(self, name, cuisine_type):
##        """Initialize the restaurant."""
##        self.name = name.title()
##        self.cuisine_type = cuisine_type
##
##    def describe_restaurant(self):
##        """Display a summary of the restaurant."""
##        msg = self.name + " serves wonderful " + self.cuisine_type + "."
##        print("\n" + msg)
##
##    def open_restaurant(self):
##        """Display a message that the restaurant is open."""
##        msg = self.name + " is open. Come on in!"
##        print("\n" + msg)
##
##mean_queen = Restaurant('the mean queen', 'pizza')
##mean_queen.describe_restaurant()
##
##ludvigs = Restaurant("ludvig's bistro", 'seafood')
##ludvigs.describe_restaurant()
##
##mango_thai = Restaurant('mango thai', 'thai food')
##mango_thai.describe_restaurant()
##
###9-3 Users
##class User():
##    """Represent a simple user profile."""
##
##    def __init__(self, first_name, last_name, username, email, location):
##        """Initialize the user."""
##        self.first_name = first_name.title()
##        self.last_name = last_name.title()
##        self.username = username
##        self.email = email
##        self.location = location.title()
##
##    def describe_user(self):
##        """Display a summary of the user's information."""
##        print("\n" + self.first_name + " " + self.last_name)
##        print("  Username: " + self.username)
##        print("  Email: " + self.email)
##        print("  Location: " + self.location)
##
##    def greet_user(self):
##        """Display a personalized greeting to the user."""
##        print("\nWelcome back, " + self.username + "!")
##
##eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
##eric.describe_user()
##eric.greet_user()
##
##willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
##willie.describe_user()
##willie.greet_user()
##
###9-4 Number Served
##class Restaurant():
##    """A class representing a restaurant."""
##
##    def __init__(self, name, cuisine_type):
##        """Initialize the restaurant."""
##        self.name = name.title()
##        self.cuisine_type = cuisine_type
##        self.number_served = 0
##
##    def describe_restaurant(self):
##        """Display a summary of the restaurant."""
##        msg = self.name + " serves wonderful " + self.cuisine_type + "."
##        print("\n" + msg)
##
##    def open_restaurant(self):
##        """Display a message that the restaurant is open."""
##        msg = self.name + " is open. Come on in!"
##        print("\n" + msg)
##
##    def set_number_served(self, number_served):
##        """Allow user to set the number of customers that have been served."""
##        self.number_served = number_served
##
##    def increment_number_served(self, additional_served):
##        """Allow user to increment the number of customers served."""
##        self.number_served += additional_served
##
##
##restaurant = Restaurant('the mean queen', 'pizza')
##restaurant.describe_restaurant()
##
##print("\nNumber served: " + str(restaurant.number_served))
##restaurant.number_served = 430
##print("Number served: " + str(restaurant.number_served))
##
##restaurant.set_number_served(1257)
##print("Number served: " + str(restaurant.number_served))
##
##restaurant.increment_number_served(239)
##print("Number served: " + str(restaurant.number_served))
##
###9-5 Login Attmepts
##class User():
##    """Represent a simple user profile."""
##
##    def __init__(self, first_name, last_name, username, email, location):
##        """Initialize the user."""
##        self.first_name = first_name.title()
##        self.last_name = last_name.title()
##        self.username = username
##        self.email = email
##        self.location = location.title()
##        self.login_attempts = 0
##
##    def describe_user(self):
##        """Display a summary of the user's information."""
##        print("\n" + self.first_name + " " + self.last_name)
##        print("  Username: " + self.username)
##        print("  Email: " + self.email)
##        print("  Location: " + self.location)
##
##    def greet_user(self):
##        """Display a personalized greeting to the user."""
##        print("\nWelcome back, " + self.username + "!")
##
##    def increment_login_attempts(self):
##        """Increment the value of login_attempts."""
##        self.login_attempts += 1
##
##    def reset_login_attempts(self):
##        """Reset login_attempts to 0."""
##        self.login_attempts = 0
##
##eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
##eric.describe_user()
##eric.greet_user()
##
##print("\nMaking 3 login attempts...")
##eric.increment_login_attempts()
##eric.increment_login_attempts()
##eric.increment_login_attempts()
##print("  Login attempts: " + str(eric.login_attempts))
##
##print("Resetting login attempts...")
##eric.reset_login_attempts()
##print("  Login attempts: " + str(eric.login_attempts))
##
###9-6 Ice cream stand
##class Restaurant():
##    """A class representing a restaurant."""
##
##    def __init__(self, name, cuisine_type):
##        """Initialize the restaurant."""
##        self.name = name.title()
##        self.cuisine_type = cuisine_type
##        self.number_served = 0
##
##    def describe_restaurant(self):
##        """Display a summary of the restaurant."""
##        msg = self.name + " serves wonderful " + self.cuisine_type + "."
##        print("\n" + msg)
##
##    def open_restaurant(self):
##        """Display a message that the restaurant is open."""
##        msg = self.name + " is open. Come on in!"
##        print("\n" + msg)
##
##    def set_number_served(self, number_served):
##        """Allow user to set the number of customers that have been served."""
##        self.number_served = number_served
##
##    def increment_number_served(self, additional_served):
##        """Allow user to increment the number of customers served."""
##        self.number_served += additional_served
##
##
##class IceCreamStand(Restaurant):
##    """Represent an ice cream stand."""
##
##    def __init__(self, name, cuisine_type='ice_cream'):
##        """Initialize an ice cream stand."""
##        super().__init__(name, cuisine_type)
##        self.flavors = []
##
##    def show_flavors(self):
##        """Display the flavors available."""
##        print("\nWe have the following flavors available:")
##        for flavor in self.flavors:
##            print("- " + flavor.title())
##
##
##big_one = IceCreamStand('The Big One')
##big_one.flavors = ['vanilla', 'chocolate', 'black cherry']
##
##big_one.describe_restaurant()
##big_one.show_flavors()
##
###9-7 Admin
##class User():
##    """Represent a simple user profile."""
##
##    def __init__(self, first_name, last_name, username, email, location):
##        """Initialize the user."""
##        self.first_name = first_name.title()
##        self.last_name = last_name.title()
##        self.username = username
##        self.email = email
##        self.location = location.title()
##        self.login_attempts = 0
##
##    def describe_user(self):
##        """Display a summary of the user's information."""
##        print("\n" + self.first_name + " " + self.last_name)
##        print("  Username: " + self.username)
##        print("  Email: " + self.email)
##        print("  Location: " + self.location)
##
##    def greet_user(self):
##        """Display a personalized greeting to the user."""
##        print("\nWelcome back, " + self.username + "!")
##
##    def increment_login_attempts(self):
##        """Increment the value of login_attempts."""
##        self.login_attempts += 1
##
##    def reset_login_attempts(self):
##        """Reset login_attempts to 0."""
##        self.login_attempts = 0
##
##
##class Admin(User):
##    """A user with administrative privileges."""
##
##    def __init__(self, first_name, last_name, username, email, location):
##        """Initialize the admin."""
##        super().__init__(first_name, last_name, username, email, location)
##        self.privileges = []
##
##    def show_privileges(self):
##        """Display the privileges this administrator has."""
##        print("\nPrivileges:")
##        for privilege in self.privileges:
##            print("- " + privilege)
##
##
##eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
##eric.describe_user()
##
##eric.privileges = [
##    'can reset passwords',
##    'can moderate discussions',
##    'can suspend accounts',
##    ]
##
##eric.show_privileges()
##
###9-8 Priviledges
##class User():
##    """Represent a simple user profile."""
##
##    def __init__(self, first_name, last_name, username, email, location):
##        """Initialize the user."""
##        self.first_name = first_name.title()
##        self.last_name = last_name.title()
##        self.username = username
##        self.email = email
##        self.location = location.title()
##        self.login_attempts = 0
##
##    def describe_user(self):
##        """Display a summary of the user's information."""
##        print("\n" + self.first_name + " " + self.last_name)
##        print("  Username: " + self.username)
##        print("  Email: " + self.email)
##        print("  Location: " + self.location)
##
##    def greet_user(self):
##        """Display a personalized greeting to the user."""
##        print("\nWelcome back, " + self.username + "!")
##
##    def increment_login_attempts(self):
##        """Increment the value of login_attempts."""
##        self.login_attempts += 1
##
##    def reset_login_attempts(self):
##        """Reset login_attempts to 0."""
##        self.login_attempts = 0
##
##
##class Admin(User):
##    """A user with administrative privileges."""
##
##    def __init__(self, first_name, last_name, username, email, location):
##        """Initialize the admin."""
##        super().__init__(first_name, last_name, username, email, location)
##
##        # Initialize an empty set of privileges.
##        self.privileges = Privileges()
##
##class Privileges():
##    """A class to store an admin's privileges."""
##
##    def __init__(self, privileges=[]):
##        self.privileges = privileges
##
##    def show_privileges(self):
##        print("\nPrivileges:")
##        if self.privileges:
##            for privilege in self.privileges:
##                print("- " + privilege)
##        else:
##            print("- This user has no privileges.")
##
##
##eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
##eric.describe_user()
##
##eric.privileges.show_privileges()
##
##print("\nAdding privileges...")
##eric_privileges = [
##    'can reset passwords',
##    'can moderate discussions',
##    'can suspend accounts',
##    ]
##eric.privileges.privileges = eric_privileges
##eric.privileges.show_privileges()
##
###9-9 Battery Upgrade
##class Car():
##    """A simple attempt to represent a car."""
##
##    def __init__(self, manufacturer, model, year):
##        """Initialize attributes to describe a car."""
##        self.manufacturer = manufacturer
##        self.model = model
##        self.year = year
##        self.odometer_reading = 0
##        
##    def get_descriptive_name(self):
##        """Return a neatly formatted descriptive name."""
##        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
##        return long_name.title()
##    
##    def read_odometer(self):
##        """Print a statement showing the car's mileage."""
##        print("This car has " + str(self.odometer_reading) + " miles on it.")
##        
##    def update_odometer(self, mileage):
##        """
##        Set the odometer reading to the given value.
##        Reject the change if it attempts to roll the odometer back.
##        """
##        if mileage >= self.odometer_reading:
##            self.odometer_reading = mileage
##        else:
##            print("You can't roll back an odometer!")
##    
##    def increment_odometer(self, miles):
##        """Add the given amount to the odometer reading."""
##        self.odometer_reading += miles
##
##class Battery():
##    """A simple attempt to model a battery for an electric car."""
##
##    def __init__(self, battery_size=60):
##        """Initialize the batteery's attributes."""
##        self.battery_size = battery_size
##
##    def describe_battery(self):
##        """Print a statement describing the battery size."""
##        print("This car has a " + str(self.battery_size) + "-kWh battery.")
##
##        
##    def get_range(self):
##        """Print a statement about the range this battery provides."""
##        if self.battery_size == 60:
##            range = 140
##        elif self.battery_size == 85:
##            range = 185
##            
##        message = "This car can go approximately " + str(range)
##        message += " miles on a full charge."
##        print(message)
##
##    def upgrade_battery(self):
##        """Upgrade the battery if possible."""
##        if self.battery_size == 60:
##            self.battery_size = 85
##            print("Upgraded the battery to 85 kWh.")
##        else:
##            print("The battery is already upgraded.")
##    
##        
##class ElectricCar(Car):
##    """Models aspects of a car, specific to electric vehicles."""
##
##    def __init__(self, manufacturer, model, year):
##        """
##        Initialize attributes of the parent class.
##        Then initialize attributes specific to an electric car.
##        """
##        super().__init__(manufacturer, model, year)
##        self.battery = Battery()
##
##
##print("Make an electric car, and check the battery:")
##my_tesla = ElectricCar('tesla', 'model s', 2016)
##my_tesla.battery.describe_battery()
##
##print("\nUpgrade the battery, and check it again:")
##my_tesla.battery.upgrade_battery()
##my_tesla.battery.describe_battery()
##
##print("\nTry upgrading the battery a second time.")
##my_tesla.battery.upgrade_battery()
##my_tesla.battery.describe_battery()

#9-10
from restaurant import Restaurant

channel_club = Restaurant('the channel club', 'steak and seafood')
channel_club.describe_restaurant()
channel_club.open_restaurant()

#9-11
##from user import Admin
##
##eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
##eric.describe_user()
##
##eric_privileges = [
##    'can reset passwords',
##    'can moderate discussions',
##    'can suspend accounts',
##    ]
##eric.privileges.privileges = eric_privileges
##
##print("\nThe admin " + eric.username + " has these privileges: ")
##eric.privileges.show_privileges()
##
#9-12
from admin import Admin

eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
eric.privileges.privileges = eric_privileges

print("\nThe admin " + eric.username + " has these privileges: ")
eric.privileges.show_privileges()

#9-13 OrderedDict Rewrite
