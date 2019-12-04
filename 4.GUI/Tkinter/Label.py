from tkinter import *

root = Tk()

frame = Frame(root, width=500, height=500)

frame.pack()

# imagePlaneta=PhotoImage(file="Ud-logoR.png")

# TEXTO
labelT = Label(frame, text="LICENCIAS MÉDICAS", fg="red", font=("Arial", 15))
labelT.place(x=140, y=250)

# IMAGEN
# labelI = Label(frame, image=imagePlaneta)
#labelI.place(x=50, y=0)

root.mainloop()
