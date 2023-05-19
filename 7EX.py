from tkinter import *
import tkinter as tk
window = Tk()  
window.title("Добро пожаловать в приложение PythonRu")  
window.geometry('400x250')  

price = IntVar() # создаем переменную, которую будем использовать для хранения значения цены

#функция, которая будет вызываться при выборе radiobutton


#функция, которая будет вызываться при нажатии на кнопку "ОК"
def calculate():
    result = int(entry.get()) * int(radio_var.get())
    output_label.config(text=str(result))

#создаем radiobuttonы и привязываем их к функции set_price
radio_var = tk.IntVar()
plastic_rb = Radiobutton(window, text="9x12", variable=radio_var, value="1")
plastic_rb.grid(column=0, row=0, sticky=W)
straw_rb = Radiobutton(window, text="10x15", variable=radio_var, value="2")
straw_rb.grid(column=0, row=1, sticky=W)
aluminum_rb = Radiobutton(window, text="18x24", variable=radio_var, value="3")
aluminum_rb.grid(column=0, row=2, sticky=W)

#создаем поле ввода и кнопку "ОК"
btn = Button(window, text="Ок", command=calculate, width=15)  
btn.grid(column=0, row=4, sticky=W,pady=10)  
entry = Entry(window)
entry.grid(row=3, column=0, sticky=W)
#ok_button = Button(window, text="ОК", command=calculate)
#ok_button.pack()

#создаем поле вывода для результата
output_label = Label(window, text="")
output_label.grid(column=0, row=5, sticky=W)

window.mainloop()