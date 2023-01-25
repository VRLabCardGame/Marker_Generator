import os

import create_pattern

path_to_images = "../../Modelle/Monster\\"

images = os.listdir(path_to_images)
print(images)

elemente = ["Blitz.png",
            "Blitz.png",
            "Blitz.png",
            "Blitz.png",
            "Wasser.png",
            "Wasser.png",
            "Feuer.png",
            "Feuer.png",
            "Natur.png",
            "Natur.png",
            "Natur.png",
            "Natur.png",
            "Wasser.png",
            "Wasser.png"]

monster_stats = [
    [2, 2],  # bird1
    [2, 1],  # bird2
    [3, 1],  # dog1
    [3, 0],  # dog2
    [1, 3],  # fish1
    [2, 2],  # fish2
    [4, 1],  # fox1
    [2, 2],  # fox2
    [3, 2],  # monkey1
    [1, 4],  # monkey2
    [3, 0],  # snake1
    [2, 1],  # snake2
    [0, 4],  # turtle1
    [1, 2]  # turtle2
]

for i in range(len(images)):
    print(i)
    create_pattern.draw_pattern(marker_style=0,
                                red_scale=1,
                                green_scale=0.1,
                                blue_scale=0.1,
                                brightness_scale=10,
                                shape_number=500,
                                shape_size=1 / 15,
                                marker_id=i + 100,
                                create_just_pattern=False,
                                marker_width=1600,
                                save_marker=True,
                                visualize_marker=False,
                                output_path="C:\\Users\\Jonas\\Documents\\Studium\\Master\\01_VRLab\\Karten"
                                            "\\Generated_Cards\\Monster\\",
                                image_path=path_to_images + images[i],
                                marker_name="Monster",
                                stats=monster_stats[i],
                                use_extra_symbols=True,
                                extra_symbols=["C:\\Users\\Jonas\\Documents\\Studium\\Master\\01_VRLab\\Karten"
                                               "\\Modelle\\Objekte\\Schwert.png",
                                               "C:\\Users\\Jonas\\Documents\\Studium\\Master\\01_VRLab\\Karten"
                                               "\\Modelle\\Objekte\\Schild.png"],
                                element="C:\\Users\\Jonas\\Documents\\Studium\\Master\\01_VRLab\\Karten"
                                        "\\Modelle\\Elemente\\" + elemente[i],
                                rgb_range=[255, 255],
                                bg_color="#222222")
