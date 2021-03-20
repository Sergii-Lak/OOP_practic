from tkinter import *
import shutil
import datetime

def copy_files(x):
    lab['text'] = ""
    y = datetime.datetime.today().strftime(" DATE-%Y_%m_%d_%H_%M_%S")
    shutil.copytree("C:\\Users\\Serg\\Zomboid\\Saves\\Builder", f"W:\\Sergii\\Games\\SAVES_ZOBOID\\zomboid{y}")
    lab['text'] = "Saved!"


root = Tk()

ent = Entry(width=30)
but = Button(text="COPY")
lab = Label(width=30, bg='black', fg='white')

but.bind('<Button-1>', copy_files)

ent.pack()
but.pack()
lab.pack()
root.mainloop()