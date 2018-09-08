import random

secretWordBank = ["blue", "yellow", "orange", "red", "purple", "white", "black", "green"]

secureRandom = random.SystemRandom()

pickedColor = secureRandom.choice(secretWordBank)
print(pickedColor)