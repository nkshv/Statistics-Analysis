import statistics 
from collections import Counter
from math import log, ceil
import tkinter as tk
from tkinter import ttk

def process_values():
    values_str = values.get()
    args = [float(i) for i in values_str.split(",")]
    len_values = len(args)
    mean = statistics.mean(args)
    median = statistics.median(args)
    mode = statistics.mode(args)
    stdev = statistics.stdev(args)
    variance = statistics.variance(args)
    maximum = max(args)
    minimum = min(args)
    variation_coefficient = statistics.stdev(args)/statistics.mean(args) * 100

    q = statistics.quantiles(args)
    IQR = q[2] - q[0]
    upper_fence = q[2] + 1.5 * IQR
    lower_fence = q[0] - 1.5 * IQR
    outliers = [i for i in args if i > upper_fence or i < lower_fence]

    result_label.config(text=f"""{len_values} Values\nMean: {mean:.4f}\nMedian: {median:.4f}\nMode: {mode}\nStandard deviation: {stdev:.4f}\nVariance: {variance:.4f}\nMaximum: {maximum}\tMinimum: {minimum}\nQ1 - {q[0]}   Q2 - {q[1]}   Q3 - {q[2]}\nN. of outliers: {len(outliers)}
        """)

root = tk.Tk()
result_label = tk.Label(root, text="")
result_label.pack()
root.geometry('1200x720+350+100')

root.title("Statistics Calculator")
image = tk.PhotoImage(file='anime.png')
background_label = tk.Label(root, image=image)
background_label.place(relwidth=1, relheight=1)

result_label.lift()

values = tk.StringVar()

signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)
email_label = ttk.Label(signin, text="Values:")
email_label.pack(fill='x', expand=True)
email_entry = ttk.Entry(signin, textvariable=values)
email_entry.pack(fill='x', expand=True)

email_entry.focus()

login_button = ttk.Button(signin, text="Calculate", command=process_values)
login_button.pack(fill='x', expand=True, pady=10)

# bind the 'Return' key to the process_values function
root.bind('<Return>', lambda event: process_values())

root.mainloop()
