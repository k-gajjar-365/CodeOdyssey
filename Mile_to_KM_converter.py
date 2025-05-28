from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=340,height=250)
window.config(padx=70,pady=70)

# user input to enter mile
input_mile = Entry(width=7)
input_mile.grid(column=1,row=0)
input_mile.focus()

# Miles label
ml = Label(text="Miles")
ml.grid(column=2,row=0)


# is equal to
l1 = Label(text="is equal to ")
l1.grid(column=0,row=1)

# converted km
km = Label(text=0)
km.grid(column=1,row=1)

# KM label
kml = Label(text="Km")
kml.grid(column=2,row=1)

def calculate():
    mile = float(input_mile.get())
    km.config(text=f"{round(mile*1.609,2)}")
# calculate button
cal = Button(text="Calculate",command=calculate)
cal.grid(column=1,row=2)


window.mainloop()