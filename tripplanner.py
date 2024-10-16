# Bob is planning a trip from Houston, Texas, to New York City on his car, and we offered to help by creating a customized app just for him.

# Welcoming Bob:

def trip_planner_welcome(name):
  print("Welcome to tripplanner v2.0 " + name)

trip_planner_welcome("Bob")

# We are going to be using user-defined and pre-built functions to round the hours it would take him to get there.

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(26.7)

# Creating a function that will take the arguments to complete the app's purpose.

def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")

destination_setup("Texas", "New York", estimate)

# By now, Bob must be eating pizza somewhere in time square.

# (FUNCTIONS)
