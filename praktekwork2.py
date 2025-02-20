import tkinter as tk
import random

def pick_winner():
    names = [entry1.get(), entry2.get(), entry3.get()]
    winner = random.choice(names)
    result_label.config(text=f"Переможець: {winner}")

def set_bg_color(color):
    app.config(bg=color)
    entry1.config(bg=color)
    entry2.config(bg=color)
    entry3.config(bg=color)
    result_label.config(bg=color)

app = tk.Tk()
app.title("Додаток вибору переможця")

entry1 = tk.Entry(app, font=('Arial', 12), bg='lightyellow', fg='black')
entry1.pack(pady=5)
entry2 = tk.Entry(app, font=('Arial', 12), bg='lightyellow', fg='black')
entry2.pack(pady=5)
entry3 = tk.Entry(app, font=('Arial', 12), bg='lightyellow', fg='black')
entry3.pack(pady=5)

pick_button = tk.Button(app, text="случайний переможечь", font=('Arial', 14), bg='lightblue', fg='black', command=pick_winner)
pick_button.pack(pady=20)

result_label = tk.Label(app, text="", font=('Arial', 14), bg='white', fg='red')
result_label.pack(pady=5)

menu = tk.Menu(app)
app.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Вихід", command=app.quit)

help_menu = tk.Menu(menu)
menu.add_cascade(label="Допомога", menu=help_menu)
help_menu.add_command(label="Про програму", command=lambda: tk.messagebox.showinfo("Про програму", "Це простий додаток на tkinter для вибору переможця."))

color_menu = tk.Menu(menu)
menu.add_cascade(label="Змінити фон", menu=color_menu)
color_menu.add_command(label="Синій", command=lambda: set_bg_color('blue'))
color_menu.add_command(label="Червоний", command=lambda: set_bg_color('red'))
color_menu.add_command(label="Чорний", command=lambda: set_bg_color('black'))
color_menu.add_command(label="Білий", command=lambda: set_bg_color('white'))
color_menu.add_command(label="Зелений", command=lambda: set_bg_color('green'))

app.mainloop()





