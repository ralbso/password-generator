__author__ = "Raul Mojica Soto-Albors"
__copyright__ = "Copyright (c) 2019 Raul Mojica Soto-Albors"
__license__ = "MIT License"
__version__ = "1.2.1"

import io
import os
import platform
from tkinter import *
from tkinter import filedialog
from email_attendees import *
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

def select_font(event=None):
    global FilePath
    global FontName
    global FontSize
    choose = Tk()
    choose.title("Font? What font?")

    if platform.system() == "Windows":
        choose.filename = filedialog.askopenfilename(initialdir = "C:/", title="Font? What font?", \
        filetypes=[("Font file formats",("*.ttf","*.otf","*.fnt"))])
    else:
        choose.filename = filedialog.askopenfilename(initialdir = "~/", title="Font? What font?", \
        filetypes=[("Font file formats",("*.ttf","*.otf","*.fnt"))])

    FilePath = choose.filename
    FontName = str(fontName.get())
    FontSize = str(fontSize.get())
    choose.destroy()

def choose_font(event=None):
    global fontName
    global fontSize
    fontDialog = Tk()
    fontDialog.title("Choose your font!")

    Label(fontDialog, text="Font Name").grid(row=0, column=0)
    Label(fontDialog, text="Size").grid(row=0, column=2)
    fontName = Entry(fontDialog)
    fontSize = Entry(fontDialog, width=4)
    fontName.grid(row=0, column=1)
    fontSize.grid(row=0, column=3)
    Button(fontDialog, text="Enter", command=get_font).grid(row=1,column=0,sticky=W+E,pady=4)
    Button(fontDialog, text="Choose file", command=select_font).grid(row=1,column=1,sticky=W+E,pady=4)
    Button(fontDialog, text="Quit", command=fontDialog.destroy).grid(row=1,column=2,columnspan=2,sticky=W+E,pady=4)
    fontDialog.bind('<Return>', get_font)

def choose_template(event=None):
    global TemplatePath
    template = Tk()
    template.title("Choose your template!")

    if platform.system() == "Windows":
        template.filename = filedialog.askopenfilename(initialdir="C:/", title="Choose your template!", \
        filetypes=[("PDF",("*.pdf"))])
    else:
        template.filename = filedialog.askopenfilename(initialdir="~/", title="Choose your template!", \
        filetypes=[("PDF",("*.pdf"))])

    TemplatePath = template.filename
    template.destroy()

def save_file(event=None):
    global SavePath
    save = Tk()
    save.title("Choose destination")

    if platform.system() == "Windows":
        save.filename = filedialog.askdirectory(initialdir="C:/", title="Select directory")
    else:
        save.filename = filedialog.askdirectory(initialdir="~/", title="Select directory")

    SavePath = save.filename
    print(SavePath)
    save.destroy()

def master(event=None):
    global first
    global last
    global email

    master = Tk()
    master.title("Certificate Generator 3000")

    Label(master, text="First Name").grid(row=0)
    Label(master, text="Last Name").grid(row=1)
    Label(master, text="Email").grid(row=2)
    Label(master, text=__copyright__).grid(row=5, columnspan=5)

    first = Entry(master, width=30)
    last = Entry(master, width=30)
    email = Entry(master, width=30)

    first.grid(row=0, column=1, columnspan=5)
    last.grid(row=1, column=1, columnspan=5)
    email.grid(row=2, column=1, columnspan=5)

    Button(master, text="Enter", command=show_entry_fields).grid(row=4,column=0,sticky=W+E,pady=4)
    Button(master, text="Select font", command=choose_font).grid(row=4,column=1,sticky=W+E,pady=4)
    Button(master, text="Select template", command=choose_template).grid(row=4,column=2,sticky=W+E,pady=4)
    Button(master, text="Save in", command=save_file).grid(row=4, column=3,sticky=W+E,pady=4)
    Button(master, text="Quit", command=master.quit).grid(row=4,column=4,sticky=W+E,pady=4)

    master.bind('<Return>',show_entry_fields)

    mainloop()

master()

for name in names:
    packet = io.BytesIO()
    # create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    can.getAvailableFonts()
    try:
        can.setFont(FontName, size=FontSize)
    except:
        pdfmetrics.registerFont(TTFont(FontName,FilePath))
        can.setFont(FontName, size=FontSize)
    can.drawCentredString(400, 300, name)
    can.save()

    #move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open(TemplatePath, "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    loc = SavePath+"/certificate "+str(name)+".pdf"
    outputStream = open(loc, "wb")
    output.write(outputStream)
    outputStream.close()

email_attendees(names, loc)
