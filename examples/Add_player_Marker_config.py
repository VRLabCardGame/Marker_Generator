import os

import create_pattern

path_to_image = "../../Modelle/Zauber/Spieler.png"
create_pattern.draw_pattern(marker_style=2,
                            red_scale=0.1,
                            green_scale=1,
                            blue_scale=0.15,
                            brightness_scale=8,
                            shape_number=2500,
                            shape_size=1/10,
                            marker_id=1000000,
                            create_just_pattern=False,
                            marker_width=800,
                            save_marker=True,
                            visualize_marker=False,
                            output_path="C:\\Users\\Jonas\\Documents\\Studium\\Master\\01_VRLab\\Karten"
                                        "\\Generated_Cards\\Zauber\\",
                            image_path=path_to_image,
                            marker_name="Spieler")
