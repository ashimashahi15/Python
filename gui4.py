import tkinter as tk
from tkinter import PhotoImage

# Create a main window
window = tk.Tk()
# Set window size
window.geometry("420x420")
# Set window title
window.title("first gui program")
# Change window background color to sky blue
window.config(background="white")

#Create a label widget
label = tk.Label(window, text="Hello, world")
#Pack the label into the window
label.place(x=100, y=100)

# Customize the label (font, foreground, background)
label.config(font=("Arial", 40, "bold"), fg="green", bg="black")
# Add a border and padding to the label
label.config(relief="raised", bd=10, padx=20, pady=20)

# Add an image to the label
# First, create a PhotoImage object
photo = PhotoImage(file="fig2.png")
# Set the image in the label
label.config(image=photo, compound='bottom') # 'bottom' aligns the image below the text

def click():
    print("Hello")

# Create a button and pack it into the window
button = tk.Button(window, text="Click me!!")
button.pack()
button.config(command=click) # performs call back of function



window.mainloop()
