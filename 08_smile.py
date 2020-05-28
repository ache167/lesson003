# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def draw_smiley(x, y, color):
    left_bottom_point = simple_draw.get_point(x - 50, y - 42)
    right_top_point = simple_draw.get_point(x + 50, y + 42)
    simple_draw.ellipse(left_bottom=left_bottom_point, right_top=right_top_point, color=color, width=2)
    left_eye_point = simple_draw.get_point(x - 17, y + 14)
    right_eye_point = simple_draw.get_point(x + 17, y + 14)
    eye_radius = 10
    simple_draw.circle(center_position=left_eye_point, color=color, radius=eye_radius)
    simple_draw.circle(center_position=right_eye_point, color=color, radius=eye_radius)
    lip_left_top_point = simple_draw.get_point(x - 30, y - 15)
    lip_left_bottom_point = simple_draw.get_point(x - 11, y - 25)
    simple_draw.line(start_point=lip_left_top_point, end_point=lip_left_bottom_point, color=color)
    lip_right_top_point = simple_draw.get_point(x + 30, y - 15)
    lip_right_bottom_point = simple_draw.get_point(x + 11, y - 25)
    simple_draw.line(start_point=lip_right_top_point, end_point=lip_right_bottom_point, color=color)
    simple_draw.line(start_point=lip_left_bottom_point, end_point=lip_right_bottom_point, color=color)


screen_resolution = simple_draw.resolution
screen_border = 50

for i in range(10):
    random_x = simple_draw.randint(screen_border, screen_resolution[0] - screen_border)
    random_y = simple_draw.randint(screen_border, screen_resolution[1] - screen_border)
    draw_smiley(random_x, random_y, simple_draw.COLOR_DARK_RED)

simple_draw.pause()
