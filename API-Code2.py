import tkinter as Tinty
from PIL import Image, ImageTk
import requests
from tkinter import messagebox



window = Tinty.Tk()
window.configure(bg= "white")
window.title("NUTRITION")

Nutrition_label = Tinty.Label(window, font = ("Times New Roman", 14), justify = "left", bg= "white", text= "Nutrition is about eating a healthy and balanced diet. Food and drink provide the energy and nutrients you need to be healthy." "\n" "Understanding these nutrition terms may make it easier for you to make better food choices. You can easily get some" "\n" "information regarding the kind of food you eat and the amount of nutrients found in it by entering the kind of food you eat in the box below.")
Nutrition_label.place(x= 8, y=15)

Food_label = Tinty.Label(window, justify= "left", text="Enter the name of food you want to have information about:", font= ("Times New Roman", 14), bg= "white")
Food_label.place(x=20, y=150)

Text_Entry = Tinty.Entry(window, font=("Times New Roman", 14), fg= "black", bg = "white", relief="groove")
Text_Entry.place(x=8,y=200, height= 150, width= 460)

txtbox = Tinty.Text(window, font = ("Times New Roman", 14), relief= "groove", bg = "green")
txtbox.place(x= 530, y=150)

def store_input():
    word = Text_Entry.get()
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(word)
    response = requests.get(api_url, headers={'X-Api-Key': 'COPPW1S/OA8pVTHL3frRkg==CyGz60wdlNbvRxek'})
    if response.status_code == requests.codes.ok:
        Answer_Textbox= response.text
        txtbox.delete("1.0", Tinty.END)
        txtbox.insert(Tinty.END, Answer_Textbox)
    if word.isdigit():
        messagebox.showwarning("Enter alpha characters only")
    else:
        messagebox.showinfo("Error in fetching food info")

def Previous_Window():
    window.deiconify()
    window.destroy()


Enter_button = Tinty.Button(window, text= "Next", font= ("Times New Roman", 13), relief= "raised", command= store_input)
Enter_button.place(x=20, y= 360)
Exit_button = Tinty.Button(window, text= "Exit", font= ("Times New Roman", 13), relief= "raised", command=Previous_Window)
Exit_button.place(x=140, y= 360) 


window.mainloop()

