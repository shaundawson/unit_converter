from tkinter import *

# The distance in kilometers is equal to the distance in miles multiplied by 1.609344.
conversion_factor = 1.60934

def miles_to_km():
    miles = int(miles_input.get())
    calc = round(miles * conversion_factor,2)
    km_output.config(text=calc)

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

is_equal_label = Label(text="is equal to", font=("Arial", 18, "normal"))
is_equal_label.grid(column=0, row=1)

miles_input = Entry(width="5")
miles_input.grid(column=1,row=0)

miles_label = Label(text="Miles", font=("Arial", 18, "normal"))
miles_label.grid(column=2, row=0)

km_output = Label(text = "0",font=("Arial", 18, "normal"))
km_output.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 18, "normal"))
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=3)


window.mainloop()