import pandas as pd
import numpy as np

class Fusee():
    """La classe fusee prend en attribut, la taille, le poids, le nombre de modules"""
    def __init__(self, name, nom_fichier):
        database = pd.read_csv(nom_fichier, sep=',')
        caracteristiques = database.loc[database.Name == name]
        self.name = name
        self.year = caracteristiques['Year'].values[0]
        self.country = caracteristiques['Country'].values[0]
        self.mission = caracteristiques['Mission'].values[0]
        self.stage_number = caracteristiques['Stages number'].values[0]
        self.height = caracteristiques['Height [m]'].values[0]
        self.lift_off_mass = caracteristiques['Lift-off mass [tons]'].values[0]
        self.payload_mass = caracteristiques['Payload mass [kg]'].values[0]
        self.s1_length = caracteristiques['S1 length [m]'].values[0]
        self.s1_diameter = caracteristiques['S1 diameter [m]'].values[0]
        self.s1_thrust = caracteristiques['S1 thrust [kN]'].values[0]
        self.s1_isp = caracteristiques['S1 Isp [s]'].values[0]
        self.s1_m0 = caracteristiques['S1 m0 [tons]'].values[0]
        self.s1_mp = caracteristiques['S1 mp [tons]'].values[0]
        self.s2_length = caracteristiques['S2 length [m]'].values[0]
        self.s2_diameter = caracteristiques['S2 diameter [m]'].values[0]
        self.s2_thrust = caracteristiques['S2 thrust [kN]'].values[0]
        self.s2_isp = caracteristiques['S2 Isp [s]'].values[0]
        self.s2_m0 = caracteristiques['S2 m0 [tons]'].values[0]
        self.s2_mp = caracteristiques['S2 mp [tons]'].values[0]

sputnik = Fusee('Sputnik','~rocket_database.csv')






































