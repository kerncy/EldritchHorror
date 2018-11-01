# !/bin/python
# coding: utf-8


class Monstre:
    m_nom = ""
    m_horreur = 0
    m_degat = 0
    m_resistance = 0

    m_blessure = 0

    def __init__(self, nom, horreur, degat, resistance):
        self.m_nom = nom
        self.m_horreur = horreur
        self.m_degat = degat
        self.m_resistance = resistance

