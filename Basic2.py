from tkinter import *
from tkinter.ttk import *


context = ''


root =  Tk()
root.title("Caly")
root.eval("tk::PlaceWindow . center")


style = Style()

style.configure("TButton", font=(None,10), background="#5b8269")
style.configure("TFrame", font=(None,10), background="red")
style.configure("TLabel", font=(None,10), background="#f0eed1")
style.configure("flex_sep.TLabel", font=(None,10), background="#a6a5a1")





screen = Entry(root, font= (None,36), justify=RIGHT)
# screen.pack()
screen.pack(fill=X)

label = Label(root, text='0', font=(None,36), anchor=E)
label.pack(fill=X)

flex_sep = Label(root, font=(None,36), anchor=E, style="flex_sep.TLabel")
flex_sep.pack(fill=BOTH, expand=True)

########################## FRAME AND BUTTONS ##########################
#######################################################################

frame = Frame(root)
frame.pack(fill=BOTH, expand=True)



val_mod = Button(frame, text = '%', command= lambda: screen.insert(END, '%'))
val_CE = Button(frame, text = 'CE', command= lambda: screen.delete(0, END))
val_C = Button(frame, text = 'C', command= lambda: screen.delete(END))
val_backspace = Button(frame, text = 'BS', command= lambda: screen.insert(END, '0'))


val_reci = Button(frame, text = '1/x', command= lambda: screen.insert(END, '0'))
val_sqr = Button(frame, text = 'x^2', command= lambda: screen.insert(END, '0'))
val_root2 = Button(frame, text = 'r2', command= lambda: screen.insert(END, '0'))
val_div = Button(frame, text = '/', command= lambda: screen.insert(END, '0'))


val_0 = Button(frame, text='0', command= lambda: screen.insert(END, '0'))
val_1 = Button(frame, text='1', command= lambda: screen.insert(END, '1'))
val_2 = Button(frame, text='2', command= lambda: screen.insert(END, '2'))
val_3 = Button(frame, text='3', command= lambda: screen.insert(END, '3'))
val_4 = Button(frame, text='4', command= lambda: screen.insert(END, '4'))
val_5 = Button(frame, text='5', command= lambda: screen.insert(END, '5'))
val_6 = Button(frame, text='6', command= lambda: screen.insert(END, '6'))
val_7 = Button(frame, text='7', command= lambda: screen.insert(END, '7'))
val_8 = Button(frame, text='8', command= lambda: screen.insert(END, '8'))
val_9 = Button(frame, text='9', command= lambda: screen.insert(END, '9'))



val_mul = Button(frame, text = 'x', command= lambda: screen.insert(END, 'x'))
val_sub = Button(frame, text = '-', command= lambda: screen.insert(END, '-'))
val_add = Button(frame, text = '+', command= lambda: screen.insert(END, '+'))

val_sign = Button(frame, text = '+/-')


val_dot = Button(frame, text = '.', command= lambda: screen.insert(END, '.'))
val_equal = Button(frame, text = '=', command= lambda: simplify())


buttons = [[val_mod,   val_CE,   val_C,   val_backspace],
           [val_reci,   val_sqr,   val_root2,   val_div],
           [val_7,      val_8,      val_9,      val_mul],
           [val_4,      val_5,      val_6,      val_sub],
           [val_1,      val_2,      val_3,      val_add],
           [val_sign,   val_0,      val_dot,    val_equal],]



for i in range(6):
    for j in range(4):
        buttons[i][j].grid(row=i, column=j, ipady=23, sticky=NSEW)
        # buttons[i][j].grid_propagate(False)
        
frame.columnconfigure((0,1,2,3), weight=1)        
frame.rowconfigure((0,1,2,3,4,5), weight=1)        

# grid(row=0, column=0)   grid(row=0, column=1)   grid(row=0, column=2)
# grid(row=1, column=0)   grid(row=1, column=0)   grid(row=1, column=0)
# grid(row=1, column=0)   grid(row=1, column=0)   grid(row=1, column=0)


# screen = Entry(root, width=57)
# screen.grid(columnspan=4)


#######################################################################
#######################################################################

def simplify():
    exp = screen.get()
    exp = exp.replace('x','*')
    
    screen.delete(0, END)
    screen.insert(0, eval(exp))



root.mainloop()