from tkinter import *

#initial setup
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200,height=100)
window.config(padx=20, pady=20)

#functions
def mile_km_conv():
    mile = int(mile_entry.get())
    km = 1.6093*mile
    km_calc_label.config(text = str(km))
#widgets
# Entries
mile_entry = Entry(width=10)
# mile_entry.insert(END,string = "0")
mile_entry.grid(column=1,row=0)

# labels
Miles_label = Label(text="Miles")
Miles_label.grid(column=2,row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0,row=1)

km_calc_label = Label(text="0")
km_calc_label.grid(column=1,row=1)

km_label = Label(text="Km")
km_label.grid(column=2,row=1)


# button
calc_button = Button(text = "Calculate",command = mile_km_conv)
calc_button.grid(column=1,row=2)
window.mainloop()
