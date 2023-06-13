# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 21:19:39 2023

@author: neera
"""

from plyer import notification
from tkinter import *

window=Tk()
window.title('Notify')
window.geometry('200x200')

def notfun():
    notification.notify(title='Notification',message='notification notified')

btn=Button(window,text="Click",command=notfun,width=10)
btn.pack()
window.mainloop()