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
CHECKMARK = "✓"

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #


def create_button(txt):
    button = Button(text=txt, highlightthickness=0)
    return button


def create_label(txt):
    label = Label(text=txt, fg=GREEN, bg=YELLOW)
    return label


def setup_window():
    window = Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=50, bg=YELLOW)
    return window


def create_canvas(img):
    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    canvas.create_image(100, 112, image=img)
    canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    return canvas


def main():
    window = setup_window()
    image = PhotoImage(file="tomato.png")

    canvas = create_canvas(image)
    canvas.grid(column=1, row=1)

    timer_label = create_label("Timer")
    timer_label.config(font=(FONT_NAME, 50))
    timer_label.grid(column=1, row=0)

    check_label = create_label(CHECKMARK)
    check_label.grid(column=1, row=3)

    start_button = create_button("Start")
    start_button.grid(column=0, row=2)

    reset_button = create_button("Reset")
    reset_button.grid(column=2, row=2)
    window.mainloop()


main()
