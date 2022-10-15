import random

length = int(input("length: "))
order = int(input("asc/desc(0/1): "))

random_list = [random.randint(0, 100) for i in range(length)]

print("before: ", random_list)

for i in range(1, length):
  for j in range(0, length - i):
    if order == 1:
        if random_list[j] < random_list[j + 1]:
            random_list[j], random_list[j + 1] = random_list[j + 1], random_list[j]
    else:
        if random_list[j] > random_list[j + 1]:
            random_list[j], random_list[j + 1] = random_list[j + 1], random_list[j]

print("after: ", random_list)