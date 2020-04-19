from Spanish_Utils.string_utils import *
from Spanish_Utils.randomize import choice
from Spanish_Utils.vocab_sets import *
import numpy as np


        #Juan se imagina a si mismo viendo Maria
        #Juan se imagina a si mismo vio Maria
        
special_verbs_sg = ['se imagina','se está imaginando','se está olvidando de']
special_verbs_pl = ['se imaginan','se están imaginando','se están olvidando de']


def sample(max_iter):
    for i in range(max_iter):
        #plural subject
        if choice([True,False]):
            V2_good = choice(all_transitive_gerunds)
            V2_bad = verb_cleanup(get_corresponding_pastpret(V2_good, 'PL'))
            V = choice(special_verbs_pl)
            if choice([True,False]):
                #feminine
                D = choice(d_fem_pl)
                Subj = choice(n_fem_pl)
                refl = pl_reflexives[1]
                V = de_a_cleanup(V,refl)
            else:
                #masc
                D = choice(d_masc_pl)
                Subj = choice(n_masc_pl)
                refl = pl_reflexives[0]
                V = de_a_cleanup(V,refl)
        #singular subject
        else:
            V = choice(special_verbs_sg)
            V2_good = choice(all_transitive_gerunds)
            V2_bad = verb_cleanup(get_corresponding_pastpret(V2_good, 'SG'))
            if choice([True,False]):
                #feminine
                D = choice(d_fem_sg)
                Subj = choice(np.union1d(all_proper_nouns,n_fem_sg))
                refl = sg_reflexives[1]
                V = de_a_cleanup(V,refl)
            else:
                #masculine
                D = choice(d_masc_sg)
                Subj = choice(np.union1d(all_proper_nouns,n_masc_sg))
                refl = sg_reflexives[0]
                V = de_a_cleanup(V,refl)
                
        if choice([True,False]):
            #plural onject
            if choice([True,False]):
                D_Obj = choice(d_fem_pl)
                Obj = choice(n_fem_pl)
            else:
                D_Obj = choice(d_masc_pl)
                Obj = choice(n_masc_pl)
        else:
            if choice([True,False]):
                D_Obj = choice(d_fem_sg)
                Obj = choice(n_fem_sg)
            else:
                D_Obj = choice(d_masc_sg)
                Obj = choice(n_masc_sg)
        

        if Subj[0] >= 'A' and Subj[0] <= 'Z':
            #Proper noun subject and object
            if Obj[0] >= 'A' and Obj[0] <= 'Z':
                data = {
                    'sentence_good' : string_beautify('%s %s %s %s.' % (Subj,V,V2_good,Obj)),
                    'sentence_bad': string_beautify('%s %s %s %s.' % (Subj,V,V2_bad,Obj))
                }
            else:
                data = {
                    'sentence_good' : string_beautify('%s %s %s %s %s.' % (Subj,V,V2_good,D_Obj,Obj)),
                    'sentence_bad': string_beautify('%s %s %s %s %s.' % (Subj, V, V2_bad, D_Obj, Obj))
                }
        else:
            #non-proper subject proper object
            if Obj[0] >= 'A' and Obj[0] <= 'Z':
                data = {
                    'sentence_good' : string_beautify('%s %s %s %s %s.' % (D,Subj,V,V2_good,Obj)),
                    'sentence_bad': string_beautify('%s %s %s %s %s.' % (D,Subj,V,V2_bad,Obj))
                }
            else:
                #non-proper subject and non-proper object
                data = {
                    'sentence_good' : string_beautify('%s %s %s %s %s %s.' % (D, Subj,V,V2_good,D_Obj,Obj)),
                    'sentence_bad': string_beautify('%s %s %s %s %s %s.' % (D, Subj, V, V2_bad, D_Obj, Obj))
                }
        print(data)
sample(10)
