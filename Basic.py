from tkinter import *
from tkinter.ttk import *


root =  Tk()
root.title("Caly")
root.eval("tk::PlaceWindow . center")


style = Style()

style.configure("TButton", font=(None,10), background="#323232")



val_mod = Button(root, text = '%')
val_CE = Button(root, text = 'CE')
val_C = Button(root, text = 'C')
val_backspace = Button(root, text = 'BS')

val_0 = Button(root, text='0')
val_1 = Button(root, text='1')
val_2 = Button(root, text='2')
val_3 = Button(root, text='3')
val_4 = Button(root, text='4')
val_5 = Button(root, text='5')
val_6 = Button(root, text='6')
val_7 = Button(root, text='7')
val_8 = Button(root, text='8')
val_9 = Button(root, text='9')



val_mul = Button(root, text = 'x')
val_sub = Button(root, text = '-')
val_add = Button(root, text = '+')

val_dot = Button(root, text = '.')
val_equal = Button(root, text = '=')


buttons = [[val_mod,   val_CE,   val_C,   val_backspace],
           [Button(),   Button(),   Button(),   Button()],
           [val_7,      val_8,      val_9,      val_mul],
           [val_4,      val_5,      val_6,      val_sub],
           [val_1,      val_2,      val_3,      val_add],
           [Button(),   val_0,      val_dot,    val_equal],]



for i in range(6):
    for j in range(4):
        buttons[i][j].grid(row=i, column=j, ipady=23)
        buttons[i][j].grid_propagate(True)
        
        
    
    
# grid(row=0, column=0)   grid(row=0, column=1)   grid(row=0, column=2)
# grid(row=1, column=0)   grid(row=1, column=0)   grid(row=1, column=0)
# grid(row=1, column=0)   grid(row=1, column=0)   grid(row=1, column=0)


# screen = Entry(root, width=57)
# screen.grid(columnspan=4)



root.mainloop()