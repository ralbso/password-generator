import io
import os
import platform
from email_attendees import *
from tkinter import *
from tkinter import filedialog
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfbase.pdfmetrics import stringWidth

names = {}
quit = False

def show_entry_fields(event=None):
    print("First Name: %s\nLast Name: %s\nEmail: %s\n" % (first.get(), last.get(),email.get()))
    names.update({str(first.get())+" "+str(last.get()):str(email.get())})
    first.delete(0,END)
    last.delete(0,END)
    email.delete(0,END)
    first.focus()

def get_font(event=None):
    global FontName
    global FontSize
    FontName = str(fontName.get())
    FontSize = str(fontSize.get())
    print(FontName)
    print(FontSize)

def choose_font(event=None):
    global FilePath
    global FontName
    global FontSize
    choose = Tk()

    if platform.system() == "Windows":
        choose.filename = filedialog.askopenfile(initialdir = "C:/", title="Select font", filetypes=[("Font file formats",("*.ttf","*.otf","*.fnt"))])
    else:
        choose.filename = filedialog.askopenfilename(initialdir = "~/", title="Select font", filetypes=[("Font file formats",("*.ttf","*.otf","*.fnt"))])

    FilePath = choose.filename
    FontName = str(fontName.get())
    FontSize = str(fontSize.get())
    choose.destroy()


fontDialog = Tk()
Label(fontDialog, text="Font Name").grid(row=0, column=0)
Label(fontDialog, text="Size").grid(row=0, column=2)
fontName = Entry(fontDialog)
fontSize = Entry(fontDialog, width=4)
fontName.grid(row=0, column=1)
fontSize.grid(row=0, column=3)
Button(fontDialog, text="Enter", command=get_font).grid(row=1,column=0,sticky=W+E,pady=4)
Button(fontDialog, text="Select font", command=choose_font).grid(row=1,column=1,sticky=W+E,pady=4)
Button(fontDialog, text="Quit", command=fontDialog.destroy).grid(row=1,column=2,sticky=W+E,pady=4)
fontDialog.bind('<Return>', get_font)


master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)
Label(master, text="Email").grid(row=2)

first = Entry(master)
last = Entry(master)
email = Entry(master)

first.grid(row=0, column=1)
last.grid(row=1, column=1)
email.grid(row=2, column=1)

Button(master, text="Quit", command=master.quit).grid(row=4,column=2,sticky=W+E,pady=4)
Button(master, text="Enter", command=show_entry_fields).grid(row=4,column=0,sticky=W+E,pady=4)
Button(master, text="Select font", command=get_font).grid(row=4,column=1,sticky=W+E,pady=4)

master.bind('<Return>',show_entry_fields)

mainloop()


for name in names:
    packet = io.BytesIO()
    # create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    can.getAvailableFonts()
    try:
        can.setFont(FontName, size=38)
    except:
        pdfmetrics.registerFont(TTFont(FontName,FilePath))
        can.setFont(FontName, size=38)
    can.drawCentredString(400, 300, name)
    can.save()

    #move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open("/Users/Raul/Downloads/Certificate.pdf", "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    outputStream = open("/Users/Raul/Documents/UPRM/ODN/WPRNS/Certificates/certificate "+str(name)+".pdf", "wb")
    output.write(outputStream)
    outputStream.close()

email_attendees(names)
