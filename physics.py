# As a local university professor, I want to share some functions that will help students calculate some fundamental physical properties for the upcoming semester.

# We do the following:

# Variables of the first class:

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Students functions: 


# Fahrenheit converter:

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp 

f100_in_celsius = f_to_c(100)

print(f100_in_celsius)


# Celsius converter:

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)

print(c0_in_fahrenheit)


# Force calculator:

def get_force(mass, acceleration):
  force = mass * acceleration
  return force


# First class exercises:

# How do you get a train force?

train_force = get_force(train_mass,train_acceleration)

print("The GE train supplies", train_force, "Newtons of force.")


# How do you get energy?

def get_energy(mass, c=3*10**8):
  energy = mass * c**2
  return energy


# How do you get bomb energy?
bomb_energy = get_energy(bomb_mass)

print("A 1kg bomb supplies", bomb_energy, "Joules.")


# Getting the work of a train:

def get_work(mass, acceleration, distance):
  work = get_force(mass,acceleration) * distance
  return work

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does", train_work, "Joules of work over", train_distance, "meters.")


# (FUNCTIONS- RETURN)
