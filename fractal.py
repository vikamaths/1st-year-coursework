from PIL import Image, ImageTk
import customtkinter as ctk
from customtkinter import CTkImage
import tkinter as tk
from tkinter import messagebox, filedialog


def int_number(entry_current, meaning):
    try:
        value = int(entry_current.get())
        if meaning == "width" or meaning == "height":
            if value >= 100:
                return value
            else:
                raise ValueError
        elif meaning == "n":
            if value > 0:
                return value
            else:
                raise ValueError
        elif meaning in ("R", "G", "B"):
            if 0 <= value <= 255:
                return value  
            else:
                raise ValueError
        else:
            raise ValueError
    except:
        messagebox.showinfo("Ошибка!", "Значение должно быть целое и не меньше 100")
        return None

def float_number(entry_current):
    try:
        value = float(entry_current.get())
        return value
    except:
        messagebox.showinfo("Ошибка!", "Значение должно быть вещественное")
        return None
    
def check_bounds(current_min, current_max, meaning_min, meaning_max):
    if current_min < current_max:
        return True
    else:
        messagebox.showinfo("Ошибка!", f"{meaning_min} должен быть меньше, чем {meaning_max}")
        return False

def fractal():
    global img #для того чтобы можно было сохранить изображение
    #разрешение изображения
    width = int_number(entry_width, "width")
    height = int_number(entry_height, "height")
    img = Image.new("RGB", (width, height), "white") #создаю поле рисования
    #в этой области существует фрактал, масштабирование
    xmin = float_number(entry_xmin)
    xmax = float_number(entry_xmax)
    if not(check_bounds(xmin, xmax, "xmin", "xmax")):
        return
    ymin = float_number(entry_ymin)
    ymax = float_number(entry_ymax)
    if not(check_bounds(ymin, ymax, "ymin", "ymax")):
        return

    n = int_number(entry_n, "n") #кол-во итераций
    #переменные для получений случайных цветов
    r_random = int_number(entry_red, "R")
    g_random = int_number(entry_green, "G")
    b_random = int_number(entry_blue, "B")

    for current in width, height, xmin, xmax, ymin, ymax, n, r_random, g_random, b_random:
        if current == None:
            return

    for px in range(width):
        for py in range(height):
            x = xmin + px * ((xmax - xmin) / width) #перевод из пикселей в координаты декартовой плоскости
            y = ymin + py * ((ymax - ymin) / height) 
            c = complex(x, y)
            z = complex(0)
            for i in range(n):
                z = z**2 + c
                if abs(z) > 2: #фрактала не существует в этой области
                    r = (i * r_random) % 256 #создание случайных цветов
                    g = (i * g_random) % 256 
                    b = (i * b_random) % 256
                    img.putpixel((px, py), (r, g, b))
                    break
            else:
                img.putpixel((px, py), (0, 0, 0))
                
    global tk_image
    tk_image = ImageTk.PhotoImage(img) #сохранения ссылки на изображения, чтобы при выходе из функции
    canvas.delete("all")
    canvas.create_image(canvas.winfo_width()//2, canvas.winfo_height()//2, #canvas продолжат показывать изображение
                        anchor = 'center',
                        image = tk_image)
    current_img = img.copy()
    current_img.thumbnail((150, 150), Image.LANCZOS)
    ctk_current_img = CTkImage(light_image=current_img, dark_image=current_img, size=(150,150))
    row = len(all_images) // 2
    column = len(all_images) % 2
    all_images.append(ctk_current_img)
    label = ctk.CTkLabel(frame_right_gallery , image=ctk_current_img, text='')
    label.grid(row=row, column=column, padx=10, pady=10)
    label.bind("<Button-1>", lambda e, img = tk_image: show_in_center(img))

def show_in_center(img):
    canvas.delete("all")
    canvas.create_image(canvas.winfo_width()//2, canvas.winfo_height()//2, #canvas продолжат показывать изображение
                        anchor = 'center',
                        image = img)

def save_fractal():
    if 'img' in globals(): #проверка на то, что изображение было создано
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
                img.save(file_path, fmt)
                messagebox.showinfo('Успешно!', f'Изображение сохранено как {file_path}')
            except PermissionError:
                messagebox.showinfo('Ошибка!', 'Нет прав для записи в эту папку или файл открыт в другой программе!')
            except OSError as e:
                messagebox.showinfo('Ошибка!', f'Ошибка при сохранении файла: {e}')
    else:
        messagebox.showinfo('Ошибка!', 'Сначала сгенерируйте изображение!')


root = ctk.CTk()
root.state('zoomed')
root.title('Фрактал Мандельброта')
root.iconbitmap('calculating.ico')
root.configure(fg_color='#161A22')

frame_left = ctk.CTkFrame(root, width=400, fg_color="#242830", corner_radius=30, 
                          border_width=1, border_color="#454545")
frame_left.pack(side="left", fill='y', padx=(30, 15), pady=(30))

frame_center = ctk.CTkFrame(root, fg_color="#242830", corner_radius=30, 
                            border_width=1, border_color="#454545")
frame_center.pack(side="left", fill='both', expand=True, padx=15, pady=30)

frame_right = ctk.CTkScrollableFrame(root, width=400, fg_color="#242830", 
                                     corner_radius=30, border_width=1, border_color="#454545")
frame_right.pack(side="right", fill='y', padx=(15,30), pady=30)
frame_right_title = ctk.CTkFrame(frame_right, fg_color="#242830")
frame_right_title.pack(fill='x', pady=(0,60))
ctk.CTkLabel(frame_right_title, text = 'Story',
            font = ('Montserrat', 25, 'bold'),
            text_color = '#5355EA').pack(side='left')

frame_right_gallery = ctk.CTkFrame(frame_right, fg_color="#242830")
frame_right_gallery.pack(fill='both', expand=True)
all_images = []

#создание холста
canvas = ctk.CTkCanvas(frame_center, bg = '#242830', highlightthickness=0)
canvas.pack(fill="both", expand=True, padx=15, pady=30)
canvas.update() 
canvas.create_text(canvas.winfo_width() //2, canvas.winfo_height()//2,
                   text = 'There will be a fractal here!',
                   font = 'Montserrat 15',
                   fill = '#6C6C6C',
                   anchor="center")

#подблок 1
frame_header = ctk.CTkFrame(frame_left, fg_color="#242830")
frame_header.pack(fill = 'x', padx = 40, pady = (40, 30))

circle_image_1 = CTkImage(light_image = Image.open("Group 2.png"), 
                          dark_image = Image.open("Group 2.png"),
                          size=(62,62))

label_circle_1 = ctk.CTkLabel(frame_header, image = circle_image_1, text="")
label_circle_1.pack(side='left', padx=(0,20))

ctk.CTkLabel(frame_header,
            text = 'MANDELBROTH\nFRACTAL',
            font = ('Montserrat', 25, 'bold'),
            text_color = '#5355EA',
            justify="left").pack(side='left', anchor="center")

line_left = ctk.CTkCanvas(frame_left, width=frame_left.winfo_width(),
                         height=1, bg="#242830",
                         highlightthickness=0)
line_left.pack(fill='x', pady=(10,10))
frame_right.update()
line_left.create_line(0,0, frame_left.winfo_width(),0,fill="#454545",width=1)

#подблок 2
block_1 = ctk.CTkFrame(frame_left, fg_color="#242830")
block_1.pack(fill='x', padx=40, pady=(30, 15))
circle_image_2 = CTkImage(light_image=Image.open("Group 3.png"),
                          dark_image=Image.open("Group 3.png"),
                          size=(45,45))
label_circle_2 = ctk.CTkLabel(block_1, image=circle_image_2, text='')
label_circle_2.pack(side = 'left', padx=(0,15))
ctk.CTkLabel(block_1,
            text = 'Fractal color',
            font = ('Montserrat', 20, 'bold'),
            text_color = 'white').pack(side='left', anchor='center')
#подблок 3
block_2 = ctk.CTkFrame(frame_left, fg_color="#242830")
block_2.pack(fill='x', padx=40, pady=(0, 30))
entry_red = ctk.CTkEntry(block_2,
                        text_color = 'white',
                        fg_color = '#606060',
                        placeholder_text="RED")
entry_red.pack(fill='x', pady=(0,10))

entry_green = ctk.CTkEntry(block_2, text_color = 'white', 
                           fg_color = '#606060', placeholder_text="GREEN")
entry_green.pack(fill='x', pady=(0,10))

entry_blue = ctk.CTkEntry(block_2,
                        text_color = 'white',
                        fg_color = '#606060',
                        placeholder_text="BLUE")
entry_blue.pack(fill='x')

#подблок 4
block_3 = ctk.CTkFrame(frame_left, fg_color="#242830")
block_3.pack(fill='x', padx=40, pady=(0, 15))
circle_image_3 = CTkImage(light_image=Image.open('Group 4.png'),
                          dark_image=Image.open('Group 4.png'),
                          size=(45,45))
label_circle_3 = ctk.CTkLabel(block_3, image=circle_image_3, text='')
label_circle_3.pack(side = 'left', padx=(0,15))
ctk.CTkLabel(block_3,
            text = 'Resolution',
            font = ('Montserrat', 20, 'bold'),
            text_color = 'white').pack(side='left', anchor='center')

#подблок 5
block_4 = ctk.CTkFrame(frame_left, fg_color="#242830")
block_4.pack(fill='x', padx=40, pady=(0, 30))
entry_width = ctk.CTkEntry(block_4,
                           text_color = 'white', fg_color = '#606060',
                           placeholder_text="width")
entry_width.pack(side='left', padx=(0,7))

entry_height = ctk.CTkEntry(block_4,
                            text_color = 'white', fg_color = '#606060',
                            placeholder_text="height")
entry_height.pack(side='left', padx=(7,0))

#подблок 6
block_5 = ctk.CTkFrame(frame_left, fg_color="#242830")
block_5.pack(fill='x', padx=40, pady=(0, 15))
circle_image_4 = CTkImage(light_image=Image.open('Group 5.png'),
                          dark_image=Image.open('Group 5.png'),
                          size=(45,45))
label_circle_4 = ctk.CTkLabel(block_5, image=circle_image_4, text='')
label_circle_4.pack(side = 'left', padx=(0,15))
ctk.CTkLabel(block_5,
            text = 'Coordinates',
            font = ('Montserrat', 20, 'bold'),
            text_color = 'white').pack(side='left', anchor='center')

#подблок 7
block_6 = ctk.CTkFrame(frame_left, fg_color="#242830")
block_6.pack(fill='x', padx=40, pady=(0, 10))
entry_xmin = ctk.CTkEntry(block_6,
                          text_color = 'white', fg_color = '#606060',
                          placeholder_text="xmin")
entry_xmin.pack(side='left', padx=(0,7))

entry_xmax = ctk.CTkEntry(block_6,
                          text_color = 'white', fg_color = '#606060',
                          placeholder_text="xmax")
entry_xmax.pack(side='left', padx=(7,0))

#подблок 8
block_7 = ctk.CTkFrame(frame_left, fg_color="#242830")
block_7.pack(fill='x', padx=40, pady=(0, 30))
entry_ymin = ctk.CTkEntry(block_7,
                          text_color = 'white', fg_color = '#606060',
                          placeholder_text="ymin")
entry_ymin.pack(side='left', padx=(0,7))

entry_ymax = ctk.CTkEntry(block_7,
                          text_color = 'white', fg_color = '#606060',
                          placeholder_text="ymax")
entry_ymax.pack(side='left', padx=(7,0))

#подблок 9
block_8 = ctk.CTkFrame(frame_left, fg_color="#242830")
block_8.pack(fill='x', padx=40, pady=(0, 15))
circle_image_5 = CTkImage(light_image=Image.open('Group 6.png'),
                          dark_image=Image.open('Group 6.png'),
                          size=(45,45))
label_circle_5 = ctk.CTkLabel(block_8, image=circle_image_5, text='')
label_circle_5.pack(side = 'left', padx=(0,15))
ctk.CTkLabel(block_8,
            text = 'Coordinates',
            font = ('Montserrat', 20, 'bold'),
            text_color = 'white').pack(side='left', anchor='center')

#подблок 10
block_9 = ctk.CTkFrame(frame_left, fg_color="#242830")
block_9.pack(fill='x', padx=40)
entry_n = ctk.CTkEntry(block_9,
                      text_color = 'white', fg_color = '#606060',
                      placeholder_text="n")
entry_n.pack(fill='x')

#подблок 11
block_10 = ctk.CTkFrame(frame_left, fg_color="#242830")
block_10.pack(fill='x', padx=40, pady=(40,0))

ctk.CTkButton(block_10,
              text = 'Generation',
              font = ('Montserrat', 20, 'bold'),
              fg_color = '#5355EA',
              command = fractal).pack(side='left', padx=(0,8))
ctk.CTkButton(block_10,
              text = 'Save',
              font = ('Montserrat', 20, 'bold'),
              fg_color = '#5355EA',
              command = save_fractal).pack(side='left', padx=(8,0))

root.mainloop()
