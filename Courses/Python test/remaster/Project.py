from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import csv
from collections import Counter
def drawPieChart():
    c = Counter()
    with open('test3.csv') as my_file:
        data = csv.DictReader(my_file)
        print(data)
        for i in data:
            c.update(i['LanguagesWorkedWith'].split(';'))
    x = []
    y = []
    print(c)
    for i in c.most_common(10):
        x.append(i[0])
        y.append(i[1])
    plt.barh(x, y)
    plt.tight_layout()
    plt.show()

window = Tk()
window.geometry('1500x1500')
window.title('adham ali')
button = Button(text='Pie Chart',image=img,command=drawPieChart,padx=10).pack()
window.mainloop()

