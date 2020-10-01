import sys
from tkinter import *
from PIL import Image, ImageTk

file_path = str(sys.argv[1])

imagePIL = Image.open(file_path)
(width, height) = imagePIL.size

imagePIL = Image.open(file_path)
imagePIL = imagePIL.resize((width, int(imagePIL.size[1] * (width / imagePIL.size[0]))), Image.ANTIALIAS)

root = Tk()
root.title("Picture reader")
root.geometry(f'{width}x{height}')
root.resizable(False, False)

image = ImageTk.PhotoImage(imagePIL)

canv = Canvas(root, width = width, height = height)
imageSprite = canv.create_image(width / 2, height / 2, image = image)
canv.pack()

root.mainloop()