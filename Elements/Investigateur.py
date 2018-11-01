# !/bin/python
# coding: utf-8


class Investigateur:
    m_nom = ""

    m_vie = 0
    m_santeMentale = 0

    m_savoir = 0
    m_influence = 0
    m_observation = 0
    m_force = 0
    m_volonte = 0

    m_sort = []
    m_condition = []
    m_objet = []
    m_artefact = []

    def __init__(self, vie, santeMentale, nom, savoir, influence, observation, force, volonte):
        self.m_nom = nom
        self.m_vie = vie
        self.m_santeMentale = santeMentale
        self.m_savoir = savoir
        self.m_influence = influence
        self.m_observation = observation
        self.m_force = force
        self.m_volonte = volonte


