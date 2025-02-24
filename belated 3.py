import tkinter as tk
from tkinter import messagebox
import os

def open_folder(folder_name):
    folder_contents = {
        "10 Things I Love About You": show_love_list,
        "our memories": lambda: show_placeholder("our memories"),
        "my favorite calls with you": lambda: show_placeholder("my favorite calls with you")
    }
    
    if folder_name in folder_contents:
        folder_contents[folder_name]()
    else:
        messagebox.showerror("Error", "Folder not found!")

def show_folders():
    for widget in root.winfo_children():
        widget.destroy()
    
    tk.Label(root, text="choose a folder mi amore:", font=("Consolas", 19, "bold"), bg="#FFD1DC").pack(pady=10)
    
    folders = ["10 Things I Love About You", "our memories", "my favorite calls with you"]
    for folder in folders:
        tk.Button(root, text=folder, font=("Consolas", 15), bg="#FF69B4", fg="white", width=28, height=2, 
                  command=lambda f=folder: open_folder(f)).pack(pady=5)

def show_love_list():
    for widget in root.winfo_children():
        widget.destroy()
    
    tk.Button(root, text="Back", font=("Consolas", 12), bg="#FF69B4", fg="white", command=show_folders).pack(pady=5)
    
    love_list = [
        "❥ I love the way you talk to me",
        "❥ I love the way you say my name",
        "❥ I love your melodic laugh",
        "❥ I love the way you sing",
        "❥ I love the way you tease me",
        "❥ I love it when you make me laugh",
        "❥ I love sitting behind you on rides",
        "❥ I love the way you touch me",
        "❥ I love how perfectly your body fits with mine",
        "❥ I love your eyes, your hair, your smile, your voice, your walk, your fashion sense, the way you play your guitar, \n   the look on your face when you sleep, your hands, your boobies, your tummy, your cheeks, your nose, your eyes \n   (ik i already said that but that's just how much i love your eyes-)"
    ]
    
    frame = tk.Frame(root, bg="#FFD1DC")
    frame.pack(pady=10)
    
    def reveal_text(index=0):
        if index < len(love_list):
            tk.Label(frame, text=love_list[index], font=("Consolas", 13), bg="#FFD1DC", wraplength=400, justify="left").pack(anchor="w", pady=2)
            root.after(900, lambda: reveal_text(index + 1))
    
    reveal_text()

def show_placeholder(folder_name):
    for widget in root.winfo_children():
        widget.destroy()
    
    tk.Button(root, text="Back", font=("Consolas", 13), bg="#FF69B4", fg="white", command=show_folders).pack(pady=5)
    
    tk.Label(root, text=f"coming soon when I’m not drowning in exams\n(patience)", font=("Consolas", 15, "bold"), bg="#FFD1DC", wraplength=400, justify="center").pack(pady=20)

def next_message(index):
    if index < len(messages):
        label.config(text=messages[index])
        root.after(2000, lambda: next_message(index + 1))
    else:
        button.pack(pady=20)

root = tk.Tk()
root.title("for loml")
root.geometry("500x550")
root.configure(bg="#FFD1DC")

messages = ["hi, love", "here's your belated valentine's gift!", "hope you like it-\n(fingers crossed)", "hehehehehhehehe, go on-"]
label = tk.Label(root, text="", font=("Consolas", 18, "bold"), bg="#FFD1DC")
label.pack(pady=30)

button = tk.Button(root, text="CLICK ME", font=("Consolas", 20), bg="#FF69B4", fg="white", command=show_folders)
button.pack_forget()

next_message(0)
root.mainloop()
