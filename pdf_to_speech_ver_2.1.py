# Python code for converting pdf file to audio file.
#Author: Nishant Thosar
#Date: 24 Nov 2024
#version: 2.1

"""
Whats new:
1) User can now select the pace of speech
2) User can now select the type of voice.
3) Performance improvement
"""

import time  # to give some time for opening the mp3 file.
import pypdf
import pyttsx3
import tkinter as tk
from tkinter.filedialog import askopenfilename
import threading

# Variable to store selected checkbox value
selected_values = {}
voice = 0  # To store the voice value
slider_value = 150  # Variable to store the pace

# Function to update the countdown message
def countdown(label, root):
    for i in range(len(readpdf.pages), 0, -1):
        label.config(text=f"Please wait... {i} seconds remaining")
        time.sleep(1.5)
    label.config(text="PDF is Successfully converted to MP3 file")
    root.after(2000, root.quit)  # Quit the main loop after 2 seconds

def open_dialog_with_slider_and_checkbox(root, options):
    dialog = tk.Toplevel(root)
    dialog.title("Select an Option and Value")

    global slider_value, voice

    # Slider label and widget
    tk.Label(dialog, text="Select a value between 150 and 300:").pack(pady=10)
    slider = tk.Scale(dialog, from_=150, to=300, orient="horizontal")
    slider.pack(pady=10)

    # Checkboxes
    for option in options:
        selected_values[option] = tk.IntVar()
        checkbox = tk.Checkbutton(dialog, text=option, variable=selected_values[option])
        checkbox.pack(anchor="w", padx=20, pady=5)

    # Function to handle the submit action
    def on_submit():
        global slider_value, voice  # Declare global variables
        for option, value in selected_values.items():
            if value.get() == 1:  # Check which voice option is selected
                voice = options[option]
                break
        slider_value = slider.get()  # Get the selected speech rate
        dialog.destroy()  # Close the dialog window

    # Submit button
    tk.Button(dialog, text="Submit", command=on_submit).pack(pady=10)

    dialog.wait_window()  # Wait for the user to close the dialog

# Main application window
root = tk.Tk()
root.withdraw()  # Hide main window initially

# Voice options
options = {
    "Microsoft Zira Desktop": 1,
    "Microsoft David Desktop": 0
}

# Open dialog to select voice and speed
open_dialog_with_slider_and_checkbox(root, options)

# File selection
f = askopenfilename(title="Select PDF file", filetypes=[("PDF files", "*.pdf")])
if not f:
    print("No file selected. Exiting.")
    exit()

print("Got your file; it might take several minutes depending on the input PDF file.")
print(f"Rate of speech: {slider_value}")
print(f"Selected speech option: {voice}")

# PDF reading
with open(f, "rb") as readfile:
    readpdf = pypdf.PdfReader(readfile)
    text = "".join(page.extract_text() for page in readpdf.pages)

# Text-to-speech setup
s = pyttsx3.init()
s.setProperty("rate", slider_value)
s.setProperty("volume", 1)
v = s.getProperty("voices")
s.setProperty("voice", v[voice].id)
s.save_to_file(text, "Pdf2Speech.mp3")
s.runAndWait()

# Create countdown window
root.deiconify()  # Show main window
root.title("Wait Dialog")
label = tk.Label(root, text="Please wait... Processing", font=("Helvetica", 14))
label.pack(pady=20)

# Countdown in a separate thread
thread = threading.Thread(target=countdown, args=(label, root))
thread.start()

root.mainloop()
thread.join()  # Wait for the thread to finish
