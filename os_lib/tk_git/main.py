import os
import requests
import tkinter as tk

OWNER = "Kaloyan"

try:
    os.mkdir(OWNER)
except FileExistsError:
    pass

os.chdir(OWNER)

''' for i in files_to_download:
    r = requests.get("https://raw.githubusercontent.com/KokosTech/Python-HW/main/Holiday-HW/" + i)
    with open(i, "wb") as f:
        for i in r.iter_content(chunk_size=8192):
            f.write(i) '''

def download():
    link = get_link.get()
    name = get_name.get()

    r = requests.get(link)
    with open(name, "wb") as f:
        for i in r.iter_content(chunk_size=8192):
            f.write(i)

window = tk.Tk()
window.geometry("500x300")

label = tk.Label(text='Link')
get_link = tk.Entry()
get_name = tk.Entry()
button = tk.Button(text='Download', command=lambda: download())

label.pack()
get_link.pack()
get_name.pack()
button.pack()

window.mainloop()