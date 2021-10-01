from tkinter import *
from time import strftime

class Clock:
    
    #Initializer

    def __init__(self):
        self.tk = Tk()
        self.tk.title('Clock')
        self.tk.attributes('-zoomed', True)
        self.tk.configure(background='#1a1a1a')
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.lbl1 = Label(self.tk, font = ('Courier',100,'normal'),
                          background= '#1a1a1a',
                          foreground= '#ffffda',
                          relief= 'flat')
        self.lbl1.place(relx=0.5, rely=0.4, anchor='center')
        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        self.lbl2 = Label(self.tk, font =('Courier',50,'normal'),
                          background= '#1a1a1a',
                          foreground= '#ffffda',
                          relief= 'flat')
        self.lbl2.place(relx=0.5, rely=0.6, anchor='center')
    
    #Time function for showing the hour/minute/second
    def time(self):
        self.string1 = strftime('%H:%M:%S')
        self.lbl1.config(text= self.string1)
        self.lbl1.after(1000,self.time)
    
    def time_date(self):
        self.string2 = strftime('%A\n%d %m %Y')
        self.lbl2.config(text=self.string2)
    
    #toggle fullscreen when F11 is pressed

    def toggle_fullscreen(self, event = None):
        self.state = not self.state
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    #end fullscreen when ESC is pressed

    def end_fullscreen(self, event = None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

if __name__ == '__main__':
    w = Clock()
    w.time()
    w.time_date()
    w.tk.mainloop()