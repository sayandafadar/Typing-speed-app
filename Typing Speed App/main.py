from tkinter import *
from tkinter import messagebox
from essential_generators import DocumentGenerator
import sys

# ---------------------------- CONSTANTS ------------------------------- #

gen = DocumentGenerator()
new_paragraph = gen.paragraph(min_sentences=10, max_sentences=16)
print(new_paragraph)

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
typed_word = 0
accurate_words = None


# ---------------------------- TIMER RESET ------------------------------- #
def paragraph():
    global new_paragraph
    new_paragraph = gen.paragraph(min_sentences=10, max_sentences=16)
    text_samp.config(text=new_paragraph)


def inputed_words():
    global accurate_words
    t = new_paragraph.split()
    words = input_text.get()
    word_set = words.split()
    accurate_words = len(set(t) & set(word_set))
    print(accurate_words)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_down(1 * 60)


def close(event):
    window.withdraw()
    sys.exit()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # print(count)
    global accurate_words
    if count < 10:
        canvas.itemconfig(timer_text, text=f"00:0{count}")
    else:
        canvas.itemconfig(timer_text, text=f"00:{count}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    elif count == 0:
        inputed_words()
        messagebox.showinfo(title="hello", message=f"Your have typed {accurate_words} words\nin one minute.\n"
                                                   f"Your typing speed is {accurate_words} words per minute.")
        input_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Typing Speed")
fullscreen = window.attributes("-fullscreen", True)
window.bind('<Escape>', close, fullscreen)
window.config(padx=200, pady=4, bg=YELLOW)

title_label = Label(text="Test Your Speed", fg=RED, bg=YELLOW, font=('Times', 40))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=220, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="typing.png")
canvas.create_image(100, 78, image=tomato_img)
timer_text = canvas.create_text(106, 84, text="00:00", fill=RED, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=1)

reset_button = Button(text="Reset", highlightthickness=0, command=paragraph)
reset_button.grid(column=2, row=1)

sample_text_label = Label(text="SAMPLE TEXT", fg=RED, bg=YELLOW, font=(FONT_NAME, 14))
sample_text_label.grid(column=1, row=2)

text_samp = Message(text=new_paragraph, width=1030, bg=YELLOW, font=('Arial', 18))
text_samp.grid(column=1, row=4)

sample_text_label = Label(text="Type your text_samp below", fg=RED, bg=YELLOW, font=(FONT_NAME, 15))
sample_text_label.grid(column=1, row=6, pady=10)

input_text = Entry(width=58, bg=YELLOW, font=('Arial', 18))
input_text.focus()
input_text.grid(column=1, row=8)
window.mainloop()
