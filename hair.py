# Alice wants to be able to market her low prices. We want to find out what the average price of a cut is.

# Setting things up:

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]


total_price = 0

for price in prices:
  total_price += price

# print(len(prices))

average_price = total_price / 8

print("Average Haircut Price:", average_price)

# That average price is more expensive than Alice thought it would be! She wants to cut all prices by 5 dollars.

new_prices = [cut - 5 for cut in prices]
print("New Prices:", new_prices)


# She wants to know how much revenue was brought in last week.

total_revenue = 0

# for elemental in range(len(hairstyles)) would also be valid.

for elemental in range(0, 8):
 total_revenue += prices[elemental] * last_week[elemental]
  
print("Total Revenue:", total_revenue)

average_daily_revenue = total_revenue / 7
print("Average Daily Revenue:", average_daily_revenue)


# Alice thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.


cuts_under_30 = [hairstyles[elementary] for elementary in range(len(new_prices)) if new_prices[elementary] < 30]

# 'elementary' was used to access corresponding elements in both new_prices and hairstyles

print(cuts_under_30)

