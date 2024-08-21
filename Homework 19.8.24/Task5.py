import random

rand_list = [random.randint(100,500) for i in range (50)]
rand_set= set(rand_list)
# The assignment requested us to initially create a list, this is why I perform the above instead the below:
#rand_set ={random.randint(100,500) for i in range (50)}
print(rand_list)
print(rand_set)
