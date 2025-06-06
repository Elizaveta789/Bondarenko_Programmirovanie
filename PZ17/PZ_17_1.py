import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Форма заявки на работу в зоопарке")
root.geometry("600x700")


title = tk.Label(root, text="Форма заявки на работу в зоопарке", font=("Arial", 16, "bold"))
title.pack(pady=10)

subtitle = tk.Label(root, text="Пожалуйста, заполните форму. Обязательные поля помечены *", fg="black")
subtitle.pack()


frame1 = tk.LabelFrame(root, text="Контактная информация", padx=20, pady=10)
frame1.pack(fill="x", padx=20, pady=10)

tk.Label(frame1, text="Имя *").grid(row=0, column=0, sticky="w", pady=5)
entry_name = tk.Entry(frame1, width=40)
entry_name.grid(row=0, column=1, pady=5)

tk.Label(frame1, text="Телефон").grid(row=1, column=0, sticky="w", pady=5)
entry_phone = tk.Entry(frame1, width=40)
entry_phone.grid(row=1, column=1, pady=5)

tk.Label(frame1, text="Email *").grid(row=2, column=0, sticky="w", pady=5)
entry_email = tk.Entry(frame1, width=40)
entry_email.grid(row=2, column=1, pady=5)


frame2 = tk.LabelFrame(root, text="Персональная информация", padx=10, pady=10)
frame2.pack(fill="x", padx=20, pady=10)

tk.Label(frame2, text="Возраст *").grid(row=0, column=0, sticky="w", pady=5)
entry_age = tk.Entry(frame2, width=20)
entry_age.grid(row=0, column=1, pady=5)

tk.Label(frame2, text="Пол").grid(row=1, column=0, sticky="w", pady=5)
gender = ttk.Combobox(frame2, values=["Женщина", "Мужчина"], state="readonly", width=17)
gender.current(0)
gender.grid(row=1, column=1, pady=5)

tk.Label(frame2, text="Перечислите личные качества").grid(row=2, column=0, sticky="nw", pady=5)
text_traits = tk.Text(frame2, height=4, width=40)
text_traits.grid(row=2, column=1, pady=5)



frame3 = tk.LabelFrame(root, text="Выберите ваших любимых животных", padx=10, pady=10)
frame3.pack(fill="x", padx=20, pady=10)

animals = ["Зебра", "Кошка", "Анаконда", "Человек",
           "Слон", "Антилопа", "Голубь", "Краб"]

animal_vars = []
for index, animal in enumerate(animals):
    var = tk.BooleanVar()
    chk = tk.Checkbutton(frame3, text=animal, variable=var)
    chk.grid(row=index // 4, column=index % 4, sticky="w", padx=5, pady=2)
    animal_vars.append(var)

submit_btn = tk.Button(root, text="Отправить информацию", width=25)
submit_btn.pack(pady=20)

root.mainloop()
