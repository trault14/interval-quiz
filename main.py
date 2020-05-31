import random
from interval import Interval
from note import Note


print("Press enter to start the quiz")
while True:
    interval = Interval.random()
    note = Note.random()
    direction = random.choice(["up", "down"])
    input()
    print(str(interval) + " " + direction + " from " + str(note))
