# This project involves setting up a business system that manages multiple franchises.
# It defines businesses, their franchise locations, and available menus.
# Customers can check which menus are available at a given time and calculate their total bill.

# <---- Making the Menu ---->
# The 'Menu' class represents a menu with available items and their respective times.
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name  # Stores the name of the menu.
    self.items = items  # Stores a dictionary of menu items and their prices.
    self.start_time = start_time  # Defines the menu's starting time.
    self.end_time = end_time  # Defines the menu's ending time.

  def __repr__(self):
    # Returns a string representation of the menu with availability times.
    return "{name} menu available from {start_time} to {end_time}.".format(name=self.name, start_time=self.start_time, end_time=self.end_time)
  
  def calculate_bill(self, purchased_items):
    # Calculates the total bill for a list of purchased items.
    total_price = 0
    for item in purchased_items:
      if item in self.items:
        total_price += self.items[item]
    return total_price

# <-- Creating the Businesses -->
# The 'Business' class represents a business with multiple franchises.
class Business:
  def __init__(self, name, franchises):
    self.name = name  # Stores the name of the business.
    self.franchises = franchises  # Stores a list of franchise locations.

# <-- Creating the Franchises -->
# The 'Franchise' class represents a single franchise location of a business.
class Franchise:
  def __init__(self, address, menus):
    self.address = address  # Stores the franchise address.
    self.menus = menus  # Stores a list of available menus.
  
  def __repr__(self):
    # Returns a string representation of the franchise location.
    return "Franchise located at {address}.".format(address=self.address)
  
  def available_menus(self, time):
    # Determines which menus are available based on the provided time.
    return [menu for menu in self.menus if menu.start_time <= time < menu.end_time]


# <-- Defining Menu Items -->
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch = Menu("Brunch", brunch_items, 1100, 1600)

early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
early_bird = Menu("Early Bird", early_bird_items, 1500, 1800)

# <-- Defining additional menus -->
dinner_items = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
dinner = Menu("Dinner", dinner_items, 1700, 2300)

kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids = Menu("Kids", kids_items, 1100, 2100)

# <-- Displaying the menu information -->
print(brunch)
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

# <-- Defining the Franchises -->
# List of all available menus.
menus = [brunch, early_bird, dinner, kids]

# Defining franchise locations.
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

# <-- Displaying franchise information -->
print(flagship_store)
print(flagship_store.available_menus(1700))

# <-- Creating the Business -->
# Creating a business with multiple franchises.
basta_fazoolin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# <-- Creating a new specialized business -->
arepas_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas_menu = Menu("Take a’ Arepa", arepas_items, 1000, 2000)
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])
take_arepa = Business("Take a' Arepa", [arepas_place])

# Displaying menu start time.
print(arepas_menu.start_time)

# Tip: There is no need to rewrite code that's already been written.
# (CLASSES2)
