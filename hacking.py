# This project involves accessing the attacker’s system, retrieving compromised usernames from a file, notifying the boss, and obfuscating the file by scrambling the information with a signature.

## Module Imports:
# The program uses the 'csv' module for handling CSV files, 'json' for creating structured data, and 'os' for file operations.
import csv
import json
import os

## Retrieving Compromised Usernames:
# The program initializes an empty list called 'compromised_users' to store usernames.
compromised_users = []

# It then checks if a file named 'passwords.csv' exists. If so, it reads through it using 'csv.DictReader', which treats each row as a dictionary.
if os.path.exists('passwords.csv'):
  with open('passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)
    # The program collects all usernames found under the 'Username' column and adds them to the list.
    for row in password_csv:
      compromised_users.append(row['Username'])

## Saving Compromised Usernames:
# The program saves the list of compromised usernames to a text file named 'compromised_users.txt'. Each username is placed on a separate line.
with open('compromised_users.txt', 'w') as compromised_user_file:
  for compromised_user in compromised_users:
    compromised_user_file.write(compromised_user + "\n")

## Notifying the Boss:
# A JSON file named 'boss_message.json' is created to notify the boss.
with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
  json.dump(boss_message_dict, boss_message)

## Scrambling Passwords with a Signature:
# Finally, a new file called 'new_passwords.csv' is generated, replacing passwords with ASCII art.
with open('new_passwords.csv', 'w') as new_passwords_obj:
  null_sig = """  _  _     ___   __  ____            
/ )( \   / __) /  \(_  _)           
) \/ (  ( (_ \(  O ) )(             
\____/   \___/ \__/ (__)            
 _  _   __    ___  __ _  ____  ____ 
/ )( \ / _\  / __)(  / )(  __)(    \
) __ (/    \\( (__  )  (  ) _)  ) D (
\_)(_\/_/\_/ \___)(__\_)(____)(____/ 
"""
  new_passwords_obj.write(null_sig)


# (FILES)
