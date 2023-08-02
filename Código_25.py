# Labels:

from tkinter import *

window = Tk()

photo = PhotoImage(file="demolidor_icon.png")

label = Label(window,
              text="Olá mundo!",
              font=("Comic Sans",40,"bold"),
              fg="purple",
              bg="black",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound="bottom")
label.pack()
#label.place(x=100,y=100)


window.mainloop()