import tkinter

import bot
import customtkinter
from pathlib import Path
from tkinter import Tk, Canvas, Entry, PhotoImage
from bot import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.geometry("400x400")
window.configure(bg="#7C4040")
window.title("Slido Bot")

canvas = Canvas(
    window,
    bg="#7C4040",
    height=400,
    width=400,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    200.5,
    250.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F1F5FF",
    fg="#000716",
    font="Elephant",
    justify='center',
    highlightthickness=0
)
entry_1.place(
    x=40.0,
    y=220.0,
    width=321.0,
    height=50.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    200.5,
    180.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F1F5FF",
    fg="#000716",
    font="Elephant",
    justify='center',
    highlightthickness=0
)
entry_2.place(
    x=40.0,
    y=150.0,
    width=321.0,
    height=50.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    200.5,
    110.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#F1F5FF",
    fg="#000716",
    font="Elephant",
    justify='center',
    highlightthickness=0
)
entry_3.place(
    x=40.0,
    y=80.0,
    width=321.0,
    height=50.0
)
entry_1.insert(0, "Amount of threads")
entry_2.insert(0, "XPath")
entry_3.insert(0, "Room Hash")

canvas.create_text(
    97.0,
    6.0,
    anchor="nw",
    text="Slido Bot",
    fill="#3AB2F6",
    font=("Elephant", 48 * -1)
)
tmp = threads_controller()
button = customtkinter.CTkButton(window, font=("Elephant", 18), text="Start the Bot", fg_color="#3A7FF6",
                                 corner_radius=50, width=180, height=55,
                                 command=lambda: tmp.thread_start(entry_1, entry_2, entry_3, window, ))
button.grid(row=0, column=0, padx=110, pady=308)

window.resizable(False, False)
window.mainloop()
