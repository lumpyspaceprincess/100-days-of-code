from tkinter import *


def button_clicked():
    miles = float(miles_entry.get())
    kms = round(miles * 1.609344, 2)
    km_var.config(text=f"{kms}")


window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=5, height=3)
window.config(padx=7, pady=7)

# Miles entry box
miles_entry = Entry(width=5, font=("Ariel", 24, ))
miles_entry.grid(column=1, row=0)

# Static text: "Is equal to", "miles", "kilometres"
is_equal_to_label = Label(text="is equal to", font=("Ariel", 24, ))
is_equal_to_label.grid(column=0, row=1)

miles_static_label = Label(text="miles", font=("Ariel", 24,))
miles_static_label.grid(column=2, row=0)

kilometres_static_label = Label(text="kilometres", font=("Ariel", 24,))
kilometres_static_label.grid(column=2, row=1)

# Kilometres variable
km_var = Label(text="0", font=("Ariel", 24, ))
km_var.grid(column=1, row=1)

# Calculate button

calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)

# def lets_try_a_spinbox():
#     spinstr = spinbox.get()
#     spinfloat = float(spinstr)
#     calculated = spinfloat * 1.609344
#     km_var.config(text=round(calculated, 2))
#
# spinbox = Spinbox(from_=0, to=10000, width=5, command=lets_try_a_spinbox)
# spinbox.grid(column=1, row=0)

window.mainloop()
