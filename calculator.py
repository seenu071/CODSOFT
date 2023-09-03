from tkinter  import *
cal = Tk()
cal.title("CALCULATOR")
cal.geometry("600x700")
cal.configure(bg="grey")
def click2(event):
    global value
    text2 = event.widget.cget("text")
    if screenValue.get().isdigit():
        int(display.update())
    square = (int(screenValue.get()) * int(screenValue.get()))
    cube = (int(screenValue.get()) * int(screenValue.get()) * int(screenValue.get()))
    if text2 == "x²":
        screenValue.set(square)
        
    elif text2 == "x³":
        screenValue.set(cube)
def click(event):
    
    global screenValue
    text = event.widget.cget("text")
               
    if text == "=":

        if screenValue.get().isdigit():
            value = int(screenValue.get())

        else:
            try:
                value = eval(screenValue.get())
            
            except Exception as e:
                value= "ERROR"

        screenValue.set(value)
        display.update()

    elif text == "C":
        screenValue.set(" ")

    else:
        screenValue.set(str(screenValue.get()) + str(text))
        display.update()

screenValue = StringVar()

screenValue.set(" ")

display = Entry(cal, textvariable=screenValue, bg='white',font="arial 38", relief=RIDGE)
display.pack(pady=50,padx=20)



button = Button(cal, text="C", font="lucida 20 bold", height=2, width=5, bd=2, fg="blue")
button.place(x=2, y=120)
button.bind("<Button-1>", click)

button = Button(cal, text="%", font="lucida 20 bold", height=2, width=5, bd=2, fg="blue")
button.place(x=108, y=120)
button.bind("<Button-1>", click)

button = Button(cal, text="x²", font="lucida 20 bold", height=2, width=5, bd=2, fg="blue")
button.place(x=212, y=120)
button.bind("<Button-1>", click2)

button = Button(cal, text="x³", font="lucida 20 bold", height=2, width=5, bd=2, fg="blue")
button.place(x=317, y=120)
button.bind("<Button-1>", click2)

button = Button(cal, text="+", font="lucida 20 bold", height=2, width=8, bd=2, fg="blue")
button.place(x=419, y=120)
button.bind("<Button-1>", click)


button = Button(cal, text="9", font="lucida 20 bold", height=2, width=7, bd=2, fg="black")
button.place(x=3, y=220)
button.bind("<Button-1>", click)

button = Button(cal, text="8", font="lucida 20 bold", height=2, width=7, bd=2, fg="black")
button.place(x=140, y=220)
button.bind("<Button-1>", click)

button = Button(cal, text="7", font="lucida 20 bold", height=2, width=7, bd=2, fg="black")
button.place(x=278, y=220)
button.bind("<Button-1>", click)

button = Button(cal, text="-", font="lucida 20 bold", height=2, width=8, bd=2, fg="blue")
button.place(x=420, y=220)
button.bind("<Button-1>", click)

button = Button(cal, text="6", font="lucida 20 bold", height=2, width=7, bd=2, fg="black")
button.place(x=3, y=320)
button.bind("<Button-1>", click)

button = Button(cal, text="5", font="lucida 20 bold", height=2, width=7, bd=2, fg="black")
button.place(x=140, y=320)
button.bind("<Button-1>", click)

button = Button(cal, text="4", font="lucida 20 bold", height=2, width=7, bd=2, fg="black")
button.place(x=278, y=320)
button.bind("<Button-1>", click)

button = Button(cal, text="*", font="lucida 20 bold", height=2, width=8, bd=2, fg="blue")
button.place(x=420, y=320)
button.bind("<Button-1>", click)

button = Button(cal, text="3", font="lucida 20 bold", height=2, width=7, bd=2, fg="black")
button.place(x=3, y=420)
button.bind("<Button-1>", click)

button = Button(cal, text="2", font="lucida 20 bold", height=2, width=7, bd=2, fg="black")
button.place(x=140, y=420)
button.bind("<Button-1>", click)

button = Button(cal, text="1", font="lucida 20 bold", height=2, width=7, bd=2, fg="black")
button.place(x=278, y=420)
button.bind("<Button-1>", click)

button = Button(cal, text="/", font="lucida 20 bold", height=2, width=8, bd=2, fg="blue")
button.place(x=420, y=420)
button.bind("<Button-1>", click)

button = Button(cal, text="=", font="lucida 20 bold", height=2, width=8, bd=2, fg="blue")
button.place(x=420, y=518)
button.bind("<Button-1>", click)

button = Button(cal, text=".", font="lucida 20 bold", height=2, width=7, bd=2, fg="blue")
button.place(x=275, y=518)
button.bind("<Button-1>", click)

button = Button(cal, text="0", font="lucida 20 bold", height=2, width=15, bd=2, fg="blue")
button.place(x=3, y=518)
button.bind("<Button-1>", click)

cal.mainloop()