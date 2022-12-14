import os

import create_pattern

path_to_images = "../../Modelle/Monster\\"

images = os.listdir(path_to_images)
print(images)

for i in range(len(images)):
    print(i)
    create_pattern.draw_pattern(marker_style=0,
                                red_scale=1,
                                green_scale=0.1,
                                blue_scale=0,
                                brightness_scale=10,
                                shape_number=500,
                                shape_size=1/15,
                                marker_id=i+100,
                                create_just_pattern=False,
                                marker_width=800,
                                save_marker=True,
                                visualize_marker=False,
                                folder_path="C:\\Users\\Jonas\\Documents\\Studium\\Master\\01_VRLab\\Karten"
                                            "\\Generated_Cards\\Monster\\",
                                image_path=path_to_images + images[i],
                                use_image=True,
                                marker_name="Monster",
                                use_stat_fields=True)
