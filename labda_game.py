#-------------------------------------------------------------------------------
# Name:        labda_game.py
# Purpose:     Készíts egy programot, melyben egy labda cikk-cakk mozgást végez,
#              a felhasználónak pedig az egér kurzor segítségévek rá kell kattintania a labdára.
#              Minden eltalált kattintásnál a labdának gyorsabb mozgást kell végeznie.
#-------------------------------------------------------------------------------
from tkinter import *
from tkinter.messagebox import showinfo


def move():
    global x1, y1, dx, dy, flag, sebesseg
    x1, y1 = x1 + dx, y1 + dy
    if x1 >= 360:
       x1, dx, dy = 360, -12, 5
    if x1 <= 10:
       x1, dx, dy = 10, 12, 5
    if y1 >= 360:
       x1, dx, dy = 360, -12, -5
    if y1 <= 10:
       y1, dx, dy = 10, 12, -5
    can1.coords(oval1, x1, y1, x1 + 30, y1 + 30)
    if flag > 0:
       abl1.after(sebesseg, move)

def eger(event):
    global katt, pont, x1, y1, sebesseg
    ex = event.x
    ey = event.y
    if (event.x < x1 + 20 and event.x > x1 - 20) and (event.y > y1 - 20 and event.y < y1 + 20):
       pont += 1
       sebesseg = sebesseg-10
    #print('sebesség: ' +str(sebesseg))
    #print('egér koordináták: ' +str(ex) +' ,' +str(ey) +' , Labda koordinátái : ' +str(x1) +', ' + str(y1))
    #print(katt)
    if katt <= 19 :
       katt +=1
    if katt == 20 :
       stop()
    #print('kattintás után: ' +str(katt))
    #print('pontszam : ' +str(pont))
    pont_katt.configure(text='Katintások : '+ str(katt) +' , Pontod: ' + str(pont))

def stop():
    global flag
    flag = 0
    popup_showinfo()

def start():
    global flag
    if flag == 0:
       flag = 1
       move()

def popup_showinfo():
    global pont
    showinfo('Eredmény: ', 'A játékban elért pont számod: ' +str(pont) +'\n(az "ok" gombra kattintva kilép a program')

# --- globális változok alap értékei
x1, y1 = 10, 10
dx, dy = 12, 5
flag = 0
pont=0
katt=0
sebesseg =150


# --- master witget
abl1 = Tk()
abl1.title("Labda Játék")

# --- slave witget
can1 = Canvas(abl1, bg="dark grey", height = 400, width = 400)
can1.grid(row=1, columnspan=3, padx=3,pady=3)
# --- labda
oval1 = can1.create_oval(x1, y1, x1 + 30, y1 + 30, fill = "white")
# --- gombok
Button(abl1, text = "Kilépés", command=abl1.destroy).grid(row=2, column=2, sticky=E, padx = 3, pady = 5)
Button(abl1, text = "Indítás", command=start).grid(row=2, column=1, sticky=W,padx = 1, pady = 5)
# --- szöveges megjelenítés
can1.bind('<Button-1>', eger)
pont_katt = Label(abl1)
pont_katt.grid(row=2,column=2, sticky=W, padx=3,pady=3)


abl1.mainloop()