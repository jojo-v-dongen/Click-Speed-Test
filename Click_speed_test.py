import tkinter as tk; from tkinter import ttk
import time; from time import sleep
from threading import Thread

root = tk.Tk()
root.geometry("800x700+300+60")
root.title("CPS TEST")
x = False
def home_page():
    root.config(bg = "#a8a8a8")

    topframe = tk.Frame(root)
    topframe.pack(anchor="n")
    topframe.config( bg = "#a8a8a8")
    
    s5_button = HoverButton(topframe, text="5 Seconds", fg="black", bg = "white", width=10, height=1, activebackground='green', command=lambda: clicking_page(5) )
    s5_button.pack( side = tk.LEFT, padx=10)
    s10_button = HoverButton(topframe, text="10 Seconds", fg="black",  bg = "white", width=10, height=1, activebackground='red', command=lambda: clicking_page(10) )
    s10_button.pack( side = tk.LEFT )

    s30_button = HoverButton(topframe, text="30 Seconds", fg="black", bg = "white", width=10, height=1, activebackground='blue', command=lambda: clicking_page(30) )
    s30_button.pack( side = tk.LEFT, padx=10)
    s60_button = HoverButton(topframe, text="60 Seconds", fg="black",  bg = "white", width=10, height=1, activebackground='purple', command=lambda: clicking_page(60) )
    s60_button.pack( side = tk.LEFT )



def clicking_page(t):
    global label, x, time, score, s5_button, s10_button, s30_button, s60_button, highscore
    highscore = 0
    score = 0
    x = False
    time = t
    delete_screen()
    root.config(bg = "#a8a8a8")

    topframe = tk.Frame(root)
    topframe.pack(anchor="n")
    topframe.config( bg = "#a8a8a8")
    
    s5_button = HoverButton(topframe, text="5 Seconds", fg="black", bg = "white", width=10, height=1, activebackground='green', command=lambda: clicking_page(5) )
    s5_button.pack( side = tk.LEFT, padx=10)
    s10_button = HoverButton(topframe, text="10 Seconds", fg="black",  bg = "white", width=10, height=1, activebackground='red', command=lambda: clicking_page(10))
    s10_button.pack( side = tk.LEFT )

    s30_button = HoverButton(topframe, text="30 Seconds", fg="black", bg = "white", width=10, height=1, activebackground='blue', command=lambda: clicking_page(30) )
    s30_button.pack( side = tk.LEFT, padx=10)
    s60_button = HoverButton(topframe, text="60 Seconds", fg="black",  bg = "white", width=10, height=1, activebackground='purple', command=lambda: clicking_page(60))
    s60_button.pack( side = tk.LEFT )

    centerframe = tk.Frame(root)
    centerframe.pack(anchor="s")
    centerframe.config( bg = "#a8a8a8")

    c_button = HoverButton(centerframe, text="Click me!", fg="black", bg = "#deddd9", width=55, height=12, activebackground='#32CD32', command=lambda: click() )
    c_button.pack( side = tk.BOTTOM, pady=30)
    
    label = tk.Label(centerframe, text = "Click the button to start the {} seconds timer".format(str(time)), fg="black", bg = "#a8a8a8", font=("Arial", 25))
    label.pack(side =  tk.BOTTOM, pady=50)



def delete_screen() :
    s = root.winfo_children()

    for i in s :
        try:
            i.destroy()
        except:
            i.delete()
    root.config(bg = "SystemButtonFace")



def score_screen():
    global x, score_label, score, label, time, s5_button, s10_button, s30_button, s60_button, highscore, highscore_label, cps_label
    try:
        score_label.destroy()
        cps_label.destroy()
    except NameError:
        pass

    if highscore < score:
        highscore = score
        try:
            highscore_label.destroy()
        except NameError:
            pass
        highscore_label = tk.Label(text = "Highscore: {}".format(str(highscore)), fg="black", bg = "#a8a8a8", font=("Arial", 25))
        highscore_label.pack(side = tk.BOTTOM, pady=5)
        
    score_label = tk.Label(text = "YOUR SCORE: {}".format(str(score)), fg="black", bg = "#a8a8a8", font=("Arial", 25))
    score_label.pack(side = tk.BOTTOM, pady=15)
    cps_label = tk.Label(text = "CPS: {}".format(str(round(score/time, 3))), fg="black", bg = "#a8a8a8", font=("Arial", 25))
    cps_label.pack(side = tk.BOTTOM, pady=23)
    
    sleep(1)
    score = 0
    x = False
    label.configure(text="Click the button to start the {} seconds timer".format(str(time)))
    s5_button["state"] = s10_button["state"] = s30_button["state"] = s60_button["state"] = "normal"
    

def click():
    global x, score, s5_button, s10_button, s30_button, s60_button
    score += 1
    if x == False:
        s5_button["state"] = s10_button["state"] = s30_button["state"] = s60_button["state"] = "disabled"
        x = True
        t1 = Thread(target=timer)
        t1.setDaemon(True)
        t1.start()
    



def timer():
    global label, time, i
    for i in range(time, -1, -1):
        label.configure(text="TIME: {}".format(str(i)))
        sleep(0.9)
    score_screen()

    



class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground
home_page()

root.mainloop()
