from Spanish_Utils.randomize import choice
from Spanish_Utils.vocab_sets import *
from Spanish_Utils.string_utils import *
import numpy as np
import random
import sys

       # Subj1         V    D1  Obj   Adj    y Subj2 V   D2
        # Juan          tuvo dos tazas verdes y Jane tuvo tres
        # John  has(?)  had two green cups and Jane  has had three.
        # Subj1 Aux1 V   D1  Adj   Obj  AND Subj2 Aux2 V   D2

        #Subj1          V    D1  Obj   y Subj2 V   D2  Adj
        # Juan          tuvo dos tazas y Jane tuvo tres verdes.
        # John  has(?)  had two cups and Jane  has  had three green.
        # Subj1 Aux1 V   D1  Obj  AND Subj2 Aux2 V   D2    Adj
plural_dets_fem = [("dos", "tres"),
               ("tres", "dos"),
               ("quatro", "cinco"),
               ("cinco", "quatro"),
               ("varias", "unas cuantas"),
               ("unas cuantas", "varios"),
               ("muchos", "pocas"),
               ("pocas", "muchas"),
               ("muchas", "unas"),
               ("tres", "más"),
               ("tres", "menos"),
               ("tres", "al menos tantas"),
               ("tres", "casi la misma cantidad de")]
plural_dets_masc = [("dos", "tres"),
               ("tres", "dos"),
               ("quatro", "cinco"),
               ("cinco", "quatro"),
               ("varios", "unos pocos"),
               ("unos pocos", "varios"),
               ("muchos", "pocos"),
               ("pocos", "muchos"),
               ("muchos", "unos"),
               ("tres", "más"),
               ("tres", "menos"),
               ("tres", "al menos tantos"),
               ("tres", "casi la misma cantidad de")]
singular_dets_masc = [("uno", "tres"),
                      ("uno", "dos"),
                      ("uno", "cinco"),
                      ("uno", "quatro"),
                      ("uno", "varios"),
                      ("uno", "many"),
                      ("uno", "muchos"),
                      ("uno", "unos"),
                      ("uno", "más"),
                      ("uno", "casi la misma cantidad")]
singular_dets_fem = [("una", "tres"),
                     ("una", "dos"),
                     ("una", "cinco"),
                     ("una", "quatro"),
                     ("una", "varias"),
                     ("una", "pocas"),
                     ("una", "muchas"),
                     ("una", "unas"),
                     ("una", "más"),
                     ("una", "casi la misma cantidad")]
safe_objs = np.setdiff1d(all_nominals, all_proper_nouns)

def sample(iter, out):
    for i in range(iter):
        V = choice(past_pret_3s)
        Subj1 = choice(all_proper_nouns)
        Subj2 = choice(all_proper_nouns, Subj1)
        if choice([True,False]):
            #Plural Obj
            if choice([True,False]):
                Obj = choice(all_inanimate_pl_nouns_fem)
                Adj = choice(np.union1d(all_adj_pl_fem,all_adj_pl_neuter))
                D1, D2 = random.choice(plural_dets_fem)
            else:
                Obj = choice(all_inanimate_pl_nouns_masc)
                Adj = choice(np.union1d(all_adj_pl_masc, all_adj_pl_neuter))
                D1, D2 = random.choice(plural_dets_masc)
        else:
            #Singular Obj
            if choice([True,False]):
                Obj = choice(all_inanimate_sg_nouns_fem)
                Adj = choice(np.union1d(all_adj_sg_fem, all_adj_sg_neuter))
                D1, D2 = random.choice(singular_dets_fem)
            else:
                Obj = choice(all_inanimate_sg_nouns_masc)
                Adj = choice(np.union1d(all_adj_sg_masc,all_adj_sg_neuter))
                D1, D2 = random.choice(singular_dets_masc)

        data = {
            "sentence_good": "%s %s %s %s %s %s %s %s %s." % (Subj1, V, D1, Obj, Adj, 'y', Subj2, V, D2),
            "sentence_bad": "%s %s %s %s %s %s %s %s %s." % (Subj1, V, D1, Obj, 'y', Subj2, V, D2, Adj),
        }
        out.write(str(data) + '\n')
try:
    iter = int(sys.argv[1])
    out = open(sys.argv[2], 'w')
    sample(iter, out)
except IndexError:
    print("To run this file:\npython ellipsis_n_bar_1.py <# sentences> <output path>")
    sys.exit()

 
