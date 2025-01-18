# In this project, a Python script was made to simulate the experience of time travel using modules.

## Importing necessary modules:

import datetime as dt # For handling dates and times.
from decimal import Decimal # For precise calculations.
from random import randint, choice # For generating random numbers.
import custom_module as time_travelers_toolkit # For generating time travel messages.


## Getting today's date:

# Retrieving the current date and time in a readable format:
date = dt.date.today().strftime('%B %d, %Y')
time = dt.datetime.now().time().strftime('%I:%M %p.')

print(f"Current date and time: {date} at {time}")


## Calculating the time travel cost:

# Setting a base cost as Decimal object:
base_cost = Decimal('1350.00')

# Getting the current year:
current_year = dt.date.today().year
# Genererating a random year ranging between the current year and 2047:
target_year = randint(current_year, 2047)
# Calculating the cost multiplier based on the difference between the current year and the target year:
cost_multiplier = abs(current_year - target_year)
# Calculating the travel cost:
travel_cost = base_cost * cost_multiplier

# Formatting the cost to two decimal places:
formatted_cost = f"{travel_cost:.2f}"


## Randomly selecting a destination for time travel:

# List of destinations:
destinations = ["Pyramid of Giza", "Pyramid of Khafre", "Pyramid of the Sun", "Pyramid of the Moon"]

destination = choice(destinations)


## Generating and printing the time travel message:

time_travelers_toolkit.generate_time_travel_message(target_year=target_year, destination=destination, cost=formatted_cost)


# (MODULES)
