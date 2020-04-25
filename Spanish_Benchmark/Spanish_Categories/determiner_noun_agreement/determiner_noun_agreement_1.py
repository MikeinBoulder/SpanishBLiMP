import numpy as np
import pandas as pd
from Spanish_Utils.vocab_sets import *
from Spanish_Utils.randomize import *
from Spanish_Utils.string_utils import * 
import random
import sys


def sample(iter,out):
    for i in range(iter):
        #plural verb
        V = verb_cleanup(choice(all_trans_p3is))
        N1 = choice(all_proper_nouns)
        #fem sg
        n_choice = choice(['nfsg','nfpl','nmsg','nmpl'])
        if n_choice == 'nfsg':
            demonst = choice(all_demonstratives_fem_sg)
            N2_good = choice(n_fem_sg, all_proper_nouns)
            N2_bad = choice(all_plural_nouns, all_proper_nouns)
        elif n_choice == 'nfpl':
            demonst = choice(all_demonstratives_fem_pl)
            N2_good = choice(n_fem_pl, all_proper_nouns)
            N2_bad = choice(all_singular_nouns, all_proper_nouns)
        elif n_choice == 'nmsg':
            demonst = choice(all_demonstratives_masc_sg)
            N2_good = choice(n_masc_sg, all_proper_nouns)
            N2_bad = choice(all_plural_nouns, all_proper_nouns)
        elif n_choice == 'nmpl':
            demonst = choice(all_demonstratives_masc_pl)
            N2_good = choice(n_masc_pl, all_proper_nouns)
            N2_bad = choice(all_singular_nouns, all_proper_nouns)
        data = {
            "sentence_good" : string_beautify("%s %s %s %s." % (N1, V, demonst, N2_good)),
            "sentence_bad" : string_beautify("%s %s %s %s." % (N1, V, demonst, N2_bad))
        }
        out.write(str(data)+'\n')

try:
    iter = int(sys.argv[1])
    out = open(sys.argv[2],'w')
    sample(iter,out)
except IndexError:
    print('To run this file use:\npython determiner_noun_agreement_1.py <# of sentences> <output path>')
    sys.exit()
        
