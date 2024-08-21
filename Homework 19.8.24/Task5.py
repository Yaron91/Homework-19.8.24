import random

rand_list = [random.randint(100,500) for i in range (50)]
rand_set= set(rand_list)

print(rand_list)
print(rand_set)