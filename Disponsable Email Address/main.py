# ----- IMPORTING -----
from tkinter import *
from tkinter import messagebox
import requests

# ----- COLORS -----
PINK = "#FFF2CF"

# ----- DISPONSABLE EMAIL -----


def emailchecker():
    try:
        email = entry1.get()
        response = requests.get(url=f"https://api.mailcheck.ai/email/{email}")
        response.raise_for_status()

        disposable = (response.json()["disposable"])
        print(disposable)

    except requests.exceptions.HTTPError:
        print("Bad Request for URL, Check the URL")

    if disposable == True:
        messagebox.showinfo(title="Email Verifier", message=f"The email: {
                            email}\n Was created for one time use.")

    else:
        messagebox.showinfo(title="Email Verifier",
                            message=f"The email: {email}\n Is legit.")

# ----- DISPLAY MESSAGE -----

# def showmessage():


# ----- GUI -----


window = Tk()
window.title("Disponsable Email")

canvas = Canvas(width=600, height=400, bg=PINK)
canvas.grid()

image = PhotoImage(file="Gmail.png")
resized_image = image.subsample(7, 7)
canvas.create_image(300, 80, image=resized_image)

label1 = Label(window, text="Insert The Email",
               font=("Helvetia", 16, "bold"), bg=PINK).place(x=217, y=140)

entry1 = Entry(window, width=35)
entry1.place(x=200, y=190)

button = Button(text="Verify", command=emailchecker,
                width=10).place(x=265, y=220)


window.mainloop()
