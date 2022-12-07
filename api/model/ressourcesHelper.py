# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 13:50:16 2022

@author: leabu
"""
import matplotlib
import os
from pathlib import Path


path_donnees = Path("model/ressources/")
name_donnees = "Balayages_1_A_1_Canaux_1001 _A_1002 .csv"
path_density = Path("model/ressources/")
name_density = "Density_top.csv"
images = Path("Images/")
print("testtetestest " + str(path_donnees))

matplotlib.rcParams.update({
    'font.family': 'serif',
    'font.size' : 14,
    'text.usetex': True,
    'pgf.rcfonts': False,
    'legend.facecolor': 'white',
    'legend.frameon': False,
    'grid.linestyle': 'dotted',
})