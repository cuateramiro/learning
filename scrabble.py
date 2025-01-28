# In this project, we will process data from a group of Scrabble players, using dictionaries to organize players, words, and points.


## Dictionary: 

# Lists of letters and their corresponding point values.
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Adding lowercase letters to the list.
letters += [letter.lower() for letter in letters]
# Duplicating points for lowercase letters
points += points

# Mapping each letter to its point value.
letter_to_points = {key:value for key, value in zip(letters, points)}
# A blank tile with value of 0 points.
letter_to_points[" "] = 0

# Letter to points dictionary.
print(letter_to_points)

## Word Score:

# Function to calculate the score of a word:
def score_word(word):
  point_total = 0
# Adding up points for each letter in the word.  
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

# Testing how many points "BROWNIE" gets:
brownie_points = score_word("BROWNIE")
print(brownie_points)

## Scoring the Game:

# Dictionary mapping players to the list of words they've played:
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

# Empty dictionary to keep track of player points.
player_to_points = {}

# Function to update each player's total points:
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words: #player_to_words.values(): Mistake I'd like to remember.
      player_points += score_word(word)
    player_to_points[player] = player_points

update_point_totals()

## Extras:

# Function to let a player play a new word.
def play_word(player, word):
# Checking if the player exists in the records:
  if player in player_to_words:
    player_to_words[player].append(word)
# Error handling.
  else:
    print(f"Player {player} not found.")

# Let's have player1 play the word "ALEJANDRO"
play_word("player1", "ALEJANDRO")

print(player_to_words) # Printing the updated list of words played by each player.
print(player_to_points)  # Printing the current standings.


# (DICTIONARIES)
