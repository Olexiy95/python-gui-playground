import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Simple GUI")

# Create a function to be called when the button is clicked
def say_hello():
    tk.Label(text="Hello, World!").pack()

# Create a button and specify the function to be called when it is clicked
tk.Button(text="Click me", command=say_hello).pack()

# Run the GUI
window.mainloop()
