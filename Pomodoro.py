# What is a Pomodoro Timer ? --> [Click Here](https://en.wikipedia.org/wiki/Pomodoro_Technique)


from tkinter import *
import math
from tkinter import messagebox

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checks = ""
timer = None
message = yes = no = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    global checks
    window.after_cancel(timer)
    timer_label.config(text="Timer",fg=GREEN)
    canvas.itemconfig(text_can,text="00:00")
    check_mark.config(text="",highlightthickness=0)
    checks=""
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_counting():
    global reps
    reps+=1
    work_count_down = WORK_MIN * 60
    short_break_count_down = SHORT_BREAK_MIN * 60
    long_break_count_down = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Long Break", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=PINK)
        window.config(padx=37,pady=50,bg=YELLOW)
        count_down(long_break_count_down)
    elif reps % 2 == 0:
        timer_label.config(text="Break", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
        count_down(short_break_count_down)
    else:
        timer_label.config(text="Work", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=RED)
        count_down(work_count_down)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    timer_min = math.floor(count / 60)
    timer_sec = count % 60
    if timer_sec < 10:
        timer_sec = f"0{timer_sec}"

# --------------or---------------- #
    # if timer_sec == 0:
    #     timer_sec = "00"
    # if 0 < int(timer_sec) < 10:
    #     timer_sec = f"0{timer_sec}"

    canvas.itemconfig(text_can,text = f"{timer_min}:{timer_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down,count - 1)
    else:
        start_counting()
        if reps%2==0:
            global checks
            checks += "✓ "
            check_mark.config(text=f"{checks}", fg=GREEN, font=("Arial", 15, "bold"), bg=YELLOW,border=3,highlightbackground="black",highlightthickness=1)


# ---------------------------- WINDOW EXIT ------------------------------- #

def exit_screen():
    is_ok = messagebox.askokcancel(title="Exit?",message="Are you sure you want to Quit ?")
    
    if is_ok:
        window.destroy()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200,height=223,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,111,image=tomato_img)
text_can = canvas.create_text(100,130,text="00:00",font=(FONT_NAME,35,"bold"),fill="white")

canvas.grid(column=1,row=3)

# Timer Label
timer_label = Label(text="Timer",font=(FONT_NAME,40,"bold"),bg=YELLOW,fg=GREEN)
timer_label.grid(column=1,row=2)

# start button
start_button = Button(text="START",command=start_counting,fg="green")
start_button.grid(column=0,row=4)

# exit button
exit_button = Button(text="Quit",command=exit_screen,fg="red")
exit_button.grid(column=2,row=2)


# reset button
reset_button = Button(text="RESET",command=reset_timer,fg="orange")
reset_button.grid(column=2,row=4)

# check mark ✓
check_mark = Label(fg=GREEN,font=("Arial",15,"bold"),bg=YELLOW)
check_mark.grid(column=1,row=7)


window.mainloop()