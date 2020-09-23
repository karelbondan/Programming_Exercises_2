# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:09:46 2020

@author: karel
"""

mass,force = eval(input("Enter mass(kg) and force(N) sequentially, separated by a comma: ", ))
acc = force/mass
print("The acceleration is", acc)