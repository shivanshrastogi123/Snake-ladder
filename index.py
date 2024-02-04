import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import random
import time 
import threading
from tkinter import messagebox
import time
win=Tk()
win.geometry('320x250')
win.title("Gamers :-) ")
win.resizable(False,False)
win.configure(bg='grey')

def name():
    if name1.get=="" or name2.get()=="":
        messagebox.showwarning("Warning","Please enter the player  name")
    else:
        win.destroy()

name1=StringVar()
name2=StringVar()
ex=Label(win,text="1st player->  ",font=('arial',12,'bold')).place(x=10,y=10)
ex=Label(win,text="2st player->  ",font=('arial',12,'bold')).place(x=10,y=50)

n1=Entry(win,width=20,bd=7,bg='orange',textvariable=name1,font='bold').place(x=100,y=10)
n2=Entry(win,width=20,bd=7,bg='white',textvariable=name2,font='bold').place(x=100,y=50)


ok=Button(win,text='Go',width=25,bg='green',bd=7,command=name).place(x=60,y=100)
win.mainloop()


def func(event):
    pass
def left():
    msg=messagebox.askquestion('Warning',"Are you sure to quit the game?")
    if msg=='yes':
        root.destroy()
    else:
        messagebox.showinfo("Return","you will now return to the application.")
def stategame():
    global imdice
    global dice
    global b1,b2
    b1.place(x=700,y=375)
    b2.place(x=700,y=450)
    time.sleep(1)
#add buttons 
    
    b3=tk.Button(root,text="Click here to end the Game ",cursor='hand2',bg='yellow' ,bd=13, foreground='red',width=35,height=5,activebackground='green',activeforeground='white',command=left).place(x=700,y=100)
    b4=tk.Button(root,text="Restart",cursor="hand2",bg="olive",bd=13,foreground="black",activebackground="black",command=restart).place(x=850,y=250)
#dice
    imdice=Image.open("diceroll1.png")
    imdice.resize((65,65))
    imdice=ImageTk.PhotoImage(imdice)
    bdice=tk.Button(root,image=imdice,bd=5,border=3,bg='red').place(x=700,y=245)

def restart():
    mssg=messagebox.askquestion("Warning","Are you sure to restart the game?")
    if mssg=="yes":
        reset_coins()
    

def reset_coins():
    global p1,p2
    global pos1,pos2
    p1.place(x=0,y=650)
    p2.place(x=50,y=650)
    pos1=0
    pos2=0
def dice_im():
    global dice
    names=['1.png','2.png','3.png','4.png','5.png','6.png']
    for num in names:
        imdice=Image.open(""+num)
        imdice=imdice.resize((65,65))
        imdice=ImageTk.PhotoImage(imdice)
        dice.append(imdice)

def check_ladder(Turn):
    global pos1,pos2
    global ladder

    f=0
    if Turn==1:
        if pos1 in ladder:
            pos1=ladder[pos1]
            f=1
    else:
        if pos2 in ladder:
            pos2=ladder[pos2]
            f=1
    return f 

def check_snake(Turn):
    global pos1,pos2
    if Turn==1:
        if pos1 in snake:
            pos1=snake[pos1]
    else:
        if pos2 in snake:
            pos2=snake[pos2]
def cut(Turn):
    global pos1,pos2
    global p1,p2
    if Turn==1:
        if pos1==pos2:
            p2.place(x=50,y=600)
            pos2=0
    else:
        if pos2==pos1:
            p1.place(x=0,y=600)
            pos1=0
    
def  roll_dice1():
    return random.randint(1,6)      
def roll_dice():
    global dice
    global turn
    global pos2,pos1
    global b1,b2
    r=roll_dice1()
    

    bdice=tk.Button(root,image=dice[r-1],height=80,width=80).place(x=700,y=245)
    lad=0
    if turn==1:
        #time.sleep(0.6)
        demo=pos1
        c=1
        if r==6:
            c+=1
        if c==4:
            pos1=demo
        if pos1>95:
            if r==6:
                turn=2
                b1.configure(state='disabled')
                b2.configure(state='normal')
        if (pos1+r<=100):
            
            pos1+=r
        lad=check_ladder(turn)
        cut(turn)
        check_snake(turn)
        move_coin(turn,pos1)
        if r!=6:
            turn=2
            b1.configure(state='disabled')
            b2.configure(state='normal')

    else:
        #time.sleep(0.6)
        demo1=pos2
        c1=1
        if r==6:
            c1+=1
        if c1==4:
            pos2=demo1
        if pos2>95:
            if r==6:
                turn=1
                b2.configure(state='disabled')
                b1.configure(state='normal')
        if (pos2+r<=100):
            
            pos2+=r
        lad=check_ladder(turn)
        cut(turn)
        check_snake(turn)
        move_coin(turn,pos2)
        if r!=6:
            turn=1
            b2.configure(state='disabled')
            b1.configure(state='normal')

    is_winner()         
def is_winner():
    global pos1,pos2
    if pos1==100:
        time.sleep(1)
        msg="{} is the Winner ".format(name1.get())
        lab=tk.Label(root,text=msg,height=2,width=20,bg='red',font=('Cursive',30,'bold'))
        lab.place(x=300,y=300)
        reset_coins()
        msg1=messagebox.askquestion("??","Do you want to play again?")
        if msg1=='yes':
            
            lab.destroy()
            reset_coins()
            turn=1
            b1.configure(state='normal')
            b2.configure(state='disabled')
        else:
            root.destroy()

    elif pos2==100:
        msg="{} is the winner ".format(name2.get())
        lab=tk.Label(root,text=msg,height=2,width=20,bg='red',font=('Cursive',30,'bold'))
        lab.place(x=300,y=300)
        lab.after(2000,lab.destroy())

        reset_coins()
        msg1=messagebox.askquestion("??","Do you want to play again?")
        if msg1=='yes':
            lab.config(text='')
            reset_coins()
            turn=1
            b1.configure(state='normal')
            b2.configure(state='disabled')
        else:
            root.destroy()
def move_coin(Turn, r):
    global p1,p2
    global Index
    if Turn==1:
        p1.place(x=Index[r][0],y=Index[r][1])
    else:
        p2.place(x=Index[r][0],y=Index[r][1])

def move_slow(trun,r):
    global p1,p2
    global Index
    x=Index[r][0]
    while True:
        time.sleep(0.1)

threading.Thread(target=lambda:move_slow().start())

def get_index():
    global p1,p2
    Num=[100,99,98,97,96,95,94,93,92,91,81,82,83,84,85,86,87,88,89,90,80,79,78,77,76,75,74,73,72,71,61,62,63,64,65,66,67,68,69,70,60,59,58,57,56,55,54,53,52,51,41,42,43,44,45,46,47,48,49,50,40,39,38,37,36,35,34,33,32,31,21,22,23,24,25,26,27,28,29,30,20,19,18,17,16,15,14,13,12,11,1,2,3,4,5,6,7,8,9,10]
    '''p1.place(x=135,y=20)
    p2.place(x=495,y=500)'''
    row=20
    col=50
    i=0
    for x in range(1,11):
        col=50
        for y in range(1,11):
            Index[Num[i]]=(col,row)
            col=col+61
            i+=1
        row+=64
    
dice=[]
Index={}

#initial ostion

pos1=None
pos2=None

#ladder 
ladder={1:38,4:14,9:31,21:42,28:84,51:67,72:91,80:99}


#Snakes
snake={17:7,54:34,62:19,64:60,87:36,93:73,95:75,98:79}

root=tk.Tk()
root.title("Snakes and Ladder :-)")
root.geometry('1000x700')
f=tk.Frame(root,width=1000,height=800,relief='raised',bg="brown").place(x=0,y=0)
root.configure(bg='brown')
# add image 
im=tk.PhotoImage(file="snake4.png")
lab=tk.Label(f,image=im ,border=20,bg='black').place(x=20,y=5)

im1=tk.PhotoImage(file="snakepic3.png")
lab=tk.Label(f,image=im1 ,border=20,bg='brown').place(x=800,y=550)

#buttons 
b1=tk.Button(root,text=name1.get(),bg='light blue' ,bd=5,foreground='black',cursor='hand2',width=15,height=3,activebackground='red',activeforeground='black',command=roll_dice)
b2=tk.Button(root,text=name2.get(),bg='red' ,bd=5,foreground='black',cursor='hand2',width=15,height=3,activebackground='light blue',activeforeground='black',command=roll_dice)
b1.bind('<Key>',func)
b2.bind('<Key>',func)

#player 1
p5=tk.PhotoImage(file="blueludo1.png")
p1=tk.Label(root,image=p5,bd=5)

#player 2
p6=tk.PhotoImage(file="redludo4.png")
p2=tk.Label(root,image=p6,bd=5)

turn=1
reset_coins()
get_index()
dice_im()
stategame()
root.mainloop()