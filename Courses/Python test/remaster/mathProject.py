from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import csv
from collections import Counter
x=[]
y=[]
xlabel=""
with open('ages.csv') as my_file:
    data=csv.DictReader(my_file)
    for i in data:
        x.append(int(i[data.fieldnames[1]]))
    xlabel=data.fieldnames[1]
    x=np.array(x)
def Bar_Chart ():
    plt.figure('Bar Chart')
    plt.bar(x, y)
    plt.tight_layout()
    plt.show()
def Dot_Plot():
    plt.figure('Dot_Plot')
    plt.scatter(x, y)
    plt.tight_layout()
    plt.show()
def box_Plot():
    plt.figure('box_Plot')
    plt.boxplot(x)
    plt.tight_layout()
    plt.show()
def Histogram():
    plt.figure('Histogram')
    plt.xlabel(xlabel)
    plt.hist(x,bins=10,edgecolor='black')
    plt.axvline(np.median(x),color='orange',label='Median')
    plt.legend()
    plt.tight_layout()
    plt.show()
window=Tk()
window.geometry('500x500+100+100')
Bar_Chart_Button=Button(text='Bar chart',command=Bar_Chart,padx=10,pady=10).grid(column=1,row=1)
Histogram_Button=Button(text='Histogram',command=Histogram,padx=10,pady=10).grid(column=2,row=1)
Box_Plot_Button=Button(text='Box Plot',command=box_Plot,padx=10,pady=10).grid(column=3,row=1)
Dot_Plot_Button=Button(text='Dot Plot',command=Dot_Plot,padx=10,pady=10).grid(column=4,row=1)
Exit_Button=Button(text='X',command=window.quit,bg='red',fg='black').grid(row=1,column=5)
window.mainloop()
