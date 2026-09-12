import tkinter as tk

root = tk.Tk()

root.geometry("400x400") # the app's dimensions
root.title("Tic Tac Toe")


button = tk.Button(root, text="Play again")
button.pack(padx=10, pady=10)

root.mainloop()