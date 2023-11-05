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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #


def setup_window():
    window = Tk()
    window.title("Pomodoro")
    return window


def create_canvas(img):
    canvas = Canvas(width=200, height=224)
    canvas.create_image(100, 112, image=img)
    return canvas


def main():
    window = setup_window()
    image = PhotoImage(file="tomato.png")
    canvas = create_canvas(image)
    canvas.pack()
    window.mainloop()


main()
