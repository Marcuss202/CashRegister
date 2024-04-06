
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import RIGHT, Tk, Canvas, Entry, Text, Button, PhotoImage
import pyglet

# replace 'font.ttf' with your ttf file 
pyglet.font.add_file('D:\\GitHub\\CashRegister\\merchant-copy-doublesize.ttf')


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\GitHub\CashRegister\CashRegister\.git\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#---------- FUNCTIONS -------------------------------------------------------------#

def Fourth_Entry_input(number):
    Fourth_Entry.config(state='normal')  # Editable mode
    Fourth_Entry.insert('end', number)  # Insert number
    Fourth_Entry.config(state='disabled')  # Read-only mode

def Department_button_input(department):
    Fourth_Entry.config(state='normal')
    last_entered_number = int(Fourth_Entry.get('1.0', 'end-1c'))  # Convert to int instead of float
    last_entered_number = last_entered_number / 100  # Divide by 100 to get the correct decimal place
    last_entered_number = "{:.2f}".format(last_entered_number)  # Format as a string with 2 decimal places
    num_spaces = max(0, 27 - len(department) - len(str(last_entered_number))) # Calculate the number of spaces needed
    Fourth_Entry.delete('1.0', 'end')  # Add the start and end indices
    Fourth_Entry.insert('end', department)  # Insert the department
    Fourth_Entry.insert('end', " " * num_spaces + last_entered_number)  
    Fourth_Entry.config(state='disabled')
    print(last_entered_number)

    

#---------- WINDOW -------------------------------------------------------------#

window = Tk()

window.geometry("1920x1080")
window.configure(bg = "#BCBCBC")

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

#---------- IMAGES -------------------------------------------------------------#

canvas.place(x = 0, y = 0)
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
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Clear"),
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
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Prog"),
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
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Department_button_input("GROCERYS"),
    relief="flat"
)
button_6.place(
    x=1018.0,
    y=498.0,
    width=53.0,
    height=53.0
)


button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Department_button_input("CLOTHES"),
    relief="flat"
)
button_7.place(
    x=1018.0,
    y=548.0,
    width=53.0,
    height=53.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Department_button_input("ELECTRONICS"),
    relief="flat"
)
button_8.place(
    x=1018.0,
    y=596.0,
    width=53.0,
    height=53.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Department_button_input("MISC"),
    relief="flat"
)
button_9.place(
    x=1018.0,
    y=644.0,
    width=53.0,
    height=53.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Dept.1"),
    relief="flat"
)
button_10.place(
    x=1018.0,
    y=693.0,
    width=53.0,
    height=52.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("X/Time (X)"),
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
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Mode"),
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
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("-%"),
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
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("+%"),
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
    image=button_image_37,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Subtotal"),
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
    image=button_image_38,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Cash"),
    relief="flat"
)
button_38.place(
    x=1103.0,
    y=692.0,
    width=108.0,
    height=53.0
)

#---------- ENTRY WIDGETS -------------------------------------------------------------#

Top_Entry = Text(
    canvas,
    bd=0,
    bg="#D3EEFF",
    fg="#000716",
    highlightthickness=0,
    state='disabled'
)
Top_Entry.place(
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




#---------- END -------------------------------------------------------------#

window.resizable(False, False)
window.mainloop()
