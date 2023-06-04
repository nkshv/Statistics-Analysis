import statistics 
from collections import Counter
import re
from math import log, ceil
import tkinter as tk
from tkinter import ttk

args = [1,2,3,4,30,40,50,60,70,80,1000]

root = tk.Tk()
root.title("Table Example")
table = ttk.Treeview(root, columns=("classes", "fi", "fi (%)", "fi (%) Acc."), show="headings")
table.pack()

table.heading("classes", text="Classes", anchor='center')
table.heading("fi", text="fi", anchor='center')
table.heading("fi (%)", text="fi (%)", anchor='center')
table.heading("fi (%) Acc.", text="fi (%) Acc.", anchor='center')


denominador = round(1 + (3.3 * log(len(args), 10)))
amplitude = max(args) - min(args)
amplitude_de_intervalo = amplitude / denominador

amplitude_de_intervalo = ceil(amplitude_de_intervalo)

valor = min(args)
acumulada = 0
for i in range((denominador) - 1):
    cont = 0
    for i in args:
        if i >= valor and i < valor + amplitude_de_intervalo:
            cont += 1
    if cont > 0:
        fi = cont / len(args) * 100
    else:
        fi = 0
    acumulada += fi
    fi = float(f"{fi:.3f}")
    acumulada = float(f"{acumulada:.3f}")
    values = (f"\t{valor} |-- {valor + amplitude_de_intervalo}", f"\t{cont:4g}", f"\t{fi}%", f"\t{acumulada}%")
    table.insert("", tk.END, values=values)
    valor += amplitude_de_intervalo
cont = 0
for i in args:
    if i >= valor and i <= valor + amplitude_de_intervalo:
        cont += 1
    if cont > 0:
        fi = cont/len(args) * 100
    else:
        fi = 0
    acumulada += fi
    fi = float(f"{fi:.3f}")
    cem = 100

values = (f"\t{valor} |-| {valor + amplitude_de_intervalo}", f"\t{cont:4g}", f"\t{fi}%", f"\t{cem}%")
table.insert("", tk.END, values=values)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", rowheight=25)
style.configure("Treeview.Heading", font=("TkDefaultFont", 12, "bold"))
style.configure("Treeview.Item", borderwidth=1, relief="solid")
style.map("Treeview", background=[("selected", "#ececec")], foreground=[("selected", "black")])
style.map("Treeview.Item", background=[("selected", "#ececec")], foreground=[("selected", "black")], highlightthickness=[("selected", 2)])




root.mainloop()
