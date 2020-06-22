# -*- coding: utf-8 -*-

"""
@author: Maja Rusak
"""

import tkinter as tk
import numpy as np
import scipy.linalg as la

i=0

#Tworzenie okna, w którym podaje się wymiary macierzy do odpowiedniego rozwiązania działań, dla 
#wszystkich działań macierzowych, oprócz mnożenia macierzy, przy którym dwiemacierze nie muszą mieć
#takiego samego wymiaru
def wymiarMacierz(ramka, operacja):
    czyscRamke(ramka)
    ramka1 = tk.Frame(ramka, relief=tk.RAISED, borderwidth=1, width = 480, heigh = 540)
    ramka1.grid(row=0, column=0, columnspan=10, padx=5, pady=5)
    tk.Label(ramka1, text=u'Wymiar macierzy', font=("Verdana", 10), width = 15).grid(row=0, column=0, columnspan=4, padx=5, pady=5) 
    wymiar1 = tk.Spinbox(ramka1, values=("",1,2,3,4,5), font=("Verdana", 10), width=5)
    wymiar1.grid(row=0, column=4, columnspan=2, padx=6, pady=5)
    wymiar2 = tk.Spinbox(ramka1, values=("",1,2,3,4,5), font=("Verdana", 10), width=5)
    wymiar2.grid(row=0, column=6, columnspan=2, padx=6, pady=5)        
    if operacja == 1:
        przycisk = tk.Button(ramka1, text=u"Wartości macierzy", command=lambda: dodawanie_odejmowanie(ramka, przycisk, wymiar1.get(), wymiar2.get()), width=21, font=("Verdana", 10), state="normal", bg='#C0C0C0')
        przycisk.grid(row=0, column=8, columnspan=3, padx=12, pady=10)
    elif operacja >= 2:
        przycisk = tk.Button(ramka1, text=u"Wartości macierzy", command=lambda: wyznacznik(ramka, operacja, przycisk, wymiar1.get(), wymiar2.get()), width=21, font=("Verdana", 10), state="normal", bg='#C0C0C0')
        przycisk.grid(row=0, column=8, columnspan=3, padx=12, pady=10)
  
#Tworzenie okna dla działania mnożenia macierzy, gdzie podawane są wymiary dwóch macierzy      
def wymiarMacierzMnozenie(ramka):
    czyscRamke(ramka)
    ramka1 = tk.Frame(ramka, relief=tk.RAISED, borderwidth=1, width = 480, heigh = 540)
    ramka1.grid(row=0, column=0, rowspan = 2, columnspan=10, padx=5, pady=5)
    tk.Label(ramka1, text=u'Wymiary macierzy 1:', font=("Verdana", 10), width = 17).grid(row=0, column=0, columnspan=4, padx=5, pady=5) 
    wymiar1 = tk.Spinbox(ramka1, values=("",1,2,3,4,5), font=("Verdana", 10), width=5)
    wymiar1.grid(row=0, column=4, columnspan=2, padx=6, pady=5)
    wymiar2 = tk.Spinbox(ramka1, values=("",1,2,3,4,5), font=("Verdana", 10), width=5)
    wymiar2.grid(row=0, column=6, columnspan=2, padx=6, pady=5)
    tk.Label(ramka1, text=u'Wymiary macierzy 2:', font=("Verdana", 10), width = 17).grid(row=1, column=0, columnspan=4, padx=5, pady=5) 
    wymiar3 = tk.Spinbox(ramka1, values=("",1,2,3,4,5), font=("Verdana", 10), width=5)
    wymiar3.grid(row=1, column=4, columnspan=2, padx=6, pady=5)
    wymiar4 = tk.Spinbox(ramka1, values=("",1,2,3,4,5), font=("Verdana", 10), width=5)
    wymiar4.grid(row=1, column=6, columnspan=2, padx=6, pady=5)
    przycisk = tk.Button(ramka1, text=u"Wartości macierzy", command=lambda: mnozenie(ramka, przycisk, wymiar1.get(), wymiar2.get(), wymiar3.get(), wymiar4.get()), width=20, font=("Verdana", 10), state="normal", bg='#C0C0C0')
    przycisk.grid(row=0, column=8, columnspan=3, padx=12, pady=10)

#Okno wypisujące pola edycyjne, aby można było wpisać odpowiednie wartosci macierzy dla dodawania
#oraz odejmowania (nałożone jest również zabezpieczenie, że maksymalny wymiar macierzy, który można
#obliczyć w tym programie to 5x5)
def dodawanie_odejmowanie(ramka, przycisk, wymiar1, wymiar2):
    przycisk.config(state="disabled")
    n = int(wymiar1)
    m = int(wymiar2)
    ramka2 = tk.Frame(ramka, relief=tk.RAISED, borderwidth=1, width = 480, heigh = 540)
    ramka2.grid(row=1, column=0, rowspan=n*2+1, columnspan=10, padx=7, pady=5, sticky = "NE")
    macierz1 = []
    macierz2 = []
    if n >= 6 or m >= 6:
        tk.Label(ramka2, text=u'Maksymalny wymiar macierzy to 5x5', font=("Verdana", 10), width=57).grid(row=1, column = 0, columnspan=10,  padx=8)
        tk.Button(ramka2, text=u"ODŚWIEŻ", font=("Verdana", 10), command=lambda: wymiarMacierz(ramka,1), width = 15, bg='#C0C0C0').grid(row=2, column=0, columnspan=10,  padx=11)
        return
    tk.Label(ramka2, text=u'A:', font=("Verdana", 15)).grid(row=1, column = 0, rowspan=n)
    tk.Label(ramka2, text=u'[', font=("Verdana", 15)).grid(row=1, column = 1, rowspan=n)
    for wiersze in range(n):
        for kolumny in range(m):
            en1 = tk.Entry(ramka2, font=("Verdana", 10), width=3)
            en1.grid(row=wiersze+1, column=kolumny+2, padx=5, pady=6)
            macierz1.append(en1)
    tk.Label(ramka2, text=u']', font=("Verdana", 15)).grid(row=1, column=m+2, rowspan=n)
    tk.Label(ramka2, text=u'', font=("Verdana", 15), width=35).grid(row=n+1, column=0, columnspan=9, padx=8)
    tk.Label(ramka2, text=u'B:', font=("Verdana", 15)).grid(row=n+2, column = 0, rowspan=n)
    tk.Label(ramka2, text=u'[', font=("Verdana", 15)).grid(row=n+2, column = 1, rowspan=n)
    for wiersze in range(n):
        for kolumny in range(m):
            en2 = tk.Entry(ramka2, font=("Verdana", 10), width=3)
            en2.grid(row=wiersze+n+2, column=kolumny+2, padx=5, pady=6)
            macierz2.append(en2)
    tk.Label(ramka2, text=u']', font=("Verdana", 15)).grid(row=n+2, column=m+2, rowspan=n)  
    tk.Button(ramka2, text=u"DODAJ", width=15, font=("Verdana", 10), command=lambda: wynik(ramka, macierz1, macierz2, n, m, 0), bg='#C0C0C0').grid(row=1, column=8, columnspan=3,  padx=11)
    tk.Button(ramka2, text=u"ODEJMIJ", width=15, font=("Verdana", 10), command=lambda: wynik(ramka, macierz1, macierz2, n, m, 1), bg='#C0C0C0').grid(row=2, column=8, columnspan=3,  padx=11)
    tk.Button(ramka2, text=u"ODŚWIEŻ", font=("Verdana", 10), command=lambda: wymiarMacierz(ramka,1), width = 15, bg='#C0C0C0').grid(row=3, column=8, columnspan=3,  padx=11)

#Okno wypisujące pola edycyjne dla mnożenia macierzy
def mnozenie(ramka, przycisk, wymiar1, wymiar2, wymiar3, wymiar4):
    przycisk.config(state="disabled")
    n = int(wymiar1)
    m = int(wymiar2)
    i = int(wymiar3)
    j = int(wymiar4)
    ramka2 = tk.Frame(ramka, relief=tk.RAISED, borderwidth=1, width = 480, heigh = 540)
    ramka2.grid(row=2, column=0, rowspan=n+i+1, columnspan=10, padx=7, pady=5, sticky = "NE")
    if n >= 6 or m >= 6 or i >= 6 or j >= 6:
        tk.Label(ramka2, text=u'Maksymalny wymiar macierzy to 5x5', font=("Verdana", 10), width=57).grid(row=2, column = 0, columnspan=10,  padx=8)
        tk.Button(ramka2, text=u"ODŚWIEŻ", font=("Verdana", 10), command=lambda: wymiarMacierzMnozenie(ramka), width = 15, bg='#C0C0C0').grid(row=3, column=0, columnspan=10,  padx=11)
        return
    if wymiar2 != wymiar3:
        tk.Label(ramka2, text=u'Macierz A musi mieć tyle samo kolumn, co macierz B wierszy.', font=("Verdana", 10), width=57).grid(row=2, column = 0, columnspan=10, padx=8)
        tk.Button(ramka2, text=u"ODŚWIEŻ", font=("Verdana", 10), command=lambda: wymiarMacierzMnozenie(ramka), width = 15, bg='#C0C0C0').grid(row=3, column=0, columnspan=10,  padx=11)
        return
    macierz1 = []
    macierz2 = []
    tk.Label(ramka2, text=u'A:', font=("Verdana", 15)).grid(row=2, column = 0, rowspan=n)
    tk.Label(ramka2, text=u'[', font=("Verdana", 15)).grid(row=2, column = 1, rowspan=n)
    for wiersze in range(n):
        for kolumny in range(m):
            en1 = tk.Entry(ramka2, font=("Verdana", 10), width=3)
            en1.grid(row=wiersze+2, column=kolumny+2, padx=5, pady=6)
            macierz1.append(en1)
    tk.Label(ramka2, text=u']', font=("Verdana", 15)).grid(row=2, column=m+2, rowspan=n)
    tk.Label(ramka2, text=u'', font=("Verdana", 15), width=35).grid(row=n+2, column=0, columnspan=9, padx=8)
    tk.Label(ramka2, text=u'B:', font=("Verdana", 15)).grid(row=n+3, column = 0, rowspan=i)
    tk.Label(ramka2, text=u'[', font=("Verdana", 15)).grid(row=n+3, column = 1, rowspan=i)
    for wiersze in range(i):
        for kolumny in range(j):
            en2 = tk.Entry(ramka2, font=("Verdana", 10), width=3)
            en2.grid(row=wiersze+n+3, column=kolumny+2, padx=5, pady=6)
            macierz2.append(en2)
    tk.Label(ramka2, text=u']', font=("Verdana", 15)).grid(row=n+3, column=j+2, rowspan=i)  
    tk.Button(ramka2, text=u"POMNÓŻ", width=15, command=lambda: wynikMnozenia(ramka, macierz1, macierz2, n, m, i, j), font=("Verdana", 10), bg='#C0C0C0').grid(row=2, column=8, columnspan=3,  padx=11)
    tk.Button(ramka2, text=u"ODŚWIEŻ", command=lambda: wymiarMacierzMnozenie(ramka), font=("Verdana", 10), width = 15, bg='#C0C0C0').grid(row=3, column=8, columnspan=3,  padx=11)

#Okno wypisujące pola edycyjne dla reszty działań związanych z macierzami w tym programie
def wyznacznik(ramka, operacja, przycisk, wymiar1, wymiar2):
    przycisk.config(state="disabled")
    n = int(wymiar1)
    m = int(wymiar2)
    ramka2 = tk.Frame(ramka, relief=tk.RAISED, borderwidth=1, width = 480, heigh = 540)
    ramka2.grid(row=1, column=0, rowspan=n*2+1, columnspan=10, padx=7, pady=5, sticky = "NE")
    if n >= 6 or m >= 6:
        tk.Label(ramka2, text=u'Maksymalny wymiar macierzy to 5x5', font=("Verdana", 10), width=57).grid(row=1, column = 0, columnspan=11,  padx=11)
        tk.Button(ramka2, text=u"ODŚWIEŻ", font=("Verdana", 10), command=lambda: wymiarMacierz(ramka,1), width = 15, bg='#C0C0C0').grid(row=2, column=0, columnspan=10,  padx=11)
        return
    if wymiar1 != wymiar2 and operacja != 4:
        tk.Label(ramka2, text=u'Macierz musi być kwadratowa. Wpisz wymiar jeszcze raz.', font=("Verdana", 10), width=57).grid(row=1, column = 0, columnspan=10, padx=8)
        tk.Button(ramka2, text=u"ODŚWIEŻ", font=("Verdana", 10), command=lambda: wymiarMacierz(ramka,2), width = 15, bg='#C0C0C0').grid(row=2, column=0, columnspan=10,  padx=11)
        return
    macierz1 = []
    tk.Label(ramka2, text=u'A:', font=("Verdana", 15)).grid(row=1, column = 0, rowspan=n)
    if operacja == 2:
        tk.Label(ramka2, text=u'|', font=("Verdana", 15)).grid(row=1, column = 1, rowspan=n)
    else:
        tk.Label(ramka2, text=u'[', font=("Verdana", 15)).grid(row=1, column = 1, rowspan=n)
    for wiersze in range(n):
        for kolumny in range(m):
            en1 = tk.Entry(ramka2, font=("Verdana", 10), width=3)
            en1.grid(row=wiersze+1, column=kolumny+2, padx=5, pady=6)
            macierz1.append(en1)
    if operacja ==2:
        tk.Label(ramka2, text=u'|', font=("Verdana", 15)).grid(row=1, column=m+2, rowspan=n)
    else:
        tk.Label(ramka2, text=u']', font=("Verdana", 15)).grid(row=1, column=m+2, rowspan=n)
    tk.Label(ramka2, text=u'', font=("Verdana", 15), width=35).grid(row=n+1, column=0, columnspan=9, padx=6)
    if operacja == 2:
        tk.Button(ramka2, text=u"OBLICZ", width=15, font=("Verdana", 10), command=lambda: wynik(ramka, macierz1, macierz1, n, m, 2), bg='#C0C0C0').grid(row=1, column=8, columnspan=3,  padx=11)
        tk.Button(ramka2, text=u"ODŚWIEŻ", font=("Verdana", 10), command=lambda: wymiarMacierz(ramka,2), width = 15, bg='#C0C0C0').grid(row=2, column=8, columnspan=3,  padx=11)
    elif operacja == 3:
        tk.Button(ramka2, text=u"OBLICZ", width=15, font=("Verdana", 10), command=lambda: wynik(ramka, macierz1, macierz1, n, m, 3), bg='#C0C0C0').grid(row=1, column=8, columnspan=3,  padx=11)
        tk.Button(ramka2, text=u"ODŚWIEŻ", font=("Verdana", 10), command=lambda: wymiarMacierz(ramka,3), width = 15, bg='#C0C0C0').grid(row=2, column=8, columnspan=3,  padx=11)
    elif operacja == 4:
        tk.Button(ramka2, text=u"OBLICZ", width=15, font=("Verdana", 10), command=lambda: wynik(ramka, macierz1, macierz1, n, m, 4), bg='#C0C0C0').grid(row=1, column=8, columnspan=3,  padx=11)
        tk.Button(ramka2, text=u"ODŚWIEŻ", font=("Verdana", 10), command=lambda: wymiarMacierz(ramka,4), width = 15, bg='#C0C0C0').grid(row=2, column=8, columnspan=3,  padx=11)
    elif operacja == 5:
        tk.Button(ramka2, text=u"OBLICZ", width=15, font=("Verdana", 10), command=lambda: wynik(ramka, macierz1, macierz1, n, m, 5), bg='#C0C0C0').grid(row=1, column=8, columnspan=3,  padx=11)
        tk.Button(ramka2, text=u"ODŚWIEŻ", font=("Verdana", 10), command=lambda: wymiarMacierz(ramka,5), width = 15, bg='#C0C0C0').grid(row=2, column=8, columnspan=3,  padx=11)

#Okno, w którym pojawia się wynik mnożenia macierzy
def wynikMnozenia(ramka, macierz1, macierz2, wymiar1, wymiar2, wymiar3, wymiar4):
    M1 = np.zeros((wymiar1, wymiar2)).reshape(wymiar1, wymiar2)
    M2 = np.zeros((wymiar3, wymiar4)).reshape(wymiar3, wymiar4)
    w=0
    k=0  
    ramka3 = tk.Frame(ramka, relief=tk.RAISED, borderwidth=1)
    ramka3.grid(row=wymiar1+wymiar3+3, column=0, rowspan=wymiar1, columnspan=7, padx=7, pady=5, sticky = "WE")
    for entry in macierz1:
        try : 
            en1 = float(entry.get())            
        except ValueError:
            tk.Label(ramka3, text=u'Nie została podana odpowiednia liczba', font=("Verdana", 10), width = 57).grid(row=2*wymiar1+1, column=0, columnspan=11, padx=7, pady=5)
            return
        M1[w][k] = en1
        if k==(wymiar2-1):
            w=w+1
            k=0
        else:
            k = k+1
    w=0
    k=0
    for entry in macierz2:
        try : 
            en2 = float(entry.get())            
        except ValueError:
            tk.Label(ramka3, text=u'Nie została podana odpowiednia liczba', font=("Verdana", 10), width = 57).grid(row=2*wymiar1+1, column=0, columnspan=11, padx=7, pady=5)
            return
        M2[w][k] = en2
        if k==(wymiar4-1):
            w=w+1
            k=0
        else:
            k = k+1
    operacja = M1.dot(M2)
    tk.Label(ramka3, text=u'WYNIK', font=("Verdana", 15), width=35).grid(row=wymiar1+wymiar3+2, column=0, columnspan=9, padx=7)
    tk.Label(ramka3, text=u'C:', font=("Verdana", 15)).grid(row=wymiar1+wymiar3+3, column = 0, rowspan=wymiar1)
    tk.Label(ramka3, text=u'[', font=("Verdana", 15)).grid(row=wymiar1+wymiar3+3, column=1, rowspan=wymiar1)
    for wiersze in range(wymiar1):
        for kolumny in range(wymiar2):
            en = tk.Entry(ramka3, font=("Verdana", 10), width = 5)
            en.insert(0,round(operacja[wiersze][kolumny],2))
            en.grid(row=wymiar1+wymiar3+3, column=kolumny+2, padx=5, pady=6)
    tk.Label(ramka3, text=u']', font=("Verdana", 15)).grid(row=wymiar1+wymiar3+3, column=wymiar2+2, rowspan=wymiar1)

#Okno, w którym pojawia się wynik operacji na macierzach, wszystkich oprócz mnożenia macierzy
def wynik(ramka, macierz1, macierz2, wymiar1, wymiar2, dzialanie):
    M1 = np.zeros((wymiar1, wymiar2))
    M2 = np.zeros((wymiar1, wymiar2))
    w=0
    k=0  
    ramka3 = tk.Frame(ramka, relief=tk.RAISED, borderwidth=1)
    if dzialanie<2:
        ramka3.grid(row=2*wymiar1+10, column=0, rowspan=wymiar1, columnspan=7, padx=6, pady=5, sticky = "WE")
    elif dzialanie>=2:
        ramka3.grid(row=wymiar1+10, column=0, rowspan=wymiar1, columnspan=7, padx=7, pady=5, sticky = "WE")
    for entry in macierz1:
        try : 
            en1 = float(entry.get())            
        except ValueError:
            tk.Label(ramka3, text=u'Nie została podana odpowiednia liczba', font=("Verdana", 10), width = 57).grid(row=2*wymiar1+1, column=0, columnspan=11, padx=7, pady=5)
            return
        M1[w][k] = en1
        if k==(wymiar2-1):
            w=w+1
            k=0
        else:
            k = k+1
    if dzialanie<2:
        w=0
        k=0
        for entry in macierz2:
            try : 
                en2 = float(entry.get())            
            except ValueError:
                tk.Label(ramka3, text=u'Nie została podana odpowiednia liczba', font=("Verdana", 10), width = 57).grid(row=2*wymiar1+1, column=0, columnspan=11, padx=7, pady=5)
                return
            M2[w][k] = en2
            if k==(wymiar2-1):
                w=w+1
                k=0
            else:
                k = k+1
    if dzialanie==0:
        operacja = np.add(M1,M2)
    elif dzialanie==1:
        operacja = np.subtract(M1,M2)
    elif dzialanie==2 or dzialanie==3:
        operacja = np.linalg.det(M1)
        if operacja != 0:
            operacja = np.linalg.inv(M1)
        else:
            tk.Label(ramka3, text=u'Wynacznik macierzy jest zerowy', font=("Verdana", 10), width = 57).grid(row=2*wymiar1+1, column=0, columnspan=11, padx=7, pady=5)
            return
    elif dzialanie==4:
        operacja = M1.T
    elif dzialanie==5:
        wartosci, wektory = la.eig(M1)
    if dzialanie <= 4:
        tk.Label(ramka3, text=u'WYNIK', font=("Verdana", 15), width=35).grid(row=2*wymiar1+2, column=0, columnspan=9, padx=7)
        if dzialanie !=4:
            tk.Label(ramka3, text=u'C:', font=("Verdana", 15)).grid(row=2*wymiar1+3, column = 0, rowspan=wymiar1)
            tk.Label(ramka3, text=u'[', font=("Verdana", 15)).grid(row=2*wymiar1+3, column=1, rowspan=wymiar1)
        elif dzialanie == 4:
            tk.Label(ramka3, text=u'C:', font=("Verdana", 15)).grid(row=2*wymiar1+3, column = 0, rowspan=wymiar2)
            tk.Label(ramka3, text=u'[', font=("Verdana", 15)).grid(row=2*wymiar1+3, column=1, rowspan=wymiar2)
        for wiersze in range(wymiar1):
            for kolumny in range(wymiar2):
                en = tk.Entry(ramka3, font=("Verdana", 10), width = 5)
                if dzialanie != 4:
                    en.insert(0,round(operacja[wiersze][kolumny],2))
                elif dzialanie == 4:
                    en.insert(0,round(operacja[kolumny][wiersze],2))
                en.grid(row=kolumny+3+2*wymiar1, column=wiersze+2, padx=5, pady=6)
        if dzialanie != 4:
            tk.Label(ramka3, text=u']', font=("Verdana", 15)).grid(row=2*wymiar1+3, column=wymiar2+2, rowspan=wymiar1)
        elif dzialanie == 4:
            tk.Label(ramka3, text=u']', font=("Verdana", 15)).grid(row=2*wymiar1+3, column=wymiar1+2, rowspan=wymiar2)
    elif dzialanie==2:
        tk.Label(ramka3, text=u'WYNIK', font=("Verdana", 15), width=35).grid(row=wymiar1+2, column=0, columnspan=9, padx=7)
        tk.Label(ramka3, text=u'C:', font=("Verdana", 15)).grid(row=wymiar1+3, column = 0, rowspan=wymiar1, sticky = "NE")
        en = tk.Entry(ramka3, font=("Verdana", 10), width = 7)
        en.insert(0,round(operacja,2))
        en.grid(row=3+wymiar1, column=1, padx=5, pady=5)
    elif dzialanie==5:
        tk.Label(ramka3, text=u'WYNIK', font=("Verdana", 15), width=35).grid(row=wymiar1+2, column=0, columnspan=9, padx=7)
        tk.Label(ramka3, text=u'Wartości własne', font=("Verdana", 10), width = 50).grid(row=wymiar1+3, column = 0, columnspan=9)
        tk.Label(ramka3, text=u'[', font=("Verdana", 15)).grid(row=wymiar1+4, column=0)
        for wiersze in range(wymiar2):
                en1 = tk.Entry(ramka3, font=("Verdana", 9), width = 12)
                en1.insert(0,round(wartosci[wiersze],2))
                en1.grid(row=wymiar1+4, column=wiersze+1, padx=5, pady=6)
        tk.Label(ramka3, text=u']', font=("Verdana", 15)).grid(row=wymiar1+4, column=wymiar2+1)
        tk.Label(ramka3, text=u'Wektory własne', font=("Verdana", 10), width = 50).grid(row=wymiar1+5, column = 0, columnspan=9)
        tk.Label(ramka3, text=u'[', font=("Verdana", 15)).grid(row=wymiar1+6, column=0, rowspan=wymiar1)
        for wiersze in range(wymiar1):
            for kolumny in range(wymiar2):
                en2 = tk.Entry(ramka3, font=("Verdana", 9), width = 12)
                en2.insert(0,round(wektory[wiersze][kolumny],2))
                en2.grid(row=wymiar1+wiersze+6, column=kolumny+1, padx=5, pady=6)
        tk.Label(ramka3, text=u']', font=("Verdana", 15)).grid(row=wymiar1+6, column=wymiar1+1, rowspan=wymiar1)
   
#Funkcja czyszcząca wczesniej uzupełnioną ramkę     
def czyscRamke(ramka):
    for widget in ramka.winfo_children():
       widget.destroy()
    ramka.pack_forget()