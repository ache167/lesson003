# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

x_left = 0
y_left = 0
x_right = 100
y_right = 50


for i in range(12):
    for j in range(7):
        if i % 2 == 1:
            x_left = -50
            x_right = 50
        else:
            x_left = 0
            x_right = 100
        point_left_bottom = simple_draw.get_point(x_left + (j*100), y_left)
        point_right_top = simple_draw.get_point(x_right + (j*100), y_right)
        simple_draw.rectangle(left_bottom=point_left_bottom, right_top=point_right_top, width=2)
    y_left += 50
    y_right += 50


simple_draw.pause()
