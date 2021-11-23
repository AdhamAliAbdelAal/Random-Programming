from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import csv
from collections import Counter
x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752,]
def Bar_Chart ():
    plt.bar(x, y)
    plt.tight_layout()
    plt.show()
def Dot_Plot():
    plt.scatter(x, y)
    plt.tight_layout()
    plt.show()
def box_Plot():
    plt.boxplot(x)
    plt.tight_layout()
    plt.show()
def Histogram():
    plt.hist(x,bins=10,edgecolor='black')
    plt.tight_layout()
    plt.show()
window=Tk()
window.geometry('500x500+100+100')
Bar_Chart_Button=Button(text='Bar chart',command=Bar_Chart,padx=10,pady=10).grid(column=0,row=0)
Histogram_Button=Button(text='Histogram',command=Histogram,padx=10,pady=10).grid(column=1,row=0)
Box_Plot_Button=Button(text='Box Plot',command=box_Plot,padx=10,pady=10).grid(column=2,row=0)
Dot_Plot_Button=Button(text='Dot Plot',command=Dot_Plot,padx=10,pady=10).grid(column=3,row=0)
Exit_Button=Button(text='X',command=window.quit,bg='red',fg='black').grid(row=0,column=4)
window.mainloop()
