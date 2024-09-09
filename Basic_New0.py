from tkinter import *
from tkinter.ttk import *
from tkinter import PhotoImage

import math 

root=Tk()
root.configure(bg="#202020")

style = Style()

#Create photo object
#Create element of it
#Create the layout using these element

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

photo_asin = PhotoImage(file = r"Images/asin.png")
photo_acos = PhotoImage(file = r"Images/acos.png")
photo_atan = PhotoImage(file = r"Images/atan.png")
photo_asec = PhotoImage(file = r"Images/asec.png")
photo_acsc = PhotoImage(file = r"Images/acsc.png")
photo_acot = PhotoImage(file = r"Images/acot.png")




photo_val_0_highlighted = PhotoImage(file = r"Images/0_highlighted.png")
photo_val_1_highlighted = PhotoImage(file = r"Images/1_highlighted.png")
photo_val_2_highlighted = PhotoImage(file = r"Images/2_highlighted.png")
photo_val_3_highlighted = PhotoImage(file = r"Images/3_highlighted.png")
photo_val_4_highlighted = PhotoImage(file = r"Images/4_highlighted.png")
photo_val_5_highlighted = PhotoImage(file = r"Images/5_highlighted.png")
photo_val_6_highlighted = PhotoImage(file = r"Images/6_highlighted.png")
photo_val_7_highlighted = PhotoImage(file = r"Images/7_highlighted.png")
photo_val_8_highlighted = PhotoImage(file = r"Images/8_highlighted.png")
photo_val_9_highlighted = PhotoImage(file = r"Images/9_highlighted.png")


photo_Add_highlighted = PhotoImage(file = r"Images/Add_highlighted.png")
photo_Sub_highlighted = PhotoImage(file = r"Images/Sub_highlighted.png")
photo_Mul_highlighted = PhotoImage(file = r"Images/Mul_highlighted.png")
photo_Div_highlighted = PhotoImage(file = r"Images/Div_highlighted.png")
photo_Modulus_highlighted = PhotoImage(file = r"Images/Modulus_highlighted.png")

photo_Clear_highlighted = PhotoImage(file = r"Images/Clear_highlighted.png")
photo_Clear_entry_highlighted = PhotoImage(file = r"Images/Clear_entry_highlighted.png")

photo_Sqr_highlighted = PhotoImage(file = r"Images/Sqr_highlighted.png")
photo_Sqr_root_highlighted = PhotoImage(file = r"Images/Sqr_root_highlighted.png")


photo_Decimal_highlighted = PhotoImage(file = r"Images/Decimal_highlighted.png")
photo_Equal_highlighted = PhotoImage(file = r"Images/Equal_highlighted.png")
photo_Reci_highlighted = PhotoImage(file = r"Images/Reci_highlighted.png")
photo_Sign_rev_highlighted = PhotoImage(file = r"Images/Sign_rev_highlighted.png")
photo_Backspace_highlighted = PhotoImage(file = r"Images/Backspace_highlighted.png")

photo_sin_highlighted = PhotoImage(file = r"Images/sin_highlighted.png")
photo_cos_highlighted = PhotoImage(file = r"Images/cos_highlighted.png")
photo_tan_highlighted = PhotoImage(file = r"Images/tan_highlighted.png")
photo_sec_highlighted = PhotoImage(file = r"Images/sec_highlighted.png")
photo_csc_highlighted = PhotoImage(file = r"Images/csc_highlighted.png")
photo_cot_highlighted = PhotoImage(file = r"Images/cot_highlighted.png")

photo_asin_highlighted = PhotoImage(file = r"Images/asin_highlighted.png")
photo_acos_highlighted = PhotoImage(file = r"Images/acos_highlighted.png")
photo_atan_highlighted = PhotoImage(file = r"Images/atan_highlighted.png")
photo_asec_highlighted = PhotoImage(file = r"Images/asec_highlighted.png")
photo_acsc_highlighted = PhotoImage(file = r"Images/acsc_highlighted.png")
photo_acot_highlighted = PhotoImage(file = r"Images/acot_highlighted.png")


photo_trig = PhotoImage(file = r"Images/trig.png")
photo_inv_trig = PhotoImage(file = r"Images/inv_trig.png")




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

style.element_create("asin.field", "image", photo_asin)
style.element_create("acos.field", "image", photo_acos)
style.element_create("atan.field", "image", photo_atan)
style.element_create("asec.field", "image", photo_asec)
style.element_create("acsc.field", "image", photo_acsc)
style.element_create("acot.field", "image", photo_acot)





style.element_create("val_0_highlighted.field", "image", photo_val_0_highlighted)
style.element_create("val_1_highlighted.field", "image", photo_val_1_highlighted)
style.element_create("val_2_highlighted.field", "image", photo_val_2_highlighted)
style.element_create("val_3_highlighted.field", "image", photo_val_3_highlighted)
style.element_create("val_4_highlighted.field", "image", photo_val_4_highlighted)
style.element_create("val_5_highlighted.field", "image", photo_val_5_highlighted)
style.element_create("val_6_highlighted.field", "image", photo_val_6_highlighted)
style.element_create("val_7_highlighted.field", "image", photo_val_7_highlighted)
style.element_create("val_8_highlighted.field", "image", photo_val_8_highlighted)
style.element_create("val_9_highlighted.field", "image", photo_val_9_highlighted)

style.element_create("Add_highlighted.field", "image", photo_Add_highlighted)
style.element_create("Sub_highlighted.field", "image", photo_Sub_highlighted)
style.element_create("Mul_highlighted.field", "image", photo_Mul_highlighted)
style.element_create("Div_highlighted.field", "image", photo_Div_highlighted)
style.element_create("Modulus_highlighted.field", "image", photo_Modulus_highlighted)

style.element_create("Clear_highlighted.field", "image", photo_Clear_highlighted)
style.element_create("Clear_entry_highlighted.field", "image", photo_Clear_entry_highlighted)

style.element_create("Sqr_highlighted.field", "image", photo_Sqr_highlighted)
style.element_create("Sqr_root_highlighted.field", "image", photo_Sqr_root_highlighted)

style.element_create("Decimal_highlighted.field", "image", photo_Decimal_highlighted)
style.element_create("Equal_highlighted.field", "image", photo_Equal_highlighted)
style.element_create("Reci_highlighted.field", "image", photo_Reci_highlighted)
style.element_create("Sign_rev_highlighted.field", "image", photo_Sign_rev_highlighted)
style.element_create("Backspace_highlighted.field", "image", photo_Backspace_highlighted)


style.element_create("sin_highlighted.field", "image", photo_sin_highlighted)
style.element_create("cos_highlighted.field", "image", photo_cos_highlighted)
style.element_create("tan_highlighted.field", "image", photo_tan_highlighted)
style.element_create("sec_highlighted.field", "image", photo_sec_highlighted)
style.element_create("csc_highlighted.field", "image", photo_csc_highlighted)
style.element_create("cot_highlighted.field", "image", photo_cot_highlighted)

style.element_create("asin_highlighted.field", "image", photo_asin_highlighted)
style.element_create("acos_highlighted.field", "image", photo_acos_highlighted)
style.element_create("atan_highlighted.field", "image", photo_atan_highlighted)
style.element_create("asec_highlighted.field", "image", photo_asec_highlighted)
style.element_create("acsc_highlighted.field", "image", photo_acsc_highlighted)
style.element_create("acot_highlighted.field", "image", photo_acot_highlighted)

style.element_create("trig.field", "image", photo_trig)
style.element_create("inv_trig.field", "image", photo_inv_trig)





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

style.layout("asin", [("asin.field", {"side": LEFT, "expand": 1})])
style.layout("acos", [("acos.field", {"side": LEFT, "expand": 1})])
style.layout("atan", [("atan.field", {"side": LEFT, "expand": 1})])
style.layout("asec", [("asec.field", {"side": LEFT, "expand": 1})])
style.layout("acsc", [("acsc.field", {"side": LEFT, "expand": 1})])
style.layout("acot", [("acot.field", {"side": LEFT, "expand": 1})])

style.layout("trig", [("trig.field", {"side": LEFT, "expand": 1})])
style.layout("inv_trig", [("inv_trig.field", {"side": LEFT, "expand": 1})])




style.layout("val_0_highlighted", [("val_0_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("val_1_highlighted", [("val_1_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("val_2_highlighted", [("val_2_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("val_3_highlighted", [("val_3_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("val_4_highlighted", [("val_4_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("val_5_highlighted", [("val_5_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("val_6_highlighted", [("val_6_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("val_7_highlighted", [("val_7_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("val_8_highlighted", [("val_8_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("val_9_highlighted", [("val_9_highlighted.field", {"side": LEFT, "expand": 1})])

style.layout("Add_highlighted",   [("Add_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("Sub_highlighted",   [("Sub_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("Mul_highlighted",   [("Mul_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("Div_highlighted",   [("Div_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("Modulus_highlighted", [("Modulus_highlighted.field", {"side": LEFT, "expand": 1})])

style.layout("Clear_highlighte.",       [("Clear_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("Clear_entry_highlighted", [("Clear_entry_highlighted.field", {"side": LEFT, "expand": 1})])

style.layout("Sqr_highlighted",      [("Sqr_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("Sqr_root_highlighted", [("Sqr_root_highlighted.field", {"side": LEFT, "expand": 1})])

style.layout("Decimal_highlighted",   [("Decimal_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("Equal_highlighted",     [("Equal_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("Reci_highlighted",      [("Reci_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("Sign_rev_highlighted",  [("Sign_rev_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("Backspace_highlighted", [("Backspace_highlighted.field", {"side": LEFT, "expand": 1})])


style.layout("sin_highlighted", [("sin_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("cos_highlighted", [("cos_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("tan_highlighted", [("tan_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("sec_highlighted", [("sec_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("csc_highlighted", [("csc_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("cot_highlighted", [("cot_highlighted.field", {"side": LEFT, "expand": 1})])

style.layout("asin_highlighted", [("asin_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("acos_highlighted", [("acos_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("atan_highlighted", [("atan_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("asec_highlighted", [("asec_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("acsc_highlighted", [("acsc_highlighted.field", {"side": LEFT, "expand": 1})])
style.layout("acot_highlighted", [("acot_highlighted.field", {"side": LEFT, "expand": 1})])




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

style.configure("asin", background = "#202020")
style.configure("acos", background = "#202020")
style.configure("atan", background = "#202020")
style.configure("asec", background = "#202020")
style.configure("acsc", background = "#202020")
style.configure("acot", background = "#202020")

style.configure("trig", background = "#202020")
style.configure("inv_trig", background = "#202020")





style.configure("val_0_highlighted", background = "#202020")
style.configure("val_1_highlighted", background = "#202020")
style.configure("val_2_highlighted", background = "#202020")
style.configure("val_3_highlighted", background = "#202020")
style.configure("val_4_highlighted", background = "#202020")
style.configure("val_5_highlighted", background = "#202020")
style.configure("val_6_highlighted", background = "#202020")
style.configure("val_7_highlighted", background = "#202020")
style.configure("val_8_highlighted", background = "#202020")
style.configure("val_9_highlighted", background = "#202020")

style.configure("Add_highlighted", background = "#202020")
style.configure("Sub_highlighted", background = "#202020")
style.configure("Mul_highlighted", background = "#202020")
style.configure("Div_highlighted", background = "#202020")
style.configure("Modulus_highlighted", background = "#202020")

style.configure("Clear_highlighted", background = "#202020")
style.configure("Clear_entry_highlighted", background = "#202020")

style.configure("Sqr_highlighted", background = "#202020")
style.configure("Sqr_root_highlighted", background = "#202020")

style.configure("Decimal_highlighted", background = "#202020")
style.configure("Equal_highlighted", background = "#202020")
style.configure("Reci_highlighted", background = "#202020")
style.configure("Sign_rev_highlighted", background = "#202020")
style.configure("Backspace_highlighted", background = "#202020")


style.configure("sin_highlighted", background = "#202020")
style.configure("cos_highlighted", background = "#202020")
style.configure("tan_highlighted", background = "#202020")
style.configure("sec_highlighted", background = "#202020")
style.configure("csc_highlighted", background = "#202020")
style.configure("cot_highlighted", background = "#202020")

style.configure("asin_highlighted", background = "#202020")
style.configure("acos_highlighted", background = "#202020")
style.configure("atan_highlighted", background = "#202020")
style.configure("asec_highlighted", background = "#202020")
style.configure("acsc_highlighted", background = "#202020")
style.configure("acot_highlighted", background = "#202020")




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



trig = Button(root, style = "trig")
inv_trig = Button(root, style = "inv_trig")
trig.grid(sticky=W, padx = 18, pady = 8)
# inv_trig.grid(sticky=W, padx = 8, pady = 8)

trig.bind("<Button-1>", lambda e: [trig.grid_forget(), 
                                   inv_trig.grid(row = 2, sticky=W, padx = 8, pady = 8), 
                                   trig_switch_func([sin,cos,tan,sec,csc,cot,asin,acos,atan,asec,acsc,acot])])
inv_trig.bind("<Button-1>", lambda e: [inv_trig.grid_forget(), 
                                       trig.grid(row = 2, sticky=W, padx = 18, pady = 8),
                                       trig_switch_func([asin,acos,atan,asec,acsc,acot,sin,cos,tan,sec,csc,cot])])




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




sin = Button(keypad_frame, style="sin", command = lambda: trig_func("sin"))
cos = Button(keypad_frame, style="cos", command = lambda: trig_func("cos"))
tan = Button(keypad_frame, style="tan", command = lambda: trig_func("tan"))
sec = Button(keypad_frame, style="sec", command = lambda: trig_func("sec"))
csc = Button(keypad_frame, style="csc", command = lambda: trig_func("csc"))
cot = Button(keypad_frame, style="cot", command = lambda: trig_func("cot"))

asin = Button(keypad_frame, style="asin", command = lambda: trig_func("asin"))
acos = Button(keypad_frame, style="acos", command = lambda: trig_func("acos"))
atan = Button(keypad_frame, style="atan", command = lambda: trig_func("atan"))
asec = Button(keypad_frame, style="asec", command = lambda: trig_func("asec"))
acsc = Button(keypad_frame, style="acsc", command = lambda: trig_func("acsc"))
acot = Button(keypad_frame, style="acot", command = lambda: trig_func("acot"))




val_0.bind("<Button-1>", lambda e: blink(e, ["val_0_highlighted", "val_0"]))
val_1.bind("<Button-1>", lambda e: blink(e, ["val_1_highlighted", "val_1"]))
val_2.bind("<Button-1>", lambda e: blink(e, ["val_2_highlighted", "val_2"]))
val_3.bind("<Button-1>", lambda e: blink(e, ["val_3_highlighted", "val_3"]))
val_4.bind("<Button-1>", lambda e: blink(e, ["val_4_highlighted", "val_4"]))
val_5.bind("<Button-1>", lambda e: blink(e, ["val_5_highlighted", "val_5"]))
val_6.bind("<Button-1>", lambda e: blink(e, ["val_6_highlighted", "val_6"]))
val_7.bind("<Button-1>", lambda e: blink(e, ["val_7_highlighted", "val_7"]))
val_8.bind("<Button-1>", lambda e: blink(e, ["val_8_highlighted", "val_8"]))
val_9.bind("<Button-1>", lambda e: blink(e, ["val_9_highlighted", "val_9"]))

Add.bind("<Button-1>", lambda e: blink(e, ["Add_highlighted", "Add"]))
Sub.bind("<Button-1>", lambda e: blink(e, ["Sub_highlighted", "SubDiv"]))
Mul.bind("<Button-1>", lambda e: blink(e, ["Mul_highlighted", "Mul"]))
Div.bind("<Button-1>", lambda e: blink(e, ["Div_highlighted", "Div"]))
Modulus.bind("<Button-1>", lambda e: blink(e, ["Modulus_highlighted", "Modulus"]))

Clear.bind("<Button-1>", lambda e: blink(e, ["Clear_highlighted", "Clear"]))
Clear_entry.bind("<Button-1>", lambda e: blink(e, ["CLear_entry_highlighted", "Clear_entry"]))

Sqr.bind("<Button-1>", lambda e: blink(e, ["Sqr_highlighted", "Sqr"]))
Sqr_root.bind("<Button-1>", lambda e: blink(e, ["Sqr_root_highlighted", "Sqr_root"]))

Decimal.bind("<Button-1>", lambda e: blink(e, ["Decimal_highlighted", "Decimal"]))
Equal.bind("<Button-1>", lambda e: blink(e, ["Equal_highlighted", "Equal"]))
Reci.bind("<Button-1>", lambda e: blink(e, ["Reci_highlighted", "Reci"]))

Sign_rev.bind("<Button-1>", lambda e: blink(e, ["Sign_rev_highlighted", "Sign_rev"]))

Backspace.bind("<Button-1>", lambda e: blink(e, ["Backspace_highlighted", "Backspace"]))



sin.bind("<Button-1>", lambda e: blink(e, ["sin_highlighted", "sin"]))
cos.bind("<Button-1>", lambda e: blink(e, ["cos_highlighted", "cos"]))
tan.bind("<Button-1>", lambda e: blink(e, ["tan_highlighted", "tan"]))
sec.bind("<Button-1>", lambda e: blink(e, ["sec_highlighted", "sec"]))
csc.bind("<Button-1>", lambda e: blink(e, ["csc_highlighted", "csc"]))
cot.bind("<Button-1>", lambda e: blink(e, ["cot_highlighted", "cot"]))

asin.bind("<Button-1>", lambda e: blink(e, ["asin_highlighted", "asin"]))
acos.bind("<Button-1>", lambda e: blink(e, ["acos_highlighted", "acos"]))
atan.bind("<Button-1>", lambda e: blink(e, ["atan_highlighted", "atan"]))
asec.bind("<Button-1>", lambda e: blink(e, ["asec_highlighted", "asec"]))
acsc.bind("<Button-1>", lambda e: blink(e, ["acsc_highlighted", "acsc"]))
acot.bind("<Button-1>", lambda e: blink(e, ["acot_highlighted", "acot"]))





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
            exp +=')'
            screen.delete(0,END)
        
        exp = exp.replace('x','*')
        exp = exp.replace("asin", "math.asin")
        exp = exp.replace("acos", "math.acos")
        exp = exp.replace("atan", "math.atan")
        exp = exp.replace("asec", "1/math.asin")
        exp = exp.replace("acsc", "1/math.acos")
        exp = exp.replace("acot", "1/math.atan")
        
        if "asin" not in exp and "acos" not in exp and "atan" not in exp:
            exp = exp.replace("sin", "math.sin")
            exp = exp.replace("cos", "math.cos")
            exp = exp.replace("tan", "math.tan")
            exp = exp.replace("cot", "1/math.tan")
            exp = exp.replace("csc", "1/math.sin")
            exp = exp.replace("sec", "1/math.cos")
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
    exp=str(exp)
    exp = exp+i
    
    if exp.count('(') > exp.count(')'): 
        exp +=')'
        screen.delete(0,END)
        
        
    label.configure(text = exp+'=')
    exp = exp.replace('x','*')
    exp = exp.replace("asin", "math.asin")
    exp = exp.replace("acos", "math.acos")
    exp = exp.replace("atan", "math.atan")
    exp = exp.replace("asec", "1/math.asin")
    exp = exp.replace("acsc", "1/math.acos")
    exp = exp.replace("acot", "1/math.atan")
    
    if "asin" not in exp and "acos" not in exp and "atan" not in exp:
        exp = exp.replace("sin", "math.sin")
        exp = exp.replace("cos", "math.cos")
        exp = exp.replace("tan", "math.tan")
        exp = exp.replace("cot", "1/math.tan")
        exp = exp.replace("csc", "1/math.sin")
        exp = exp.replace("sec", "1/math.cos")
    print(exp)
        
    screen.delete(0, END)
    exp = str(eval(exp))
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
    exp = exp.replace("asin", "math.asin")
    exp = exp.replace("acos", "math.acos")
    exp = exp.replace("atan", "math.atan")
    exp = exp.replace("asec", "1/math.asin")
    exp = exp.replace("acsc", "1/math.acos")
    exp = exp.replace("acot", "1/math.atan")
    
    if "asin" not in exp and "acos" not in exp and "atan" not in exp:
        exp = exp.replace("sin", "math.sin")
        exp = exp.replace("cos", "math.cos")
        exp = exp.replace("tan", "math.tan")
        exp = exp.replace("cot", "1/math.tan")
        exp = exp.replace("csc", "1/math.sin")
        exp = exp.replace("sec", "1/math.cos")
    
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
    

def trig_func(op):
    global exp
    exp=str(exp)

    exp = exp.replace('x','*')
    
    exp = exp.replace("asin", "math.asin")
    exp = exp.replace("acos", "math.acos")
    exp = exp.replace("atan", "math.atan")
    exp = exp.replace("asec", "1/math.asin")
    exp = exp.replace("acsc", "1/math.acos")
    exp = exp.replace("acot", "1/math.atan")
    
    if "asin" not in exp and "acos" not in exp and "atan" not in exp:
        exp = exp.replace("sin", "math.sin")
        exp = exp.replace("cos", "math.cos")
        exp = exp.replace("tan", "math.tan")
        exp = exp.replace("cot", "1/math.tan")
        exp = exp.replace("csc", "1/math.sin")
        exp = exp.replace("sec", "1/math.cos")
    
    if exp.count('(') > exp.count(')'): 
        # exp += screen.get()+')x'
        
        exp += screen.get() +')'
        
        print(exp)
        exp = str(eval(exp))
        exp += 'x'
        screen.delete(0,END)
        # exp = str(eval(exp))
    # label.configure(text = exp)
    print(exp)
    if screen.get():    
        exp += screen.get()+'*'
        screen.delete(0, END)
    exp+=op+'('
    label.configure(text = exp)
    
    
def trig_switch_func(op):
    
    for i in range(6):
        op[i].grid_forget()
        op[i+6].grid(row=i, padx=1.3, pady=1.3)
        

def blink(e, state):
    arrow=e.widget
    
    _ = IntVar()
    root.after(100, _.set, 1)
    root.waitvar(_)
    arrow.configure(style = state[0])
    root.update()
    root.after(200, lambda: arrow.configure(style=state[1]))
        
        
        
        
# def trig_switch_func(op):
#     global trig, inv_trig
#     print(type(inv_trig))
#     if op == trig:
#         trig.grid_forget()
#         inv_trig.grid(sticky=W, padx = 8, pady = 8)
    
#     else:
#         inv_trig.grid_forget()
#         trig.grid(sticky=W, padx = 18, pady = 8)
        
    
#     op.grid(row = 2)
    
    



    
    
    


root.mainloop()