import pyttsx3
import PyPDF2

book = open('Software Engineering.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)

speaker = pyttsx3.init()
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()

for num in range(32,pages):
    page = pdfReader.getPage(32)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()