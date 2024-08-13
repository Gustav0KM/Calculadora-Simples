import tkinter as tk

def on_button_click(value):
    if value == "=":
        calc_result()
        
    elif value == "C":
        text.delete("1.0", tk.END)
        
    else:
        current_text = text.get("1.0", tk.END).strip()  #Obtém o texto atual
        new_text = current_text + value
        text.delete("1.0", tk.END)  #Limpa o widget Text
        text.insert(tk.END, new_text)  #Insere o novo texto
        
def calc_result():
        try:
            #Substitui texto 'x' por '*'(expressão) para poder calcular
            expression = text.get("1.0", tk.END).strip().replace("x", "*")
            result = eval(expression)
            text.delete("1.0", tk.END)
            text.insert(tk.END, str(result))
        except Exception as e:
            text.delete("1.0", tk.END)
            text.insert(tk.END, "Erro")
            
def on_enter(event):
    calc_result()
    return "break"
    
root = tk.Tk()
root.title("Calculadora")

text = tk.Text(root, height=1.4, width=10, font=("Arial", 52))
text.pack(pady=10)

text.bind("<Return>", on_enter)

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

button = tk.Button(frame, text="0", command=lambda: on_button_click("0"), width=5, height=1, font=("Arial", 20))
button.grid(row=3, column=2, padx=4, pady=4)

button = tk.Button(frame, text="1", command=lambda: on_button_click("1"), width=5, height=1, font=("Arial", 20))
button.grid(row=0, column=1, padx=4, pady=4)

button = tk.Button(frame, text="2", command=lambda: on_button_click("2"), width=5, height=1, font=("Arial", 20))
button.grid(row=0, column=2, padx=4, pady=4)

button = tk.Button(frame, text="3", command=lambda: on_button_click("3"), width=5, height=1, font=("Arial", 20))
button.grid(row=0, column=3, padx=4, pady=4)

button = tk.Button(frame, text="4", command=lambda: on_button_click("4"), width=5, height=1, font=("Arial", 20))
button.grid(row=1, column=1, padx=4, pady=4)

button = tk.Button(frame, text="5", command=lambda: on_button_click("5"), width=5, height=1, font=("Arial", 20))
button.grid(row=1, column=2, padx=4, pady=4)

button = tk.Button(frame, text="6", command=lambda: on_button_click("6"), width=5, height=1, font=("Arial", 20))
button.grid(row=1, column=3, padx=4, pady=4)

button = tk.Button(frame, text="7", command=lambda: on_button_click("7"), width=5, height=1, font=("Arial", 20))
button.grid(row=2, column=1, padx=4, pady=4)

button = tk.Button(frame, text="8", command=lambda: on_button_click("8"), width=5, height=1, font=("Arial", 20))
button.grid(row=2, column=2, padx=4, pady=4)

button = tk.Button(frame, text="9", command=lambda: on_button_click("9"), width=5, height=1, font=("Arial", 20))
button.grid(row=2, column=3, padx=4, pady=4)

button = tk.Button(frame, text="=", command=lambda: on_button_click("="), width=5, height=1, font=("Arial", 20))
button.grid(row=3, column=3, padx=4, pady=4)

button = tk.Button(frame, text="C", command=lambda: on_button_click("C"), width=5, height=1, font=("Arial", 20))
button.grid(row=3, column=1, padx=4, pady=4)

button = tk.Button(frame, text="/", command=lambda: on_button_click("/"), width=5, height=1, font=("Arial", 20))
button.grid(row=0, column=4, padx=4, pady=4)

button = tk.Button(frame, text="x", command=lambda: on_button_click("x"), width=5, height=1, font=("Arial", 20))
button.grid(row=1, column=4, padx=4, pady=4)

button = tk.Button(frame, text="-", command=lambda: on_button_click("-"), width=5, height=1, font=("Arial", 20))
button.grid(row=2, column=4, padx=4, pady=4)

button = tk.Button(frame, text="+", command=lambda: on_button_click("+"), width=5, height=1, font=("Arial", 20))
button.grid(row=3, column=4, padx=4, pady=4)

root.mainloop()
