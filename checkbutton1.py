import tkinter as tk

window =tk.Tk()
window.title("Python tkinter GUI checkboxes easy ✔️")

def display():
    # Define a function to display messages based on checkbox state
    if x.get() == 1:
        # Check if the checkbox is checked
        print("I like Python")
    else:
        print("I don't like Python")
        # Print if the checkbox is not checked

# Create an IntVar variable to store checkbox state
x = tk.IntVar()

# Create a Checkbutton widget with text "Python", linked to variable x,
# onvalue=1 when checked, offvalue=0 when unchecked, and execute 'display' function on state change

checkbox = tk.Checkbutton(window, text="Python", variable=x, onvalue=1, offvalue=0, command=display)
checkbox.pack()
checkbox.config(font=("Arial", 14), fg="blue", bg="white", activeforeground="blue", activebackground="white")





window.mainloop()