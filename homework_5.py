genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for genre in genres:
    print(genre, "is a music genre")
    
count = 0;
while True:
    print(genres[count])
    count += 1
    if (count == 4):
        break
    
    
value = input("Out of the list remove any that doesn't fit the light show: ")
genres.remove(value)    
for i in range(len(genres)):
    print(genres[i], "genre track ", i+1)