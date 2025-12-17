import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Ma première GUI")

label = tk.Label(fenetre, text="Bonjour Tkinter !")
label.pack()

fenetre.mainloop()
