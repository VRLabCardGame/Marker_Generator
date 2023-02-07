import os

import PIL
from PIL import Image

path_to_playground_marker = "C:\\Users\\Jonas\\Documents\\Studium\\Master\\01_VRLab\\Karten\\Generated_Cards" \
                            "\\Spielfeld\\spielfeld_complete_full_asym.png "

images = []
pos = 0

a4im = None

for x in range(0, 8):
    img = Image.open(path_to_playground_marker)
    print(img.size)
    position = None
    a4im = Image.new('RGB',
                     (int(595 * 1.31), int(842 * 1.31)),  # A4 at 72dpi
                     (255, 255, 255))  # White
    if x > 3:
        start = -img.size[1]/2
    else:
        start = 0

    if pos == 0:
        position = (0 + int(start), 0)
    elif pos == 1:
        position = (int(-img.size[1] / 4 + int(start)), 0)
    elif pos == 2:
        position = (int(-img.size[1] / 4 + int(start)), int(-img.size[0] / 2))
    else:
        position = (0 + int(start), int(-img.size[0] / 2))

    img = img.rotate(90, expand=True, fillcolor=(255, 255, 255))
    a4im.paste(img, position)
    images.append(a4im)
    a4im = None
    print(pos)
    pos += 1
    pos = pos % 4

if a4im is not None:
    images.append(a4im)

images[0].save("../Generated_Cards/playground_print.pdf", format="PDF", save_all=True, append_images=images[1:], resolution=100)
