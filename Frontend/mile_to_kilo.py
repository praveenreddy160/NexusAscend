from tkinter import *

def calculate():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilo_meter_output.config(text=f"{km}")

#Creating a new window and configurations
window = Tk()
window.title("Mile to Kilometres Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="Is equal to", font=("Arial", 24, "bold"))
is_equal_to_label.grid(column=0, row=1)

kilo_meter_output = Label(text="0", font=("Arial", 24, "bold"))
kilo_meter_output.grid(column=1, row=1)

kilo_meter_label = Label(text="Km", font=("Arial", 24, "bold"))
kilo_meter_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)  # Note: calculate, not 'calculated'
calculate_button.grid(column=1, row=2)

window.mainloop()