import numpy as np

def pointPotential(x,y,q,posx,posy):
    '''return electric potential for a point particle at (posx,posy)'''
    k = 8.98755*10**9
    Vpoint = (k*q/((x-posx)**2+(y-posy)**2)**(1/2.))
    return Vpoint

def dipolePotential(x,y,q,d):
    '''return electric potential for a dipole'''
    k = 8.98755*10**9
    Vdipole = (k*q/(x**2+(y-d)**2)**(1/2.)) - (k*q/(x**2+(y+d)**2)**(1/2.))
    return Vdipole
