from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=False)
card_front_img = PhotoImage(file="images/card_back.png")
canvas.create_image((400, 263), image=card_front_img)
canvas.config(background=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=3, rowspan=8)

title = Label(text="Title", font=("italic", 12), background=BACKGROUND_COLOR)
title.grid(row=2, column=1)

word = Label(text="Title", font=("italic", 12), background=BACKGROUND_COLOR)
word.grid(row=4, column=1)


button_red_img = PhotoImage(file="images/wrong.png")
button_red = Button(image=button_red_img, highlightthickness=False)
button_red.grid(row=8, column=0)

button_green_img = PhotoImage(file="images/right.png")
button_green = Button(image=button_green_img, highlightthickness=False)
button_green.grid(row=8, column=2)



window.mainloop()