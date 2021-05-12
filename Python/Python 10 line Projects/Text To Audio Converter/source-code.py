import pyttsx3
import PyPDF2
book=open('File-Name.pdf', 'rb')
pdfreader=PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages
#print(pages)
speaker=pyttsx3.init()
page=pdfreader.getPage(0)
text=page.extractText()
speaker.say(text)
speaker.runAndWait()
