import numpy as np
import random

class xor_hacker:
    def __init__(self, target):
        self.target = target
    
    def guess(self, iters):
        g_list = []
        for interations in range(iters):
            guess1 = ''
            guess2 = ''
            for i in self.target:
                sg1 = random.getrandbits(1)
                if i == '0':
                    sg2 = (sg1-1) * -1
                if i == '1':
                    sg2 = sg1
                guess1+=str(sg1)
                guess2+=str(sg2)
            if (guess1, guess2) not in g_list:
                g_list.append((guess1, guess2))
        return g_list
