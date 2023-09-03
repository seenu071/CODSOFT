from tkinter import *
import string
import random

def generate_password():
    password_length = int(en.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(characters) for _ in range(password_length))
    r.config(text=generated_password)
root = Tk()
root.title("Password Generator")
root.geometry("400x300")
na=Label(root,text="USERNAME")
na.pack()
n=Entry(root)
n.pack()

label=Label(root, text="Password Length:")
label.pack(pady=10)
en =Entry(root)
en.pack()

button = Button(root, text="Generate Password", command=generate_password)
button.pack(pady=10)

r = Label(root, text="", wraplength=300, justify='center', font=("Arial", 14, "bold"))
r.pack()
def accept():
    root.destroy()
    roo=Tk()
    la=Label(text="Password successfully generated",fg='red')
    la.pack()
    roo.mainloop()
b=Button(root,text="Accept",fg="blue", command=accept)
b.pack()
def dec():
    root.destroy()
    roo=Tk()
    la=Label(text="Password generation failed",fg='red')
    la.pack()
    roo.mainloop()
bu=Button(root,text="Decline",fg='blue', command=dec)
bu.pack()

root.mainloop()