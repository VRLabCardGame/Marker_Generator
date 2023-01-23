import os

import create_pattern

path_to_image = "../../Modelle/Zauber/Draw_2.png"
create_pattern.draw_pattern(marker_style=0,
                            red_scale=0.2,
                            green_scale=0.1,
                            blue_scale=1,
                            brightness_scale=10,
                            shape_number=500,
                            shape_size=1/15,
                            marker_id=5,
                            create_just_pattern=False,
                            marker_width=800,
                            save_marker=True,
                            visualize_marker=False,
                            output_path="C:\\Users\\Jonas\\Documents\\Studium\\Master\\01_VRLab\\Karten"
                                        "\\Generated_Cards\\Zauber\\",
                            image_path=path_to_image,
                            marker_name="Zauber")
