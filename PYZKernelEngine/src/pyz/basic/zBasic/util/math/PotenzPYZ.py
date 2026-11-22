# -*- coding: utf-8 -*-

'''
Created on 21.11.2026

Funktoniert auch unter Jython2.7, also auch unter Python2

@author: Fritz Lindhauer
'''

class PotenzPYZ:
    def __init__(self, exponent):
        self.Exponent = exponent
        
    def __call__(self, basis):
        return basis ** self.Exponent
    
# Code zum Test am Schluss, nur wenn diese Klasse direkt gestartet wird
if __name__ == "__main__":
    #Instanziere die Klasse mit dem passenden Namen
    hoch3 = PotenzPYZ(3)
    
    #Wende das an, als "vom Namen her sprechende" Methode
    erg01 = hoch3(2)    
    print("2 hoch 3: ", erg01) 
    
    erg02 = hoch3(5)    
    print("5 hoch 3: ", erg02) 
    
    