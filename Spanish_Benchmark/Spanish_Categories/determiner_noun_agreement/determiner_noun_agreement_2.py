import numpy as np
import pandas as pd
from Spanish_Utils.vocab_sets import *
from Spanish_Utils.randomize import *
from Spanish_Utils.string_utils import * 
import random
import sys

def sample(iter,out):
    for i in range(iter):
        V = choice(all_trans_p3is)
        N1 = choice(all_proper_nouns)
        #fem sg
        demonst_choice = choice(['nfsg','nfpl','nmsg','nmpl'])
        if demonst_choice == 'nfsg':
            demonst_good = choice(all_demonstratives_fem_sg)
            demonst_bad = choice(np.union1d(np.union1d(all_demonstratives_fem_pl, all_demonstratives_masc_sg),all_demonstratives_masc_pl))
            N2 = choice(n_fem_sg, all_proper_nouns)
        elif demonst_choice == 'nfpl':
            demonst_good = choice(all_demonstratives_fem_pl)
            demonst_bad = choice(np.union1d(np.union1d(all_demonstratives_fem_sg, all_demonstratives_masc_sg),all_demonstratives_masc_pl))
            N2 = choice(n_fem_pl, all_proper_nouns)

        elif demonst_choice == 'nmsg':
            demonst_good = choice(all_demonstratives_masc_sg)
            demonst_bad = choice(np.union1d(np.union1d(all_demonstratives_fem_pl, all_demonstratives_fem_sg),all_demonstratives_masc_pl))
            N2 = choice(n_masc_sg, all_proper_nouns)
        elif demonst_choice == 'nmpl':
            demonst_good = choice(all_demonstratives_masc_pl)
            demonst_bad = choice(np.union1d(np.union1d(all_demonstratives_fem_pl, all_demonstratives_fem_sg),all_demonstratives_masc_sg))
            N2 = choice(n_masc_pl, all_proper_nouns)
        data = {
            "sentence_good" : string_beautify("%s %s %s %s." % (N1, V, demonst_good, N2)),
            "sentence_bad" : string_beautify("%s %s %s %s." % (N1, V, demonst_bad, N2))
        }
        out.write(str(data)+'\n')

try:
    iter = int(sys.argv[1])
    out = open(sys.argv[2],'w')
    sample(iter,out)
except IndexError:
    print('To run this file use:\npython determiner_noun_agreement_2.py <# of sentences> <output path>')
    sys.exit()
