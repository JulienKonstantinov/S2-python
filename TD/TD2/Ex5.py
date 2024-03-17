import tkinter as tk
import tkinter.font as font
import random

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

liste_objet=[]

def cercle():
    global liste_objet
    x=random.randint(50,CANVAS_WIDTH-50)
    y=random.randint(50, CANVAS_HEIGHT-50)
    canvas.create_oval(x-50, y+50,x+50,y-50, fill="blue")
    liste_objet.append(canvas.create_oval(x-50, y+50,x+50,y-50, fill="blue"))

def carre():
    global liste_objet
    x=random.randint(50,CANVAS_WIDTH-50)
    y=random.randint(50, CANVAS_HEIGHT-50)
    canvas.create_rectangle(x,y,x+100,y+100,fill="red")
    liste_objet.append(canvas.create_rectangle(x,y,x+100,y+100,fill="red"))

def croix():
    global liste_objet
    x=random.randint(50,CANVAS_WIDTH-50)
    y=random.randint(50, CANVAS_HEIGHT-50)
    canvas.create_line(x-50,y+50,x+50,y-50,fill="yellow",width=25)
    canvas.create_line(x+50,y+50,x-50,y-50,fill="yellow",width=25)
    liste_objet.append(canvas.create_line(x-50,y+50,x+50,y-50,fill="yellow",width=25))
    liste_objet.append(canvas.create_line(x+50,y+50,x-50,y-50,fill="yellow",width=25))

def undo():
    if len(liste_objet)!=0:
        if canvas.type(liste_objet[-1])=="line":
            canvas.delete(liste_objet[-1])
            liste_objet.pop()
        canvas.delete(liste_objet[-1])
        liste_objet.pop()



root = tk.Tk()
root.title("Mon dessin")
police = font.Font(family='Helvetica')
canvas = tk.Canvas(root,width=CANVAS_WIDTH,heigh=CANVAS_HEIGHT,bg="black")
canvas.grid(row=1,rowspan=3,column=1)
bouton_couleur=tk.Button(root,text="Choisir une couleur",foreground="magenta")
bouton_couleur.grid(row=0,column=1)
bouton_undo=tk.Button(root,text="Undo",command=undo)
bouton_undo.grid(row=0,column=0)
bouton_cercle=tk.Button(root,text="cercle",command=cercle)
bouton_cercle.grid(row=1,column=0)
bouton_carre=tk.Button(root,text="carré",command=carre)
bouton_carre.grid(row=2,column=0)
bouton_croix=tk.Button(root,text="croix",command=croix)
bouton_croix.grid(row=3,column=0)

root.mainloop()