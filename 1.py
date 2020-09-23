# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 08:29:52 2020

@author: karel
"""

feet,inch = eval(input("Enter your height (in feet, followed by inch separated by a comma):", ))
print("Feet:", feet)
print("Inches:", inch)
float(feet)
inch=inch/12
feet+=inch
board = feet*30.48*88/100
print("Suggested board length:", board)