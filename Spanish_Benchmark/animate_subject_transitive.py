from Spanish_Utils.vocab_sets import *
from Spanish_Utils.randomize import *
from Spanish_Utils.string_utils import *
import pandas as pd
import numpy as np
import random


"""
all_animate_sg_nouns = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['sg'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==1)]
all_animate_pl_nouns = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['pl'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==1)]
all_inanimate_sg_nouns = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['sg'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==0)]
all_inanimate_pl_nouns = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['pl'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==0)]
all_p3ip_anim_subj_allowing_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'PL') & (vocab['category_2'] == 'TV') & (vocab['arg_1'].str.contains('animate=1')==True)]
all_p3is_anim_subj_allowing_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'SG') & (vocab['category_2'] == 'TV') & (vocab['arg_1'].str.contains('animate=1')==True)]
"""

dets= ['the', 'some']


def sample(max_iter):
    for i in range(max_iter):
        # def sample(self):
        # John      talked to the boy
        # N1_good   V1        N2
        # The table talked to the boy
        # N1_bad    V1        N2

        #plural verb
        if choice([True, False]):       
            V = choice(all_p3ip_anim_subj_allowing_verbs)
            N1_good = choice(all_animate_pl_nouns)
            N1_bad = choice(all_inanimate_pl_nouns)
        else: 
            V = choice(all_p3is_anim_subj_allowing_verbs)
            N1_good = choice(all_animate_sg_nouns)
            N1_bad = choice(all_inanimate_sg_nouns)
            
        N2 = choice(all_animate_sg_nouns)
      

        data = {
           "sentence_good": string_beautify("%s %s %s." % (N1_good, V, N2)),           "sentence_bad": string_beautify("%s %s %s." % (N1_bad, V, N2)),
            }
        print(data)
        
sample(10)


