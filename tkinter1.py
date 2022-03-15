import tkinter

Tk= tkinter.Tk()

canvas1 = tkinter.Canvas(Tk, width = 300, height = 300)
canvas1.pack()

def hello ():  
    label1 = tkinter.Label(Tk, text= 'Hello World!', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    
button1 = tkinter.Button(text='Click Me',command=hello, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

Tk.mainloop()