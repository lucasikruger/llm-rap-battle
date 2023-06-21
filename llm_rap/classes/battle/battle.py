
import random

from llm_rap.classes.agent.mc import Mc
class Battle:

    #inicializamos la batalla con dos mc's ya creados
    def __init__(self, mc1 : Mc, mc2: Mc):
        self.mc1 = mc1
        self.mc2 = mc2

    #la battle debería saber cuantas rondas tiene que correr.
    def startBattle(self, rounds):
        #la idea es que luego de cada ronda haya un tiempo de "feedback".
        #for round in rounds:
            #en cada ronda, ambos mcs deberían "atacar". uno debe responderle al otro
        output1 = self.mc1.rap()
        output2 = ""#self.mc2.rap()

        return output1, output2

