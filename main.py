import os

import create_pattern


images = os.listdir("../Modelle")
print(images)

for i in range(len(images)):
    print(i)
    create_pattern.draw_pattern(red_scale=1,
                                green_scale=0.1,
                                blue_scale=0,
                                brightness_scale=10,
                                shape_number=500,
                                shape_size=1/15,
                                marker_id=i,
                                create_just_pattern=False,
                                marker_width=800,
                                save_marker=True,
                                visualize_marker=False,
                                folder_path="C:\\Users\\Jonas\\Documents\\Studium\\Master\\01_VRLab\\Karten"
                                            "\\Generated_Cards\\",
                                image_path="..\\Modelle\\" + images[i],
                                use_image=True)
