# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 179, 37
temp = a
res = 0
while temp >= 0:
    temp -= b
    res += 1
else:
    # subtracting from res the last addition as temp becomes negative
    # (done for efficiency - not checking if temp became negative for every iteration of the loop)
    res -= 1
print("Целочисленное деление", a, "на", b, "дает", res)



