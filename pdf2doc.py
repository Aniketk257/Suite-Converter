from pdf2docx import Converter  # Conversion of Pdf to Document
import pyttsx3  # Conversion of Text to Speech
import config
# Initialization of Audio Engine


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Voice Automation
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# String identifier of the active voice
engine.setProperty('voice', voices[1].id)
# Integer speech rate in words per minute, can be increased or decreased to change speed of speech
engine.setProperty('rate', 145)

print("Enter name of your file without extension")
speak("Enter name of your file without extension")
name = input()
# pdf_file = r"C:\Users\Pranav\OneDrive\Desktop\Suite-Converter\Input Directory\\"+name+".pdf"
pdf_file = config.inputpath+name+".pdf"

# docx_file = r'converted.docx'       #declaring docx file name
# declaring docx file name
# address = r"C:\Users\Pranav\OneDrive\Desktop\Suite-Converter\Output Directory\\" + \
#     name+"-converted.docx"
address = config.outputpath+name+"-converted.docx"
docx_file = address

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()  # closed the pdf file

print("Your file has been converted successfully".center(400))
