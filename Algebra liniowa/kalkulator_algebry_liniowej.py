# -*- coding: utf-8 -*-

"""
@author: Maja Rusak
"""

import tkinter as tk
from macierze import *
from rownania import *

class Okno():
    
    #inicjalizacja Okna Graficznego programu, podział na dwie częci
    def __init__(self, okno):
        self.okno = okno
        
        ramka1 = tk.Frame(self.okno, relief=tk.RAISED, borderwidth=1)
        ramka1.grid(row=0, column=0, rowspan = 18, columnspan=10, padx=5, pady=5)
        ramka2 = tk.Frame(self.okno, relief=tk.RAISED, borderwidth=1, width = 480, heigh = 625)
        ramka2.grid(row=0, column=10, rowspan = 30, columnspan=10, padx=5, pady=5, sticky = "NE")
        Okno.spisTresci(ramka1, ramka2)
        
    #Spis treci działań z algebry liniowej wykonywanych przez program, po kliknięciu odpowiedniego
    #przycisku obok pojawia się panel do wpisania odpowiednich wartosci, aby rozwiązać diałanie
    def spisTresci(ramka_spis, ramka_dzialania):
        ramka1 = tk.Frame(ramka_spis, relief=tk.RAISED, borderwidth=1)
        ramka1.grid(row=0, column=0, rowspan = 9, columnspan=5, padx=5, pady=5)
        tk.Label(ramka1, text=u'MACIERZE', font=("Verdana", 15), height = 2, width = 20).grid(row=0, column=0, rowspan=2, columnspan=5, padx=5, pady=5)
        tk.Button(ramka1, text=u"DODAWANIE I ODEJMOWANIE MACIERZY", command=lambda: wymiarMacierz(ramka_dzialania, 1), font=("Verdana", 10), height = 1, width = 35, bg='#C0C0C0').grid(row=2, column=0, columnspan=5, padx=5, pady=5)
        tk.Button(ramka1, text=u"MNOŻENIE MACIERZY",command=lambda: wymiarMacierzMnozenie(ramka_dzialania), font=("Verdana", 10), height = 1, width = 35, bg='#C0C0C0').grid(row=3, column=0, columnspan=5, padx=5, pady=5)
        tk.Button(ramka1, text=u"TRANSPONOWANIE MACIERZY", command=lambda: wymiarMacierz(ramka_dzialania, 4), font=("Verdana", 10), height = 1, width = 35, bg='#C0C0C0').grid(row=4, column=0, columnspan=5, padx=5, pady=5)
        tk.Button(ramka1, text=u"WYZNACZNIK MACIERZY", command=lambda: wymiarMacierz(ramka_dzialania, 2), font=("Verdana", 10), height = 1, width = 35, bg='#C0C0C0').grid(row=5, column=0, columnspan=5, padx=5, pady=5)
        tk.Button(ramka1, text=u"MACIERZ ODWROTNA", command=lambda: wymiarMacierz(ramka_dzialania, 3), font=("Verdana", 10), height = 1, width = 35, bg='#C0C0C0').grid(row=6, column=0, columnspan=5, padx=5, pady=5)
        tk.Button(ramka1, text=u"WARTOŚCI I WEKTORY WŁASNE MACIERZY", command=lambda: wymiarMacierz(ramka_dzialania, 5), font=("Verdana", 10), height = 1, width = 35, bg='#C0C0C0').grid(row=7, column=0, columnspan=5, padx=5, pady=5)
        
        ramka2 = tk.Frame(ramka_spis, relief=tk.RAISED, borderwidth=1)
        ramka2.grid(row=9, column=0, rowspan = 9, columnspan=5, padx=5, pady=5)
        tk.Label(ramka2, text=u'UKŁADY RÓWNAŃ', font=("Verdana", 15), height = 2, width = 20).grid(row=9, column=0, rowspan=2, columnspan=5, padx=5, pady=5)
        tk.Button(ramka2, text=u"Z DWOMA NIEWIADOMYMI", command=lambda:uklad_rownan(ramka_dzialania,2), font=("Verdana", 10), height = 1, width = 35, bg='#C0C0C0').grid(row=11, column=0, columnspan=5, padx=5, pady=5)
        tk.Button(ramka2, text=u"Z TRZEMA NIEWIADOMYMI", command=lambda:uklad_rownan(ramka_dzialania,3), font=("Verdana", 10), height = 1, width = 35, bg='#C0C0C0').grid(row=12, column=0, columnspan=5, padx=5, pady=5)
        tk.Button(ramka2, text=u"Z CZTEREMA NIEWIADOMYMI", command=lambda:uklad_rownan(ramka_dzialania,4), font=("Verdana", 10), height = 1, width = 35, bg='#C0C0C0').grid(row=13, column=0, columnspan=5, padx=5, pady=5)
        tk.Button(ramka2, text=u"Z PIĘCIOMA NIEWIADOMYMI", command=lambda:uklad_rownan(ramka_dzialania,5), font=("Verdana", 10), height = 1, width = 35, bg='#C0C0C0').grid(row=14, column=0, columnspan=5, padx=5, pady=5)
        tk.Label(ramka2, text=u'', font=("Verdana", 15), height = 2, width = 20).grid(row=15, column=0, rowspan=2, columnspan=5, padx=5, pady=16)
        
okno = tk.Tk()   
glowne = Okno(okno)
okno.title("Algebra liniowa")
okno.geometry("830x635")
okno.mainloop()
