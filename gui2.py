import tkinter as tk
from tkinter import PhotoImage

#Create a tkinter window
window = tk.Tk()          
window.title("Learn Python tkinter labels easy 🏷️")

#Create a label widget
label = tk.Label(window, text="Hello, world")
#Pack the label into the window
#label.pack()
label.place(x=100, y=100)

# Customize the label (font, foreground, background)
label.config(font=("Arial", 40, "bold"), fg="green", bg="black")

# Add a border and padding to the label
label.config(relief="raised", bd=10, padx=20, pady=20)

# Add an image to the label
# First, create a PhotoImage object
photo = PhotoImage(file="fig2.png")
# Set the image in the label
label.config(image=photo, compound='bottom')  # 'bottom' aligns the image below the text

window.mainloop()