class one_round_battle:

    def __init__(self, mc1, mc2):
        self.mc1 = mc1
        self.mc2 = mc2

    def battle(self):
        self.mc1.attack(self.mc2)
        self.mc2.attack(self.mc1)
