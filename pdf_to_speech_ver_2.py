# Python code for converting pdf file to audio file.
#Author: Nishant Thosar
#Date: 24 Nov 2024
#version: 1.5

"""
Whats new:
1) User can now select the pace of speech
2) User can now select the type of voice.
"""

import time #to give some time for opening the mp3 file.
import pypdf
import pyttsx3
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import simpledialog
import threading

import tkinter as tk
from tkinter import messagebox

# Variable to store selected checkbox value
selected_values = {}
#to store the voice value
voice = 0
#variable to store the pace
slider_value = 150

# Function to update the countdown message
def countdown():
    for i in range(len(readpdf.pages), 0, -1):
        label.config(text=f"Please wait... {i} seconds remaining")
        time.sleep(1.5)
    label.config(text="PDF is Successfully converted to MP3 file")
    
    # Close the GUI after countdown
    root.after(1000, root.destroy)  # Destroy the root window after 1 second

def open_dialog_with_slider_and_checkbox(options):
    # Create a new window (dialog)
    
    dialog = tk.Toplevel()
    dialog.title("Select an Option and Value")
    
    # Add a label for the slider
    label_slider = tk.Label(dialog, text="Select a value between 150 and 300:")
    label_slider.pack(pady=10)

    # Add a slider (scale widget)
    slider = tk.Scale(dialog, from_=150, to=300, orient="horizontal")
    slider.pack(pady=10)

   

    # Create checkboxes for each option in the list
    for option, value in options.items():
        selected_values[option] = tk.IntVar()
        checkbox = tk.Checkbutton(dialog, text=option, variable=selected_values[option], onvalue=1, offvalue=0)
        checkbox.pack(anchor="w", padx=20, pady=5)

    # Function to handle the submit action
    def on_submit():
        # Add a label to show the "Wait..." message after submit
        wait_label = tk.Label(dialog, text="Now close this wondow")
        wait_label.pack(pady=10)
        for option, value in selected_values.items():
            if value.get() == 1:
                # selected_option = option
                voice = 1
                break
            else:
                voice = 0
                break
        slider_value = slider.get()
        
    # Submit button to confirm the selection
    submit_button = tk.Button(dialog, text="Submit", command=on_submit)
    submit_button.pack(pady=10)

    # Wait for the user to close the dialog
    dialog.wait_window()


# Main application window (optional, can stay hidden)
root = tk.Tk()
root.withdraw()  # Hide the main window

# Array of strings with their corresponding internal values (1 or 0)
options = {
    "Microsoft Zira Desktop": 1,
    "Microsoft David Desktop": 0
}



# Open dialog with both slider and checkboxes
open_dialog_with_slider_and_checkbox(options)


f = askopenfilename(title="Select PDF file", filetypes=[("PDF files", "*.pdf")])

print("Got your file it might take sevral minutes depending on the input pdf file")
print(f"Rate of speech: {slider_value}")
print(f"Selected speech option: {voice}")

with open(f, "rb") as readfile:  
    readpdf = pypdf.PdfReader(readfile) 
    i=0
    Text = ""
    while i<len(readpdf.pages): 
        page = readpdf.pages[i] 
        Text+=page.extract_text() 
        i+=1

s = pyttsx3.init() #initalize the text to speech engine.
s.setProperty('rate', slider_value)
s.setProperty('volume', 1)

v = s.getProperty('voices')
s.setProperty('voice', v[voice].id) # v[0] for male voice

# Create the main window
root = tk.Tk()
root.title("Wait Dialog")

# Create a label to display the countdown message
label = tk.Label(root, text="Please wait... 5 seconds remaining", font=("Helvetica", 14))
label.pack(pady=20)


# s.say(Text) #enable this to hear the output
s.save_to_file(Text, "E:\\python_programming\\Text to speech converter\\Pdf2Speech.mp3")
s.runAndWait()

# Start the countdown in a separate thread to avoid blocking the main loop
thread = threading.Thread(target=countdown)
thread.start()

# Run the GUI main loop
root.mainloop()



