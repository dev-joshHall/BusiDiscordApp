
from tkinter import ttk, messagebox, IntVar, StringVar, Toplevel, filedialog, Text
import tkinter as tk
#  from PIL import Image, ImageTk


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("BusiDiscord")
        self.master.geometry("1000x600+100+50")
        self.master.resizable(width=True, height=True)

        style = ttk.Style()
        style.configure("style.TFrame", background="#E61E50")


if __name__ == "__main__":
    root = tk.Tk()
    window = MainWindow(root)
    root.mainloop()
    print("hi")
    print("hi")
