# Python code for converting pdf file to audio file.
#Author: Nishant Thosar
#Date: 24 Nov 2024
#version: 1

import time #to give some time for opening the mp3 file.
import pypdf
import pyttsx3
from tkinter.filedialog import askopenfilename

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
s.setProperty('rate', 150)
s.setProperty('volume', 1)

v = s.getProperty('voices')
s.setProperty('voice', v[1].id) # v[0] for male voice

# s.say(Text) #enable this to hear the output
s.save_to_file(Text, "E:\\python_programming\\Text to speech converter\\Pdf2Speech.mp3")
s.runAndWait()

start_time = time.time()
while time.time() - start_time < 20:
    current_time = time.time()
    elapsed_time = current_time - start_time
    elapsed_seconds = int(elapsed_time)
    print("Wait until the timer is over.")
    print(elapsed_seconds, end= '\t')
    time.sleep(1)
print("PDF is Successfully converted to MP3 file")



