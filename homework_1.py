import random
mood = ["Happy", "Sad", "Angry", "Excited", "Scared", "Bored", "Confused", "Anxious", "Nervous", "Calm"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for i in range(0, 7):
    print(days[i], "you were",random.choice(mood))
    
