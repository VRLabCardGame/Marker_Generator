from PIL import Image, ImageDraw


def create_death_zone_p1(width):
    top_left = (width * 0.05, width * 0.05)
    bottom_right = (width * 0.25, width * 0.25)
    return top_left, bottom_right


def create_draw_zone_p1(width):
    top_left = (width * 0.75, width * 0.05)
    bottom_right = (width * 0.95, width * 0.25)
    return top_left, bottom_right


def create_spell_zone_p1(width):
    top_left = (width * 0.4, width * 0.15)
    bottom_right = (width * 0.6, width * 0.35)
    return top_left, bottom_right


def create_monster_zone1_p1(width):
    top_left = (width * 0.65, width * 0.3)
    bottom_right = (width * 0.85, width * 0.5)
    return top_left, bottom_right


def create_monster_zone2_p1(width):
    top_left = (width * 0.15, width * 0.3)
    bottom_right = (width * 0.35, width * 0.5)
    return top_left, bottom_right


def create_fight_zone_p1(width):
    top_left = (width * 0.1, width * 0.625)
    bottom_right = (width * 0.45, width * 0.85)
    return top_left, bottom_right


def create_fight_zone_p2(width):
    top_left = (width * 0.55, width * 0.625)
    bottom_right = (width * 0.9, width * 0.85)
    return top_left, bottom_right


def create_field_separator(width):
    top_left = (width * -0.5, width * 0.575)
    bottom_right = (width * 0.505, width * 0.85)
    return top_left, bottom_right


def create_layout(background_img_path,
                  background_width,
                  background_height,
                  bg_color="#222222"):
    bg = bg_color

    result_image = Image.new('RGB', (background_width, background_height), bg)
    draw = ImageDraw.Draw(result_image)

    for x in range(0, 2):
        top_left, bottom_right = create_death_zone_p1(background_width)
        ImageDraw.ImageDraw.rectangle(draw, xy=[top_left, bottom_right], fill="#222222", outline="#444444", width=7)

        top_left, bottom_right = create_draw_zone_p1(background_width)
        ImageDraw.ImageDraw.rectangle(draw, xy=[top_left, bottom_right], fill="#cccccc", outline="#444444", width=7)

        top_left, bottom_right = create_spell_zone_p1(background_width)
        ImageDraw.ImageDraw.rectangle(draw, xy=[top_left, bottom_right], fill="#FF4B4B", outline="#444444", width=7)

        top_left, bottom_right = create_monster_zone1_p1(background_width)
        ImageDraw.ImageDraw.rectangle(draw, xy=[top_left, bottom_right], fill="#767171", outline="#444444", width=7)

        top_left, bottom_right = create_monster_zone2_p1(background_width)
        ImageDraw.ImageDraw.rectangle(draw, xy=[top_left, bottom_right], fill="#767171", outline="#444444", width=7)

        top_left, bottom_right = create_fight_zone_p1(background_width)
        ImageDraw.ImageDraw.rectangle(draw, xy=[top_left, bottom_right], fill="#C00000", outline="#444444", width=7)
        top_left, bottom_right = create_fight_zone_p2(background_width)
        ImageDraw.ImageDraw.rectangle(draw, xy=[top_left, bottom_right], fill="#C00000", outline="#444444", width=7)
        top_left, bottom_right = create_field_separator(background_width)
        ImageDraw.ImageDraw.rectangle(draw, xy=[top_left, bottom_right], outline="#CF4444", width=25)

        marker_file_name = "Spielfeld_complete"
        result_image.save("..\\..\\Generated_Cards\\Spielfeld\\" + marker_file_name + str(x) + ".png")

    result_image_full = Image.new('RGB', (background_width, background_height * 2), bg)

    image_to_place = Image.open("..\\..\\Generated_Cards\\Spielfeld\\" + marker_file_name + "0.png")
    image_resized = image_to_place.resize(size=(int(background_width), int(background_height)), resample=0)
    image_position = 0, 0
    result_image_full.paste(image_resized, image_position)

    image_position_2 = 0, background_height
    image_to_place = Image.open("..\\..\\Generated_Cards\\Spielfeld\\" + marker_file_name + "1.png")
    image_resized = image_to_place.resize(size=(int(background_width), int(background_height)), resample=0)
    image_rotated = image_resized.rotate(angle=180.0)
    result_image_full.paste(image_rotated, image_position_2)

    image_to_place = Image.open(background_img_path)
    image_resized = image_to_place.resize(size=(int(result_image_full.width / 6), int(result_image_full.height / 6)), resample=0)
    image_position = int(background_width / 2 - background_width / 6 / 2), int(
        background_height - background_height / 6)
    result_image_full.paste(image_resized, image_position)

    result_image_full.save("..\\..\\Generated_Cards\\Spielfeld\\" + marker_file_name + "_full_asym.png")


def main():
    create_layout("..\\..\\Generated_Cards\\Spielfeld"
                  "\\Spielfeld_v2100000.png", 2048, 1536, bg_color="#eeeeee")


main()
