# -*- coding: utf-8 -*-
"""
arbeidskrav-2 PY1010

Created on Sun Oct  4 20:37:59 2026

@author: Terje Jakobsen
github: terjako9000

"""

#%% Oppgave 1

alder = int(input("Hvilket år er du født?  "))

a = 2024 - alder

print("Personen blir i løpet av 2024", a, "år gammel.")

"OPPDATERING 2026"

b = 2026 - alder

print("Personen blir i løpet av 2026", b, "år gammel.")

#%% Oppgave 2

antall_elever = int(input("Skriv inn antall elever: "))

antall_pizzaer = float(antall_elever/4)

p = int(antall_elever + antall_pizzaer - 1) // 4

print("Totalt antall pizzaer som må bestilles er", p)

#%% Oppgave 3

import numpy as np

v_grad = float(input("Skriv inn gradtallet: "))

v_rad = v_grad*np.pi/180

radiantallet_avrundet = round(v_rad, 2)

print("Radiantallet til gradtall", v_grad, "er", radiantallet_avrundet)

#%% Oppgave 4

# a
#setter opp datasettet fra oppgaven
    
data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

# b

#definerer land for å få inn ionformasjon
land = input("Hvilket land?")
    
#setter forutsetning for å skrive ut svaret
if land in data:
    print(data[land][0], "er hovedstaden i", land, "og det er", data[land][1], "mill. innbyggere i", data[land][0])
   
else:
    print("Fant ikke data for", land)

#%% oppgave 4 c

data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

land = input("Skriv inn et nytt land:")

if land not in data:
    hovedstad = input("Skriv inn hovedstaden:")
    innbyggere = float(input("Skriv inn antall innbyggere i millioner:"))

    data[land] = [hovedstad, innbyggere]
    
    print(data)
    
else:
    print("Landet er allerede med i dictionary")
    
#%% oppgave 5

import math   #henter mattesettet i python

#starter med omkrets

def omkrets_halvsirkel(a):
    omkrets = (math.pi * a) + (2 * a)
    return omkrets


def omkrets_trekant(a, b):
    c = math.sqrt(a**2 + b**2) #lager diagonalen c med pythagoras
    omkrets = a + b + c
    return omkrets

a = 2      #a er radius
b = 5      #b er langsiden

#definerer opp omkretsene så de kan summeres
sirkel = omkrets_halvsirkel(a)
trekant = omkrets_trekant(a, b)

tot_omkrets = sirkel + trekant - (2 * a)   #trekker fra felles side a

#fortsetter med areal

def areal_halvsirkel(a):
    return (math.pi * a**2) / 2   #areal av sirkel delt på 2
    
def areal_trekant(a, b):  
    return (a * b) / 2

#definerer arealene så de kan summeres
areal_sirkel = areal_halvsirkel(a)
areal_trek = areal_trekant(a, b)
total_areal = areal_sirkel + areal_trek
    

print("omkrets:")
print(f"omkrets av halvsirkel er: {omkrets_halvsirkel(a):.2f}.")
print(f"omkretsen til trekanten er: {omkrets_trekant(a, b):.2f}.")
print(f"den totale omkretsen blir: {tot_omkrets:.2f}, gitt radius og langside")
print("areal:")
print(f"Arealet av figuren er {total_areal:.2f}")


#%% oppgave 6

import numpy as np
import matplotlib.pyplot as plt

# Definerer funksjonen f(x) = -x^2 - 5
def f(x):
    return -x**2 - 5

# Lager 200 jevnt fordelte x-verdier fra -10 til 10
x = np.linspace(-10, 10, 200)

# Regner ut tilhørende y-verdier
y = f(x)

# Tegner grafen
plt.plot(x, y, label='f(x) = -x^2 - 5')
plt.title('Grafen til f(x) = -x^2 - 5')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()



