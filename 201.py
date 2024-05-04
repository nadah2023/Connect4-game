import tkinter as tk
import sys
from PIL import ImageTk, Image
from tkinter import messagebox
from Connect_4 import Game
from easy import easy
from meduim_ai import meduim
from hard import Hard
from AI_c import AI

def our_computer_fun():
    # Create a new window for the menu selection
    menu_window = tk.Toplevel(root)
    menu_window.title("Menu Selection")

    # Set window size
    window_width = 800
    window_height = 500
    screen_width = menu_window.winfo_screenwidth()
    screen_height = menu_window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    menu_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

    # Load background image
    background_image = Image.open("Banners.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # Create background label
    background_label = tk.Label(menu_window, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create label for the menu
    menu_label = tk.Label(menu_window, text="Please select a menu option:", font=("Helvetica", 20))
    menu_label.pack(pady=20)

    # Create title label
    title_label = tk.Label(menu_window, text=" choose option ", font=("Helvetica", 20))
    title_label.pack(side="top", anchor="nw", pady=0, padx=10)

    # Function to handle the menu selection
    def menu_option_selected(option):
        messagebox.showinfo("Option Selected", f"You selected: {option}")
        menu_window.destroy()
        if option == "Esay":
            easy()
        elif option == "medium":
            meduim()
        elif option =="hard":
             Hard()    
           

    # Create buttons for the menu options
    button_font = ("Helvetica", 12)

    Esay_button = tk.Button(menu_window, text="Esay", command=lambda: menu_option_selected("Esay"),
                                   width=15, height=2, font=button_font, bg="blue", fg="black")
    Esay_button.pack(side="top", anchor="nw", pady=20, padx=10)

    medium_button = tk.Button(menu_window, text="medium", command=lambda: menu_option_selected("medium"),
                                width=15, height=2, font=button_font, bg="orange", fg="black")
    medium_button.pack(side="top", anchor="nw", pady=20, padx=10)

    hard_button = tk.Button(menu_window, text="hard", command=lambda: menu_option_selected("hard"),
                                width=15, height=2, font=button_font, bg="red", fg="black")
    hard_button.pack(side="top", anchor="nw", pady=20, padx=10)
    
    menu_window.mainloop()


def RULE_mode():
    # Create a new window for the menu selection
    menu_window = tk.Toplevel(root)
    menu_window.title("Menu Selection")

    # Set window size
    window_width = 400
    window_height = 300
    screen_width = menu_window.winfo_screenwidth()
    screen_height = menu_window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    menu_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

    # Load background image
    background_image = Image.open("meun_1.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # Create background label
    background_label = tk.Label(menu_window, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)


    # Create label for the menu
    menu_label = tk.Label(menu_window, text="RULE", font=("Helvetica", 20))
    menu_label.pack(pady=20)
    # Create label for the rules
    rules_text = "Connect 4 is a two-player game where the goal is to form a line of four of your own colored discs in a row, column, or diagonal. Players take turns dropping one colored disc into a grid. The disc will fall to the lowest empty space in the selected column. The first player to create a line of four discs wins the game."
    rules_label = tk.Label(menu_window, text=rules_text, font=("Helvetica", 12), wraplength=350)
    rules_label.pack(pady=10)

    # Create a button to close the window
    close_button = tk.Button(menu_window, text="Close", command=menu_window.destroy, font=button_font,bg="blue")
    close_button.pack(pady=10)
    menu_window.mainloop()
def AI_r():
    AI()
    
def two_player_fun():
    Game()
    
root = tk.Tk()
root.title("Connect 4")

# Set window size
window_width = 1000
window_height = 480
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

# Load background image
background_image = Image.open("Banners.jpg")

background_photo = ImageTk.PhotoImage(background_image)

# Create background label
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create title label
title_label = tk.Label(root, text="Welcome to Connect 4", font=("Helvetica", 20))
title_label.pack(pady=20)


# Create title label
title_label = tk.Label(root, text="Choose the option", font=("Helvetica", 20))
title_label.pack(side="top", anchor="nw", pady=0, padx=11)

# Create buttons with spacing
#button_padx = 20
#button_pady = 10
button_font = ("Helvetica", 12)

two_player_fun_button = tk.Button(root, text="two player", command=two_player_fun, width=15, height=2, font=button_font,bg="blue")
two_player_fun_button.pack(side="top", anchor="nw", pady=20, padx=10)

our_computer_button = tk.Button(root, text="our computer", command=our_computer_fun, width=15, height=2, font=button_font,bg="yellow")
our_computer_button.pack(side="top", anchor="nw", pady=10, padx=10)

sample_button = tk.Button(root, text="Sample Game", command=AI_r, width=15, height=2, font=button_font,bg="red")
sample_button.pack(side="top", anchor="nw", pady=20, padx=10)

RULE_button = tk.Button(root, text="Rule", command=RULE_mode, width=15, height=2, font=button_font,bg="white")
RULE_button.pack(side="top", anchor="nw", pady=20, padx=10)


root.mainloop()
