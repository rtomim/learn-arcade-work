import arcade
arcade.open_window(800, 800, 'Mr. Peluse\'s Adventures')
arcade.set_background_color(arcade.csscolor.DARK_SEA_GREEN)
arcade.start_render()
arcade.draw_circle_filled(600.0, 700.0, 50.0, (255, 255, 49),)
arcade.draw_lrtb_rectangle_filled(0, 800, 500, 0, (93, 138, 168))
arcade.draw_rectangle_filled(550, 500, 60, 16, (90, 70, 50))
arcade.draw_rectangle_outline(550, 500, 60, 16, (60, 60, 50), 3)
arcade.draw_line(550, 510, 550, 545, (150, 113, 23), 2)
arcade.draw_triangle_filled(550, 545, 550, 535, 560, 540, (179, 27, 27))
arcade.draw_arc_filled(270, 500, 65, 105, (120, 134, 107), 0, 180,)
arcade.draw_polygon_filled(((90, 670,),
                            (112, 689),
                            (128, 674),
                            (147, 695),
                            (180, 674),
                            (206, 670),
                            (180, 668),
                            (150, 630),
                            (128, 650),
                            (114, 632)), (240, 248, 255))
# I don't know why the following command doesn't work
arcade.draw_text("The adventure awaits...", 200, 100, arcade.color.BLACK, 14)
arcade.finish_render()
arcade.run()
