from tkinter import *

main_window = Tk() # النافذة الرئيسية
main_window.title(" (الطريقة الكلاسيكية) ")

classicL=Label(main_window, text='Classic Label')
classicL.pack()

classicB=Button(main_window, text='Classic Button')
classicB.pack()

main_window.mainloop()