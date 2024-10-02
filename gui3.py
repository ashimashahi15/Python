import tkinter as tk

# Step 1: Create the main window
window = tk.Tk()

#def click():
   #print("Hello")

# Project: Counting button clicks
count = 0

#def click():
    #global count
    #count += 1
    #print(count)  # For demonstration, prints count to console

def click():
    global count
    count += 1
    label.config(text=str(count))

# Create a button and pack it into the window
button = tk.Button(window, text="Click me!!")
button.pack()
button.config(command=click) # performs call back of function

# Customize button appearance
button.config(font=("Ink Free", 50, "bold"),  # Change font style and size
              bg="#FF4500",  # Change background color to orangish-red
              fg="#FFFF00")  # Change foreground (text) color to bright neon yellow

# Add an image to the button
image = tk.PhotoImage(file="fig2.png")  # Replace with your image path
button.config(image=image, compound='bottom')



# Create a label to display count
label = tk.Label(window, text="0", font=("Arial", 50))
label.pack()

window.mainloop()