#-------------------------------------------------------------------------------
# Name:        othello
# Purpose:     CS project
#
# Author:      Aditya Vashista
#
#
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#
import turtle,os
from time import sleep
import winsound
from turtle import *
title("THE GAME OF OTHELLO")
setup(1000,625)
turtle.pen(fillcolor="black", pencolor="red", pensize=3)
bgcolor("Dark Slate Blue")
bgcolor()
up()
#
class Box_dont_exist(Exception):
    pass
#
class Box_Occupied_already(Exception):
    pass
#
def Winner_Sound():
    winsound.Beep(640, 50)
    winsound.SND_NOSTOP
    winsound.Beep(800, 50)
    winsound.SND_NOSTOP
    winsound.Beep(1000, 50)
    winsound.SND_NOSTOP
    winsound.Beep(1300, 50)
#
def Move_Token_Sound():
    winsound.Beep(1000,10)
    winsound.SND_NOSTOP
#
def Bad_Sound():
    winsound.Beep(500, 700)
    sleep(1)
#
def draw_square(h,k):
    speed(0)
    goto(h,k)
    down()
    color("")
    hideturtle()
    pencolor("black")
    for i in range(4):
        forward(70)
        left(90)
    up()
#
def draw_token(h,k,c):
    goto(h+35,k+20)
    down()
    speed(0)
    pensize=1
    begin_fill()
    color(c)
    pencolor("red")
    circle(20)
    end_fill()
    up()
    Move_Token_Sound()
#
def draw_board(box_codes):
    speed(0)
    turtle.goto(-420,-280)
    down()
    begin_fill()
    color("red")
    pencolor("black")
    for i in range(4):
        forward(560)
        left(90)
    end_fill()
    up()
    for i in box_codes.values():
        x=i.x
        y=i.y
        draw_square(x,y)
    draw_token(box_codes["E4"].x,box_codes["E4"].y,box_codes["E4"].value)
    draw_token(box_codes["D5"].x,box_codes["D5"].y,box_codes["D5"].value)
    draw_token(box_codes["E5"].x,box_codes["E5"].y,box_codes["E5"].value)
    draw_token(box_codes["D4"].x,box_codes["D4"].y,box_codes["D4"].value)
    goto(-260,280)
    down()
    color("snow")
    write("Virtual Othello", font = ("OCR A Extended", 20, "bold"))
    up()
    x=-450
    y=-250
    goto(x,y)
    down()
    write("A", font = ("OCR A Extended", 25, "bold"))
    up()
    y+=70
    goto(x,y)
    down()
    write("B", font = ("OCR A Extended", 25, "bold"))
    up()
    y+=70
    goto(x,y)
    down()
    write("C", font = ("OCR A Extended", 25, "bold"))
    up()
    y+=70
    goto(x,y)
    down()
    write("D", font = ("OCR A Extended", 25, "bold"))
    up()
    y+=70
    goto(x,y)
    down()
    write("E", font = ("OCR A Extended", 25, "bold"))
    up()
    y+=70
    goto(x,y)
    down()
    write("F", font = ("OCR A Extended", 25, "bold"))
    up()
    y+=70
    goto(x,y)
    down()
    write("G", font = ("OCR A Extended", 25, "bold"))
    up()
    y+=70
    goto(x,y)
    down()
    write("H", font = ("OCR A Extended", 25, "bold"))
    up()
    x=-385
    y=-330
    goto(x,y)
    down()
    write("1", font = ("OCR A Extended", 25, "bold"))
    up()
    x+=70
    goto(x,y)
    down()
    write("2", font = ("OCR A Extended", 25, "bold"))
    up()
    x+=70
    goto(x,y)
    down()
    write("3", font = ("OCR A Extended", 25, "bold"))
    up()
    x+=70
    goto(x,y)
    down()
    write("4", font = ("OCR A Extended", 25, "bold"))
    up()
    x+=70
    goto(x,y)
    down()
    write("5", font = ("OCR A Extended", 25, "bold"))
    up()
    x+=70
    goto(x,y)
    down()
    write("6", font = ("OCR A Extended", 25, "bold"))
    up()
    x+=70
    goto(x,y)
    down()
    write("7", font = ("OCR A Extended", 25, "bold"))
    up()
    x+=70
    goto(x,y)
    down()
    write("8", font = ("OCR A Extended", 25, "bold"))
    up()

#
class box:
    def __init__(self,x,y,code):
        self.x=x
        self.y=y
        self.code=code
        self.value=()
#
def black_n_white(box_codes):
    b=0
    w=0
    for i in box_codes.values():
        if i.value!=():
            if i.value=="black":
                b+=1
            else:
                w+=1
    up()
    speed()
    goto(200,-270)
    down()
    begin_fill()
    color("Dark Slate Blue")
    hideturtle()
    pencolor("Dark Slate Blue")
    for i in range(2):
        forward(250)
        left(90)
        forward(70)
        left(90)
    end_fill()
    up()
    b=str(b)
    w=str(w)
    color("snow")
    up()
    speed()
    goto(200,-240)
    down()
    write("Black Tokens= "+b, font = ("OCR A Extended", 16, "bold"))
    up()
    goto(200,-260)
    down()
    write("White Tokens= "+w, font = ("OCR A Extended", 16, "bold"))
    up()
#
def Rules_N_Guidelines():
    color("gold")
    up()
    goto(200,280)
    down()
    write("Rules & GUIDELINES:", font = ("OCR A Extended", 20, ("bold","underline","italic")))
    up()
    color("green2")
    goto(200,-150)
    down()
    write("""
    (1) THE OBJECTIVE OF THE
    GAME IS TO GET MAX NO.
    OF YOUR COLOR TOKENS ON
    THE BOARD AT THE END OF
    THE GAME
    (2) The INPUT OF THE BOX SHOULD
    IN FORM JI ONLY;WHERE J=A,B,C,D,
    E,F,G OR H & I=1,2,3,4,5,6,7 OR 8
    (3) WHEN EVER THERE ARE 4 OR
    MORE THAN 4 TOKENS OF SAME COLOR
    CONSECUTIVELY ALONG A DIAGONAL,
    ROW, COLUMN; THEN ALL THE TOKENS
    IN A LINE CONNETED AT THE END OF
    THE SERIES WILL CHANGE THERE
    COLOR INTO THAT OF THE COLOUR OF
    THE SERIES.
    (4) Players take alternate turns.
    EACH PLAYER GETS 32 CHANCES""", font = ("OCR A Extended", 15, ("bold","italic")))
    up()

#
box_codes={}
row=["1","2","3","4","5","6","7","8"]
column=["A","B","C","D","E","F","G","H"]
x_p=-490
y_p=-350
for j in column:
    y_p+=70
    x_p=-490
    for i in row:
        x_p+=70
        box_codes[j+i]=box(x_p,y_p,j+i)
#
box_codes["E4"].value="black"
box_codes["D5"].value="black"
box_codes["E5"].value="snow"
box_codes["D4"].value="snow"

draw_board(box_codes)
Winner_Sound()
Rules_N_Guidelines()
#
Diagonal_Relation1=[["A1","B2","C3","D4","E5","F6","G7","H8"],["B1","C2","D3","E4","F5","G6","H7"],["C1","D2","E3","F4","G5","H6"],["D1","E2","F3","G4","H5"],["E1","F2","G3","H4"],["A2","B3","C4","D5","E6","F7","G8"],["A3","B4","C5","D6","E7","F8"],["A4","B5","C6","D7","E8"],["A5","B6","C7","D8"]]
Diagonal_Relation2=[["D1","C2","B3","A4"],["E1","D2","C3","B4","A5"],["F1","E2","D3","C4","B5","A6"],["G1","F2","E3","D4","C5","B6","A7"],["H1","G2","F3","E4","D5","C6","B7","A8"],["H2","G3","F4","E5","D6","C7","B8"],["H3","G4","F5","E6","D7","C8"],["H4","G5","F6","E7","D8"],["H5","G6","F7","E8"]]
#
print("INPUT SCREEN")
Player1=input("Enter name of Player 1: ")
Player2=input("Enter name of Player 2: ")
print("Color of Player 1 tokens are BLACK....")
print("Color of Player 2 tokens are WHITE....")
print("Player 1 wil make the first move, followed by player 2!!")
#
color("snow")
up()
goto(200,-180)
down()
write("Player 1: "+Player1, font = ("OCR A Extended", 16, "bold"))
color("snow")
up()
goto(200,-200)
down()
write("Player 2: "+Player2, font = ("OCR A Extended", 16, "bold"))
up()
#
token=1
black_n_white(box_codes)

while token<65:
#
    if token%2!=0:
        while True:
            try:
                move=input("Enter the box where Player 1 would like to place the token: ")
                if move in box_codes:
                    if box_codes[move].value==():
                        box_codes[move].value="black"
                        break
                    else:
                        raise Box_Occupied_already
                else:
                    raise Box_dont_exist
            except Box_Occupied_already:
                print("The given box is already occupied!!! Please enter another box code...")
            except Box_dont_exist:
                print("The given box doesn't exist!!! Please enter valid box code....")
    else:
         while True:
            try:
                move=input("Enter the box where Player 2 would like to place the token: ")
                if move in box_codes:
                    if box_codes[move].value==():
                        box_codes[move].value="snow"
                        break
                    else:
                        raise Box_Occupied_already
                else:
                    raise Box_dont_exist
            except Box_Occupied_already:
                print("The given box is already occupied!!! Please enter another box code...")
            except Box_dont_exist:
                print("The given box doesn't exist!!! Please enter valid box code....")
    draw_token(box_codes[move].x,box_codes[move].y,box_codes[move].value)
#
    row_tokens_count=0
    row_elements_to_be_changed=[]
    c_none=0
    no_of_elements_out_8=0
    for i in row:
        no_of_elements_out_8+=1
        s=move[0]+i
        if box_codes[s].value!=box_codes[move].value:
            if row_tokens_count<4:
                row_tokens_count=0
            if box_codes[s].value!=():
                if c_none==0 :
                    row_elements_to_be_changed.append(s)
            elif box_codes[s].value==():
                if no_of_elements_out_8<5:
                    row_tokens_count=0
                    row_elements_to_be_changed=[]
                else:
                    c_none=1
        else:
            if c_none==0:
                row_tokens_count+=1
                row_elements_to_be_changed.append(s)
    if row_tokens_count>3:
        for z in row_elements_to_be_changed:
            Bad_Sound()
            box_codes[z].value=box_codes[move].value
            draw_token(box_codes[z].x,box_codes[z].y,box_codes[z].value)

#
    column_tokens_count=0
    column_elements_to_be_changed=[]
    c_none=0
    no_of_elements_out_8=0
    for j in column:
        no_of_elements_out_8+=1
        s=j+move[1]
        if box_codes[s].value!=box_codes[move].value:
            if column_tokens_count<4:
                column_tokens_count=0
            if box_codes[s].value!=():
                if c_none==0 :
                    column_elements_to_be_changed.append(s)
            elif box_codes[s].value==():
                if no_of_elements_out_8<5:
                    column_tokens_count=0
                    column_elements_to_be_changed=[]
                else:
                    c_none=1
        else:
            if c_none==0:
                column_tokens_count+=1
                column_elements_to_be_changed.append(s)
    if column_tokens_count>3:
        for z in column_elements_to_be_changed:
            Bad_Sound()
            box_codes[z].value=box_codes[move].value
            draw_token(box_codes[z].x,box_codes[z].y,box_codes[z].value)
#
    diagonal_tokens_count=0
    diagonal_elements_to_be_changed=[]
    c_none=0
    no_of_elements_out_8=0
    for digonal1 in Diagonal_Relation1:
        if move in digonal1:
            for s in digonal1:
                no_of_elements_out_8+=1
                if box_codes[s].value!=box_codes[move].value:
                    if diagonal_tokens_count<4:
                        diagonal_tokens_count=0
                    if box_codes[s].value!=():
                        if c_none==0 :
                            diagonal_elements_to_be_changed.append(s)
                    elif box_codes[s].value==():
                        if no_of_elements_out_8<5:
                            diagonal_tokens_count=0
                            diagonal_elements_to_be_changed=[]
                        else:
                            c_none=1
                else:
                    if c_none==0:
                        diagonal_tokens_count+=1
                        diagonal_elements_to_be_changed.append(s)
    if diagonal_tokens_count>3:
        Bad_Sound()
        for z in diagonal_elements_to_be_changed:
            box_codes[z].value=box_codes[move].value
            draw_token(box_codes[z].x,box_codes[z].y,box_codes[z].value)
#
    diagonal_tokens_count=0
    diagonal_elements_to_be_changed=[]
    c_none=0
    no_of_elements_out_8=0
    for digonal2 in Diagonal_Relation2:
        if move in digonal2:
            for s in digonal2:
                no_of_elements_out_8+=1
                if box_codes[s].value!=box_codes[move].value:
                    if diagonal_tokens_count<4:
                        diagonal_tokens_count=0
                    if box_codes[s].value!=():
                        if c_none==0 :
                            diagonal_elements_to_be_changed.append(s)
                    elif box_codes[s].value==():
                        if no_of_elements_out_8<5:
                            diagonal_tokens_count=0
                            diagonal_elements_to_be_changed=[]
                        else:
                            c_none=1
                else:
                    if c_none==0:
                        diagonal_tokens_count+=1
                        diagonal_elements_to_be_changed.append(s)
    if diagonal_tokens_count>3:
        Bad_Sound()
        for z in diagonal_elements_to_be_changed:
            box_codes[z].value=box_codes[move].value
            draw_token(box_codes[z].x,box_codes[z].y,box_codes[z].value)
    black_n_white(box_codes)

    token+=1

Winner_Sound()
b=0
w=0
for i in box_codes.values():
    if i.value!=():
        if i.value=="black":
            b+=1
        else:
            w+=1
up()
speed()
goto(180,-300)
color("turquoise1")
down()
if b>w:
    write("WINNER: "+Player1, font = ("OCR A Extended", 30, ("bold","italic","underline")))
elif w>b:
    write("WINNER: "+Player2, font = ("OCR A Extended", 30, ("bold","italic","underline")))
else:
    write("DRAW", font = ("OCR A Extended", 30, ("bold","italic","underline")))

Winner_Sound()

os.system("pause")
mainloop()
