from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_COLOR = "#FFFFFF"
random_word = {}
french_dictionary = {}

window = Tk()
window.title("French Falsh Cards")

window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

try:
    data = pandas.read_csv("data/words_to_learn.csv")
    french_dictionary = data.to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    french_dictionary = data.to_dict(orient="records")

# card image
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
# titles
language = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text=random_word, font=("Arial", 60, "bold"))

def generate_random_word():
    global random_word
    canvas.itemconfig(language, text="French", fill="black")
    random_word =random.choice(french_dictionary)
    canvas.itemconfig(word, text=random_word["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    timer()
    
def flip_card():
    canvas.itemconfig(language, text="English", fill=FONT_COLOR)
    canvas.itemconfig(word, text=random_word["English"], fill=FONT_COLOR)
    canvas.itemconfig(card_background, image=card_back_img)   
    
def is_known():
    french_dictionary.remove(random_word)
    data = pandas.DataFrame(french_dictionary)
    data.to_csv("data/words_to_learn.csv", index=False)
    generate_random_word()

def timer():
    window.after(5000, flip_card)

# buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=generate_random_word)
wrong_button.grid(column=0, row=1)

canvas.grid(column=0, row=0, columnspan=2)

generate_random_word()
timer()
window.mainloop()

