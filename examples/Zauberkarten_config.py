import os

import create_pattern

path_to_images = "..\\..\\Modelle\\Zauber\\"

images = os.listdir(path_to_images)
print(images)

texts = ["Blitz\n+2 ATK",
         "Feuer\n+2 ATK",
         "Natur\n+2 ATK",
         "Wasser\n+2 ATK",
         "Blitz\n+2 DEF,\nnutze DEF",
         "Feuer\n+2 DEF,\nnutze DEF",
         "Natur\n+2 DEF,\nnutze DEF",
         "Wasser\n+2 DEF,\nnutze DEF",
         "-1 Leben für\ngegnerischen\nSpieler",
         "Ziehe\n2 Karten",
         "Element-\nreihenfolge\ntauschen",
         "ATK und DEF\ntauschen"
         ]

for i in range(len(images)):
    print(i)
    create_pattern.draw_pattern(marker_style=0,
                                red_scale=0.2,
                                green_scale=0.1,
                                blue_scale=1,
                                brightness_scale=10,
                                shape_number=500,
                                shape_size=1/15,
                                marker_id=i,
                                create_just_pattern=False,
                                marker_width=1600,
                                save_marker=True,
                                visualize_marker=False,
                                output_path="..\\..\\Generated_Cards\\Zauber\\",
                                image_path=path_to_images + images[i],
                                marker_name="Zauber",
                                rgb_range=[0, 0],
                                bg_color="#dddddd",
                                text=texts[i])
