from tkinter import *
from imageprocessing import Imageprocessing
from knnmodel import MLmodel
import tkcap

class Main:
    def __init__(self,master):
        self.master = master                 # default window of tkinter
        self.model = MLmodel.trainModel()    # prediction algorithm model
        self.color_fg = 'black'              # foreground color white
        self.color_bg = 'white'              # background color white
        self.old_x = None                    # x-coordinate of the drawing pen 
        self.old_y = None                    # y-coordinate of the drawing pen 
        self.penwidth = 15                   # pen width
        self.drawWidgets()                   # method for creating widgets for the application

        # methods used for tracking the movement of mouse
        self.c.bind('<B1-Motion>',self.paint)                 #drawing the line when the mouse button is pressed
        self.c.bind('<ButtonRelease-1>',self.resetAndSave)    #terminating the line when the button is released  
                       

    def paint(self,e):         # Method to draw a line
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, e.x, e.y, width=self. penwidth, fill=self.color_fg, capstyle=ROUND, smooth=True)

        self.old_x = e.x
        self.old_y = e.y

    def resetAndSave(self,e):         # Method for reseting the coordinates of the pen(termination of line)
        self.old_x = None
        self.old_y = None   
        cap = tkcap.CAP(self.master)
        cap.capture('data_images/image.png', overwrite=True)

    def clear(self):           # Method for clearing canvas
        self.c.delete(ALL)

    def predict(self):
        ML_data = Imageprocessing.cleanImage()
        prediction = self.model.predict(ML_data)
        Label(self.controls, text='Prediction: ',font=('arial 10')).grid(row=1,column=0)
        Label(self.controls, text = int(prediction[0]), font=('arial 15')).grid(row=1, column=1)

    def drawWidgets(self):
        self.controls = Frame(self.master,padx = 5,pady = 5)
        Button(self.controls, text = "Clear", font=('Comicsansms 20'),command=self.clear).grid(row=0, column=0)
        Button(self.controls, text = "Prediction", font=('Comicsansms 20'),command=self.predict).grid(row=0, column=1)
        self.controls.pack(side=BOTTOM)

        self.c = Canvas(self.master,width=500,height=400,bg=self.color_bg,)
        self.c.pack(fill=BOTH,expand=True)

        menu = Menu(self.master)
        self.master.config(menu=menu)
        optionmenu = Menu(menu)
        menu.add_cascade(label='Options',menu=optionmenu)
        optionmenu.add_command(label='Exit',command=self.master.destroy) 

if __name__ == "__main__":
    root = Tk()
    root.geometry("500x500")
    root.maxsize(500,500)
    root.minsize(500,500)
    root.title("Digit Recognition App")
    Main(root)
    root.mainloop()

