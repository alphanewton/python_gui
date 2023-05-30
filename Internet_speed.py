from tkinter import *
import speedtest

def speedCheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    downloading = str(round(sp.download()/(10**6),3))+" Mbps"
    uploading = str(round(sp.upload()/(10**6),3))+" Mbps"
    lab_down.config(text=downloading)
    lab_up.config(text=uploading)

sp = Tk()
sp.title("Newton's Internet Speed Test ")
sp.geometry("500x700")
sp.config(bg="Black")

lab = Label(sp, text = "Internet Speed Test", font=("Time New Roman", 40, "bold"),bg="Black", fg="White")
lab.place(x=60, y=40, height=50, width=380)

lab = Label(sp, text = "Download Speed", font=("Time New Roman", 40, "bold"),bg="Black", fg="Blue")
lab.place(x=60, y=130, height=50, width=380)

lab_down = Label(sp, text = "00", font=("Time New Roman", 40, "bold"),bg="Black", fg="Blue")
lab_down.place(x=60, y=200, height=50, width=380)

lab = Label(sp, text = "Upload Speed ", font=("Time New Roman", 40, "bold"),bg="Black", fg="Green")
lab.place(x=60, y=290, height=50, width=380)

lab_up = Label(sp, text = "00", font=("Time New Roman", 40, "bold"),bg="Black", fg="Green")
lab_up.place(x=60, y=360, height=50, width=380)

button = Button(sp, text = "TEST SPEED", font=("Time New Roman",40,"bold"), relief=RAISED, bg="Red", command=speedCheck)
button.place(x=60, y=460, height=50, width=380)

sp.mainloop()
