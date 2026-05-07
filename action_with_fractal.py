"""Module for fractal action.

Module draws, save fractal and also can clean gallery with fractals.

Contains:
    draw_fractal() - the function which draws fractal
    save_fractal() - the function which saves fractal
    clear_gallery() - the function which clear gallery with fractals

Author: Viktoria Chelpykh
Date: 2026-05-06
"""


from tkinter import messagebox, filedialog

import check_correct_input
import fractal_new


FRACTAL = None


def draw_fractal(entry_red, entry_green, entry_blue,
                 entry_width, entry_height, entry_xmin, 
                 entry_xmax, entry_ymin, entry_ymax,
                 entry_number, canvas, gallery):
    """The function which draws fractal.
    
    The function check all inputs. If there are errors it show
    a message about it. If all inputs correct the function
    generate fractal, put it's image in canvas and add
    it's image at the table.

    Args:
        entry_red (ctk.CTkEntry): The field for entry red color (0-255)
        entry_green (ctk.CTkEntry): The field for entry green color (0-255)
        entry_blue (ctk.CTkEntry): The field for entry blue color (0-255)
        entry_width (ctk.CTkEntry): The field for entry width
        entry_height (ctk.CTkEntry): The field for entry height
        entry_xmin (ctk.CTkEntry): The field for entry minimum x coordinate of the fractal region
        entry_xmax (ctk.CTkEntry): The field for entry maximum x coordinate of the fractal region
        entry_ymin (ctk.CTkEntry): The field for entry minimum y coordinate of the fractal region
        entry_ymax (ctk.CTkEntry): The field for entry maximum y coordinate of the fractal region
        entry_number (ctk.CTkEntry): The field for entry number of iterations
        canvas: Canvas for fractal
        gallery: The frame where there are fractals images

    Returns:
        None
    """
    global FRACTAL
    errors = set()
    width = check_correct_input.int_number(entry_width, "width")
    height = check_correct_input.int_number(entry_height, "height")
    xmin = check_correct_input.float_number(entry_xmin)
    xmax = check_correct_input.float_number(entry_xmax)
    ymin = check_correct_input.float_number(entry_ymin)
    ymax = check_correct_input.float_number(entry_ymax)
    red = check_correct_input.int_number(entry_red, "RED")
    green = check_correct_input.int_number(entry_green, "GREEN")
    blue = check_correct_input.int_number(entry_blue, "BLUE")
    number = check_correct_input.int_number(entry_number, "number")

    for element in width, height, xmin, \
                    xmax, ymin, ymax, \
                    red, green, blue, number:
        if isinstance(element, str):
            errors.add(element)

    if len(errors) == 0:
        result_of_check_x = check_correct_input.check_bounds(xmin, xmax,
                                                             "xmin", "xmax")
        if isinstance(result_of_check_x, str):
            errors.add(result_of_check_x)
        
        result_of_check_y = check_correct_input.check_bounds(ymin, ymax,
                                                             "ymin", "ymax")
        if isinstance(result_of_check_y, str):
            errors.add(result_of_check_y)
    
    if len(errors) > 0:
        string_errors = '\n'.join(errors)
        messagebox.showinfo("Ошибка!", string_errors)
        return

    FRACTAL = fractal_new.Fractal(width, height, number,
                                  xmin, xmax, ymin, ymax,
                                  red, green, blue)
    FRACTAL.generation()
    FRACTAL.image(canvas)
    FRACTAL.add_in_table(gallery, canvas)


def save_fractal():
    """The function which saves fractal.

    The function checks that fractal and its image exist.  If verification is successful,
    a dialog box opens for selecting a save path.  Supports PNG and JPEG formats.

    Global variables:
        FRACTAL (object): Fractal object.

    Args:
        None

    Returns:
        None

    Raises:
        PermissionError: Intercepted internally, displays a message to the user
        OSError: Intercepted internally, displays a message to the user
    """
    global FRACTAL
    if FRACTAL != None and FRACTAL.img != None:
        file_path = filedialog.asksaveasfilename(
            defaultextension = ".png",
            filetypes = [("PNG файл", "*.png"), ("JPEG файл", "*.jpeg"), ("Все файлы", "*.*")],
            title = "Сохранить фрактал как..."
        )
        if len(file_path) > 0:
            if file_path.lower().endswith(".jpeg") or file_path.lower().endswith(".jpg"):
                fmt = "JPEG"
            else:
                fmt = "PNG"
            try:
                FRACTAL.img.save(file_path, fmt)
                messagebox.showinfo('Успешно!', f'Изображение сохранено как {file_path}')
            except PermissionError:
                messagebox.showinfo('Ошибка!', 'Нет прав для записи в эту папку или файл открыт в другой программе!')
            except OSError as e:
                messagebox.showinfo('Ошибка!', f'Ошибка при сохранении файла: {e}')
    else:
        messagebox.showinfo('Ошибка!', 'Сначала сгенерируйте изображение!')


def clear_gallery(gallery):
    """The function which clear gallery with fractals.
    
    The function checks at the gallery are there images of fractals.
    If they are the function clears gallery but if not it shows
    a message anout if. 

    Args:
        gallery: The frame where there are fractals images

    Returns:
        None
    """

    children = gallery.winfo_children()
    if len(children) == 0:
        messagebox.showinfo("Ошибка!", "Галерея уже пуста")
        return
    
    fractal_new.ALL_IMAGES.clear()
    for widget in children():
        widget.destroy()
