from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None # set global variable for timer

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    # reset timer using global variable
    window.after_cancel(timer)
    # reset canvas text
    canvas.itemconfig(timer_text, text="00:00")
    # reset title label
    title_label.config(text="Timer")
    # reset check marks
    check_label.config(text="")
    # reset reps
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    # start the reps
    global reps
    reps += 1

    # set the title depending on the reps
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # get mins and seconds
    mins = math.floor(count / 60)
    secs = count % 60

    # format mins and secs to show 0n if less then 10
    if mins < 10:
        mins = f"0{mins}"
    if secs < 10:
        secs = f"0{secs}"

    canvas.itemconfig(timer_text, text=f"{mins}:{secs}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        # use window.after to change value of canvas timer evry second
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#labels

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)


# canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png") # read png using tk.photoimage
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)







window.mainloop()











