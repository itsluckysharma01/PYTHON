import tkinter
import pyshorteners


def shorten():
    shortner = pyshorteners.Shortener()
    short_url = shortner.tinyurl.short(longurl_entry.get())
    shorturl_entry.insert(0, short_url)
  

root = tkinter.Tk()
root.title("URL SHORTNER")
root.geometry("400x190")
root.configure(bg='purple')



head_label = tkinter.Label(root, text="URL SHORTNER",  font=("Arial",25), bg="red")


longurl_label = tkinter.Label(root, text="Enter Long URL",  bg='purple', fg='white',font=("Aeial",15))
longurl_entry = tkinter.Entry(root, width=40) 
shorturl_label = tkinter.Label(root , text="Output Shortened URL",  bg='purple', fg='white', font=("Aeial",15) )
shorturl_entry = tkinter.Entry(root, width=40)
shorten_button = tkinter.Button(root,  text="SHORTEN",bg="#FF3399", width=15, height=2,activebackground="yellow" ,fg="#FFFFFF",command=shorten)

head_label.pack()
longurl_label.pack()
longurl_entry.pack()
shorturl_label.pack()
shorturl_entry.pack()
shorten_button.pack()


root.mainloop()