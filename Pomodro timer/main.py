
from tkinter import *
import time,math
# ---------------------------- CONSTANTS ------------------------------- #
# for color picking:- https://colorhunt.co/
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#1875d2"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5 
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    win.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    head.config(text="Timer",font=(FONT_NAME,40,"bold"),fg=GREEN,bg=YELLOW)
    global marks,reps
    marks=''
    reps=0
    check_mark.config(text="",font=(20),fg=GREEN,bg=YELLOW)
    


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1
    work_secs=WORK_MIN *60
    short_break=SHORT_BREAK_MIN *60
    long_break=LONG_BREAK_MIN*60

    if reps%8==0:
        countdown(long_break)
        head.config(text="Break",font=(FONT_NAME,40,"bold"),fg=RED,bg=YELLOW)
        canvas.itemconfig(pic, image=snorlax_pic) 
    elif reps%2==0:
        countdown(short_break)
        head.config(text="Break",font=(FONT_NAME,40,"bold"),fg=PINK,bg=YELLOW)
        canvas.itemconfig(pic, image=snorlax_pic) 
    else:
        countdown(work_secs)
        head.config(text="Work",font=(FONT_NAME,40,"bold"),fg=GREEN,bg=YELLOW)
        canvas.itemconfig(pic, image=goku_pic) 
        
        
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min=math.floor(count/60)
    count_sec=count%60

    if count_sec<10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=win.after(1000,countdown,count-1)
    else:
        start_timer()
        marks=""
        work_Sessions=math.floor(reps/2)
        for _ in range(work_Sessions):
            marks+="✔"
        check_mark.config(text=marks,font=(20),fg=GREEN,bg=YELLOW)

# ---------------------------- UI SETUP ------------------------------- #
win=Tk()
win.title("Pomodoro")
win.config(padx=100,pady=50,bg=YELLOW,) 




head=Label(text="Timer",font=(FONT_NAME,40,"bold"),fg=GREEN,bg=YELLOW)
head.grid(row=0,column=1)

canvas=Canvas(width=220,height=230,bg=YELLOW,highlightthickness=0)
snorlax_pic=PhotoImage(file="snorlax.png")
goku_pic=PhotoImage(file="pngwing.com.png")
pic=canvas.create_image(115,112,image=snorlax_pic)
timer_text=canvas.create_text(105,105,text="00:00",fill="black",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)



but1=Button(text="Start",font=(FONT_NAME,),highlightthickness=0,command=start_timer)
but1.grid(row=2,column=0)

but2=Button(text="Reset",font=(FONT_NAME,),highlightthickness=0,command=reset)
but2.grid(row=2,column=2)

check_mark=Label(text="",font=(20),fg=GREEN,bg=YELLOW)
check_mark.grid(row=3,column=1)

win.mainloop()
