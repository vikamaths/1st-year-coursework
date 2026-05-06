from tkinter import messagebox, filedialog

import check_correct_input
import fractal_new


FRACTAL = None


def draw_fractal(entry_red, entry_green, entry_blue,
                 entry_width, entry_height, entry_xmin, 
                 entry_xmax, entry_ymin, entry_ymax,
                 entry_number, canvas, gallery):
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
    fractal_new.ALL_IMAGES.clear()
    for widget in gallery.winfo_children():
        widget.destroy()
        