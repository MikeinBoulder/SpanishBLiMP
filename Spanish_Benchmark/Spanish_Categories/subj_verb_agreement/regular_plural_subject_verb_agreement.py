from Spanish_Utils.vocab_sets import *
import numpy as np
from Spanish_Utils.randomize import choice
from Spanish_Utils.string_utils import *
import random
import sys
"""

all_animate_sg_nouns_f = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['sg'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==1) & (vocab['gender'] == 'f')]
all_animate_sg_nouns_m = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['sg'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==1) & (vocab['gender'] == 'm')]

all_intrans_p3ip_anim_subj_allowing_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'PL') & (vocab[category] == 'S\\NP') & (vocab['arg_1'].str.contains('animate=1')==True)]
all_intrans_p3is_anim_subj_allowing_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'SG') & (vocab[category] == 'S\\NP') & (vocab['arg_1'].str.contains('animate=1')==True)]


"""

def sample(iter,out):
        for i in range(iter):
                #plural verb
                if choice([True, False]):
                        #fem pl noun
                        if choice([True,False]):
                                D = choice(d_fem_pl)
                                N = choice(all_animate_pl_nouns_f)
                                v_good = choice(all_intrans_p3ip_anim_subj_allowing_verbs)
                                v_bad = choice(all_intrans_p3is_anim_subj_allowing_verbs)
                        else:
                                D = choice(d_masc_pl)
                                N = choice(n_masc_pl)
                                v_good = choice(all_intrans_p3ip_anim_subj_allowing_verbs)
                                v_bad = choice(all_intrans_p3is_anim_subj_allowing_verbs
                 #singular verb
                 else:
                        #fem sg noun
                        if choice([True,False]):
                                D = choice(d_fem_sg)
                                N = choice(all_animate_sg_nouns_f)
                                v_good = choice(all_intrans_p3is_anim_subj_allowing_verbs)
                                v_bad = choice(all_intrans_p3ip_anim_subj_allowing_verbs)
                        else:
                                D = choice(d_masc_sg)
                                N = choice(n_masc_sg)
                                v_good = choice(all_intrans_p3is_anim_subj_allowing_verbs)
                                v_bad = choice(all_intrans_p3ip_anim_subj_allowing_verbs)

        # The cat is        eating     food
        #     N1  aux_agree V1_agree   N2
        # The cat are          eating        food
        #     N1  aux_nonagree V1_nonagree   N2


        data = {
            "sentence_good": "%s %s %s." % (N, D, v_good),
            "sentence_bad": "%s %s %s." % (N, D, v_bad),
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
