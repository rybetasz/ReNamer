from email import message
import os
from tkinter import *
from tkinter import messagebox
import time
import tkinter
from turtle import bgcolor, width

isim1 = r"Files\\row-1-column-1.png" 
isim2 = r"Files\\row-1-column-2.png" 
isim3 = r"Files\\row-1-column-3.png" 
isim4 = r"Files\\row-1-column-4.png" 
isim5 = r"Files\\row-1-column-5.png" 
isim6 = r"Files\\row-1-column-6.png" 
isim7 = r"Files\\row-1-column-7.png" 
isim8 = r"Files\\row-1-column-8.png" 
isim9 = r"Files\\row-2-column-1.png" 
isim10 = r"Files\\row-2-column-2.png" 
isim11 = r"Files\\row-2-column-3.png" 
isim12 = r"Files\\row-2-column-4.png" 
isim13 = r"Files\\row-2-column-5.png" 
isim14 = r"Files\\row-2-column-6.png" 
isim15 = r"Files\\row-2-column-7.png" 
isim16 = r"Files\\row-2-column-8.png" 
isim17 = r"Files\\row-3-column-1.png" 
isim18 = r"Files\\row-3-column-2.png" 
isim19 = r"Files\\row-3-column-3.png" 
isim20 = r"Files\\row-3-column-4.png" 
isim21 = r"Files\\row-3-column-5.png" 
isim22 = r"Files\\row-3-column-6.png" 
isim23 = r"Files\\row-3-column-7.png" 
isim24 = r"Files\\row-3-column-8.png" 
isim25 = r"Files\\row-4-column-1.png" 
isim26 = r"Files\\row-4-column-2.png" 
isim27 = r"Files\\row-4-column-3.png" 
isim28 = r"Files\\row-4-column-4.png" 
isim29 = r"Files\\row-4-column-5.png" 
isim30 = r"Files\\row-4-column-6.png" 
isim31 = r"Files\\row-4-column-7.png" 
isim32 = r"Files\\row-4-column-8.png" 
isim33 = r"Files\\row-5-column-1.png"
isim34 = r"Files\\row-5-column-2.png"
isim35 = r"Files\\row-5-column-3.png"
isim36 = r"Files\\row-5-column-4.png"
isim37 = r"Files\\row-5-column-5.png"
isim38 = r"Files\\row-5-column-6.png"
isim39 = r"Files\\row-5-column-7.png"
isim40 = r"Files\\row-5-column-8.png"
isim41 = r"Files\\row-6-column-1.png"
isim42 = r"Files\\row-6-column-2.png"
isim43 = r"Files\\row-6-column-3.png"
isim44 = r"Files\\row-6-column-4.png"
isim45 = r"Files\\row-6-column-5.png"
isim46 = r"Files\\row-6-column-6.png"
isim47 = r"Files\\row-6-column-7.png"
isim48 = r"Files\\row-6-column-8.png"
isim49 = r"Files\\row-7-column-1.png"
isim50 = r"Files\\row-7-column-2.png"
isim51 = r"Files\\row-7-column-3.png"
isim52 = r"Files\\row-7-column-4.png"
isim53 = r"Files\\row-7-column-5.png"
isim54 = r"Files\\row-7-column-6.png"
isim55 = r"Files\\row-7-column-7.png"
isim56 = r"Files\\row-7-column-8.png"
isim57 = r"Files\\row-8-column-1.png"
isim58 = r"Files\\row-8-column-2.png"
isim59 = r"Files\\row-8-column-3.png"
isim60 = r"Files\\row-8-column-4.png"
isim61 = r"Files\\row-8-column-5.png"
isim62 = r"Files\\row-8-column-6.png"
isim63 = r"Files\\row-8-column-7.png"
isim64 = r"Files\\row-8-column-8.png"
isimnew1 = r"Files\\1.png" 
isimnew2 = r"Files\\2.png" 
isimnew3 = r"Files\\3.png" 
isimnew4 = r"Files\\4.png" 
isimnew5 = r"Files\\5.png" 
isimnew6 = r"Files\\6.png" 
isimnew7 = r"Files\\7.png" 
isimnew8 = r"Files\\8.png" 
isimnew9 = r"Files\\9.png" 
isimnew10 = r"Files\\10.png" 
isimnew11 = r"Files\\11.png" 
isimnew12 = r"Files\\12.png" 
isimnew13 = r"Files\\13.png" 
isimnew14 = r"Files\\14.png" 
isimnew15 = r"Files\\15.png" 
isimnew16 = r"Files\\16.png" 
isimnew17 = r"Files\\17.png" 
isimnew18 = r"Files\\18.png" 
isimnew19 = r"Files\\19.png" 
isimnew20 = r"Files\\20.png" 
isimnew21 = r"Files\\21.png" 
isimnew22 = r"Files\\22.png" 
isimnew23 = r"Files\\23.png" 
isimnew24 = r"Files\\24.png" 
isimnew25 = r"Files\\25.png" 
isimnew26 = r"Files\\26.png" 
isimnew27 = r"Files\\27.png" 
isimnew28 = r"Files\\28.png" 
isimnew29 = r"Files\\29.png" 
isimnew30 = r"Files\\30.png" 
isimnew31 = r"Files\\31.png" 
isimnew32 = r"Files\\32.png" 
isimnew33 = r"Files\\33.png"
isimnew34 = r"Files\\34.png"
isimnew35 = r"Files\\35.png"
isimnew36 = r"Files\\36.png"
isimnew37 = r"Files\\37.png"
isimnew38 = r"Files\\38.png"
isimnew39 = r"Files\\39.png"
isimnew40 = r"Files\\40.png"
isimnew41 = r"Files\\41.png"
isimnew42 = r"Files\\42.png"
isimnew43 = r"Files\\43.png"
isimnew44 = r"Files\\44.png"
isimnew45 = r"Files\\45.png"
isimnew46 = r"Files\\46.png"
isimnew47 = r"Files\\47.png"
isimnew48 = r"Files\\48.png"
isimnew49 = r"Files\\49.png"
isimnew50 = r"Files\\50.png"
isimnew51 = r"Files\\51.png"
isimnew52 = r"Files\\52.png"
isimnew53 = r"Files\\53.png"
isimnew54 = r"Files\\54.png"
isimnew55 = r"Files\\55.png"
isimnew56 = r"Files\\56.png"
isimnew57 = r"Files\\57.png"
isimnew58 = r"Files\\58.png"
isimnew59 = r"Files\\59.png"
isimnew60 = r"Files\\60.png"
isimnew61 = r"Files\\61.png"
isimnew62 = r"Files\\62.png"
isimnew63 = r"Files\\63.png"
isimnew64 = r"Files\\64.png"


#TKINTER
wsmenu =Tk()
wsmenu.geometry('512x256')
wsmenu.title('ReNamer by rybetasz')
wsmenu.iconbitmap(r'matlist.ico')
img = PhotoImage(file="menu.png")
Label(
    wsmenu,
    image=img
).pack()

#DEFLER
def hakkinda():
     messagebox.showinfo('About','ReNamer V1.1 by rybetasz')

def dosyalariduzenle():
  os.rename(isim1, isimnew1)
  os.rename(isim2, isimnew2)
  os.rename(isim3, isimnew3)
  os.rename(isim4, isimnew4)
  os.rename(isim5, isimnew5)
  os.rename(isim6, isimnew6)
  os.rename(isim7, isimnew7)
  os.rename(isim8, isimnew8)
  os.rename(isim9, isimnew9)
  os.rename(isim10, isimnew10)
  os.rename(isim11, isimnew11)
  os.rename(isim12, isimnew12)
  os.rename(isim13, isimnew13)
  os.rename(isim14, isimnew14)
  os.rename(isim15, isimnew15)
  os.rename(isim16, isimnew16)
  os.rename(isim17, isimnew17)
  os.rename(isim18, isimnew18)
  os.rename(isim19, isimnew19)
  os.rename(isim20, isimnew20)
  os.rename(isim21, isimnew21)
  os.rename(isim22, isimnew22)
  os.rename(isim23, isimnew23)
  os.rename(isim24, isimnew24)
  os.rename(isim25, isimnew25)
  os.rename(isim26, isimnew26)
  os.rename(isim27, isimnew27)
  os.rename(isim28, isimnew28)
  os.rename(isim29, isimnew29)
  os.rename(isim30, isimnew30)
  os.rename(isim31, isimnew31)
  os.rename(isim32, isimnew32)
  os.rename(isim33, isimnew33)
  os.rename(isim34, isimnew34)
  os.rename(isim35, isimnew35)
  os.rename(isim36, isimnew36)
  os.rename(isim37, isimnew37)
  os.rename(isim38, isimnew38)
  os.rename(isim39, isimnew39)
  os.rename(isim40, isimnew40)
  os.rename(isim41, isimnew41)
  os.rename(isim42, isimnew42)
  os.rename(isim43, isimnew43)
  os.rename(isim44, isimnew44)
  os.rename(isim45, isimnew45)
  os.rename(isim46, isimnew46)
  os.rename(isim47, isimnew47)
  os.rename(isim48, isimnew48)
  os.rename(isim49, isimnew49)
  os.rename(isim50, isimnew50)
  os.rename(isim51, isimnew51)
  os.rename(isim52, isimnew52)
  os.rename(isim53, isimnew53)
  os.rename(isim54, isimnew54)
  os.rename(isim55, isimnew55)
  os.rename(isim56, isimnew56)
  os.rename(isim57, isimnew57)
  os.rename(isim58, isimnew58)
  os.rename(isim59, isimnew59)
  os.rename(isim60, isimnew60)
  os.rename(isim61, isimnew61)
  os.rename(isim62, isimnew62)
  os.rename(isim63, isimnew63)
  os.rename(isim64, isimnew64)
  time.sleep(1.40)
  messagebox.showinfo('Edit Files','Done!')

 
def vinylduzenle():
    
    xname = input('Aracınız ismini giriniz :')
    orjarac = input('Vinyli aldığınız aracın ismini giriniz: ')   
    folder = "Dosya"
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"{xname}.dds"
        src =f"{folder}/{orjarac}.dds"
        dst =f"{folder}/{xname}.dds"
        os.rename(src, dst)

def isimduzenle():
   
   isimxname = input('Enter the name: ')
   isimxname2 = input('Enter the Name: ')
   folder = "Dosya"
   for count, filename in enumerate(os.listdir(folder)):
   dst = f"{isimxname}"
   src = f"{folder}/{isimxname2}"
   dst = f"{folder}/{
   




#MENU
menubar = Menu(wsmenu, background='black', foreground='yellow', activebackground='black', activeforeground='yellow')  
file = Menu(menubar, tearoff=0, background='black', foreground='yellow')  
file.add_command(label="Edit Files",command=dosyalariduzenle,font=('Arial', 10, 'bold'))  
#file.add_command(label="Vinyl'i Düzenle",command=vinylduzenle,font=('Arial', 10, 'bold'))
file.add_separator()  
file.add_command(label="Exit", command=wsmenu.quit,font=('Arial', 10, 'bold'))  
menubar.add_cascade(label="File", menu=file) 
file.add_command(label='About',command=hakkinda,font=('Arial', 10, 'bold')) 
wsmenu.config(menu=menubar)


wsmenu.mainloop()
