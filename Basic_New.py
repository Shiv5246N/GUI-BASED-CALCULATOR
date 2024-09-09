from tkinter import *
from tkinter.ttk import *
from tkinter import PhotoImage

root=Tk()
root.configure(bg="#202020")

style = Style()

photo_val_0 = PhotoImage(file = r"Images/0.png")
photo_val_1 = PhotoImage(file = r"Images/1.png")
photo_val_2 = PhotoImage(file = r"Images/2.png")
photo_val_3 = PhotoImage(file = r"Images/3.png")
photo_val_4 = PhotoImage(file = r"Images/4.png")
photo_val_5 = PhotoImage(file = r"Images/5.png")
photo_val_6 = PhotoImage(file = r"Images/6.png")
photo_val_7 = PhotoImage(file = r"Images/7.png")
photo_val_8 = PhotoImage(file = r"Images/8.png")
photo_val_9 = PhotoImage(file = r"Images/9.png")


photo_Add = PhotoImage(file = r"Images/Add.png")
photo_Sub = PhotoImage(file = r"Images/Sub.png")
photo_Mul = PhotoImage(file = r"Images/Mul.png")
photo_Div = PhotoImage(file = r"Images/Div.png")
photo_Modulus = PhotoImage(file = r"Images/Modulus.png")

photo_Clear = PhotoImage(file = r"Images/Clear.png")
photo_Clear_entry = PhotoImage(file = r"Images/Clear_entry.png")

photo_Sqr = PhotoImage(file = r"Images/Sqr.png")
photo_Sqr_root = PhotoImage(file = r"Images/Sqr_root.png")


photo_Decimal = PhotoImage(file = r"Images/Decimal.png")
photo_Equal = PhotoImage(file = r"Images/Equal.png")
photo_Reci = PhotoImage(file = r"Images/Reci.png")
photo_Sign_rev = PhotoImage(file = r"Images/Sign_rev.png")
photo_Backspace= PhotoImage(file = r"Images/Backspace.png")

photo_sin = PhotoImage(file = r"Images/sin.png")
photo_cos = PhotoImage(file = r"Images/cos.png")
photo_tan = PhotoImage(file = r"Images/tan.png")
photo_sec = PhotoImage(file = r"Images/sec.png")
photo_csc = PhotoImage(file = r"Images/csc.png")
photo_cot = PhotoImage(file = r"Images/cot.png")





##   Change           Here                  Here
style.element_create("val_0.field", "image", photo_val_0)
style.element_create("val_1.field", "image", photo_val_1)
style.element_create("val_2.field", "image", photo_val_2)
style.element_create("val_3.field", "image", photo_val_3)
style.element_create("val_4.field", "image", photo_val_4)
style.element_create("val_5.field", "image", photo_val_5)
style.element_create("val_6.field", "image", photo_val_6)
style.element_create("val_7.field", "image", photo_val_7)
style.element_create("val_8.field", "image", photo_val_8)
style.element_create("val_9.field", "image", photo_val_9)

style.element_create("Add.field", "image", photo_Add)
style.element_create("Sub.field", "image", photo_Sub)
style.element_create("Mul.field", "image", photo_Mul)
style.element_create("Div.field", "image", photo_Div)
style.element_create("Modulus.field", "image", photo_Modulus)

style.element_create("Clear.field", "image", photo_Clear)
style.element_create("Clear_entry.field", "image", photo_Clear_entry)

style.element_create("Sqr.field", "image", photo_Sqr)
style.element_create("Sqr_root.field", "image", photo_Sqr_root)

style.element_create("Decimal.field", "image", photo_Decimal)
style.element_create("Equal.field", "image", photo_Equal)
style.element_create("Reci.field", "image", photo_Reci)
style.element_create("Sign_rev.field", "image", photo_Sign_rev)
style.element_create("Backspace.field", "image", photo_Backspace)


style.element_create("sin.field", "image", photo_sin)
style.element_create("cos.field", "image", photo_cos)
style.element_create("tan.field", "image", photo_tan)
style.element_create("sec.field", "image", photo_sec)
style.element_create("csc.field", "image", photo_csc)
style.element_create("cot.field", "image", photo_cot)




##   Change   Here      Here
style.layout("val_0", [("val_0.field", {"side": LEFT, "expand": 1})])
style.layout("val_1", [("val_1.field", {"side": LEFT, "expand": 1})])
style.layout("val_2", [("val_2.field", {"side": LEFT, "expand": 1})])
style.layout("val_3", [("val_3.field", {"side": LEFT, "expand": 1})])
style.layout("val_4", [("val_4.field", {"side": LEFT, "expand": 1})])
style.layout("val_5", [("val_5.field", {"side": LEFT, "expand": 1})])
style.layout("val_6", [("val_6.field", {"side": LEFT, "expand": 1})])
style.layout("val_7", [("val_7.field", {"side": LEFT, "expand": 1})])
style.layout("val_8", [("val_8.field", {"side": LEFT, "expand": 1})])
style.layout("val_9", [("val_9.field", {"side": LEFT, "expand": 1})])

style.layout("Add",   [("Add.field", {"side": LEFT, "expand": 1})])
style.layout("Sub",   [("Sub.field", {"side": LEFT, "expand": 1})])
style.layout("Mul",   [("Mul.field", {"side": LEFT, "expand": 1})])
style.layout("Div",   [("Div.field", {"side": LEFT, "expand": 1})])
style.layout("Modulus", [("Modulus.field", {"side": LEFT, "expand": 1})])

style.layout("Clear",       [("Clear.field", {"side": LEFT, "expand": 1})])
style.layout("Clear_entry", [("Clear_entry.field", {"side": LEFT, "expand": 1})])

style.layout("Sqr",      [("Sqr.field", {"side": LEFT, "expand": 1})])
style.layout("Sqr_root", [("Sqr_root.field", {"side": LEFT, "expand": 1})])

style.layout("Decimal",   [("Decimal.field", {"side": LEFT, "expand": 1})])
style.layout("Equal",     [("Equal.field", {"side": LEFT, "expand": 1})])
style.layout("Reci",      [("Reci.field", {"side": LEFT, "expand": 1})])
style.layout("Sign_rev",  [("Sign_rev.field", {"side": LEFT, "expand": 1})])
style.layout("Backspace", [("Backspace.field", {"side": LEFT, "expand": 1})])


style.layout("sin", [("sin.field", {"side": LEFT, "expand": 1})])
style.layout("cos", [("cos.field", {"side": LEFT, "expand": 1})])
style.layout("tan", [("tan.field", {"side": LEFT, "expand": 1})])
style.layout("sec", [("sec.field", {"side": LEFT, "expand": 1})])
style.layout("csc", [("csc.field", {"side": LEFT, "expand": 1})])
style.layout("cot", [("cot.field", {"side": LEFT, "expand": 1})])







style.configure("val_0", background = "#202020")
style.configure("val_1", background = "#202020")
style.configure("val_2", background = "#202020")
style.configure("val_3", background = "#202020")
style.configure("val_4", background = "#202020")
style.configure("val_5", background = "#202020")
style.configure("val_6", background = "#202020")
style.configure("val_7", background = "#202020")
style.configure("val_8", background = "#202020")
style.configure("val_9", background = "#202020")

style.configure("Add", background = "#202020")
style.configure("Sub", background = "#202020")
style.configure("Mul", background = "#202020")
style.configure("Div", background = "#202020")
style.configure("Modulus", background = "#202020")

style.configure("Clear", background = "#202020")
style.configure("Clear_entry", background = "#202020")

style.configure("Sqr", background = "#202020")
style.configure("Sqr_root", background = "#202020")

style.configure("Decimal", background = "#202020")
style.configure("Equal", background = "#202020")
style.configure("Reci", background = "#202020")
style.configure("Sign_rev", background = "#202020")
style.configure("Backspace", background = "#202020")


style.configure("sin", background = "#202020")
style.configure("cos", background = "#202020")
style.configure("tan", background = "#202020")
style.configure("sec", background = "#202020")
style.configure("csc", background = "#202020")
style.configure("cot", background = "#202020")





#############  Label  #############

style.configure("TLabel", background="#202020", foreground = "#C2C0C0")

label = Label(root, text="AND", font=(None,12), justify=RIGHT)
label.grid(sticky=E)


#############  Screen  #############

style.element_create("plain.field", "from", "classic")

style.layout("TEntry",
                [('Entry.plain.field', {'children': [(
                   'Entry.background', {'children': [(
                       'Entry.padding', {'children': [(
                           'Entry.textarea', {'sticky': 'nswe'})],
                    'sticky': 'nswe'})], 'sticky': 'nswe'})],
                    'border':'2', 'sticky': 'nswe'})])

style.configure("TEntry", borderwidth=0, fieldbackground="#202020", foreground="#FFFFFF")



# screen = Entry(root, font=(None, 37), width=14, justify=RIGHT)
screen = Entry(root, font=(None, 36), width=10, justify=RIGHT)      #Arbitary width
screen.grid(sticky=EW)



#########  Keypad Frame  #########

style.configure("keypad_frame.TFrame", background="#202020")

keypad_frame = Frame(root, style="keypad_frame.TFrame", width = 400, height = 230, padding=(2,2,2,2))
keypad_frame.grid()





val_0 = Button(keypad_frame, style = "val_0", command = lambda: screen.insert(END, 0))
val_1 = Button(keypad_frame, style = "val_1", command = lambda: screen.insert(END, 1))
val_2 = Button(keypad_frame, style = "val_2", command = lambda: screen.insert(END, 2))
val_3 = Button(keypad_frame, style = "val_3", command = lambda: screen.insert(END, 3))
val_4 = Button(keypad_frame, style = "val_4", command = lambda: screen.insert(END, 4))
val_5 = Button(keypad_frame, style = "val_5", command = lambda: screen.insert(END, 5))
val_6 = Button(keypad_frame, style = "val_6", command = lambda: screen.insert(END, 6))
val_7 = Button(keypad_frame, style = "val_7", command = lambda: screen.insert(END, 7))
val_8 = Button(keypad_frame, style = "val_8", command = lambda: screen.insert(END, 8))
val_9 = Button(keypad_frame, style = "val_9", command = lambda: screen.insert(END, 9))

Add = Button(keypad_frame, style = "Add", command = lambda: simplify('+'))
Sub = Button(keypad_frame, style = "Sub", command = lambda: simplify('-'))
Mul = Button(keypad_frame, style = "Mul", command = lambda: simplify('x'))
Div = Button(keypad_frame, style = "Div", command = lambda: simplify('/'))
Modulus = Button(keypad_frame, style = "Modulus", command = lambda: simplify('%'))

Clear = Button(keypad_frame, style = "Clear", command = lambda: (screen.delete(0, END), label.configure(text=''), clear_func()))
Clear_entry = Button(keypad_frame, style = "Clear_entry", command = lambda: screen.delete(0, END))

Sqr = Button(keypad_frame, style = "Sqr", command = lambda: s_func(2))
Sqr_root = Button(keypad_frame, style = "Sqr_root", command = lambda: s_func(1/2))

Decimal = Button(keypad_frame, style = "Decimal", command = lambda: screen.insert(END, '.'))
Equal = Button(keypad_frame, style = "Equal", command = lambda: equal_func())
Reci = Button(keypad_frame, style = "Reci", command = lambda: reci_func())

Sign_rev = Button(keypad_frame, style = "Sign_rev", command = lambda: sign_rev_func())

Backspace = Button(keypad_frame, style = "Backspace", command = lambda: screen.delete(len(screen.get())-1,END))


sin = Button(keypad_frame, style="sin", command = lambda: trig("sin"))
cos = Button(keypad_frame, style="cos", command = lambda: trig("cos"))
tan = Button(keypad_frame, style="tan", command = lambda: trig("tan"))
sec = Button(keypad_frame, style="sec", command = lambda: trig("sec"))
csc = Button(keypad_frame, style="csc", command = lambda: trig("csc"))
cot = Button(keypad_frame, style="tan", command = lambda: trig("cot"))




keypad_list = [[sin,    Modulus,    Clear_entry,    Clear,      Backspace],
               [cos,    Reci,          Sqr,        Sqr_root,       Div],
               [tan,    val_7,        val_8,        val_9,         Mul],
               [sec,    val_4,        val_5,        val_6,         Sub],
               [csc,    val_1,        val_2,        val_3,         Add],
               [cot,    Sign_rev,     val_0,       Decimal,      Equal]]


for i in range(6):  
    for j in range(5):  keypad_list[i][j].grid(row = i, column = j, padx=1.3, pady=1.3)
    

exp = ''
operator = ''

def simplify(op):
    global operator   
    global exp
    exp += screen.get()
    check = exp[-1]
    
    if check not in ('+','-','x','/','%'):
        
        if exp.count('(') > exp.count(')'): 
            exp += screen.get()+')'
            screen.delete(0,END)
        
        exp = exp.replace('x','*')
        exp = str(eval(exp))+op
        label.configure(text = exp)
        screen.delete(0, END)
        print(exp)
    
    else:
        exp = exp[:-1]+op
        label.configure(text = exp)
        
        
def equal_func():
    global exp
    
    i = screen.get()
    exp = exp+i
    
    if exp.count('(') > exp.count(')'): 
        exp += screen.get()+')x'
        screen.delete(0,END)
        
    label.configure(text = exp+'=')
    
    exp = exp.replace('x','*')
    
        
    screen.delete(0, END)
    screen.insert(END, str(eval(exp)))
    exp=0
    print(exp)
    

def sign_rev_func():
    check =  screen.get()
    if check:
        if check[0] == '-': screen.delete(0,1)
        else:   screen.insert(0, '-')
    else:
        screen.insert(0, '-')
        
        
def clear_func():
    global exp
    exp=''
        
    
def reci_func():
    global exp
    
    
    exp = exp.replace('x','*')
    exp += "1/" + screen.get()
    
    if exp.count('(') > exp.count(')'): 
        exp += screen.get()+')x'
        screen.delete(0,END)

    exp = str(eval(exp))
    label.configure(text=exp)
    screen.delete(0, END)
    
    

def s_func(op):
    check = int(screen.get())**op
    
    screen.delete(0, END)
    screen.insert(0, check)
    

def trig(op):
    global exp
    
    if exp.count('(') > exp.count(')'): 
        exp += screen.get()+')x'
        screen.delete(0,END)
    label.configure(text = exp)
    
    exp+=op+'('
    label.configure(text = exp)

    
    
    


root.mainloop()