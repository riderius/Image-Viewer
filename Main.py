""" This is the main file to launch the Image-Viewer. """

import sys
import webbrowser
from tkinter import Tk, Menu, Canvas, messagebox
from PIL import Image, ImageTk

LICENSE_TEXT = """
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

"""


def show_license():
    """ This function shows the license. """

    messagebox.showinfo('License', LICENSE_TEXT)

def opening_github():
    """ This function opens the github. """

    webbrowser.open('https://github.com/RIDERIUS/Image-Viewer')

def show_version():
    """ This function shows the version. """

    messagebox.showinfo('Version', 'Version 0.2.0')

def main():
    """ Main function in the image viewer. """

    file_path = str(sys.argv[1])

    image_pil = Image.open(file_path)
    (width, height) = image_pil.size
    image_pil = image_pil.resize(
        (width, int(image_pil.size[1] * (width / image_pil.size[0]))), Image.ANTIALIAS)

    root = Tk()
    root.title("Image-Viewer")
    root.geometry(f'{width}x{height}')
    root.resizable(False, False)

    menu = Menu(root)
    new_item = Menu(menu)
    new_item.add_command(label='License', command=show_license)
    new_item.add_command(label='Github', command=opening_github)
    new_item.add_command(label='Version', command=show_version)
    menu.add_cascade(label='About', menu=new_item)
    root.config(menu=menu)

    image = ImageTk.PhotoImage(image_pil)

    canv = Canvas(root, width=width, height=height)
    canv.create_image(width / 2, height / 2, image=image)
    canv.pack()

    root.mainloop()

main()
