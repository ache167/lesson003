import random

import simple_draw as sd

sd.resolution = (1600, 1000)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(150, 100)
bubble_radius = 50
for _ in range(3):
    bubble_radius += 5
    sd.circle(center_position=point, radius=bubble_radius)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def draw_bubble(center_coordinate, radius):
    for _ in range(3):
        radius += 5
        sd.circle(center_position=center_coordinate, radius=radius, color=sd.random_color())


# Нарисовать 10 пузырьков в ряд
for x in range(100, 1001, 100):
    point = sd.get_point(x, 300)
    draw_bubble(center_coordinate=point, radius=bubble_radius)

# Нарисовать три ряда по 10 пузырьков
for x in range(280, 1281, 100):
    for y in range(400, 551, 50):
        point = sd.get_point(x, y)
        draw_bubble(center_coordinate=point, radius=bubble_radius)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(350):
    point = sd.random_point()
    random_radius = random.randint(40, 80)
    draw_bubble(center_coordinate=point, radius=random_radius)

sd.pause()
