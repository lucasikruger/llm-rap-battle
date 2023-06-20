
from llm_rap.classes.agent import mc
import random
class Battle:

    #inicializamos la batalla con dos mc's ya creados
    def __init__(self, mc1 : mc, mc2: mc):
        self.mc1 = mc1
        self.mc2 = mc2

    #la battle debería saber cuantas rondas tiene que correr.
    def startBattle(self, rounds):
        #la idea es que luego de cada ronda haya un tiempo de "feedback".
        for round in rounds:
            #en cada ronda, ambos mcs deberían atacar.
            output1 = self.mc1.rap()
            output2 = self.mc2.attack(output2)

