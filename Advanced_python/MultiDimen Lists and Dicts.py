Movies={'Godfather':'Al pacino',
        'Fight club':'Edward Norton',
        'Inception':'Di Caprio'}
print(Movies)

# for Loop to print each key in the dictionary.
for Movie in Movies:
    print(Movie)

# For loop to print key and value in dictionary
for key,value in Movies.items():
    print(key,value)

# To add more values to each key in dictionary use lists
Movies2={'Godfather':['Al pacino','James Caan'],
        'Fight club':['Edward Norton','Brad Pitt'],
        'Inception':['Di Caprio','Ellen Page']}

#Print the values assigned to a specific key
my_movies=Movies2['Godfather']
print(my_movies)

# print the data related to the values in specifc key
print(type(my_movies))

# print specific value from list related to specific key
print(my_movies[1])
print(my_movies[0])
# alternative
my_movies=Movies2["Godfather"][1]
print(my_movies)

# return movies that have "Al pacino"
actor_to_find="Al pacino"
for movie,actors in Movies2.items():
    # Note:actors is a list,to search the list it need to
    # be looped to search each item.
    for actor in actors:
        if actor==actor_to_find:
            print(movie)


Movies3={'Godfather':{'year':1972,'actors':
                ['Al pacino','James Caan']},
        'Fight club':{'year':1999,'actors':
            ['Edward Norton','Brad Pitt']},
        'Inception':{'year':2010,'actors':['Di Caprio','Ellen Page']}}

# The code below would,return the specific keys (movie names)
# in the dictionary and all the values related.

for movie,data in Movies3.items():
    print(movie)
    print(data)

#print the specific key and access specific data in
#inner dictionary and print.

    #print(data["year"])
    print(movie,data["year"])

#accessing and printing the actors

print(movie,data["actors"])

#alternative

my_movie2= Movies3["Godfather"]
print (my_movie2)
print(my_movie2["actors"])

print(actors[0])
# This is a 3 dimensional data type
print(Movies3["Godfather"]["actors"][0])


# Code to find movies in specific year using for loop
year_to_find=1999
for movie,data in Movies3.items():
    if data["year"]==year_to_find:
        print(movie)

# Code to find movies based on specific year and actor within this data structure
actor_to_find="Brad pitt"
for movie,data in Movies3.items():
    for actor in data['actors']:
        if actor== actor_to_find:
            print(movie)


Movies4={'Godfather':[1972, ['Al pacino','James Caan']],
        'Fight club':[1999,['Edward Norton','Brad Pitt']],
        'Inception':[2010,['Di Caprio','Ellen Page']]}

my_movie3=Movies4["Godfather"]
year=my_movie3[0]
actors=my_movie3[1]
print(year)
print(actors)

print(Movies4["Fight club"][1][0])

# loop for accessing specific data structure in Movies4
# prints the specific keys and dates
for movie, data in Movies4.items():
    print(movie,data[0])
    print(data[1])

actor_to_find="James Caan"
for movie, data in Movies4.items():
    for actor in data[1]:
        if actor==actor_to_find:
            print(movie)
