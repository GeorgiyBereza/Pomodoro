import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
BUTTON_FONT = (FONT_NAME, 18, "bold")
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    button_start['state'] = "normal"
    global reps
    reps = 0
    window.after_cancel(timer)
    label_timer.config(text="Timer",foreground=GREEN)
    label_checkmark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    button_start['state'] = "disabled"
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    time = 0
    if reps % 2 == 1:
        time = work_sec
        label_timer.config(text="Work", fg=RED)

    elif reps == 8:
        label_timer.config(text="Long break", fg=GREEN)
        time = long_break_sec
        reps = 0
    else:
        time = short_break_sec
        label_timer.config(text="Short break", fg=PINK)

    countdown(time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def add_zeroes(x):
    if x < 10:
        return "0"+str(x)
    else:
        return x
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{add_zeroes(count_min)}:{add_zeroes(count_sec)}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        #counting checkmarks of work sessions
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        label_checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=100,pady=50,background=YELLOW)

canvas = Canvas(width=200, height=224,background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(103,132, text="00:00",fill="white", font=(FONT_NAME, 35,"bold"))
canvas.grid(row=1,column=1)

label_timer = Label(text="Timer",background=YELLOW,font=(FONT_NAME,32,"bold"),foreground=GREEN)
label_timer.grid(row=0, column=1)

label_checkmark = Label(background=YELLOW,font=(FONT_NAME,22,"bold"),foreground=GREEN)
label_checkmark.grid(row=3, column=1)

button_start = Button(text="Start", command=start_timer, font=BUTTON_FONT)
button_start.grid(row=2,column=0)

button_reset = Button(text="Reset", command=reset_timer,font=BUTTON_FONT)
button_reset.grid(row=2,column=2)

window.mainloop()