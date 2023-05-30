from tkinter import *
from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog


def openFile():
    global img_path
    img_path = filedialog.askopenfilename(initialdir='/', title="Pick an image")

def addWatermark():
    watermark = watermark_input.get()

    img = Image.open(img_path)
    w, h = img.size

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(font="Arial Unicode.ttf", size=36)
    txtw, txth = draw.textsize(watermark, font)

    x = w - txtw - 10
    y = h - txth - 10

    # draw.text((w,h), watermark)
    draw.text((x,y), watermark, font=font)
  
    img.show()
    


window = Tk()
window.title('Watermark by Newton')
window.config(padx=20, pady=2)

image_label = Label(window, text='Enter your file path: ')
image_label.grid(column=0, row=0)

image_input = Button(window, text='OPEN IMG FILE', command=openFile)
image_input.grid(column=1, row=0)

watermark_label = Label(window, text="What text would you like to add as a watermark? ")
watermark_label.grid(column=0, row=1)

watermark_input = Entry(width=20)
watermark_input.grid(column=1, row=1)

add_watermark_button = Button(window, text="ADD WATERMARK", command=addWatermark).grid(column=1, row=2)

window.mainloop()