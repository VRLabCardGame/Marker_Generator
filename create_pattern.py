import math

from PIL import Image, ImageDraw, ImageTk, ImageFont
from random import randint, randrange, seed, sample
import tkinter as tk


def image_placeholder(width):
    top_left = (width * 0.125 - 5, width * 0.125 - 5)
    bottom_right = ((width * 0.75) + (width * 0.125) + 5, (width * 0.75) + (width * 0.125) + 5)
    return top_left, bottom_right


def fit_image(width, image_path):
    image_to_place = Image.open(image_path)
    image_resized = image_to_place.resize(size=(int(width*0.75), int(width*0.75)), resample=0)
    image_position = int(width*0.125), int(width*0.125)
    return image_resized, image_position


def stats_placeholder(width):
    top_left = (int(width * 0.175), int(width * 1))
    bottom_right = (int(width * 0.65) + int(width * 0.175), int(width * 1.4))
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


def color_chooser(rgb_range=None, red_scale=1, green_scale=1, blue_scale=1, brightness_scale=1):
    if rgb_range is None:
        rgb_range = [0, 255]

    brightness_factor = (rgb_range[1] - rgb_range[0])/255

    if brightness_factor * brightness_scale < 1:
        brightness_factor = 1

    return (
        int(randint(rgb_range[0], rgb_range[1]) * red_scale * (brightness_scale * brightness_factor)),
        int(randint(rgb_range[0], rgb_range[1]) * green_scale * (brightness_scale * brightness_factor)),
        int(randint(rgb_range[0], rgb_range[1]) * blue_scale * (brightness_scale * brightness_factor))
        )


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
    width = int(width * 1.25)
    height = int(height * 1.25)
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


def draw_extra_symbol(size, x_pos, symbol_path, y_pos=None):
    image_to_place = Image.open(symbol_path)
    image_resized = image_to_place.resize(size=(int(size), int(size)), resample=0)
    if y_pos:
        image_position = int(x_pos), int(y_pos)
    else:
        image_position = int(x_pos), int(x_pos)
    return image_resized, image_position


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
                 use_image=False,
                 marker_name="marker",
                 stats=None,
                 marker_height=None,
                 rgb_range=None,
                 use_extra_symbols=False,
                 extra_symbols=None,
                 element=None):
    if extra_symbols is None:
        extra_symbols = [
            "C:\\Users\\Jonas\\Documents\\Studium\\Master\\01_VRLab\\Karten\\Modelle\\Objekte\\Schwert.png",
            "C:\\Users\\Jonas\\Documents\\Studium\\Master\\01_VRLab\\Karten\\Modelle\\Objekte\\Schild.png", ]
    # sets default rgb_range
    if rgb_range is None:
        rgb_range = [0, 255]
    # sets possible shapes (accessible by variable marker style -> possible values: 0,1,2)
    shape_factories = [(rand_triangle, ImageDraw.ImageDraw.polygon),
                       (rand_rect_or_ellipse, ImageDraw.ImageDraw.rectangle),
                       (rand_rect_or_ellipse, ImageDraw.ImageDraw.ellipse)]

    bg = bg_color
    # defines standard marker height if it's not specified
    if marker_height is None:
        marker_height = int(marker_width * 1.56)
    result_image = Image.new('RGB', (marker_width, marker_height), bg)
    draw = ImageDraw.Draw(result_image)
    # sets seed for reconstructable marker creation
    seed(marker_id)
    # gets a seed for each shape to draw based on the previously set seed
    seeds = sample(range(0, 100000), shape_number)
    for i in range(shape_number):
        seed(seeds[i])
        drawn_shape, draw_method = shape_factories[marker_style]
        draw_method(draw,
                    drawn_shape(width=marker_width,
                                height=marker_height,
                                shape_size=shape_size),
                    fill=color_chooser(rgb_range=rgb_range,
                                       red_scale=red_scale,
                                       green_scale=green_scale,
                                       blue_scale=blue_scale,
                                       brightness_scale=brightness_scale),
                    outline=color_chooser(rgb_range=rgb_range,
                                          red_scale=red_scale,
                                          green_scale=green_scale,
                                          blue_scale=blue_scale,
                                          brightness_scale=brightness_scale)
                    )
    # draws placeholder and images onto the marker if specified
    if not create_just_pattern:
        # draws placeholder
        top_left, bottom_right = image_placeholder(marker_width)
        ImageDraw.ImageDraw.rectangle(draw, xy=[top_left, bottom_right], fill="#cccccc", outline="#444444", width=10)
        if use_image:
            # draw image
            fitting_image, image_offset = fit_image(marker_width, image_path)
            result_image.paste(fitting_image, image_offset)

        # draws placeholder for the stat fields
        top_left, bottom_right = stats_placeholder(marker_width)
        ImageDraw.ImageDraw.rectangle(draw, xy=[top_left, bottom_right], fill="#333333", outline="#111111", width=15)

        if element is not None:

            def crop_center(pil_img, crop_width, crop_height):
                img_width, img_height = pil_img.size
                return pil_img.crop(((img_width - crop_width) // 2,
                                     (img_height - crop_height) // 2,
                                     (img_width + crop_width) // 2,
                                     (img_height + crop_height) // 2))

            element_symbol_fitting, element_symbol_offset = draw_extra_symbol(size=marker_width*20,
                                                                              x_pos=top_left[0],
                                                                              symbol_path=element,
                                                                              y_pos=top_left[1])
            element_symbol_fitting = crop_center(element_symbol_fitting,
                                                 bottom_right[0]-top_left[0],
                                                 bottom_right[1]-top_left[1])
            A = element_symbol_fitting.getchannel('A')

            # Make all opaque pixels into semi-opaque
            newA = A.point(lambda i: 48 if i > 0 else 0)

            # Put new alpha channel back into original image and save
            element_symbol_fitting.putalpha(newA)
            result_image.paste(element_symbol_fitting, element_symbol_offset, mask=element_symbol_fitting)

            element_symbol_fitting, element_symbol_offset = draw_extra_symbol(size=marker_width*1,
                                                                              x_pos=top_left[0],
                                                                              symbol_path=element,
                                                                              y_pos=top_left[1])
            element_symbol_fitting = crop_center(element_symbol_fitting,
                                                 bottom_right[0]-top_left[0],
                                                 bottom_right[1]-top_left[1])
            A = element_symbol_fitting.getchannel('A')

            # Make all opaque pixels into semi-opaque
            newA = A.point(lambda i: 64 if i > 0 else 0)

            # Put new alpha channel back into original image and save
            element_symbol_fitting.putalpha(newA)
            result_image.paste(element_symbol_fitting, element_symbol_offset, mask=element_symbol_fitting)

            element_symbol_fitting, element_symbol_offset = draw_extra_symbol(size=marker_width*0.4,
                                                                              x_pos=top_left[0],
                                                                              symbol_path=element,
                                                                              y_pos=top_left[1])
            element_symbol_fitting = crop_center(element_symbol_fitting,
                                                 bottom_right[0]-top_left[0],
                                                 bottom_right[1]-top_left[1])
            result_image.paste(element_symbol_fitting, element_symbol_offset, mask=element_symbol_fitting)

        if use_extra_symbols:
            atk_symbol_fitting, atk_symbol_offset = draw_extra_symbol(size=marker_width*0.45,
                                                                      x_pos=marker_width*0.12,
                                                                      symbol_path=extra_symbols[0],
                                                                      y_pos=marker_width*0.98)
            result_image.paste(atk_symbol_fitting, atk_symbol_offset, mask=atk_symbol_fitting)
            def_symbol_fitting, def_symbol_offset = draw_extra_symbol(size=marker_width*0.45,
                                                                      x_pos=marker_width*0.42,
                                                                      symbol_path=extra_symbols[1],
                                                                      y_pos=marker_width*0.965)
            result_image.paste(def_symbol_fitting, def_symbol_offset, mask=def_symbol_fitting)
        if stats is not None:
            font = ImageFont.truetype("arial.ttf", int(marker_width/6))
            points = stats_field_1(marker_width)
            ImageDraw.ImageDraw.polygon(draw, xy=points, fill="#cccccc", outline="#444444", width=5)
            ImageDraw.ImageDraw.text(draw, (marker_width//3.35, marker_width//0.9), str(stats[0]), (50, 50, 50), font=font)
            points = stats_field_2(marker_width)
            ImageDraw.ImageDraw.polygon(draw, xy=points, fill="#cccccc", outline="#444444", width=5)
            draw.text((marker_width//1.67, marker_width//0.9), str(stats[1]), (50, 50, 50), font=font)

    if save_marker:
        marker_file_name = marker_name + str(marker_id)
        result_image.save(folder_path + marker_file_name + ".png")
    if visualize_marker:
        root = tk.Tk()
        tk_image = ImageTk.PhotoImage(result_image)
        tk.Label(image=tk_image).pack()
        root.mainloop()
