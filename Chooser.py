import random
import time
import tkinter as tk
from tkinter import messagebox

def choose_name_surname(mentees_list):
    chosen_person = random.choice(mentees_list)
    return chosen_person

def choose_and_display_name_surname():
    countdown_label.config(text="Ready?", fg="blue")
    countdown_label.config(text="3", fg="red")
    root.update()
    time.sleep(1)
    countdown_label.config(text="2", fg="orange")
    root.update()
    time.sleep(1)
    countdown_label.config(text="1", fg="green")
    root.update()
    time.sleep(1)

    chosen_name, chosen_surname = choose_name_surname(mentees)
    messagebox.showinfo("Chosen Mentee", f"Chosen name: {chosen_name}\nChosen surname: {chosen_surname}")

# Lista de mentees
mentees = [("Kevin Adrian", "Flores Merino"), ("Fabricio Alonso", "Lanche Pacsi"), ("Paulo Isael", "Miranda Barrientos"), ("Joaquín André", "Ocaña Aniya"),("Jhogan Haldo", "Pachacutec Aguilar"),("Anyeli Azumi", "Tamara Ureta"), ("Juan Carlos", "Ticlia Maqui"),("Mario", "Urpay Enriquez")]

# Graphical Interface
root = tk.Tk()
root.title("Random Mentee Chooser")
root.geometry("400x300")
root.configure(background='#f0f0f0')

title_label = tk.Label(root, text="Random Mentee Chooser", font=("Helvetica", 18), bg='#f0f0f0', fg='#333')
title_label.pack(pady=20)

countdown_label = tk.Label(root, text="", font=("Helvetica", 14), bg='#f0f0f0')
countdown_label.pack(pady=50)

choose_button = tk.Button(root, text="Choose Mentee", command=choose_and_display_name_surname, bg="#4CAF50", fg="white", relief="raised", font=("Helvetica", 12))
choose_button.pack(pady=30)
root.mainloop()
