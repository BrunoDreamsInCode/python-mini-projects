from tkinter import *

# Function to convert miles to kilometers
def convert_miles_to_km():
    miles = float(mile_input.get())
    km = miles * 1.609
    result.config(text=f"{km}")

# Create main window
window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

# Input field for miles
mile_input = Entry(width=7)
mile_input.grid(column=1, row=0)

# Labels
miles = Label(text="Miles")
miles.grid(column=2, row=0)

is_equal_to = Label(text="Is equal to")
is_equal_to.grid(column=0, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

km = Label(text="KM")
km.grid(column=2, row=1)

# Button to trigger conversion
button2 = Button(text="Calculate", command=convert_miles_to_km)
button2.grid(column=1, row=2)

# Keep window open
window.mainloop()