# Setting up

weight = 4.8

# Ground Shipping:
# Yes, you can use a variable multiple times. 

if weight <= 2:
  ground_cost = weight * 1.50 + 20
elif weight <= 6:
  ground_cost = weight * 3.00 + 20
elif weight <= 10:
  ground_cost = weight * 4.00 + 20
else:
  ground_cost = weight * 4.74 + 20

print("Ground Shipping Cost:", ground_cost)

# Ground Shipping Premium:

ground_premium_cost = 125

print("Ground Shipping Premium Cost:", ground_premium_cost)

# Drone Shipping:

if weight <= 2:
  drone_cost = weight * 4.50
elif weight <= 6:
  drone_cost = weight * 9
elif weight <= 10:
  drone_cost = weight * 12
else:
  drone_cost = weight * 14.25

print("Drone Shipping Cost:", round(drone_cost,2))
