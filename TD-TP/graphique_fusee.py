from classe import Fusee
import tkinter as tk
#frame = tk.Frame(width=768, height=500, bg="", colormap="new")
#frame.pack()
def dessin_fusee(fusee,frame):
    """la fonction prend en argument la fusee a
     afficher et une frame : elle cree un cadre
     dans la frame pour y afficher la fusee"""
    cadre = tk.Canvas(master=frame, width=500, height=500)
    if type(fusee)!=Fusee:
        print("mauvais type")
        return 0 #renvoyer une erreur ici
    taille_totale = fusee.taille[1] +fusee.taille[3]
    dimensions = fusee.taille
    p1 = (100-dimensions[0],0)
    p2 = (100+dimensions[0],0)
    p3 = (100-dimensions[0], dimensions[1])
    p4 = (100+dimensions[0], dimensions[1])
    p5 = (100-dimensions[2], dimensions[1])
    p6 = (100+dimensions[2], dimensions[1])
    p7 = (100-dimensions[2],dimensions[1]+dimensions[3])
    p8 = (100+dimensions[2],dimensions[1]+dimensions[3])
    p9 = (100, taille_totale*1.1)
    cadre.create_rectangle(p1[0], 500-p1[1],p4[0], 500 - p4[1])
    cadre.create_rectangle(p5[0], 500 - p5[1], p8[0], 500 - p8[1])
    cadre.create_line(p7[0], 500 - p7[1], p9[0], 500 - p9[1])
    cadre.create_line(p8[0], 500 - p8[1], p9[0], 500 - p9[1])
    cadre.pack()


#ariane = Fusee([30,190,25,60],0)
#dessin_fusee(ariane)
#frame.mainloop()
