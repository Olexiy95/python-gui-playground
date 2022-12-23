import tkinter as tk

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

# Create the main window
window = tk.Tk()
window.title("Celsius to Fahrenheit Converter")
window.geometry("500x500")

# Create a label and text entry for the Celsius input
celsius_label = tk.Label(text="Enter temperature in Celsius:")
celsius_entry = tk.Entry()

# Create a function to be called when the "Convert" button is clicked
def convert_button_clicked():
    # Get the temperature in Celsius from the entry
    celsius = float(celsius_entry.get())

    # Convert the temperature to Fahrenheit
    fahrenheit = celsius_to_fahrenheit(celsius)

    # Update the label with the result
    result_label.config(text=f"{fahrenheit:.2f} Fahrenheit")

# Create a button to trigger the conversion
convert_button = tk.Button(text="Convert", command=convert_button_clicked)

# Create a label to display the result
result_label = tk.Label(text="")

# Add the widgets to the window
celsius_label.pack()
celsius_entry.pack()
convert_button.pack()
result_label.pack()

# Run the main loop
window.mainloop()
