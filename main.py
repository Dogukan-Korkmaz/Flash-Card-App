from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
rnd = {}
to_lern = {}

try:
    data = pandas.read_csv("data/words_to_lern.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


def create_new_card():
    global rnd, flip_timer
    window.after_cancel(flip_timer)
    rnd = random.choice(data_dict)
    canvas.itemconfig(card_title, text="French", fill="white")
    canvas.itemconfig(card_word, text=rnd["French"], fill="white")
    canvas.itemconfig(card, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=rnd["English"], fill="black")
    canvas.itemconfig(card, image=card_back_img)


def is_known():
    data_dict.remove(rnd)
    known_data = pandas.DataFrame(data_dict)
    known_data.to_csv("data/words_to_lern.csv", index=False)

    create_new_card()


window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=False)
card_front_img = PhotoImage(file="images/card_back.png")
card_back_img = PhotoImage(file="images/card_front.png")
card = canvas.create_image((400, 263), image=card_front_img)
canvas.config(background=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=3, rowspan=8)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 32, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 65, "bold"))

button_red_img = PhotoImage(file="images/wrong.png")
button_red = Button(image=button_red_img, command=create_new_card)
button_red.grid(row=8, column=0)

button_green_img = PhotoImage(file="images/right.png")
button_green = Button(image=button_green_img, command=is_known)
button_green.grid(row=8, column=2)

create_new_card()

window.mainloop()
