import os

import PIL
from PIL import Image

path_to_monster_markers = "..\\Generated_Cards\\Monster\\"
path_to_spell_markers = "..\\Generated_Cards\\Zauber\\"

images = []
pos = 0

a4im = None

folders = [path_to_monster_markers, path_to_spell_markers]

for i in range(0, 1):
    for x in range(0, len(folders)):
        for image in os.listdir(folders[x]):
            img = Image.open(folders[x] + image)
            print(img.size)
            position = None
            if pos == 0:
                a4im = Image.new('RGB',
                                 (int(595 * 6.5), int(842 * 6.5)),  # A4 at 72dpi
                                 (255, 255, 255))  # White
                position = (50, 50)
            elif pos == 1:
                position = (100 + img.size[0], 50)
            elif pos == 2:
                position = (50, 100 + img.size[1])
            elif pos == 3:
                position = (100 + img.size[0], 100 + img.size[1])

            a4im.paste(img, position)
            if pos == 3:
                images.append(a4im)
                a4im = None
            print(pos)
            pos += 1
            pos = pos % 4

    if a4im is not None:
        images.append(a4im)

images[0].save("..\\Generated_Cards\\print_v2.pdf", format="PDF", save_all=True, append_images=images[1:], resolution=100)
