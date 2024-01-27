import tkinter as tk
from tkinter import messagebox
import os, shutil

def submit_forms():
    global guild_id
    global bot_token
    guild_id = guild_id_entry.get()
    bot_token = bot_token_entry.get()
    
    print("Guild ID:", guild_id)
    print("Bot Token:", bot_token)
    
    messagebox.showinfo("Success", "Forms submitted successfully!")

    root.destroy()

root = tk.Tk()
root.title("App")
root.geometry("300x200")
root.resizable(False, False)

guild_id_label = tk.Label(root, text="Guild ID:")
guild_id_label.pack()

guild_id_entry = tk.Entry(root)
guild_id_entry.pack()

bot_token_label = tk.Label(root, text="Bot Token:")
bot_token_label.pack()

bot_token_entry = tk.Entry(root)
bot_token_entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit_forms)
submit_button.pack()

root.mainloop()


with open("temp.txt", "r") as file:
    file_contents = file.read()

file_contents = file_contents.replace("{token}", f"\"{bot_token}\"").replace("{guildid}", guild_id)

with open("Client.py", "w") as file:
    file.write(file_contents)

os.system("pyinstaller --onefile Client.py")

os.remove("Client.py")
shutil.rmtree("build")
os.remove("temp2.spec")
