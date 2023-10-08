import random

# method 1
random_int_1 = int(round(random.random(), 0))
print(random_int_1, end=" ")
if random_int_1 == 0:
    print("Tails")
else:
    print("Heads")

# method 2
random_int_2 = random.randint(0, 10)
print(random_int_2, end=" ")
if random_int_2 <= 5:
    print("Tails")
else:
    print("Heads")
