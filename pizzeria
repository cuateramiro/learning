# Keeping track of Al Capone's pizzeria stock.

# Setting things up:

toppings = ["Sicilian", "Neapolitan", "New York", "Detroit", "California", "Greek", "Pepperoni", "Sausage", "Hawaiian", "Cheese"]

prices = [2, 6, 1, 3, 2, 7, 2, 3, 4, 6]

# Research on $2 pizza slices
num_two_dollar_slices = prices.count(2)

# How many different kinds we offer?
num_pizzas = len(toppings)

print("We sell",num_pizzas,"different kinds of pizza!")

# Orchestrating in a 2D list
pizza_and_prices = [[2, "Sicilian"], [6, "Neapolitan"], [1, "New York"], [3, "Detroit"], [2, "California"], [7, "Greek"], [2, "Pepperoni"], [3, "Sausage"], [4, "Hawaiian"], [6, "Cheese"]]


# Sorting and slicing pizzas
pizza_and_prices.sort()


cheapest_pizza = pizza_and_prices[0]


# A man bought our last most expensive slice of pizza

priciest_pizza = pizza_and_prices[-1]



# Removing the last slice sold from our list
pizza_and_prices.pop()

# Adding a new type of pizza according to the price sorted data

pizza_and_prices.insert(4, [2.5, "Peppers"])

# Three customers walk into the store; they don't have enough money, so they ask for the three cheapest pizzas.

three_cheapest = pizza_and_prices[:3]

print(three_cheapest)
