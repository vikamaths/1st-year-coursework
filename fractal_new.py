"""Module for creating new fractal.

Does generation on formule fractal and it's image.
Also adds this image at the table.

Contains:
    Fractal - the class which does all action from the top of the file

Author: Viktoria Chelpykh
Date: 20226-05-6 
"""


from PIL import Image, ImageTk, ImageDraw
import customtkinter as ctk
from customtkinter import CTkImage

import visualization


ALL_IMAGES = []


class Fractal():
    """The class for creating fractal."""
    def __init__(self, width, height, n,
                 xmin, xmax, ymin, ymax,
                 red, green, blue):
        self.width = width
        self.height = height
        self.img = Image.new("RGB", (width, height), "white")
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax 
        self.n = n
        self.red = red
        self.green = green
        self.blue = blue
    
    def generation(self):
        """The functon for generation fractal on formule.

        This functon does translation from coordinates to pixels
        and after that put different colors in pixels on the
        math formule.

        Args:
            None
        
            
        Returns:
            None
        """
        for px in range(self.width):
            for py in range(self.height):
                x = self.xmin + px * ((self.xmax - self.xmin) / self.width)
                y = self.ymin + py * ((self.ymax - self.ymin) / self.height) 
                c = complex(x, y)
                z = complex(0)
                for i in range(self.n):
                    z = z**2 + c
                    if abs(z) > 2:
                        r = (i * self.red) % 256
                        g = (i * self.green) % 256 
                        b = (i * self.blue) % 256
                        self.img.putpixel((px, py), (r, g, b))
                        break
                else:
                    self.img.putpixel((px, py), (0, 0, 0))

    def image(self, canvas):
        """The function puts image of fractal in the
        center of canvas.

        Args:
            None

        Returns:
            None
        """
        self.tk_image = ImageTk.PhotoImage(self.img) 
        canvas.delete("all")
        canvas.create_image(canvas.winfo_width()//2,
                            canvas.winfo_height()//2, 
                            anchor = 'center',
                            image = self.tk_image)

    def add_in_table(self, gallery, canvas):
        """The functions adds new image of the fractal
        at the gallery.

        The function does corner radios on the picture
        and add it in the correct place at the table.

        Args:
            gallery: The gallery where there are all
                     fractals which was generated
            canvas: The canvas where threre are
                    image of the fractal

        Returns:
            None
        """
        current_img = self.img.copy()
        current_img.thumbnail((150, 150), Image.LANCZOS)
        mask = Image.new('L', current_img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle((0, 0, current_img.width, current_img.height), 
                            radius=25, fill=255)
        current_img.putalpha(mask)
        ctk_current_img = CTkImage(light_image=current_img,
                                   dark_image=current_img,
                                   size=(150,150))
        
        row = len(ALL_IMAGES) // 2
        column = len(ALL_IMAGES) % 2

        ALL_IMAGES.append(ctk_current_img)
   
        label = ctk.CTkLabel(gallery,
                             image=ctk_current_img,
                             text='')
        label.grid(row=row,
                   column=column,
                   padx=10,
                   pady=10,
                   sticky="w")
        label.bind("<Button-1>",
                   lambda e,
                   img = self.tk_image: visualization.show_in_center(canvas, img))
