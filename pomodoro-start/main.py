from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
check_mark = '✔'
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_function():
    global reps
    window.after_cancel(timer)
    reset_time = '00:00'
    reset_checkmarks = '✔'
    reset_title = 'Timer'
    label.config(text=reset_title)
    check_mark_label.config(text=reset_checkmarks)
    check_mark_label.grid(row=3, column=1)
    canvas.itemconfig(text, text=reset_time)
    reps = 1



# ---------------------------- TIMER MECHANISM ------------------------------- #

def timer_mechanism():
    global reps
    global check_mark
    print(reps)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 8:
        start_function(long_break_sec)
        label.config(text="Long Break")
        check_mark_label.config(text=check_mark)
        check_mark_label.grid(row=3, column=1)
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        start_function(work_sec)
        label.config(text="Timer")
    elif reps == 2 or reps == 4 or reps == 6:
        start_function(short_break_sec)
        label.config(text="Break")
        check_mark_label.config(text=check_mark)
        check_mark_label.grid(row=3, column=1)
        check_mark += '✔'

    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def start_function(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(10, start_function, count - 1)
    if reps > 8:
        reset_function()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('POMODORO')
window.config(bg=YELLOW, padx=50, pady=50)

label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45))
label.grid(row=0, column=1)

canvas = Canvas(width=210, height=224, highlightthickness=0, bg=YELLOW)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
text = canvas.create_text(100, 112, text=f"{WORK_MIN}:00", font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

check_mark_label = Label(fg=GREEN, bg=YELLOW, font=15)

start_button = Button(text='Start', bg=YELLOW, command=timer_mechanism)
start_button.grid(column=0, row=2)


reset_button = Button(text='Reset', bg=YELLOW, command=reset_function)
reset_button.grid(column=2, row=2)



window.mainloop()
