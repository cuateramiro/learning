# A company needs help parsing the following poem strings into something that can be displayed by name, title, and publication date on its website.

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(",")
# Splitting the poems at the commas.

# print(highlighted_poems_list)

highlighted_poems_stripped = []

for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip()) 
# Cleaning up inconsistent whitespace.

# print(highlighted_poems_stripped)

highlighted_poems_details = []

for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(":"))
# Iterating through the list and splitting around the colon characters.
# Separating each poem into its own list details.

print(highlighted_poems_details)

titles = []
poets = []
dates = []

for lst in highlighted_poems_details:
    titles.append(lst[0])
    poets.append(lst[1])
    dates.append(lst[2])

# Separating titles, poets, and dates into separate lists.
# Iterating through the 2D list and appending each piece of each poem into its respective category.


for i in range(len(highlighted_poems_details)):
  print("The poem {} was published by {} in {}.".format(titles[i], poets[i], dates[i]))
# Printing a custom statement for each poem.

# (STRINGS)
