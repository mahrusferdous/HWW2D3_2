# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for genre in genres[1:4]:
    print(genre, "is a music genre")

    
new_genres = [genre + " Music" for genre in genres]
print(new_genres)


for i in reversed(range(1, 11)):
    print(i)
print("The beat drops now!")