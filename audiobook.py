# importing pyttsx3 and PyPDF2 


import PyPDF2
import pyttsx3

Engine = pyttsx3.init()
PDF_Reader = PyPDF2.PdfFileReader(open("D:\\PYTHON BASIC PROJECTS\\AUDIO BOOK\\JAS.pdf", "rb"))
for Page_num in range(PDF_Reader.numPages):
    Text = PDF_Reader.getPage(Page_num).extract_text()
    Engine.say(Text)
    Engine.runAndWait()
    Engine.save_to_file(Text, "audio.mp3")
    Engine.runAndWait()


