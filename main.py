""" This is the main file to launch the Image-Viewer. """

import sys
import webbrowser
from tkinter import Tk, Menu, Canvas, messagebox, Label, Entry, Button
from PIL import Image, ImageTk


def show_license():
    """ This function shows the license. """

    messagebox.showinfo('License', """
MIT License

Copyright (c) 2020

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

""")


def opening_github():
    """ This function opens the github. """

    webbrowser.open('https://github.com/RIDERIUS/Image-Viewer')


def show_version():
    """ This function shows the version. """

    messagebox.showinfo('Version', 'Version 0.3.0')


def crop_image():
    """ This function is needed to crop images. """

    def cropping():
        """This function will crop images."""
        root.geometry(
            f"{x_entry_cropping_window.get()}x{y_entry_cropping_window.get()}")
        root.mainloop()

    cropping_window = Tk()
    cropping_window.geometry('404x65')
    cropping_window.title('Crop Image')
    cropping_window.resizable(False, False)

    x_label_cropping_window = Label(cropping_window, text='Width Image')
    x_label_cropping_window.grid(column=0, row=0)
    y_label_cropping_window = Label(cropping_window, text='Height Image')
    y_label_cropping_window.grid(column=2, row=0)

    x_entry_cropping_window = Entry(cropping_window,)
    x_entry_cropping_window.grid(column=1, row=0)
    y_entry_cropping_window = Entry(cropping_window)
    y_entry_cropping_window.grid(column=3, row=0)

    button_cropping_window = Button(
        cropping_window, text='Submit', command=cropping)
    button_cropping_window.grid(column=2, row=1)

    cropping_window.mainloop()


def resize_image():
    """ This function is needed to resizing images. """

    resizing_window = Tk()
    resizing_window.geometry('404x65')
    resizing_window.title('Resize Image')
    resizing_window.resizable(False, False)

    x_label_resizing_window = Label(resizing_window, text='Width Image')
    x_label_resizing_window.grid(column=0, row=0)
    y_label_resizing_window = Label(resizing_window, text='Height Image')
    y_label_resizing_window.grid(column=2, row=0)

    x_entry_resizing_window = Entry(resizing_window,)
    x_entry_resizing_window.grid(column=1, row=0)
    y_entry_resizing_window = Entry(resizing_window)
    y_entry_resizing_window.grid(column=3, row=0)

    button_resizing_window = Button(
        resizing_window, text='Submit')
    button_resizing_window.grid(column=2, row=1)

    resizing_window.mainloop()


FILE_PATH = str(sys.argv[1])

image_pil = Image.open(FILE_PATH)
(width, height) = image_pil.size

root = Tk()
root.title("Image-Viewer")
root.geometry(f'{width}x{height}')
root.resizable(False, False)

menu = Menu(root)
root.config(menu=menu)

about_menu = Menu(menu)
edit_image_menu = Menu(menu)

about_menu.add_command(label='License', command=show_license)
about_menu.add_command(label='Github', command=opening_github)
about_menu.add_command(label='Version', command=show_version)
edit_image_menu.add_command(label='Crop Image', command=crop_image)
edit_image_menu.add_command(label='Resize Image', command=resize_image)

menu.add_cascade(label='About', menu=about_menu)
menu.add_cascade(label='Edit Image', menu=edit_image_menu)

image = ImageTk.PhotoImage(image_pil)

canv = Canvas(root, width=width, height=height)
canv.create_image(width / 2, height / 2, image=image)
canv.pack()

root.mainloop()
