counter_1 = 0
counter_2 = 0

while id(counter_1) == id(counter_2):
    print(counter_1)
    counter_2 += 1
    counter_1 += 1
