from Spanish_Utils.randomize import choice
from Spanish_Utils.vocab_sets import *
from Spanish_Utils.string_utils import *
import numpy as np
import random
import sys

haber = ['ha', 'han']

def sample(iter, out):
    for i in range(iter):
        ptcp = choice(all_trans_ptcp_for_pres_perf)
        #ptcp_bad = choice(all_intrans_ptcp_for_pres_perf)
        #plural verb -> han ptcp
        if np.random.choice([True, False]):
            aux = haber[1]
            #Subject noun fem plural
            if np.random.choice([True, False]):
                D1 = choice(d_fem_pl)
                Subj = choice(all_animate_pl_nouns_f)
            else:
                D1 = choice(d_masc_pl)
                Subj = choice(all_animate_pl_nouns_m)
        #Singular verb -> ha ptcp
        else:
            aux = haber[0]
            #Subject noun fem sg
            if np.random.choice([True, False]):
                D1 = choice(d_fem_sg)
                Subj = choice(all_animate_sg_nouns_f)
            else:
                D1 = choice(d_masc_sg)
                Subj = choice(all_animate_sg_nouns_m)
        #Now select object
        if np.random.choice([True,False]):
            #fem pl object
            if np.random.choice([True, False]):
                D2 = choice(d_fem_pl)
                Obj = choice(all_animate_pl_nouns_f, np.union1d(Subj,all_proper_nouns))
            else:
                D2 = choice(d_fem_sg)
                Obj = choice(all_animate_sg_nouns_f, np.union1d(Subj, all_proper_nouns))
        else:
            if np.random.choice([True, False]):
                #masc pl obj
                D2 = choice(d_masc_pl)
                Obj = choice(all_animate_pl_nouns_m, np.union1d(Subj,all_proper_nouns))
            else:
                D2 = choice(d_masc_sg)
                Obj = choice(all_animate_sg_nouns_m, np.union1d(Subj,all_proper_nouns))

        V_bad = verb_cleanup(aux + " " + ptcp, make_reflex = True)
        if Subj[0] >= 'A' and Subj[0] <= 'Z':
            data = {
                'sentence_good' : '%s %s %s %s %s.' % (Subj, aux, ptcp, D2, Obj),
                'sentence_bad' : '%s %s %s %s.' % (Subj, V_bad, D2, Obj)
            }
        else:
            data = {
                'sentence_good' : string_beautify('%s %s %s %s %s %s.' % (D1, Subj, aux, ptcp, D2, Obj)),
                'sentence_bad' : string_beautify('%s %s %s %s %s.' % (D1, Subj, V_bad, D2, Obj))
            }
        out.write(str(data)+'\n')

try:
        iter = int(sys.argv[1])
        out = sys.argv[2]
        out = open(out,'w')
        sample(iter,out)
except IndexError:
        print('To run this file use:\npython causative.py <# of sentences> <output path>')
        sys.exit()
