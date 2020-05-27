# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)


for i in range(7):
    start_point = sd.get_point(50 + (i*5), 50)
    end_point = sd.get_point(550 + (i*5), 550)
    sd.line(start_point=start_point, end_point=end_point, color=rainbow_colors[i], width=4)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
width = 20
for i in range(7):
    center_point = sd.get_point(430, -200)
    sd.circle(center_position=center_point, radius=500 + (i*width), color=rainbow_colors[i], width=width)

sd.pause()
