from tkinter import *
from tkinter import ttk  # For combobox
from pytube import YouTube
import os

root = Tk()
root.geometry('600x400')
root.resizable(0,0)
root.title("Scorpion-youtube video downloader")

Label(root, text='Youtube Video Downloader', font='algerian 22 italic').pack()

# Enter link
link = StringVar()
Label(root, text='Paste Link Here:', font='algerian 15 italic').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)

# Format selection
format_var = StringVar()
format_var.set("MP4")  # default value
Label(root, text='Select Format:', font='algerian 15 italic').place(x=160, y=120)
format_menu = ttk.Combobox(root, textvariable=format_var, values=["MP4", "MP3"])
format_menu.place(x=32, y=150)

# Quality selection
quality_var = StringVar()
quality_var.set("High")  # default value
Label(root, text='Select Quality:', font='algerian 15 italic').place(x=320, y=120)
quality_menu = ttk.Combobox(root, textvariable=quality_var, values=["High", "Medium", "Low"])
quality_menu.place(x=320, y=150)

def Downloader():
    url = YouTube(str(link.get()))
    if format_var.get() == "MP4":
        if quality_var.get() == "High":
            video = url.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        elif quality_var.get() == "Medium":
            video = url.streams.filter(progressive=True, file_extension='mp4').get_by_resolution("720p")
        else:  # Low
            video = url.streams.filter(progressive=True, file_extension='mp4').get_lowest_resolution()
    else:  # MP3
        video = url.streams.filter(only_audio=True).first()
        # Download and save as MP4 then convert to MP3 as PyTube does not directly download MP3
    download_path = video.download()
    if format_var.get() == "MP3":
        base, ext = os.path.splitext(download_path)
        new_file = base + '.mp3'
        os.rename(download_path, new_file)  # Rename the file to MP3
        download_path = new_file  # Update download_path to reflect the new file
    Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=280)

Button(root, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=2, command=Downloader).place(x=180, y=210)

root.mainloop()
