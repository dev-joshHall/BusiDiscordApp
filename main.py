
from tkinter import ttk, messagebox, IntVar, StringVar, Toplevel, filedialog, Text
import tkinter as tk
from User import User
from Server import Server
#  from PIL import Image, ImageTk


class MainWindow:
    def __init__(self, master: tk.Tk, user):
        self.master = master
        self.user = user
        self.master.title("BusiDiscord")
        self.master.geometry("1000x600+100+50")
        self.master.resizable(width=True, height=True)
        style = ttk.Style()
        style.configure("style.TFrame", background="#E61E50")

        self.top_nav = ttk.Frame(self.master, borderwidth=1)
        self.top_nav.pack(side=tk.TOP, anchor="w")
        self.left_nav = ttk.Frame(self.master, borderwidth=1)
        self.left_nav.pack(side=tk.LEFT, anchor="nw")
        self.body = ttk.Frame(self.master, borderwidth=1, width=800, height=500)
        self.body.pack(anchor="nw")
        self.home_btn = ttk.Button(self.top_nav, text="Home", command=self.home_display)
        self.home_btn.pack(side=tk.LEFT, padx=0, anchor="w")
        self.friends_btn = ttk.Button(self.top_nav, text="Friends", command=self.friends_display)
        self.friends_btn.pack(side=tk.LEFT)
        self.messages_btn = ttk.Button(self.top_nav, text="Messages", command=self.messages_display)
        self.messages_btn.pack(side=tk.LEFT)
        self.servers_btn = ttk.Button(self.top_nav, text="Servers", command=self.servers_display)
        self.servers_btn.pack(side=tk.LEFT)
        # add server buttons on the left

        self.server_btns = []
        for server in self.user.servers:
            button = ttk.Button(self.left_nav, text=server.name)
            self.server_btns.append(button)
            button.pack(side=tk.TOP, anchor="n")

        self.home_display()  # start at home on login

    def home_display(self):
        self.clear_body()
        ttk.Label(self.body, text="Welcome to", font=("Garamond", 50)).pack(anchor="w")
        ttk.Label(self.body, text="BusiDiscord", font=("Garamond", 60)).pack(anchor="w")

    def friends_display(self):
        self.clear_body()
        ttk.Label(self.body, text="Friends", font=("Garamond", 32)).pack(anchor="w")
        ttk.Button(self.body, text="Add Friend").pack(anchor="w")
        inner_frame = ttk.Frame(self.body)
        inner_frame.pack(anchor="w")
        friend_btns = []
        for friend in self.user.friends:
            button = ttk.Button(inner_frame, text=friend.uname)
            friend_btns.append(button)
            button.pack(side=tk.TOP, anchor="n")

    def messages_display(self):
        self.clear_body()

    def servers_display(self):
        self.clear_body()

    def clear_body(self):
        """
        Clears the body frame of all widgets
        """
        for widget in self.body.winfo_children():
            widget.destroy()


def main():
    root = tk.Tk()
    server = Server("minecraft", [], [])
    user = User("noobmaster", "nmaster@gmail.com", "pass1234")
    user.servers.append(server)
    user.friends.append(User("asdf", "daf@gamil.com", "password"))
    window = MainWindow(root, user)
    root.mainloop()


if __name__ == "__main__":
    main()
