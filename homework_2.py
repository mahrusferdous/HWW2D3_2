import random
time_of_day = ['morning', 'afternoon', 'evening']
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
mood = ["Happy", "Sad", "Energetic", "Calm"]

for day in days:
    for time in time_of_day:
        print(day, time, "you were", random.choice(mood))