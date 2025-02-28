# This project involves creating a student management system using classes, where students are assigned grades, and grades are calculated.
# The system allows for adding grades, checking their status, and maintaining a record of students.

# The 'Student' class is defined to represent a student with attributes like 'name', 'year', and 'grades'.
class Student:
  def __init__(self, name, year):
    # Initializes the student's name and year, and sets up an empty list for grades.
    self.name = name
    self.year = year
    self.grades = []

# The 'add_grade' method allows the addition of grades to the student's list.
# It checks if the grade is a 'Grade' class before adding it.
  def add_grade(self, grade):
    # Checks that the grade is an instance of the 'Grade' class.
    if type(grade) is Grade:
      # If valid, appends the grade to the student's grades list.
      self.grades.append(grade)

# Three instances of the 'Student' class are instantiated.
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

# The 'Grade' class is defined with a class variable 'minimum_passing' that holds the passing score threshold.
class Grade:
  minimum_passing = 65
  
  # The method 'is_passing' checks if the grade score meets or exceeds the passing threshold.
  def is_passing(self):
    return self.score >= 65

# The 'Grade' class constructor initializes the 'score' attribute for each grade.
  def __init__(self, score):
    self.score = score

# An instance of 'Grade' with a score of 100 is added to Pieter's grades list.
pieter.add_grade(Grade(100))

# This will print whether each grade in Pieter’s grades list is passing.
# The 'is_passing' method is called for each grade to determine if it's passing.
for grade in pieter.grades:
    print(grade.is_passing())

# (CLASSES1)
