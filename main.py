import visualization
import action_with_fractal


def main():
    root = visualization.my_root()
    frame_left = visualization.FrameLeft(root)
    canvas = visualization.my_canvas(root)
    frame_right = visualization.FrameRight(root)
    frame_right.gallery_header()
    gallery = frame_right.real_gallery()
    frame_left.main_header()
    frame_left.color_header()
    entry_red, entry_green, entry_blue = frame_left.color_entry()
    frame_left.resolution_header()
    entry_width, entry_height = frame_left.resolution_entry()  
    frame_left.coordinates_header()
    entry_xmin, entry_xmax = frame_left.coordinates_entry_x()
    entry_ymin, entry_ymax = frame_left.coordinates_entry_y()
    frame_left.number_of_iterations_header()
    entry_number = frame_left.number_of_iterations_entry()


    frame_left.buttons(lambda: action_with_fractal.draw_fractal(entry_red, entry_green, entry_blue,
                                                                entry_width, entry_height, entry_xmin,
                                                                entry_xmax, entry_ymin, entry_ymax,
                                                                entry_number, canvas, gallery), action_with_fractal.save_fractal)
    frame_right.clear_button(lambda: action_with_fractal.clear_gallery(gallery))

    root.mainloop()


if __name__ == "__main__":
    main()