import math

from PIL import Image, ImageDraw, ImageTk
from random import randint, randrange, seed, sample
import tkinter as tk


def image_placeholder(width):
    top_left = (width * 0.125, width * 0.125)
    bottom_right = ((width * 0.75) + (width * 0.125), (width * 0.75) + (width * 0.125))
    return top_left, bottom_right


def fit_image(width, image_path):
    image_to_place = Image.open(image_path)
    image_resized = image_to_place.resize(size=(int(width*0.75), int(width*0.75)), resample=0)
    image_position = int(width*0.125), int(width*0.125)
    return image_resized, image_position


def stats_placeholder(width):
    top_left = (width * 0.175, width * 1)
    bottom_right = ((width * 0.65) + (width * 0.175), (width * 1.4))
    return top_left, bottom_right


def stats_field_1(width):
    side = 5
    points = [
        (
            (math.sin(th + 120) + width * 0.0045) * (width*0.095),
            (math.cos(th + 120) + width * 0.01575) * (width*0.095)
        )
        for th in [i * (2 * math.pi) / side for i in range(side)]
    ]
    return points


def stats_field_2(width):
    side = 5
    points = [
        (
            (math.sin(th + 120) + width * 0.0085) * (width*0.095),
            (math.cos(th + 120) + width * 0.01575) * (width*0.095)
        )
        for th in [i * (2 * math.pi) / side for i in range(side)]
    ]
    return points


def color_chooser(rgb_range=[0, 255], red_scale=1, green_scale=1, blue_scale=1, brightness_scale=1):
    return (int(randint(rgb_range[0], rgb_range[1]) * red_scale * brightness_scale),
            int(randint(rgb_range[0], rgb_range[1]) * green_scale * brightness_scale),
            int(randint(rgb_range[0], rgb_range[1]) * blue_scale * brightness_scale))


def rand_triangle(width, height, shape_size=1 / 4):
    width = int(width * 1.25)
    height = int(height * 1.25)
    x1, y1 = randrange(-50, width) * shape_size, randrange(-50, height) * shape_size
    x2, y2 = randrange(-50, width) * shape_size, randrange(-50, height) * shape_size
    x3, y3 = randrange(-50, width) * shape_size, randrange(-50, height) * shape_size

    widths = [x1, x2, x3]
    heights = [y1, y2, y3]
    offset_width = randint(-50, width) / 1.2
    offset_height = randint(-50, height) / 1.2

    for width_idx in range(0, len(widths)):
        widths[width_idx] += offset_width
    for height_idx in range(0, len(heights)):
        heights[height_idx] += offset_height

    return [(widths[0], heights[0]), (widths[1], heights[1]), (widths[2], heights[2])]


def rand_rect_or_ellipse(width, height, shape_size=1 / 4):
    width = width * 1.25
    height = height * 1.25
    x1, y1 = randrange(-50, width) * shape_size, randrange(-50, height) * shape_size
    x2, y2 = randrange(-50, width) * shape_size, randrange(-50, height) * shape_size

    widths = [x1, x2]
    heights = [y1, y2]
    offset_width = randint(-50, width) / 1.2
    offset_height = randint(-50, height) / 1.2

    for width_idx in range(0, len(widths)):
        widths[width_idx] += offset_width
    for height_idx in range(0, len(heights)):
        heights[height_idx] += offset_height

    return [(widths[0], heights[0]), (widths[1], heights[1])]


def draw_pattern(marker_style=0,
                 red_scale=1,
                 green_scale=1,
                 blue_scale=1,
                 brightness_scale=1,
                 shape_number=1000,
                 shape_size=1 / 4,
                 bg_color="#222222",
                 marker_id=1,
                 create_just_pattern=False,
                 marker_width=800,
                 save_marker=True,
                 visualize_marker=True,
                 folder_path="C:\\Users\\Jonas\\Documents\\Studium\\Master\\01_VRLab\\Karten\\",
                 image_path="",
                 use_image=False):
    shape_factories = [(rand_triangle, ImageDraw.ImageDraw.polygon),
                       (rand_rect_or_ellipse, ImageDraw.ImageDraw.rectangle),
                       (rand_rect_or_ellipse, ImageDraw.ImageDraw.ellipse)]

    bg = bg_color
    marker_height = int(marker_width * 1.56)
    result_image = Image.new('RGB', (marker_width, marker_height), bg)
    draw = ImageDraw.Draw(result_image)
    seed(marker_id)
    seeds = sample(range(0, 100000), shape_number)
    for i in range(shape_number):
        seed(seeds[i])
        drawn_shape, draw_method = shape_factories[marker_style]
        draw_method(draw,
                    drawn_shape(width=marker_width, height=marker_height, shape_size=shape_size),
                    fill=color_chooser(red_scale=red_scale, green_scale=green_scale, blue_scale=blue_scale,
                                       brightness_scale=brightness_scale),
                    outline=color_chooser(red_scale=red_scale, green_scale=green_scale, blue_scale=blue_scale,
                                          brightness_scale=brightness_scale))
    if not create_just_pattern:
        if use_image:
            fitting_image, image_offset = fit_image(marker_width, image_path)
            result_image.paste(fitting_image, image_offset)
        else:
            top_left, bottom_right = image_placeholder(marker_width)
            ImageDraw.ImageDraw.rectangle(draw, xy=[top_left, bottom_right], fill="#cccccc", outline="#444444", width=2)

        top_left, bottom_right = stats_placeholder(marker_width)
        ImageDraw.ImageDraw.rectangle(draw, xy=[top_left, bottom_right], fill="#333333", outline="#111111", width=15)
        points = stats_field_1(marker_width)
        ImageDraw.ImageDraw.polygon(draw, xy=points, fill="#cccccc", outline="#444444", width=5)
        points = stats_field_2(marker_width)
        ImageDraw.ImageDraw.polygon(draw, xy=points, fill="#cccccc", outline="#444444", width=5)

    if save_marker:
        marker_file_name = "marker" + str(marker_id)
        result_image.save(folder_path + marker_file_name + ".png")
    if visualize_marker:
        root = tk.Tk()
        tk_image = ImageTk.PhotoImage(result_image)
        tk.Label(image=tk_image).pack()
        root.mainloop()
