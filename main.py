import sys
import os
from tkinter import *
from tkinter import Tk
from PIL import Image, ImageTk

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def tk():
    root = Tk()
    root.attributes("-topmost", True)
    root.title("Калькулятор")
    root.geometry("400x657+100+100")
    root.attributes("-toolwindow", False)
    root.resizable(False, False)
    root.configure(bg="#1c1c1c")
    root.overrideredirect(True)

    window_history = None
    history = []
    clear_on_next_input = False

    title_bar = Frame(root, bg="#01622B", relief="raised", bd=0)
    title_bar.pack(side=TOP, fill=X)

    original_icon = Image.open(resource_path("icon.png"))
    resized_icon = original_icon.resize((20, 20), Image.Resampling.LANCZOS)
    icon = ImageTk.PhotoImage(resized_icon)

    icon_label = Label(title_bar, image=icon, bg="#01622B")
    icon_label.image = icon
    icon_label.pack(side=LEFT, padx=0)
    
    title_label = Label(title_bar, text="Калькулятор", bg="#01622B", fg="white", font=("Arial", 12))
    title_label.pack(side=LEFT, padx=0)

    close_button = Button(title_bar, text="X", bg="#FF5C5C", fg="white", bd=0, font=("Arial", 13),
                          command=root.destroy)
    close_button.pack(side=RIGHT, padx=3, pady=2, ipady=0, ipadx=2)

    def move_window(event):
        x = root.winfo_pointerx() - root._offset_x
        y = root.winfo_pointery() - root._offset_y
        root.geometry(f"+{x}+{y}")
    
    def start_move(event):
        root._offset_x = event.x
        root._offset_y = event.y

    title_bar.bind("<Button-1>", start_move)
    title_bar.bind("<B1-Motion>", move_window)
        
    entry = Entry(root, width=13, font=("Arial", 40), bg="#01622B", fg="white", bd=0, justify="right", 
                  highlightbackground="#003315", highlightcolor="#008F3C", highlightthickness=3)
    entry.pack(pady=(5, 0), fill=X, ipady=40)

    def handle_keyboard_input(event):
        nonlocal clear_on_next_input
        if clear_on_next_input:
            entry.delete(0, END)
            clear_on_next_input = False

    entry.bind("<Key>", handle_keyboard_input)

    def insert_number(number):
        nonlocal clear_on_next_input
        if clear_on_next_input:
            entry.delete(0, END)
            clear_on_next_input = False
        entry.insert(END, number)

    def insert_operator(operator):
        nonlocal clear_on_next_input
        if entry.get() == "":
            return
        if entry.get()[-1] in "+-*/":
            entry.delete(len(entry.get()) - 1)
        entry.insert(END, operator)
        clear_on_next_input = False

    frame = Frame(root, bg="#003315", bd=1)
    frame.pack(fill=BOTH, expand=True, padx=2, pady=(5, 5))

    button_1 = Button(frame, text="1", width=5, height=2, font=("Arial", 20), bg="#1c1c1c", fg="white", bd=0,
                      activebackground="#008F3C", activeforeground="white",
                      command=lambda: insert_number("1"))
    button_1.grid(row=2, column=0, padx=7, pady=4)

    button_2 = Button(frame, text="2", width=5, height=2, font=("Arial", 20), bg="#1c1c1c", fg="white", bd=0,
                      activebackground="#008F3C", activeforeground="white",
                      command=lambda: insert_number("2"))
    button_2.grid(row=2, column=1, padx=7, pady=4)

    button_3 = Button(frame, text="3", width=5, height=2, font=("Arial", 20), bg="#1c1c1c", fg="white", bd=0,
                      activebackground="#008F3C", activeforeground="white",
                      command=lambda: insert_number("3"))
    button_3.grid(row=2, column=2, padx=7, pady=4)

    button_4 = Button(frame, text="4", width=5, height=2, font=("Arial", 20), bg="#1c1c1c", fg="white", bd=0,
                      activebackground="#008F3C", activeforeground="white",
                      command=lambda: insert_number("4"))
    button_4.grid(row=3, column=0, padx=4, pady=4)

    button_5 = Button(frame, text="5", width=5, height=2, font=("Arial", 20), bg="#1c1c1c", fg="white", bd=0,
                      activebackground="#008F3C", activeforeground="white",
                      command=lambda: insert_number("5"))
    button_5.grid(row=3, column=1, padx=4, pady=4)

    button_6 = Button(frame, text="6", width=5, height=2, font=("Arial", 20), bg="#1c1c1c", fg="white", bd=0,
                      activebackground="#008F3C", activeforeground="white",
                      command=lambda: insert_number("6"))
    button_6.grid(row=3, column=2, padx=4, pady=4)

    button_7 = Button(frame, text="7", width=5, height=2, font=("Arial", 20), bg="#1c1c1c", fg="white", bd=0,
                      activebackground="#008F3C", activeforeground="white",
                      command=lambda: insert_number("7"))   
    button_7.grid(row=4, column=0, padx=4, pady=4)

    button_8 = Button(frame, text="8", width=5, height=2, font=("Arial", 20), bg="#1c1c1c", fg="white", bd=0,
                      activebackground="#008F3C", activeforeground="white",
                      command=lambda: insert_number("8"))
    button_8.grid(row=4, column=1, padx=4, pady=4)

    button_9 = Button(frame, text="9", width=5, height=2, font=("Arial", 20), bg="#1c1c1c", fg="white", bd=0,
                      activebackground="#008F3C", activeforeground="white",
                      command=lambda: insert_number("9"))
    button_9.grid(row=4, column=2, padx=4, pady=4)

    button_0 = Button(frame, text="0", width=5, height=2, font=("Arial", 20), bg="#1c1c1c", fg="white", bd=0,
                      activebackground="#008F3C", activeforeground="white",
                      command=lambda: insert_number("0"))
    button_0.grid(row=5, column=1, padx=4, pady=4)

    button_plus = Button(frame, text="+", width=5, height=2, font=("Arial", 20), bg="#1c1c1c", fg="white", bd=0,
                         activebackground="#008F3C", activeforeground="white",
                         command=lambda: insert_operator("+"))
    button_plus.grid(row=2, column=3, padx=4, pady=4)

    button_minus = Button(frame, text="-", width=5, height=2, font=("Arial", 20), bg="#1c1c1c", fg="white", bd=0,
                         activebackground="#008F3C", activeforeground="white",
                         command=lambda: insert_operator("-"))
    button_minus.grid(row=3, column=3, padx=4, pady=4)

    button_multiply = Button(frame, text="*", width=5, height=2, font=("Arial", 20), bg="#1c1c1c", fg="white", bd=0,
                            activebackground="#008F3C", activeforeground="white",
                            command=lambda: insert_operator("*")) 
    button_multiply.grid(row=4, column=3, padx=4, pady=4)

    button_divide = Button(frame, text="/", width=5, height=2, font=("Arial", 20), bg="#1c1c1c", fg="white", bd=0,
                         activebackground="#008F3C", activeforeground="white",
                         command=lambda: insert_operator("/"))
    button_divide.grid(row=5, column=3, padx=4, pady=4)

    button_clear = Button(frame, text="C", width=5, height=2, font=("Arial", 20), bg="#1c1c1c", fg="white", bd=0,
                         activebackground="#008F3C", activeforeground="white",
                         command=lambda: entry.delete(0, END))
    button_clear.grid(row=1, column=2, padx=4, pady=4)

    button_erase = Button(frame, text="⌫", width=5, height=2, font=("Arial", 20), bg="#1c1c1c", fg="white", bd=0,
                         activebackground="#008F3C", activeforeground="white",
                         command=lambda: entry.delete(len(entry.get())-1))
    button_erase.grid(row=1, column=3, padx=4, pady=4)

    button_dot = Button(frame, text=".", width=5, height=2, font=("Arial", 20), bg="#1c1c1c", fg="white", bd=0,
                        activebackground="#008F3C", activeforeground="white",
                        command=lambda: entry.insert(END, "."))
    button_dot.grid(row=5, column=0, padx=4, pady=4)

    button_percent = Button(frame, text="%", width=5, height=2, font=("Arial", 20), bg="#1c1c1c", fg="white", bd=0,
                         activebackground="#008F3C", activeforeground="white",
                         command=lambda: entry.insert(END, "%"))
    button_percent.grid(row=1, column=0, padx=4, pady=4)

    button_square = Button(frame, text="x²", width=5, height=2, font=("Arial", 20), bg="#1c1c1c", fg="white", bd=0,
                         activebackground="#008F3C", activeforeground="white",
                         command=lambda: entry.insert(END, "**2"))
    button_square.grid(row=1, column=1, padx=4, pady=4)
    
    button_equals = Button(frame, text="=", width=5, height=2, font=("Arial", 20), bg="#1c1c1c", fg="white", bd=0,
                        activebackground="#008F3C", activeforeground="white",
                        command=lambda: calculate(entry))
    button_equals.grid(row=5, column=2, padx=4, pady=4)

    root.bind("<Return>", lambda event: calculate(entry))
    
    def toggle_history(): 
        nonlocal window_history
        if window_history is None or not window_history.winfo_exists():
            button_x = history_button.winfo_rootx()
            button_y = history_button.winfo_rooty() + history_button.winfo_height()
            window_history = Toplevel(root)
            window_history.title("История")
            window_history.configure(bg="#1c1c1c")
            window_history.attributes("-topmost", True)
            window_history.overrideredirect(True)

            window_history.geometry(f"+{button_x}+{button_y}")

            history_label = Label(window_history, text="История операций", bg="#1c1c1c", fg="white", font=("Arial", 12))
            history_label.pack(pady=10)

            history_content = Text(window_history, bg="#1c1c1c", fg="white", font=("Arial", 10), height=10, width=30, bd=0)
            history_content.pack(padx=10, pady=10)

            history_content.delete(1.0, END)
            for operation in history:
                history_content.insert(END, operation + "\n")

            close_window_button = Button(window_history, text="Закрыть", bg="#012A12", fg="white", bd=0, font=("Arial", 12),
                             command=window_history.destroy)
            close_window_button.pack(pady=10)
            root.bind("<Button-1>", lambda event: window_history.destroy())
            root.bind("<FocusIn>", lambda event: window_history.destroy())
        else:
            window_history.destroy()

    history_button = Button(title_bar, text="История", bg="#012A12", fg="white", bd=0, font=("Arial", 13),
                           command=lambda: toggle_history())
    history_button.pack(side=RIGHT, padx=3, pady=2, ipady=0, ipadx=2)

    def calculate(entry):
        nonlocal clear_on_next_input
        try:
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, END)
            entry.insert(0, str(result))
            history.append(f"{expression} = {result}")
            clear_on_next_input = True
        except Exception as e:
            entry.delete(0, END)
            entry.insert(0, "ОШИБКА")
            clear_on_next_input = True

    root.mainloop()

if __name__ == "__main__":
    tk()