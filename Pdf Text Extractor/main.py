import tkinter, PyPDF2
from tkinter import filedialog

def openfile():
    filename =filedialog.askopenfilename(title="Open PDF File",
                                         initialdir='F:\PROGRAMMING\MY PROJECTS\PDF TEXT EXTRACTOR',
                                         filetypes=[('pdf files', '*.pdf')])
    print(filename)
    outputfile_text.delete("1.0", tkinter.END)
    reader = PyPDF2.PdfReader(filename)
    for i in range (reader.numPages):
        current_text = reader.getPage(i).extractText()
        outputfile_text.insert(tkinter.END, current_text)
        


root = tkinter.Tk()
root.title("PYTHON TEXT EXTRACTOR")

filename_label = tkinter.Label(root, text="No File Selected")

outputfile_text = tkinter.Text(root)
openfile_button = tkinter.Button(root, text="OPEN PDF FILE", command=openfile)
filename_label.pack()
outputfile_text.pack()
openfile_button.pack()

root.mainloop()