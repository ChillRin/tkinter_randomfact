import random
import tkinter as tk

facts = [
    "Бананы радиоактивны и излучают небольшое количество гамма-излучения.",
    "Человек может обойтись без пищи до 2 месяцев, а без воды — всего несколько дней.",
    "Голубые киты ежедневно потребляют около 4 тонн пищи.",
    "Пчёлы могут распознавать лица людей.",
    "Существует 6 000 видов бананов, а не только один."
]

github = "https://github.com/ChillRin/tkinter_randomfact"

root = tk.Tk()
root.title("Random Facts")
root.geometry("600x300")

fact_label = tk.Label(root, text="Нажмите на кнупку чтобы увидеть факт", font=("Arial", 12))
fact_label.pack(pady=20)

def show_fact():
    fact = random.choice(facts)
    fact_label.config(text=fact)

show_button = tk.Button(root, text="Показать факт", command=show_fact, font=("Arial", 12))
show_button.pack(pady=20)

root.mainloop()