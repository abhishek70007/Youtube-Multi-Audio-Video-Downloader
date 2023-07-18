#program is written and maintained by Abhishek_Bhattacharya
#version- beta(1.00)
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube
import random



SAVE_PATH="E:/soft-files"


def yt_getlink():
    global link
    link = input.get()
    try:
        yt = YouTube(link)
        yt_download_video()

    except:
        messagebox.showerror("Connection Info", "Connection Establishment Failed!")
    #label.config(text=str + " downloaded")

def yt_get_pathchange():
    #root.withdraw()
    global SAVE_PATH
    SAVE_PATH = filedialog.askdirectory()

def video_with_audio():
    global link
    link = input.get()
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()
    num = random.randint(0, 9999999)
    num1 = random.randint(-99999999,99999997)
    title = yt.title.replace("|","")
    ys.download(SAVE_PATH,filename="video-playback-withAV"+"[ "+title+" ]"+str(num)+str(yt.views)+str(num1)+".mp4")
    messagebox.showinfo("Download Info", "File Downloaded!")

def video_without_audio():
    yt = YouTube(link)
    ys = yt.streams.filter(adaptive=True)
    num = random.randint(0, 9999999)
    num1 = random.randint(-99999999, 99999997)
    title = yt.title.replace("|", "")
    ys[0].download(SAVE_PATH,filename="video-playback-withNAV"+"[ "+title+" ]"+str(num)+str(yt.views)+str(num1)+".mp4")
    messagebox.showinfo("Download Info", "File Downloaded!")

def only_audio():
    global link
    link = input.get()
    yt = YouTube(link)
    ys=yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first()
    #ys=yt.streams.filter(only_audio=True)
    num = random.randint(0, 9999999)
    num1 = random.randint(-99999999, 99999997)
    title = yt.title.replace("|", "")
    ys.download(SAVE_PATH,filename="video-playback-withANV"+"[ "+title+" ]"+str(num)+str(yt.views)+str(num1)+".mp3")
    messagebox.showinfo("Download Info", "File Downloaded!")




def yt_download_video():
    global link
    link = input.get()
    yt = YouTube(link)
    subroot = Tk()
    subroot.geometry("700x420")
    subroot.iconbitmap('icon1.ico')
    subroot.title("YT MULTI Download Request")
    global l1, l2, l3, l4
    l1 = Label(subroot, text="Title: " + yt.title, font=("Helvetica", 14,'bold'), fg="red", anchor='w')
    l2 = Label(subroot, text="Views: " + str(yt.views),font=("Helvetica", 14), fg="green", anchor='w')
    l3 = Label(subroot, text="Length of Video: " + str(yt.length) + " seconds",font=("Helvetica", 14),fg="magenta", anchor='w')
    l4 = Label(subroot, text="Ratings: " + str(yt.rating), font=("Helvetica", 14), fg="blue", anchor='w')
    l1.pack(fill='both')
    l2.pack(fill='both')
    l3.pack(fill='both')
    l4.pack(fill='both')
    Label(subroot,text="      ",font=("arial",9)).pack()
    Button(subroot,text="Download the Video! with Audio [720P]",font=("Verdana",14,'bold'),pady=20,command=video_with_audio,fg="yellow",bg="#8B19DA").pack(fill='x',pady=(0,7))
    Button(subroot, text="Download the Video! without Audio [HQ]",font=("Verdana",14,'bold'),pady=20,command=video_without_audio,fg="#F90858",bg="#25EC73").pack(fill='x',pady=(0,7))
    Button(subroot, text="Download only Audio without Video [mp3]",font=("Verdana",14,'bold'),pady=20,command=only_audio,fg="#CAF908",bg="black").pack(fill='x')

root = Tk()
root.geometry("700x420")
root.iconbitmap('icon1.ico')
root.title(" YT Video-Audio Downloader by c0DeV")
title = Label(root,text="YOUTUBE VIDEO/AUDIO DOWNLOADER",font=("Arial",23),anchor='center',fg="red")
input = Entry(root,width = 100 , borderwidth=2 , justify='center',bd=3,font=("Microsoft Sans Serif",13),fg="#3C3245")
space_1=Label(root,text="           ",font=("Arial",75),justify='center')
space_2=Label(root,text="           ",font=("Arial",70),justify='center')
sub_title_1 = Label(root,text="Enter the Youtube Video/Audio Link",anchor='w',font=("Segoe UI Semibold",10,'bold'),fg="blue")
button_download = Button(root , text = "Download" ,font=("Verdana",14,'bold'), padx=40 , pady=20, command=yt_getlink,foreground='#CAFB22', background='#F90858',activeforeground='red', activebackground='blue')
button_pathlink = Button(root , text = "Choose Directory To Save" ,font=("Verdana",14,'bold'), padx=40 , pady=20,command=yt_get_pathchange,foreground='black', background='#F39E29',activeforeground='red', activebackground='blue')
label=Label(root, text = "")
title.pack(fill='both',expand=True)
space_1.pack(fill='both',expand=True)
sub_title_1.pack()
input.pack(fill=X,expand=True)
Label(root, text = "          ",font=("arial",15)).pack()
button_download.pack(fill='x',pady=10)
button_pathlink.pack(fill='x')
label.pack(pady=20)
root.mainloop()
