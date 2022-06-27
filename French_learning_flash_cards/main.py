from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

current_card={} # create empty dict
learning_words = {} # initial learrning words

#--------------------brain ------------------------------------

try:
    data_df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError: # if running for first time read from origninal french words data
    original_data = pandas.read_csv("data/french_words.csv")
    learning_words = original_data.to_dict(orient="records")
else:

    learning_words = data_df.to_dict(orient="records")
# this creates a list [{french:word,english:meaning},...]


def card_next():
    global current_card,timer_flip
    window.after_cancel(timer_flip) # cancel the timer when card is clicked
    current_card = choice(learning_words) #
    canvas.itemconfig(title,text = "French",fill="black")
    canvas.itemconfig(word,text = current_card["French"],fill="black")
    canvas.itemconfig(background,image=front_image)
    timer_flip = window.after(3000,func =card_flip) # set up new flip timer to wait for 3 secs

def card_flip():
    canvas.itemconfig(title,text = "English", fill="white")
    canvas.itemconfig(word,text = current_card["English"],fill="white")
    canvas.itemconfig(background,image=back_image)

def known_words():
    learning_words.remove(current_card)
    data = pandas.DataFrame(learning_words)
    data.to_csv("data/words_to_learn.csv",index=False)
    # index is false to avoid multiple columns of indexes being created each time the function is run
    card_next()

#--------------------UI Interface------------------------------------

window = Tk()
window.title("Flash cards")
window.config(padx = 50, pady=50, bg=BACKGROUND_COLOR)

#auto flip
timer_flip = window.after(3000,func =card_flip) # run the cardflip after 3 seconds

# Canvas
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
background = canvas.create_image(400,263,image=front_image)

title = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))

word = canvas.create_text(400,263,text="",font=("Ariel",60 ,"bold"))
canvas.grid(column=0,row=0, columnspan=2)

# buttons
wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image,highlightthickness=0,command=card_next)
unknown_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image,highlightthickness=0,command=known_words)
known_button.grid(column=1, row=1)

card_next()

window.mainloop()
