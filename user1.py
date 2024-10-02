import tkinter as tk
window = tk.Tk()
window.title("python tkinter GUI user input Easy")
window.geometry("420x420")

#create an entry widget
entry=tk.Entry(window)
entry.pack()

def submit():
    username = entry.get() #Retrieve text from entry widget
    print(username)

# Function to handle the delete button click
def delete():
    entry.delete(0, 'end')  # Clear all text in the entry widget

def backspace():
    current_text = entry.get()  # Get current text in entry widget
    entry.delete(len(current_text) - 1, 'end')  # Delete last character
    
#create a submit button
submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack(side='right')

# Create a delete button
delete_button = tk.Button(window, text="Delete", command=delete)
delete_button.pack(side='right')  # Align button to the right

# Create a backspace button
backspace_button = tk.Button(window, text="Backspace", command=backspace)
backspace_button.pack(side='right')  # Align button to the right"""

window.mainloop()