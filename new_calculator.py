from tkinter import *
#functions
def clear():
    textfield.delete(0,END)

def click_btn_function(event):
    b = event.widget
    text = b['text']
    print(text)

    if text == "=":

        ex = textfield.get()
        answer = eval(ex)
        textfield.delete(0,END)
        textfield.insert(0,answer)
        return

    textfield.insert(END, text)

f = ('Verdana', 80 , 'bold')
window = Tk() 
window.title("Calculator by Mohit")
window.geometry("740x520")

#Label name
name = Label(window, text="Calculator", font="lucida 20 bold")
name.pack(side=TOP,pady = 6)

#text enter
textfield = Entry(window, font = f, justify = RIGHT)
textfield.pack(side = TOP,pady = 2,padx=8)

#button 

b_frame = Frame(window)
b_frame.pack(side=TOP)

temp = 1
for i in range(0,3):
    for j in range(0,3):
        btn= Button(b_frame, text=str(temp), font="lucida 50 bold",width = 5, relief='solid')
        btn.grid(row=i,column=j,padx=3 , pady=3)
        temp+=1
        btn.bind('<Button-1>',click_btn_function)


dot = Button(b_frame, text=".", font="lucida 50 bold",width = 5, relief='solid')
dot.grid(row=3,column=0,padx=3 , pady=3)

zerobtn = Button(b_frame, text="0", font="lucida 50 bold",width = 5, relief='solid')
zerobtn.grid(row=3,column=1,padx=3 , pady=3)

div = Button(b_frame, text="/", font="lucida 50 bold",width = 5, relief='solid')
div.grid(row=3,column=2,padx=3 ,pady=3)

cancel = Button(b_frame, text="C", font="lucida 50 bold",width = 5, relief='solid', command = clear)
cancel.grid(row=0,column=3,padx=3 ,pady=3)

add = Button(b_frame, text="+", font="lucida 50 bold",width = 5, relief='solid')
add.grid(row=1,column=3,padx=3 , pady=3)

sub = Button(b_frame, text="-", font="lucida 50 bold",width = 5, relief='solid')
sub.grid(row=2,column=3,padx=3 , pady=3)

mul = Button(b_frame, text="*", font="lucida 50 bold",width = 5, relief='solid')
mul.grid(row=3,column=3,padx=3 ,pady=3)

equal = Button(b_frame, text="=", font="lucida 50 bold",width = 22, relief='solid')
equal.grid(row=4,column=0, columnspan=4, )

#binding button

dot.bind('<Button-1>',click_btn_function)
zerobtn.bind('<Button-1>',click_btn_function)
div.bind('<Button-1>',click_btn_function)
cancel.bind('<Button-1>',click_btn_function)
add.bind('<Button-1>',click_btn_function)
sub.bind('<Button-1>',click_btn_function)
mul.bind('<Button-1>',click_btn_function)
equal.bind('<Button-1>',click_btn_function)


window.mainloop()