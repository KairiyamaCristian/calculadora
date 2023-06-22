#importamos libreria de tkinter para dar una interfaz grafica
import tkinter as tk

#evento para dar click (numero)
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

#evento para limpiar consola
def button_clear():
    entry.delete(0, tk.END)

#evento para realizar operacion
def button_equal():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

def toggle_black_mode():
    bg_color = "#000000" if ventana["bg"] == "white" else "white"
    fg_color = "white" if ventana["bg"] == "white" else "black"
    entry.configure(bg=bg_color, fg=fg_color)
    ventana.configure(bg=bg_color)
    for button in buttons:
        button.configure(bg=bg_color, fg=fg_color)

#creamos objeto ventana
ventana = tk.Tk()
ventana.title("KAIRI")

#ENTRADA
entry = tk.Entry(ventana, font=("Calibri 20"))
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=28)

#Botones

button_1 = tk.Button(ventana, relief='flat', text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(ventana, relief='flat', text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(ventana, relief='flat', text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(ventana, relief='flat', text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(ventana, relief='flat', text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(ventana, relief='flat', text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(ventana, relief='flat', text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(ventana, relief='flat', text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(ventana, relief='flat', text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(ventana, relief='flat', text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = tk.Button(ventana, relief='flat', text="+", padx=36, pady=20, command=lambda: button_click("+"))
button_subtract = tk.Button(ventana, relief='flat', text="-", padx=40, pady=20, command=lambda: button_click("-"))
button_multiply = tk.Button(ventana, relief='flat', text="*", padx=40, pady=20, command=lambda: button_click("*"))
button_divide = tk.Button(ventana, relief='flat', text="/", padx=40, pady=20, command=lambda: button_click("/"))
button_equal = tk.Button(ventana, relief='flat', text="=", padx=80, pady=20, command=button_equal)
button_clear = tk.Button(ventana, relief='flat', text="Limpiar", padx=120, pady=20, command=button_clear)
button_black_mode = tk.Button(ventana, relief='flat', text="B", padx=40, pady=20, command=toggle_black_mode, fg="black")
buttons = [button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9,button_0,button_add,button_subtract,
button_multiply,button_divide,button_equal,button_clear,button_black_mode]

# Ubicación de los botones en la cuadrícula
button_clear.grid(row=1, column=0,columnspan=3)
button_divide.grid(row=1, column=3)

button_1.grid(row=2, column=0)
button_2.grid(row=2, column=1)
button_3.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)

button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_0.grid(row=5, column=1)

button_equal.grid(row=5, column=2, columnspan=2)

button_black_mode.grid(row=5, column=0)

#hacemos que siga viva
ventana.mainloop()
