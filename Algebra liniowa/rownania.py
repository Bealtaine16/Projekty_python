# -*- coding: utf-8 -*-

"""
@author: Maja Rusak
"""

import tkinter as tk
import numpy as np
from scipy.linalg import solve
from macierze import *

#Tworzenie okna, w którym ma się pojawić możliwosć wypisywania wartosci rownania oraz wynik
def uklad_rownan(ramka, ilosc):    
    czyscRamke(ramka)
    ramka1 = tk.Frame(ramka, relief=tk.RAISED, borderwidth=1, width = 480)
    ramka1.grid(row=0, column=0, rowspan=ilosc+3, columnspan=10, padx=5, pady=5, sticky = "NE")
    ramka2 = tk.Frame(ramka, relief=tk.RAISED, borderwidth=1, width = 480)
    ramka2.grid(row=ilosc+3, column=0, rowspan=ilosc+3, columnspan=10, padx=5, pady=5, sticky = "NE")
    uklad(ramka, ramka1, ramka2, ilosc)
  
#Okno z układem równań, w zależnosci od wybranej opcji możliwy jest układ równań od 2 do 5 niewiadomych     
def uklad(ramka, ramka1, ramka2, ilosc):
    niewiadome = ilosc
    rownanie = []
    ramka1 = tk.Frame(ramka, relief=tk.RAISED, borderwidth=1, width = 455)
    ramka1.grid(row=0, column=0, rowspan=ilosc+3, columnspan=10, padx=5, pady=5, sticky = "NE")
    tk.Label(ramka1, text=u'RÓWNANIA', font=("Verdana", 15), width = 35).grid(row=0, column=0, columnspan=11, padx=7, pady=5)
    for n in range(niewiadome):
        en1 = tk.Entry(ramka1, font=("Verdana", 10), width=5)
        en1.grid(row=n+1, column=0, padx=5, pady=6)
        rownanie.append(en1)
        tk.Label(ramka1, text="X +", font=("Verdana", 10), width=2).grid(row=n+1, column=1, padx=5, pady=6)    
        en2 = tk.Entry(ramka1, font=("Verdana", 10), width=5)
        en2.grid(row=n+1, column=2, padx=5, pady=6)
        rownanie.append(en2)
        if niewiadome==2:
            tk.Label(ramka1, text="Y =", font=("Verdana", 10), width=2).grid(row=n+1, column=3, padx=5, pady=6)
        elif niewiadome>=3:
            tk.Label(ramka1, text="Y +", font=("Verdana", 10), width=2).grid(row=n+1, column=3, padx=5, pady=6)    
            en3 = tk.Entry(ramka1, font=("Verdana", 10), width=5)
            en3.grid(row=n+1, column=4, padx=5, pady=6)
            rownanie.append(en3)
            if niewiadome==3:
                tk.Label(ramka1, text="Z =", font=("Verdana", 10), width=2).grid(row=n+1, column=5, padx=5, pady=6)
            elif niewiadome>=4:
                tk.Label(ramka1, text="Z +", font=("Verdana", 10), width=2).grid(row=n+1, column=5, padx=5, pady=6)    
                en4 = tk.Entry(ramka1, font=("Verdana", 10), width=5)
                en4.grid(row=n+1, column=6, padx=5, pady=6)
                rownanie.append(en4)
                if niewiadome==4:
                    tk.Label(ramka1, text="S =", font=("Verdana", 10), width=2).grid(row=n+1, column=7, padx=5, pady=6)
                elif niewiadome==5:
                    tk.Label(ramka1, text="S +", font=("Verdana", 10), width=2).grid(row=n+1, column=7, padx=5, pady=6)    
                    en5 = tk.Entry(ramka1, font=("Verdana", 10), width=5)
                    en5.grid(row=n+1, column=8, padx=5, pady=6)
                    rownanie.append(en5)
                    tk.Label(ramka1, text="T =", font=("Verdana", 10), width=2).grid(row=n+1, column=9, padx=5, pady=6)
        en6 = tk.Entry(ramka1, font=("Verdana", 10), width=5)
        en6.grid(row=n+1, column=2*niewiadome, padx=5, pady=6)
        rownanie.append(en6)
    przycisk = tk.Button(ramka1, text=u"OBLICZ", width=50, command=lambda: wynik_rownania(ramka, ramka2, przycisk, rownanie, niewiadome), font=("Verdana", 10), bg='#C0C0C0')
    przycisk.grid(row=niewiadome+2, column=0, columnspan=11, padx=3, pady=6)
    tk.Button(ramka1, text=u"ODŚWIEŻ", font=("Verdana", 10), command=lambda: uklad_rownan(ramka, niewiadome), width = 50, bg='#C0C0C0').grid(row=niewiadome+3, column=0, columnspan=11,  padx=5, pady=6)
    
#Okno, w którym otrzymuje się wynik równania
def wynik_rownania(ramka, ramka2, przycisk, rownanie, niewiadome):
    przycisk.config(state="disabled")
    matrix = np.zeros((niewiadome, niewiadome))
    matrix1 = np.zeros((niewiadome, niewiadome))
    matrix2 = np.zeros((niewiadome, 1))
    w=0
    k=0
    ramka2 = tk.Frame(ramka, relief=tk.RAISED, borderwidth=1, width = 480)
    ramka2.grid(row=niewiadome+3, column=0, rowspan=niewiadome+3, columnspan=10, padx=5, pady=5, sticky = "NE")
    for entry in rownanie:
        try : 
            en = float(entry.get())            
        except ValueError:
            tk.Label(ramka2, text=u'Nie została podana odpowiednia liczba', font=("Verdana", 10), width = 57).grid(row=niewiadome+5, column=0, columnspan=11, padx=7, pady=5)
            return
        if k<niewiadome:
            matrix1[w][k] = en
        else:
            matrix2[w][0] = en
        if k==(niewiadome):
            w=w+1
            k=0
        else:
            k = k+1
    try:
        rozwiazanie = solve(matrix1,matrix2)
    except:
        rozwiazanie = 0
        for n in range(niewiadome):
            matrix = matrix1
            for m in range(niewiadome):
                matrix[m][n] = matrix2[m][0]
                wyznacznik = np.linalg.det(matrix)
                if wyznacznik == 0:
                    rozwiazanie = rozwiazanie + 1
        if rozwiazanie == niewiadome:
           tk.Label(ramka2, text=u'Układ jest nieoznaczony', font=("Verdana", 10), width = 57).grid(row=niewiadome+5, column=0, columnspan=11, padx=7, pady=5)
           return
        else:
           tk.Label(ramka2, text=u'Układ jest sprzeczny', font=("Verdana", 10), width = 57).grid(row=niewiadome+5, column=0, columnspan=11, padx=7, pady=5)
           return   
    tk.Label(ramka2, text=u'WYNIK', font=("Verdana", 15), width = 35).grid(row=niewiadome+5, column=0, columnspan=11, padx=7, pady=5)
    tk.Label(ramka2, text="X:", font=("Verdana", 10), width=2).grid(row=niewiadome+6, column=0, padx=5, pady=6)  
    en1 = tk.Entry(ramka2, font=("Verdana", 10), width=5)
    en1.grid(row=niewiadome+6, column=1, padx=5, pady=6)
    en1.insert(0,rozwiazanie[0][0])
    tk.Label(ramka2, text="Y:", font=("Verdana", 10), width=2).grid(row=niewiadome+6, column=2, padx=5, pady=6)  
    en2 = tk.Entry(ramka2, font=("Verdana", 10), width=5)
    en2.grid(row=niewiadome+6, column=3, padx=5, pady=6)
    en2.insert(0,rozwiazanie[1][0])
    if niewiadome >= 3:
        tk.Label(ramka2, text="Z:", font=("Verdana", 10), width=2).grid(row=niewiadome+6, column=4, padx=5, pady=6)  
        en3 = tk.Entry(ramka2, font=("Verdana", 10), width=5)
        en3.grid(row=niewiadome+6, column=5, padx=5, pady=6)
        en3.insert(0,rozwiazanie[2][0])
    elif niewiadome >= 4:
        tk.Label(ramka2, text="S:", font=("Verdana", 10), width=2).grid(row=niewiadome+6, column=6, padx=5, pady=6)  
        en3 = tk.Entry(ramka2, font=("Verdana", 10), width=5)
        en3.grid(row=niewiadome+6, column=7, padx=5, pady=6)
        en3.insert(0,rozwiazanie[3][0])
    elif niewiadome >= 4:
        tk.Label(ramka2, text="T:", font=("Verdana", 10), width=2).grid(row=niewiadome+6, column=8, padx=5, pady=6)  
        en3 = tk.Entry(ramka2, font=("Verdana", 10), width=5)
        en3.grid(row=niewiadome+6, column=9, padx=5, pady=6)
        en3.insert(0,rozwiazanie[4][0])