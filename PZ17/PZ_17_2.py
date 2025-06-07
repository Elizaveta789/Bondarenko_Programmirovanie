# Даны два целых числа A и B (A < B). Вывести в порядке убывания все целые числа,
# расположенные между A и B (не включая числа A и B), а также количество N этих чисел
# решить задачу с помощью tkinter

import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())

        if a >= b - 1:
            result_label.config(text="Нет чисел между A и B.")
            return

        numbers = list(range(b - 1, a, -1))
        result_text = ", ".join(map(str, numbers))
        count = len(numbers)
        result_label.config(text=f"Числа: {result_text}\nКоличество: {count}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите целые числа!")


root = tk.Tk()
root.title("Числа между A и B")
root.geometry("400x200")

tk.Label(root, text="Введите два целых числа (A < B)", font=("Arial", 12, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="A:").grid(row=0, column=0, padx=5)
entry_a = tk.Entry(frame, width=10)
entry_a.grid(row=0, column=1, padx=5)

tk.Label(frame, text="B:").grid(row=0, column=2, padx=5)
entry_b = tk.Entry(frame, width=10)
entry_b.grid(row=0, column=3, padx=5)

btn = tk.Button(root, text="Показать числа", command=calculate)
btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 10), wraplength=350, justify="left")
result_label.pack(pady=10)

root.mainloop()
