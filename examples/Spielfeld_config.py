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
                            marker_width=1600,
                            save_marker=True,
                            visualize_marker=False,
                            output_path="..\\..\\Generated_Cards\\Spielfeld\\",
                            marker_name="Spielfeld",
                            rgb_range=[230, 230])
