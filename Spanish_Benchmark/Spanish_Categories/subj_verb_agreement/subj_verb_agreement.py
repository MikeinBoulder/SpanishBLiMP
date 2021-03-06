from Spanish_Utils.vocab_sets import *
import numpy as np
from Spanish_Utils.randomize import choice
from Spanish_Utils.string_utils import *
import random
import sys
"""

all_animate_sg_nouns_f
all_animate_sg_nouns_m 
all_intrans_p3ip_anim_subj_allowing_verbs 
all_intrans_p3is_anim_subj_allowing_verbs

"""

def sample(iter,out):
        for i in range(iter):
                #plural noun
                if choice([True, False]):
                        #fem pl noun
                        if choice([True,False]):
                                D = choice(d_fem_pl)
                                N = choice(all_animate_pl_nouns_f)
                                v_good = verb_cleanup(choice(all_intrans_p3ip_anim_subj_allowing_verbs))
                                v_bad = verb_cleanup(choice(all_intrans_p3is_anim_subj_allowing_verbs))
                        else:
                                D = choice(d_masc_pl)
                                N = choice(n_masc_pl)
                                v_good = verb_cleanup(choice(all_intrans_p3ip_anim_subj_allowing_verbs))
                                v_bad = verb_cleanup(choice(all_intrans_p3is_anim_subj_allowing_verbs))
                else:
                        #fem sg noun
                        if choice([True,False]):
                                D = choice(d_fem_sg)
                                N = choice(all_animate_sg_nouns_f)
                                v_good = verb_cleanup(choice(all_intrans_p3is_anim_subj_allowing_verbs))
                                v_bad = verb_cleanup(choice(all_intrans_p3ip_anim_subj_allowing_verbs))
                        else:
                                D = choice(d_masc_sg)
                                N = choice(n_masc_sg)
                                v_good = verb_cleanup(choice(all_intrans_p3is_anim_subj_allowing_verbs))
                                v_bad = verb_cleanup(choice(all_intrans_p3ip_anim_subj_allowing_verbs))
                if choice([True,False]):
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
                        
                if N[0] >= 'A' and N[0] <= 'Z':
                        #Proper noun subject and object
                        if Obj[0] >= 'A' and Obj[0] <= 'Z':
                                data = {
                                        'sentence_good' : string_beautify('%s %s %s.' % (N,v_good,Obj)),
                                        'sentence_bad': string_beautify('%s %s %s.' % (N,v_bad,Obj))
                                }
                        else:
                                data = {
                                        'sentence_good' : string_beautify('%s %s %s %s.' % (N,v_good,D_Obj,Obj)),
                                        'sentence_bad': string_beautify('%s %s %s %s.' % (N, v_bad, D_Obj, Obj))
                                }
                else:
                        #non-proper subject proper object
                        if Obj[0] >= 'A' and Obj[0] <= 'Z':
                                data = {
                                        'sentence_good' : string_beautify('%s %s %s %s.' % (D,N,v_good,Obj)),
                                        'sentence_bad': string_beautify('%s %s %s %s.' % (D,N,v_bad,Obj))
                                }
                        else:
                                #non-proper subject and non-proper object
                                data = {
                                        'sentence_good' : string_beautify('%s %s %s %s %s.' % (D,N,v_good,D_Obj,Obj)),
                                        'sentence_bad': string_beautify('%s %s %s %s %s.' % (D,N,v_bad,D_Obj,Obj))
                                }
                out.write(str(data)+'\n')
try:
        iter = int(sys.argv[1])
        out = sys.argv[2]
        out = open(out,'w')
        sample(iter,out)
except IndexError:
        print('To run this file use:\npython anaphor_number_agreement.py <# of sentences> <output path>')
        sys.exit()
