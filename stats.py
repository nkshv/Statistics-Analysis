import statistics 
from collections import Counter
from math import log, ceil
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import ImageTk, Image, ImageFilter, ImageGrab

import matplotlib.pyplot as plt

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

    result_window = tk.Toplevel(root)
    result_window.title("Result")

    result_window.geometry("400x300")
    result_window.resizable(False, False)
    
    result_label = tk.Label(result_window, text="", font='verdana 13', justify='left')
   

    result_label.pack(side='top', pady=20)
    result_label.lift()
    result_label.config(text=f"""Number of values: {len_values}\nMean: {mean:.4f}\nMedian: {median:.4f}\nMode: {mode}\nStandard deviation: {stdev:.4f}\nVariance: {variance:.4f}\nMaximum: {maximum}\nMinimum: {minimum}\nQ1: {q[0]}   Q2: {q[1]}   Q3: {q[2]}\nN. of outliers: {len(outliers)}""")

def show_popup():
    popup = tk.Toplevel()
    popup.title("Graphs")

    label = tk.Label(popup, text="")
    label.pack(pady=10)

    button1 = tk.Button(popup, text="Boxplot", command=lambda: show_image('boxplot'))
    button1.pack(pady=5)

    button2 = tk.Button(popup, text="Scatterplot", command=lambda: show_image('scatterplot'))
    button2.pack(pady=5)

    button3 = tk.Button(popup, text="Bar Plot", command=lambda: show_image('barplot'))
    button3.pack(pady=5)

    button4 = tk.Button(popup, text="Violin Plot", command=lambda: show_image('violinplot'))
    button4.pack(pady=5)

    button5 = tk.Button(popup, text="Lineplot", command=lambda: show_image('lineplot'))
    button5.pack(pady=5)

    button6 = tk.Button(popup, text="Hexbin", command=lambda: show_image('hexbin'))
    button6.pack(pady=5)

def show_image(plot_type):
    values_str = values.get()
    args = [float(i) for i in values_str.split(",")]
    fig, ax = plt.subplots()
    if plot_type == 'boxplot':
        ax.boxplot(args)
    elif plot_type == 'scatterplot':
        ax.scatter(range(1, len(args) + 1), args)
    elif plot_type == 'barplot':
        ax.bar(range(1, len(args) + 1), args)
    elif plot_type == 'violinplot':
        ax.violinplot(args)
    elif plot_type == 'hexbin':
        ax.hexbin(range(1, len(args) + 1), args, gridsize=10, cmap='YlOrRd')
    elif plot_type == 'lineplot':
        ax.plot(range(1, len(args) + 1), args)
    fig.savefig('stats.png')

    image = Image.open("stats.png")
    photo = ImageTk.PhotoImage(image)

    popup = tk.Toplevel(root)
    popup.title("Image")
    popup.geometry("%dx%d" % (image.width, image.height))

    label = tk.Label(popup, image=photo)
    label.image = photo
    label.pack()

    popup.mainloop()

root = tk.Tk()

root.geometry('1600x900+100+100')
root.title("Statistics Calculator")
image = tk.PhotoImage(file='assets/bg.png')
background_label = tk.Label(root, image=image)
background_label.place(relwidth=1, relheight=1)

values = tk.StringVar()

signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, expand=True)
label = ttk.Label(signin, text="Values:", font='verdana 14')

label.pack(fill='x', expand=True)
entry = ttk.Entry(signin, textvariable=values)
entry.pack(fill='x', expand=True)

entry.focus()

img1 = PhotoImage(file='assets/button.png')
img2 = PhotoImage(file='assets/button2.png')
button = ttk.Button(signin, text="Calculate", command=process_values)
button.config(image=img1)
button.pack()
data_button = ttk.Button(signin, text="Data visualization", command=show_popup)
data_button.config(image=img2)
data_button.pack()


root.bind('<Return>', lambda event: process_values())

root.mainloop()