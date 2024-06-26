
from pathlib import Path

# from tkinter import *
from time import sleep
from datetime import date
from tkinter import RIGHT, Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, Toplevel
import pyglet


#TO run change directory and add \\ on all \
# To run install python 1.11.0 and pip install pyglet
# pyglet.font.add_file("C:\\Users\\202-10\\Documents\\GitHub\\CashRegister\\Merchant_Copy_Doublesize.ttf")
# pyglet.font.add_file("C:\\Users\\202-10\\Documents\\GitHub\\CashRegister\\Open 24 Display St.ttf")

pyglet.font.add_file("D:\GitHub\CashRegister\Merchant_Copy_Doublesize.ttf")
pyglet.font.add_file("D:\GitHub\CashRegister\Open 24 Display St.ttf")

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


#---------- FUNCTIONS -------------------------------------------------------------#

def Cash_Register_turn_on():
    Last_Entry.config(state='normal')
    Last_Entry.insert('end', 'REG')
    Last_Entry.config(state='disabled')
    Register_mode()

def Fourth_Entry_input(number):
    global Department_button_pressed
    if mode == "PROG":
        pass
    else:
        if Department_button_pressed == True:
            Fourth_Entry.config(state='normal')
            Fourth_Entry.delete('1.0', 'end')
            Fourth_Entry.insert('end', number)
            Fourth_Entry.config(state='disabled')
            Department_button_pressed = False
        elif X_time_button_pressed == True:
            Fourth_Entry.config(state='normal')
            Fourth_Entry.insert('end', number)
            Fourth_Entry.config(state='disabled')
        else:
            Fourth_Entry.config(state='normal')
            Fourth_Entry.insert('end', number)
            Fourth_Entry.config(state='disabled')

def Department_button_input(department):
    global last_entered_number, Department_button_pressed
    if mode == "PROG":
        error_message()
    else:
        Department_button_pressed = True
        Fourth_Entry.config(state='normal')
        last_entered_number = int(Fourth_Entry.get('1.0', 'end-1c'))
        last_entered_number = last_entered_number / 100 
        last_entered_number = "{:.2f}".format(last_entered_number)
        num_spaces_dep = max(0, 27 - len(department) - len(str(last_entered_number)))
        Fourth_Entry.delete('1.0', 'end')
        Fourth_Entry.insert('end', department)

        Second_Entry.config(state='normal')
        Second_Entry.delete('1.0', 'end')
        Second_Entry.insert('end', department)
        Second_Entry.config(state='disabled')

        Fourth_Entry.insert('end', " " * num_spaces_dep + last_entered_number)  
        Fourth_Entry.config(state='disabled')
        First_Entry_input()
        Total_amount()

def First_Entry_input():
    global last_entered_number, How_many_bought, num_spaces_first_entry, X_Cost
    X_Cost = float(last_entered_number) * int(How_many_bought)
    X_Cost = "{:.2f}".format(X_Cost)
    X_Cost = str(X_Cost)
    First_Entry.config(state='normal')
    How_many_bought = str(How_many_bought)
    How_many_bought = str(How_many_bought+"x"+last_entered_number)
    First_Entry.delete('1.0', 'end')
    First_Entry.insert('end', How_many_bought)
    num_spaces_first_entry = max(0, 20 - len(How_many_bought) - len(str(last_entered_number)))
    First_Entry.insert('end', " " * num_spaces_first_entry + X_Cost)
    First_Entry.config(state='disabled')
    How_many_bought = 1



def Change_mode():
    global mode
    mode_index = All_Modes.index(mode)
    mode_index = (mode_index + 1) % len(All_Modes)
    mode = All_Modes[mode_index]
    Last_Entry.config(state='normal')
    Last_Entry.delete('1.0', 'end')
    Last_Entry.insert('end', mode)
    Last_Entry.config(state='disabled')
    mode_operator()


def Program_button_input():
    global mode, mode_index
    clear_screen()
    mode_index = 1
    mode = All_Modes[mode_index]
    Last_Entry.config(state='normal')
    Last_Entry.delete('1.0', 'end')
    Last_Entry.insert('end', mode)
    Last_Entry.config(state='disabled')
    mode_operator()

def Register_mode():
    global Total
    clear_screen()
    Total = 0
    Third_Entry.config(state='normal')
    Third_Entry.config(bg="#51458B", fg="#FFFFFF")
    num_spaces_reg = max(0, 17 - len("***TOTAL") - len(str(0.00)))
    Third_Entry.delete('1.0', 'end')
    Third_Entry.insert('end', '***TOTAL')
    Third_Entry.insert('end', " " * num_spaces_reg + "0.00")
    Third_Entry.config(state='disabled')
    
def Total_amount():
    global Total, num_spaces_reg, last_entered_number, Department_button_pressed, X_Cost, X_time_button_pressed, procent_button_pressed, new_price, Subtotal_button_pressed
    last_entered_number = float(last_entered_number)
    Total = float(Total)
    X_Cost = float(X_Cost)

    if X_time_button_pressed == True:
        Total = X_Cost + Total
        X_time_button_pressed = False
    elif procent_button_pressed == True:
        if Subtotal_button_pressed == True:
            Total = Total*0 + new_price
            procent_button_pressed = False
            Subtotal_button_pressed = False
        else:
            Total = Total - last_entered_number + new_price
            procent_button_pressed = False

    else:
        Total = last_entered_number + Total
    Total = "{:.2f}".format(Total)
    Third_Entry.config(state='normal')
    Third_Entry.config(bg="#51458B", fg="#FFFFFF")
    num_spaces_reg = max(0, 18 - len("***TOTAL") - len(str(Total)))
    Third_Entry.delete('1.0', 'end')
    Third_Entry.insert('end', '***TOTAL')
    Third_Entry.insert('end', " " * num_spaces_reg + Total)
    Third_Entry.config(state='disabled')

def X_time():
    global last_entered_number, How_many_bought, X_Cost, X_time_button_pressed
    X_time_button_pressed = True
    last_entered_number = float(last_entered_number)
    How_many_bought = Fourth_Entry.get('1.0', 'end-1c')
    X_Cost = last_entered_number * int(How_many_bought)
    Fourth_Entry.config(state='normal')
    Fourth_Entry.delete('1.0', 'end')
    Fourth_Entry.config(state='disabled')

def minus_percent():
    global Total, How_many_percent, last_entered_number, X_Cost, new_price, Inputed_last_discount, money_saved, procent_button_pressed, Subtotal_button_pressed
    if Department_button_pressed == True: #because the last pressed button is actually the discount amount.
        error_message()
    else:
        procent_button_pressed = True
        Inputed_last_discount = int(Fourth_Entry.get('1.0', 'end-1c'))  # gets last entered 10%
        if Inputed_last_discount < 0 or Inputed_last_discount > 100:
            error_message()
        else:
            if Subtotal_button_pressed == True:
                How_many_percent = Inputed_last_discount / 100 #percent in 0.10 format
                money_saved = float(Total) * How_many_percent
                new_price = float(Total) - float(money_saved)
                money_saved = "{:.2f}".format(money_saved)
            else:
                How_many_percent = Inputed_last_discount / 100 #percent in 0.10 format
                money_saved = last_entered_number * How_many_percent
                new_price = float(last_entered_number) - float(money_saved)
                money_saved = "{:.2f}".format(money_saved)

            clear_screen()
            First_Entry.config(state='normal')
            num_spaces_first_entry = max(0, 20 - len(str(Inputed_last_discount) + "%" + "-"))
            First_Entry.insert('end', " " * num_spaces_first_entry + "-" + str(Inputed_last_discount) + "%")
            First_Entry.config(state='disabled')

            Second_Entry.config(state='normal')
            Second_Entry.insert('end', "-%")
            num_spaces_second_entry = max(0, 20 - len("-%") - len("-" + str(money_saved)))
            Second_Entry.insert('end', " " * num_spaces_second_entry + "-" + money_saved)
            Second_Entry.config(state='disabled')

            Fourth_Entry.config(state='normal')
            Fourth_Entry.insert('end', "-%")
            num_spaces_second_entry = max(0, 27 - len("-%") - len("-" + str(money_saved)))
            Fourth_Entry.insert('end', " " * num_spaces_second_entry + "-" + money_saved)
            Fourth_Entry.config(state='disabled')
            Total_amount()

def plus_percent():
    global Total, How_many_percent, last_entered_number, X_Cost, new_price, Inputed_last_discount, money_saved, procent_button_pressed, Subtotal_button_pressed
    if Department_button_pressed == True: #because the last pressed button is actually the discount amount.
        error_message()
    else:
        procent_button_pressed = True
        Inputed_last_discount = int(Fourth_Entry.get('1.0', 'end-1c'))  # gets last entered 10%
        if Inputed_last_discount < 0 or Inputed_last_discount > 100:
            error_message()
        else:
            if Subtotal_button_pressed == True:
                How_many_percent = Inputed_last_discount / 100 #percent in 0.10 format
                money_saved = float(Total) * How_many_percent
                new_price = float(Total) + float(money_saved)
                money_saved = "{:.2f}".format(money_saved)
            else:
                How_many_percent = Inputed_last_discount / 100 #percent in 0.10 format
                money_saved = last_entered_number * How_many_percent
                new_price = float(last_entered_number) + float(money_saved)
                money_saved = "{:.2f}".format(money_saved)

            clear_screen()
            First_Entry.config(state='normal')
            num_spaces_first_entry = max(0, 20 - len(str(Inputed_last_discount) + "%" + "+"))
            First_Entry.insert('end', " " * num_spaces_first_entry + "+" + str(Inputed_last_discount) + "%")
            First_Entry.config(state='disabled')

            Second_Entry.config(state='normal')
            Second_Entry.insert('end', "+%")
            num_spaces_second_entry = max(0, 20 - len("+%") - len("+" + str(money_saved)))
            Second_Entry.insert('end', " " * num_spaces_second_entry + "+" + money_saved)
            Second_Entry.config(state='disabled')

            Fourth_Entry.config(state='normal')
            Fourth_Entry.insert('end', "+%")
            num_spaces_second_entry = max(0, 27 - len("+%") - len("+" + str(money_saved)))
            Fourth_Entry.insert('end', " " * num_spaces_second_entry + "+" + money_saved)
            Fourth_Entry.config(state='disabled')
            Total_amount()




def Subtotal_button_input():
    global num_spaces_second_entry, Total, Subtotal_button_pressed
    Subtotal_button_pressed = True
    Subtotal_Entry.config(state='normal')
    Subtotal_Entry.delete('1.0', 'end')
    Subtotal_Entry.insert('end', Total)
    Subtotal_Entry.config(state='disabled')

    Fourth_Entry.config(state='normal')
    Fourth_Entry.delete('1.0', 'end')
    Fourth_Entry.insert('end', "Subtotal")
    num_spaces_second_entry = max(0, 27 - len("Subtotal") - len(str(Total)))
    Fourth_Entry.insert('end', " " * num_spaces_second_entry + str(Total))
    Fourth_Entry.config(state='disabled')

def Clear_button_input():
    global Department_button_pressed
    if Department_button_pressed == False:
        Fourth_Entry.config(state="normal")
        Fourth_Entry.delete('1.0', 'end')
        Fourth_Entry.config(state="disabled")
    else:
        error_message()



def Program_mode():
    global Programmable_buttons, current_index
    clear_screen()
    First_Entry.config(state='normal')
    First_Entry.insert('end', 'Program Mode:')
    First_Entry.config(state='disabled')
    Third_Entry.config(state='normal')
    

    

def Report_mode():
    clear_screen()

def mode_operator():
    global mode
    if mode == "REG":
        Register_mode()
    elif mode == "PROG":
        Program_mode()
    elif mode == "REP":
        Report_mode()

#---------- CASH BUTTON -------------------------------------------------------------#

def CASH_button_input():
    global Cash_given, Total, Change, num_spaces_change, last_entered_number
    if Department_button_pressed == True or len(Fourth_Entry.get('1.0', 'end-1c')) == 0 or Total == 0:
        error_message()
    else:
        Cash_given = float(Fourth_Entry.get('1.0', 'end-1c'))
        Subtotal_button_input()
        Cash_given = Cash_given / 100 
        Cash_given = "{:.2f}".format(Cash_given)
        if float(Cash_given) < float(Total):
            error_message()
        else:
            clear_screen()
            Change = float(Cash_given) - float(Total)
            Change = "{:.2f}".format(Change)

            First_Entry.config(state='normal')
            num_spaces_change = max(0, 20 - len("CASH") - len(Cash_given))
            First_Entry.delete('1.0', 'end')
            First_Entry.insert('end', 'CASH')
            First_Entry.insert('end', " " * num_spaces_change + Cash_given)
            First_Entry.config(state='disabled')

            Third_Entry.config(state='normal')
            Third_Entry.config(bg="#51458B", fg="#FFFFFF")
            num_spaces_change = max(0, 17 - len("CHANGE") - len(Change))
            Third_Entry.delete('1.0', 'end')
            Third_Entry.insert('end', 'CHANGE')
            Third_Entry.insert('end', " " * num_spaces_change + Change)
            Third_Entry.config(state='disabled')
            Change_to_till()
            Cash_and_change_till()

#---------- Till Def -------------------------------------------------------------#

def Cash_and_change_till():
    Cash_gave_till = str(First_Entry.get('1.0', 'end-1c'))
    Cash_change_till = str(Third_Entry.get('1.0', 'end-1c'))
    First_Entry_till.insert(Cash_gave_till)
    Third_Entry_till.insert(Cash_change_till)



    
#---------- GLOBAL VARIABLES -------------------------------------------------------------#

All_Modes = ["REG","PROG","REP"]

mode = "REG"
Total = 0
last_entered_number = 0
Department_button_pressed = False
X_time_button_pressed = False
procent_button_pressed = False
Subtotal_button_pressed = False
How_many_bought = 1
X_Cost = 1
current_index = 0

Dept1 = "FOOD"
Dept2 = "CLOTHES"
Dept3 = "ELECTRONICS"
Dept4 = "TOYS"
Dept5 = "OTHERS"



#---------- EXTRA def -------------------------------------------------------------#

def clear_screen():
    First_Entry.config(state='normal')
    First_Entry.delete('1.0', 'end')
    First_Entry.config(state='disabled')
    Second_Entry.config(state='normal')
    Second_Entry.delete('1.0', 'end')
    Second_Entry.config(state='disabled')
    Third_Entry.config(state='normal')
    Third_Entry.delete('1.0', 'end')
    Third_Entry.config(bg="#D3EEFF", fg="#000000")
    Third_Entry.config(state='disabled')
    Fourth_Entry.config(state='normal')
    Fourth_Entry.delete('1.0', 'end')
    Fourth_Entry.config(state='disabled')

def hide_screen():
    First_Entry.place_forget()
    Second_Entry.place_forget()
    Third_Entry.place_forget()
    Fourth_Entry.place_forget()

def unhide_screen():
    First_Entry.place(x=1069.0, y=288.0, width=166.0, height=17.0 )
    Second_Entry.place(x=1069.0, y=307.0, width=166.0, height=18.0)
    Third_Entry.place(x=1069.0, y=327.0, width=166.0, height=17.0)
    Fourth_Entry.place(x=1069.0, y=346.0, width=166.0, height=12.0)
    Last_Entry.place(x=1069.0, y=356.0, width=166.0, height=12.0)

def hide_error_message():
    Third_Entry_ERROR.config(state='normal')
    Third_Entry_ERROR.delete('1.0', 'end')
    Third_Entry_ERROR.place_forget()
    unhide_screen()

def error_message():
    hide_screen()
    Third_Entry_ERROR.place(x=1069.0, y=327.0, width=166.0, height=17.0)
    Third_Entry_ERROR.config(state='normal')
    Third_Entry_ERROR.insert('end', 'ERROR  ')
    Third_Entry_ERROR.config(state='disabled')
    window.after(3000, hide_error_message)

def Change_to_till():
    canvas.place_forget()
    canvasCash.place(x = 0, y = 0)

def Change_to_main():
    canvasCash.place_forget()
    canvas.place(x = 0, y = 0)

#---------- WINDOW -------------------------------------------------------------#

window = Tk()
window.title("Cash Register")

window.geometry("1920x1080")
window.configure(bg = "#BCBCBC")


#---------- Canvas Till -------------------------------------------------------------#

canvasCash = Canvas(
    window,
    bg = "#BCBCBC",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvasCash.place_forget()

#---------- Images till -------------------------------------------------------------#

image_till_1 = PhotoImage(
    file=relative_to_assets("TillImage.png"))
image_1 = canvasCash.create_image(
    0.0,
    0.0,
    anchor='nw',
    image=image_till_1
)



#---------- Buttons till -------------------------------------------------------------#

button_till_image_1 = PhotoImage(
    file=relative_to_assets("CloseButton.png"))
button_till_1 = Button(
    canvasCash,
    image=button_till_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Change_to_main(),
    relief="flat",
)
button_till_1.place(
    x=1745.0,
    y=51.0,
    width=114.0,
    height=119.0
)

button_till_image_2 = PhotoImage(
    file=relative_to_assets("Button(1).png"))
button_till_2 = Button(
    canvasCash,
    image=button_till_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("50EUR"),
    relief="flat",
)
button_till_2.place(
    x=429.0,
    y=545.0,
    width=234.0,
    height=59.0
)

button_till_image_3 = PhotoImage(
    file=relative_to_assets("Button-9.png"))
button_till_3 = Button(
    canvasCash,
    image=button_till_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("20EUR"),
    relief="flat",
)
button_till_3.place(
    x=706.0,
    y=545.0,
    width=234.0,
    height=59.0
)

button_till_image_4 = PhotoImage(
    file=relative_to_assets("Button-10.png"))
button_till_4 = Button(
    canvasCash,
    image=button_till_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("10EUR"),
    relief="flat",
)
button_till_4.place(
    x=973.0,
    y=545.0,
    width=234.0,
    height=59.0
)

button_till_image_5 = PhotoImage(
    file=relative_to_assets("Button-11.png"))
button_till_5 = Button(
    canvasCash,
    image=button_till_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("5EUR"),
    relief="flat",
)
button_till_5.place(
    x=1250.0,
    y=545.0,
    width=234.0,
    height=59.0
)

button_till_image_6 = PhotoImage(
    file=relative_to_assets("Button-1.png"))
button_till_6 = Button(
    canvasCash,
    image=button_till_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("1EUR"),
    relief="flat",
)
button_till_6.place(
    x=439.0,
    y=771.0,
    width=180.0,
    height=59.0
)

button_till_image_7 = PhotoImage(
    file=relative_to_assets("Button-2.png"))
button_till_7 = Button(
    canvasCash,
    image=button_till_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("2EUR"),
    relief="flat",
)
button_till_7.place(
    x=728.0,
    y=771.0,
    width=180.0,
    height=59.0
)

button_till_image_8 = PhotoImage(
    file=relative_to_assets("Button-3.png"))
button_till_8 = Button(
    canvasCash,
    image=button_till_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("0,50EUR"),
    relief="flat",
)
button_till_8.place(
    x=1017.0,
    y=771.0,
    width=180.0,
    height=59.0
)

button_till_image_9 = PhotoImage(
    file=relative_to_assets("Button-4.png"))
button_till_9 = Button(
    canvasCash,
    image=button_till_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("0,20EUR"),
    relief="flat",
)
button_till_9.place(
    x=1296.0,
    y=771.0,
    width=180.0,
    height=59.0
)

button_till_image_10 = PhotoImage(
    file=relative_to_assets("Button-5.png"))
button_till_10 = Button(
    canvasCash,
    image=button_till_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("0,10EUR"),
    relief="flat",
)
button_till_10.place(
    x=1329.0,
    y=1002.0,
    width=180.0,
    height=59.0
)

button_till_image_11 = PhotoImage(
    file=relative_to_assets("Button-6.png"))
button_till_11 = Button(
    canvasCash,
    image=button_till_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("0,05EUR"),
    relief="flat",
)
button_till_11.place(
    x=1017.0,
    y=1002.0,
    width=180.0,
    height=59.0
)

button_till_image_12 = PhotoImage(
    file=relative_to_assets("Button-7.png"))
button_till_12 = Button(
    canvasCash,
    image=button_till_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("0,02EUR"),
    relief="flat",
)
button_till_12.place(
    x=727.0,
    y=1002.0,
    width=180.0,
    height=59.0
)

button_till_image_13 = PhotoImage(
    file=relative_to_assets("Button-8.png"))
button_till_13 = Button(
    canvasCash,
    image=button_till_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("0,01EUR"),
    relief="flat",
)
button_till_13.place(
    x=415.0,
    y=1002.0,
    width=180.0,
    height=59.0
)

#---------- CANVAS -------------------------------------------------------------#

canvas = Canvas(
    window,
    bg = "#BCBCBC",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
#---------- IMAGES -------------------------------------------------------------#


image_image_9 = PhotoImage(
    file=relative_to_assets("table.png"))
image_9 = canvas.create_image(
    953.0,
    700.0,
    image=image_image_9
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    960.0,
    539.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1044.37451171875,
    732.5860595703125,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    879.37451171875,
    731.5860595703125,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    934.37451171875,
    731.5860595703125,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    989.37451171875,
    731.5860595703125,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    730.37451171875,
    731.5860595703125,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    785.37451171875,
    731.5860595703125,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    1156.3935546875,
    731.5860595703125,
    image=image_image_8
)



#---------- BUTTONS -------------------------------------------------------------#

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    canvas,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Clear_button_input(),
    relief="flat",
)
button_1.place(
    x=853.0,
    y=498.0,
    width=53.0,
    height=53.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    canvas,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Feed"),
    relief="flat"
)
button_2.place(
    x=704.0,
    y=498.0,
    width=54.0,
    height=53.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    canvas,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Refound"),
    relief="flat"
)
button_3.place(
    x=704.0,
    y=548.0,
    width=53.0,
    height=51.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    canvas,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Void"),
    relief="flat"
)
button_4.place(
    x=704.0,
    y=596.0,
    width=53.0,
    height=52.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    canvas,
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Program_button_input(),
    relief="flat"
)
button_5.place(
    x=908.0,
    y=498.0,
    width=53.0,
    height=53.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
Dept5_button = Button(
    canvas,
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Department_button_input(Dept5),
    relief="flat"
)
Dept5_button.place(
    x=1018.0,
    y=498.0,
    width=53.0,
    height=53.0
)


button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
Dept4_button = Button(
    canvas,
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Department_button_input(Dept4),
    relief="flat"
)
Dept4_button.place(
    x=1018.0,
    y=548.0,
    width=53.0,
    height=53.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
Dept3_button = Button(
    canvas,
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Department_button_input(Dept3),
    relief="flat"
)
Dept3_button.place(
    x=1018.0,
    y=596.0,
    width=53.0,
    height=53.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
Dept2_button = Button(
    canvas,
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Department_button_input(Dept2),
    relief="flat"
)
Dept2_button.place(
    x=1018.0,
    y=644.0,
    width=53.0,
    height=53.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
Dept1_button = Button(
    canvas,
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Department_button_input(Dept1),
    relief="flat"
)
Dept1_button.place(
    x=1018.0,
    y=693.0,
    width=53.0,
    height=52.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    canvas,
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: X_time(),
    relief="flat"
)
button_11.place(
    x=963.0,
    y=498.0,
    width=53.0,
    height=53.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    canvas,
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Receipt  ON/OFF"),
    relief="flat"
)
button_12.place(
    x=759.0,
    y=498.0,
    width=53.0,
    height=53.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    canvas,
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Change_mode(),
    relief="flat"
)
button_13.place(
    x=1158.0,
    y=499.0,
    width=53.0,
    height=52.0
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    canvas,
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("No Sale"),
    relief="flat"
)
button_14.place(
    x=1103.0,
    y=499.0,
    width=53.0,
    height=52.0
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    canvas,
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("-"),
    relief="flat"
)
button_15.place(
    x=759.0,
    y=548.0,
    width=53.0,
    height=52.0
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    canvas,
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("PO"),
    relief="flat"
)
button_16.place(
    x=1158.0,
    y=548.0,
    width=53.0,
    height=52.0
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    canvas,
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("RA"),
    relief="flat"
)
button_17.place(
    x=1103.0,
    y=548.0,
    width=53.0,
    height=53.0
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    canvas,
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: minus_percent(),
    relief="flat"
)
button_18.place(
    x=759.0,
    y=596.0,
    width=53.0,
    height=52.0
)

button_image_19 = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_19 = Button(
    canvas,
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: plus_percent(),
    relief="flat"
)
button_19.place(
    x=759.0,
    y=644.0,
    width=53.0,
    height=52.0
)

button_image_20 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_20 = Button(
    canvas,
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Clerk"),
    relief="flat"
)
button_20.place(
    x=704.0,
    y=644.0,
    width=53.0,
    height=52.0
)

button_image_21 = PhotoImage(
    file=relative_to_assets("button_21.png"))
Button_7 = Button(
    canvas,
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Fourth_Entry_input(7),
    relief="flat"
)
Button_7.place(
    x=853.0,
    y=548.0,
    width=53.0,
    height=53.0
)

button_image_22 = PhotoImage(
    file=relative_to_assets("button_22.png"))
Button_4 = Button(
    canvas,
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Fourth_Entry_input(4),
    relief="flat"
)
Button_4.place(
    x=853.0,
    y=596.0,
    width=53.0,
    height=53.0
)

button_image_23 = PhotoImage(
    file=relative_to_assets("button_23.png"))
Button_1 = Button(
    canvas,
    image=button_image_23,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Fourth_Entry_input(1),
    relief="flat"
)
Button_1.place(
    x=853.0,
    y=644.0,
    width=53.0,
    height=53.0
)

button_image_24 = PhotoImage(
    file=relative_to_assets("button_24.png"))
Button_8 = Button(
    canvas,
    image=button_image_24,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Fourth_Entry_input(8),
    relief="flat"
)
Button_8.place(
    x=908.0,
    y=548.0,
    width=53.0,
    height=53.0
)

button_image_25 = PhotoImage(
    file=relative_to_assets("button_25.png"))
Button_9 = Button(
    canvas,
    image=button_image_25,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Fourth_Entry_input(9),
    relief="flat"
)
Button_9.place(
    x=963.0,
    y=548.0,
    width=53.0,
    height=53.0
)

button_image_26 = PhotoImage(
    file=relative_to_assets("button_26.png"))
Button_5 = Button(
    canvas,
    image=button_image_26,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Fourth_Entry_input(5),
    relief="flat"
)
Button_5.place(
    x=908.0,
    y=596.0,
    width=53.0,
    height=53.0
)

button_image_27 = PhotoImage(
    file=relative_to_assets("button_27.png"))
Button_6 = Button(
    canvas,
    image=button_image_27,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Fourth_Entry_input(6),
    relief="flat"
)
Button_6.place(
    x=963.0,
    y=596.0,
    width=53.0,
    height=53.0
)

button_image_28 = PhotoImage(
    file=relative_to_assets("button_28.png"))
Button_2 = Button(
    canvas,
    image=button_image_28,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Fourth_Entry_input(2),
    relief="flat"
)
Button_2.place(
    x=908.0,
    y=644.0,
    width=53.0,
    height=53.0
)

button_image_29 = PhotoImage(
    file=relative_to_assets("button_29.png"))
Button_3 = Button(
    canvas,
    image=button_image_29,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Fourth_Entry_input(3),
    relief="flat"
)
Button_3.place(
    x=963.0,
    y=644.0,
    width=53.0,
    height=53.0
)

button_image_30 = PhotoImage(
    file=relative_to_assets("button_30.png"))
button_30 = Button(
    canvas,
    image=button_image_30,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Cheque"),
    relief="flat"
)
button_30.place(
    x=1103.0,
    y=597.0,
    width=53.0,
    height=54.0
)

button_image_31 = PhotoImage(
    file=relative_to_assets("button_31.png"))
Button_0 = Button(
    canvas,
    image=button_image_31,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Fourth_Entry_input(0),
    relief="flat"
)
Button_0.place(
    x=853.0,
    y=692.0,
    width=53.0,
    height=53.0
)

button_image_32 = PhotoImage(
    file=relative_to_assets("button_32.png"))
Button_00 = Button(
    canvas,
    image=button_image_32,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Fourth_Entry_input('00'),
    relief="flat",
)
Button_00.place(
    x=908.0,
    y=692.0,
    width=53.0,
    height=53.0
)

button_image_33 = PhotoImage(
    file=relative_to_assets("button_33.png"))
button_33 = Button(
    canvas,
    image=button_image_33,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("."),
    relief="flat"
)
button_33.place(
    x=963.0,
    y=692.0,
    width=53.0,
    height=53.0
)

button_image_34 = PhotoImage(
    file=relative_to_assets("button_34.png"))
button_34 = Button(
    canvas,
    image=button_image_34,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Tax"),
    relief="flat"
)
button_34.place(
    x=704.0,
    y=692.0,
    width=53.0,
    height=53.0
)

button_image_35 = PhotoImage(
    file=relative_to_assets("button_35.png"))
button_35 = Button(
    canvas,
    image=button_image_35,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Charge"),
    relief="flat"
)
button_35.place(
    x=1158.0,
    y=597.0,
    width=53.0,
    height=55.0
)

button_image_36 = PhotoImage(
    file=relative_to_assets("button_36.png"))
button_36 = Button(
    canvas,
    image=button_image_36,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Conv"),
    relief="flat"
)
button_36.place(
    x=759.0,
    y=692.0,
    width=53.0,
    height=53.0
)

button_image_37 = PhotoImage(
    file=relative_to_assets("button_37.png"))
button_37 = Button(
    canvas,
    image=button_image_37,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Subtotal_button_input(),
    relief="flat"
)
button_37.place(
    x=1103.0,
    y=644.0,
    width=108.0,
    height=53.0
)

button_image_38 = PhotoImage(
    file=relative_to_assets("button_38.png"))
button_38 = Button(
    canvas,
    image=button_image_38,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: CASH_button_input(),
    relief="flat"
)
button_38.place(
    x=1103.0,
    y=692.0,
    width=108.0,
    height=53.0
)

#---------- ENTRY WIDGETS -------------------------------------------------------------#

First_Entry = Text(
    canvas,
    bd=0,
    bg="#D3EEFF",
    fg="#000716",
    highlightthickness=0,
    font=("Merchant Copy DoubleSize", 8),
    state='disabled'
)
First_Entry.place(
    x=1069.0,
    y=288.0,
    width=166.0,
    height=17.0
)

Second_Entry = Text(
    canvas,
    bd=0,
    bg="#D3EEFF",
    fg="#000716",
    highlightthickness=0,
    font=("Merchant Copy DoubleSize", 8),
    state='disabled'
)
Second_Entry.place(
    x=1069.0,
    y=307.0,
    width=166.0,
    height=18.0
)

Third_Entry = Text(
    canvas,
    bd=0,
    bg="#D3EEFF",
    fg="#000716",
    highlightthickness=0,
    font=("Merchant Copy DoubleSize", 8, "bold"),
    state='disabled'
)
Third_Entry.place(
    x=1069.0,
    y=327.0,
    width=166.0,
    height=17.0
)

Fourth_Entry = Text(
    canvas,
    bd=0,
    bg="#D3EEFF",
    fg="#000716",
    highlightthickness=0,
    font=("Merchant Copy DoubleSize", 6),
    state='disabled'
)
Fourth_Entry.place(
    x=1069.0,
    y=346.0,
    width=166.0,
    height=12.0
)

Last_Entry = Text(
    canvas,
    bd=0,
    bg="#D3EEFF",
    fg="#000716",
    highlightthickness=0,
    font=("TkDefaultFont", 7),
    state='disabled'
)
Last_Entry.place(
    x=1069.0,
    y=356.0,
    width=166.0,
    height=12.0
)

Third_Entry_ERROR = Text(
    canvas,
    bd=0,
    bg="#D3EEFF",
    fg="#000716",
    highlightthickness=0,
    font=("Merchant Copy DoubleSize", 8, "bold"),
    state='disabled'
)
Third_Entry_ERROR.pack_forget() 


Subtotal_Entry = Text(
    canvas,
    bd=0,
    bg="#000000",
    fg="#93BA34",
    highlightthickness=0,
    font=("Open 24 Display St", 28),
    state='disabled'
)

Subtotal_Entry.place(
    x=1036,
    y=113,
    width=188,
    height=44,
)
# -------- Entry Till ----------------------------------------------------------------#

First_Entry_till = Text(
    canvasCash,
    bd=0,
    bg="#171916",
    fg="#F5F5F5",
    highlightthickness=0,
    font=("Merchant Copy DoubleSize", 8),
    state='disabled'
)
First_Entry_till.place(
    x=868.0,
    y=51.0,
    width=166.0,
    height=17.0
)

Third_Entry_till = Text(
    canvasCash,
    bd=0,
    bg="#171916",
    fg="#F5F5F5",
    highlightthickness=0,
    font=("Merchant Copy DoubleSize", 8, "bold"),
    state='disabled'
)
Third_Entry_till.place(
    x=868.0,
    y=71.0,
    width=166.0,
    height=17.0
)

# --------- AUTO RUN CODE -------------------------------------------------------------#

Cash_Register_turn_on()
Programmable_buttons = ["Dept1", "Dept2", "Dept3", "Dept4"]

#---------- END -------------------------------------------------------------#

window.resizable(False, False)
window.mainloop()
