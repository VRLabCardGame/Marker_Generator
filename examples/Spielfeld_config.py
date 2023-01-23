import os

import create_pattern

create_pattern.draw_pattern(marker_style=1,
                            red_scale=1,
                            green_scale=1,
                            blue_scale=1,
                            brightness_scale=0.85,
                            shape_number=1500,
                            shape_size=1/25,
                            marker_id=100000,
                            create_just_pattern=True,
                            marker_width=2048,
                            save_marker=True,
                            visualize_marker=False,
                            output_path="C:\\Users\\Jonas\\Documents\\Studium\\Master\\01_VRLab\\Karten"
                                        "\\Generated_Cards\\Spielfeld\\",
                            image_path="Spielfeld",
                            marker_name="Spielfeld",
                            marker_height=1536,
                            rgb_range=[230, 230])
