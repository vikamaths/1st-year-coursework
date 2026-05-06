"""Module for creating a graphical interface.

Creates all application panels: a panel for creating a fractal, 
a panel for displaying a fractal, and a panel for all generated fractals.

Contains:
    FrameLeft - the class for the consciousness of the left control panel of the fractal
    FrameRight - the class for creating a gallery
    my_root() - application window creation function
    my_canvas() - canvas creation function
    show_in_center() - the function to display an image in the center of the canvas

Author: Viktoria Chelpykh
Date: 2026-05-06
"""


from PIL import Image
import customtkinter as ctk
from customtkinter import CTkImage


class FrameLeft():
    """The class for creating the left panel for
    generation of fractals."""
    def __init__(self, root):
        self.frame_left = ctk.CTkFrame(root,
                                       width=400, 
                                       fg_color="#242830",
                                       corner_radius=30,
                                       border_width=1,
                                       border_color="#454545")
        
        self.frame_left.pack(side="left",
                             fill='y',
                             padx=(30, 15),
                             pady=(30))
    
    def main_header(self):
        """The functon for left panel header.
        
        The function create text, put image and
        also paint a line which divides the header
        and different sections.

        Args:
            None

        Returns:
            None
        """
        frame_header = ctk.CTkFrame(self.frame_left,
                                    fg_color="#242830")
        frame_header.pack(fill='x',
                          padx=40,
                          pady=(40, 30))

        circle_image = CTkImage(light_image=Image.open("img/Group 2.png"), 
                                dark_image=Image.open("img/Group 2.png"),
                                size=(62,62))

        label_circle = ctk.CTkLabel(frame_header,
                                    image=circle_image,
                                    text="")
        label_circle.pack(side='left', padx=(0,20))

        ctk.CTkLabel(frame_header,
                     text='MANDELBROTH\nFRACTAL',
                     font=('Montserrat', 25, 'bold'),
                     text_color = '#5355EA',
                     justify="left").pack(side='left', anchor="center")

        line_left = ctk.CTkCanvas(self.frame_left,
                                  width=self.frame_left.winfo_width(),
                                  height=1,
                                  bg="#242830",
                                  highlightthickness=0)
        line_left.pack(fill='x', pady=(10,10))
        def draw_line(event=None):
            """The function create new line when 
            window's width was change.
            
            Args:
                event (tk.Event): A resize event,
                                  contains the widget's 
                                  new width
                
            Returns:
                None
            """
            line_left.delete("all")  
            line_left.create_line(0, 0, line_left.winfo_width(), 0, 
                                  fill="#454545", width=1)

        line_left.bind("<Configure>", draw_line)

    def color_header(self):
        """The functon for header of color section.
    
        The function create text and put image.

        Args:
            None

        Returns:
            None
        """
        block = ctk.CTkFrame(self.frame_left,
                             fg_color="#242830")
        block.pack(fill='x',
                   padx=40,
                   pady=(30, 15))
        
        circle_image = CTkImage(light_image=Image.open("img/Group 3.png"),
                                dark_image=Image.open("img/Group 3.png"),
                                size=(45,45))
        label_circle = ctk.CTkLabel(block,
                                    image=circle_image,
                                    text='')
        label_circle.pack(side='left', padx=(0,15))

        ctk.CTkLabel(block,
                    text='Fractal color',
                    font=('Montserrat', 20, 'bold'),
                    text_color='white').pack(side='left',
                                             anchor='center')
        
    def color_entry(self):
        """The function does fields for
        colors' entries.
        
        The function does fileds for red,
        green and blue colors.

        Args:
            None

        Returns:
            tuple: A tuple of three objects CustomTkinter Entry in order:
            - entry_red (ctk.CTkEntry): The field for entry red color (0-255)
            - entry_green (ctk.CTkEntry): The field for entry green color (0-255)
            - entry_blue (ctk.CTkEntry): The field for entry blue color (0-255)
        """
        block = ctk.CTkFrame(self.frame_left,
                             fg_color="#242830")
        block.pack(fill='x',
                   padx=40,
                   pady=(0, 30))
        
        entry_red = ctk.CTkEntry(block,
                                 text_color='white',
                                 fg_color='#606060',
                                 placeholder_text="RED")
        entry_red.pack(fill='x', pady=(0, 10))

        entry_green = ctk.CTkEntry(block,
                                   text_color='white',
                                   fg_color='#606060',
                                   placeholder_text="GREEN")
        entry_green.pack(fill='x', pady=(0, 10))

        entry_blue = ctk.CTkEntry(block,
                                  text_color='white',
                                  fg_color='#606060',
                                  placeholder_text="BLUE")
        entry_blue.pack(fill='x')
        
        return entry_red, entry_green, entry_blue

    def resolution_header(self):
        """The functon for header of resolution section.
    
        The function create text and put image.

        Args:
            None

        Returns:
            None
        """
        block = ctk.CTkFrame(self.frame_left,
                             fg_color="#242830")
        block.pack(fill='x',
                   padx=40,
                   pady=(0, 15))

        circle_image = CTkImage(light_image=Image.open('img/Group 4.png'),
                                dark_image=Image.open('img/Group 4.png'),
                                size=(45,45))
        label_circle = ctk.CTkLabel(block,
                                    image=circle_image,
                                    text='')
        label_circle.pack(side='left', padx=(0, 15))

        ctk.CTkLabel(block,
                     text='Resolution',
                     font=('Montserrat', 20, 'bold'),
                     text_color='white').pack(side='left', anchor='center')

    def resolution_entry(self):
        """The function does fields for
        resolution's entries.
        
        The function does filed for width and height.

        Args:
            None

        Returns:
            tuple: A tuple of two objects CustomTkinter Entry in order:
            - entry_width (ctk.CTkEntry): The field for entry width
            - entry_height (ctk.CTkEntry): The field for entry height
        """
        block = ctk.CTkFrame(self.frame_left,
                             fg_color="#242830")
        block.pack(fill='x',
                   padx=40,
                   pady=(0, 30))

        entry_width = ctk.CTkEntry(block,
                                   text_color='white',
                                   fg_color='#606060',
                                   placeholder_text="width")
        entry_width.pack(side='left', padx=(0,7))

        entry_height = ctk.CTkEntry(block,
                                    text_color='white',
                                    fg_color='#606060',
                                    placeholder_text="height")
        entry_height.pack(side='left', padx=(7,0))

        return entry_width, entry_height

    def coordinates_header(self):
        """The functon for header of coordinates section.
    
        The function create text and put image.

        Args:
            None

        Returns:
            None
        """
        block = ctk.CTkFrame(self.frame_left,
                             fg_color="#242830")
        block.pack(fill='x',
                   padx=40,
                   pady=(0, 15))

        circle_image = CTkImage(light_image=Image.open('img/Group 5.png'),
                                dark_image=Image.open('img/Group 5.png'),
                                size=(45, 45))
        label_circle = ctk.CTkLabel(block,
                                    image=circle_image,
                                    text='')
        label_circle.pack(side='left', padx=(0, 15))

        ctk.CTkLabel(block,
                     text='Coordinates',
                     font=('Montserrat', 20, 'bold'),
                     text_color='white').pack(side='left', anchor='center')
        
    def coordinates_entry_x(self):
        """The function does fields for
        coordinates of the fractal region's entries.
        
        The function does fileds for minimum and maximum
        x coordinates.

        Args:
            None

        Returns:
            tuple: A tuple of two objects CustomTkinter Entry in order:
            - entry_xmin (ctk.CTkEntry): The field for entry minimum x coordinate of the fractal region
            - entry_xmax (ctk.CTkEntry): The field for entry maximum x coordinate of the fractal region
        """
        block = ctk.CTkFrame(self.frame_left,
                             fg_color="#242830")
        block.pack(fill='x',
                   padx=40,
                   pady=(0, 10))

        entry_xmin = ctk.CTkEntry(block,
                                  text_color='white',
                                  fg_color='#606060',
                                  placeholder_text="xmin")
        entry_xmin.pack(side='left', padx=(0, 7))

        entry_xmax = ctk.CTkEntry(block,
                                  text_color='white',
                                  fg_color='#606060',
                                  placeholder_text="xmax")
        entry_xmax.pack(side='left', padx=(7, 0))

        return entry_xmin, entry_xmax

    def coordinates_entry_y(self):
        """The function does fields for
        coordinates of the fractal region's entries.
        
        The function does fileds for minimum and maximum
        y coordinates.

        Args:
            None

        Returns:
            tuple: A tuple of two objects CustomTkinter Entry in order:
            - entry_ymin (ctk.CTkEntry): The field for entry minimum y coordinate of the fractal region
            - entry_ymax (ctk.CTkEntry): The field for entry maximum y coordinate of the fractal region
        """
        block = ctk.CTkFrame(self.frame_left,
                             fg_color="#242830")
        block.pack(fill='x',
                   padx=40, 
                   pady=(0, 30))

        entry_ymin = ctk.CTkEntry(block,
                                  text_color='white',
                                  fg_color='#606060',
                                  placeholder_text="ymin")
        entry_ymin.pack(side='left', padx=(0, 7))

        entry_ymax = ctk.CTkEntry(block,
                                  text_color='white', 
                                  fg_color='#606060',
                                  placeholder_text="ymax")
        entry_ymax.pack(side='left', padx=(7, 0)) 

        return entry_ymin, entry_ymax

    def number_of_iterations_header(self):
        """The functon for header of number of iterations section.
    
        The function create text and put image.

        Args:
            None

        Returns:
            None
        """
        block = ctk.CTkFrame(self.frame_left,
                             fg_color="#242830")
        block.pack(fill='x',
                   padx=40,
                   pady=(0, 15))

        circle_image = CTkImage(light_image=Image.open('img/Group 6.png'),
                                dark_image=Image.open('img/Group 6.png'),
                                size=(45, 45))
        label_circle = ctk.CTkLabel(block,
                                    image=circle_image,
                                    text='')
        label_circle.pack(side='left', padx=(0, 15))

        ctk.CTkLabel(block,
                     text='Number of iterations',
                     font=('Montserrat', 20, 'bold'),
                     text_color='white').pack(side='left', anchor='center')

    def number_of_iterations_entry(self):
        """The function does field for
        number of iterations's entry.

        Args:
            None

        Returns:
            entry_number (ctk.CTkEntry): The field for entry number of iterations
        """  
        block = ctk.CTkFrame(self.frame_left,
                             fg_color="#242830")
        block.pack(fill='x', padx=40)

        entry_number = ctk.CTkEntry(block,
                                    text_color='white',
                                    fg_color='#606060',
                                    placeholder_text="n")
        entry_number.pack(fill='x')

        return entry_number
    
    def buttons(self, function_1, function_2):
        """The function create buttons in the left frame.
        
        The function does button for fractal generation
        and button for saving fractal.

        Args:
            function_1: function for fractal generation
            function_2: function for saving fractal

        Returns:
            None
        """
        block = ctk.CTkFrame(self.frame_left,
                             fg_color="#242830")
        block.pack(fill='x',
                   padx=40,
                   pady=(40, 0))

        ctk.CTkButton(block,
                      text='Generation',
                      font=('Montserrat', 20, 'bold'),
                      fg_color='#5355EA',
                      command=function_1).pack(side='left', padx=(0, 8))
        ctk.CTkButton(block,
                      text='Save',
                      font=('Montserrat', 20, 'bold'),
                      fg_color='#5355EA',
                      command=function_2).pack(side='left', padx=(8, 0))
    

class FrameRight():
    """Class for the consciousness of
    the left control panel of the fractal.
    """
    def __init__(self, root):
        self.frame_right = ctk.CTkScrollableFrame(root,
                                                  width=400,
                                                  fg_color="#242830",
                                                  corner_radius=30, 
                                                  border_width=1,
                                                  border_color="#454545")
        self.frame_right.pack(side="right",
                              fill='y',
                              padx=(15, 30),
                              pady=30)

    def gallery_header(self):
        """The function generates the gallery title.

        Args:
            None
        
        Returns:
            None
        """
        frame_right_title = ctk.CTkFrame(self.frame_right,
                                         fg_color="#242830")
        frame_right_title.pack(fill='x', pady=(0, 60))

        
        ctk.CTkLabel(frame_right_title,
                     text='Story',
                     font=('Montserrat', 25, 'bold'),
                     text_color='#5355EA').pack(anchor="w")
    
        line_right = ctk.CTkCanvas(frame_right_title,
                          height=1,
                          bg="#242830",
                          highlightthickness=0)
        line_right.pack(fill='x', pady=(10, 0))

        def draw_line(event=None):
            """The function draws a dividing line between
            the gallery title and the gallery.

            Args:
                event (tk.Event): A resize event,
                                  contains the widget's new width

            Returns:
                None
            """
            line_right.delete("all")
            line_right.create_line(0, 0, line_right.winfo_width(), 0, 
                                   fill="#454545", width=1)

        line_right.bind("<Configure>", draw_line)

    def real_gallery(self):
        """The function creates a gallery.

        Args:
            None
        
        Returns:
            frame_right_gallery: The frame where will be fractals images
        """
        frame_right_gallery = ctk.CTkFrame(self.frame_right,
                                           fg_color="#242830")
        frame_right_gallery.pack(fill='both', expand=True)
        frame_right_gallery.grid_rowconfigure(0, weight=1)
        frame_right_gallery.grid_columnconfigure(0, weight=1)
        return frame_right_gallery
    
    def clear_button(self, clear_function):
        """The function create button which can clear the gallery.

        Args:
            clear_function: The fucnction which clear content in the gallery

        Returns:
            None
        """
        button_frame = ctk.CTkFrame(self.frame_right,
                                    fg_color= "#242830")
        button_frame.pack(fill='x',
                          side="bottom",
                          padx=40,
                          pady=40)
        
        button = ctk.CTkButton(button_frame,
                               text="Clear",
                               fg_color='#5355EA',
                               command=clear_function)
        button.pack(padx=20, pady=10, fill='x')


def my_root():
    """Application window creation function.

    Args:
        None

    Returns:
        root: Application window

    """
    root = ctk.CTk()
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
    root.title('Фрактал Мандельброта')
    root.iconbitmap('img/calculating.ico')
    root.configure(fg_color='#161A22')
    return root


def my_canvas(root):
    """Canvas creation function

    Args:
        root: Application window

    Returns:
        None
    """
    frame_center = ctk.CTkFrame(root,
                                fg_color="#242830",
                                corner_radius=30,
                                border_width=1,
                                border_color="#454545")
    frame_center.pack(side="left",
                      fill='both',
                      expand=True,
                      padx=15,
                      pady=30)
    
    canvas = ctk.CTkCanvas(frame_center,
                           bg='#242830',
                           highlightthickness=0)
    canvas.pack(fill="both",
                expand=True,
                padx=15,
                pady=30)
    def draw_text():
        """The text function 'There will be a fractal here!'
        in the center of the canvas

        Args:
            None

        Returns:
            None
        """
        canvas.delete("all")
        canvas.create_text(canvas.winfo_width()//2,
                           canvas.winfo_height()//2,
                           text='There will be a fractal here!',
                           font='Montserrat 15',
                           fill='#6C6C6C',
                           anchor="center")
    canvas.after(50, draw_text)
    canvas.bind("<Configure>", lambda e: draw_text())
    return canvas


def show_in_center(canvas, img):
    """Places the fractal image in the center of the canvas.

    Args:
        canvas: Canvas for fractal
        img: Fractal image

    Returns:
        None
    """
    canvas.delete("all")
    canvas.create_image(canvas.winfo_width()//2, 
                        canvas.winfo_height()//2,
                        anchor='center',
                        image=img)
