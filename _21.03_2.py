from tkinter import * 
from turtle import width
from PIL import ImageGrab
import io
raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=600, height=600, background="#ed8282")
k=7
x0=0
y0=0
x1=550
y1=550
for i in range(k):
    x0+=50
    y0+=50
    x1-=50
    y1-=50
    tahvel.create_rectangle(x0,y0,x1,y1,width=1,outline="black", fill="#992222")
    tahvel.create_oval(x0,y0,x1,y1,width=1, outline="black", fill="#870505")
tahvel.grid()

ps = tahvel.postscript(colormode='color')
x1=tahvel.winfo_width()
y1=tahvel.winfo_height()

ImageGrab.grab().crop((0,0,x1,y1)).save("image.jpg")
raam.mainloop()