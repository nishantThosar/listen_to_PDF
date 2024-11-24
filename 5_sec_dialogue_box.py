import tkinter as tk
import time
import threading

# Function to update the countdown message
def countdown():
    for i in range(5, 0, -1):
        label.config(text=f"Please wait... {i} seconds remaining")
        time.sleep(1)
    label.config(text="Time's up!")

# Create the main window
root = tk.Tk()
root.title("Wait Dialog")

# Create a label to display the countdown message
label = tk.Label(root, text="Please wait... 5 seconds remaining", font=("Helvetica", 14))
label.pack(pady=20)

# Start the countdown in a separate thread to avoid blocking the main loop
thread = threading.Thread(target=countdown)
thread.start()

# Run the GUI main loop
root.mainloop()
