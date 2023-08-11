import tkinter as Tinty
from PIL import Image, ImageTk
import subprocess

window = Tinty.Tk()
window.configure(bg= "white")
window.title("MY HEALTH MY LIFE")
icon = Tinty.PhotoImage(file= "tivia3.png")
window.iconphoto(True,icon)


welcome_label = Tinty.Label(window, text= "WELCOME TO THE NUTRITION HUB:", font= ("Arial Black", 35), bg= "white", fg= "green", justify= "center", relief= "ridge")
welcome_label.place(x=100, y=30)

image = Image.open("nutrition2.png")
photo = ImageTk.PhotoImage(image)
image_label = Tinty.Label(window, image=photo, bg= "white")
image_label.place(x=10,y=100, height= 700, width= 800)

Text_show = Tinty.Label(window, text = "Please click 'Next' to continue and 'Exit' to close the page", bg= "white", font= ("Times New Roman",15))
Text_show.place(x=850, y= 220)

def run_script():
    return(subprocess.Popen(["python", "API-Code2.py"]))

Next_Button = Tinty.Button(window, text= "Next", bg="green", font = ("Times New Roman", 20), borderwidth= 4, relief = "raised", command= run_script)
Next_Button.place(x= 980, y= 300)


def Exit_Page():
    window.destroy()

Cancel_Button= Tinty.Button(window, text= "Exit", bg= "green", font = ("Times New Roman", 20), borderwidth= 4, relief = "raised", command = Exit_Page)
Cancel_Button.place(x=980, y=450)


window.mainloop()

    

