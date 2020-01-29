import tkinter as tk
import pytube
def save():
    url = textField.get()
    video = pytube.YouTube(url)
    youtube1 = video.streams.first()
    print(youtube1)
    print("LOC=",location.get())
    var = tk.StringVar()
    label = tk.Message(win, textvariable=var)
    var.set("Download Started Please Check Downloading location")
    label.pack(side=tk.TOP)
    youtube1.download(location.get())

win = tk.Tk()
win.title('Youtube Downloader')
win.geometry('800x200')

l1=tk.Label(win,text="Link Of Youtube Video ")
l1.pack(side=tk.TOP)
# create text field
textFormat=tk.StringVar()
textField = tk.Entry(win, width=100)
textField.pack(fill=tk.NONE, side=tk.TOP)

l2=tk.Label(win,text="Link Of Download location eg: C:\something\something ")
l2.pack(side=tk.TOP)
#create TEXT FIELD for Download Location file
location = tk.Entry(win, width=100)
location.pack(fill=tk.NONE, side=tk.TOP)

# create button to start file
saveBtn = tk.Button(win, text='Start Download', command=save)
saveBtn.pack(expand=tk.FALSE, fill=tk.X, side=tk.TOP)

win.mainloop()