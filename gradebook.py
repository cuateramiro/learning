# Storing information about a student progress.
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Setting things up: 

subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

# Orchestrating in a 2D list

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# Changes # You can also use append method to add a list.
gradebook.append(["computer science", 100])

gradebook.append(["visual arts", 93])

# Adjustment, adding extra five points.

gradebook[5][1] = 93 + 5

gradebook[2].remove(85)

gradebook[2].append("Pass")

# Final gradebook 

full_gradebook = [last_semester_gradebook] + [gradebook]
print(full_gradebook)




