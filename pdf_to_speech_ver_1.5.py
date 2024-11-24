# Python code for converting pdf file to audio file.
#Author: Nishant Thosar
#Date: 24 Nov 2024
#version: 1.5

"""
Whats new:
1) User can now select the pace of speech
"""

import time #to give some time for opening the mp3 file.
import pypdf
import pyttsx3
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import simpledialog

def open_dialog_with_slider():
    # Create a new window
    dialog = tk.Toplevel()
    dialog.title("Select a Value")

    # Add a label
    label = tk.Label(dialog, text="Select a value between 150 and 300:")
    label.pack(pady=10)

    # Add a slider (scale widget)
    slider = tk.Scale(dialog, from_=150, to=300, orient="horizontal")
    slider.pack(pady=10)

    # Variable to store the selected value
    result = {"value": None}

    # Function to close the dialog and save the slider value
    def on_submit():
        result["value"] = slider.get()
        dialog.destroy()

    # Add a submit button
    submit_button = tk.Button(dialog, text="Submit", command=on_submit)
    submit_button.pack(pady=10)

    # Wait for the user to close the dialog
    dialog.wait_window()
    return result["value"]

# Main application window (optional, can stay hidden)
root = tk.Tk()
root.withdraw()  # Hide the main window

# Open a dialog with a slider
selected_value = open_dialog_with_slider()

# Display the selected value
print(f"You selected rate: {selected_value}")


f = askopenfilename(title="Select PDF file", filetypes=[("PDF files", "*.pdf")])

print("Got your file it might take sevral minutes depending on the input pdf file")

with open(f, "rb") as readfile:  
    readpdf = pypdf.PdfReader(readfile) 
    i=0
    Text = ""
    while i<len(readpdf.pages): 
        page = readpdf.pages[i] 
        Text+=page.extract_text() 
        i+=1
s = pyttsx3.init() #initalize the text to speech engine.
s.setProperty('rate', selected_value)
s.setProperty('volume', 1)

v = s.getProperty('voices')
s.setProperty('voice', v[1].id) # v[0] for male voice

# s.say(Text) #enable this to hear the output
s.save_to_file(Text, "E:\\python_programming\\Text to speech converter\\Pdf2Speech.mp3")
s.runAndWait()

start_time = time.time()
while time.time() - start_time < 2:
    current_time = time.time()
    elapsed_time = current_time - start_time
    elapsed_seconds = int(elapsed_time)
    print("Wait until the timer is over.")
    print(elapsed_seconds, end= '\t')
    time.sleep(1)
print("PDF is Successfully converted to MP3 file")



