from tkinter import *

conversion_factor = 1.6

def button_clicked():
    miles = int(input.get())
    calc = round(miles * conversion_factor,1)
    km_output.config(text=calc)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

#Label
main_label = Label(text="is equal to", font=("Arial", 18, "normal"))
main_label.grid(column=0, row=2)

#Entry
input = Entry(width="10")
input.grid(column=1,row=1)

# Miles Label
miles_label = Label(text="Miles", font=("Arial", 18, "normal"))
miles_label.grid(column=2, row=1)


# Km output
km_output = Label(font=("Arial", 18, "normal"))
km_output.grid(column=1, row=2)

# Km Label
km_label = Label(text="Km", font=("Arial", 18, "normal"))
km_label.grid(column=2, row=2)


#Calculate Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)








window.mainloop()