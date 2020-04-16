from Spanish_Utils.vocab_sets import *
from Spanish_Utils.randomize import *
from Spanish_Utils.string_utils import *
import pandas as pd
import numpy as np
import random


"""
all_animate_sg_nouns_f = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['sg'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==1) & (vocab['gender'] == 'f')]
all_animate_sg_nouns_m = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['sg'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==1) & (vocab['gender'] == 'm')]

all_inanimate_sg_nouns_f = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['sg'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==0)& (vocab['gender'] == 'f')]
all_inanimate_pl_nouns_m = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['pl'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==0)& (vocab['gender'] == 'm')]

all_p3ip_anim_subj_allowing_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'PL') & (vocab['category_2'] == 'TV') & (vocab['arg_1'].str.contains('animate=1')==True)]
all_p3is_anim_subj_allowing_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'SG') & (vocab['category_2'] == 'TV') & (vocab['arg_1'].str.contains('animate=1')==True)]

all_p3ip_inanim_subj_allowing_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'PL') & (vocab['category_2'] == 'TV') & (vocab['arg_2'].str.contains('inanimate=1')==True)]
all_p3is_inanim_subj_allowing_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'SG') & (vocab['category_2'] == 'TV') & (vocab['arg_2'].str.contains('inanimate=1')==True)]


all_p3is_anim_anim_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'SG') & (vocab['category_2'] == 'TV')(vocab['arg_1'].str.contains('animate=1')==True) & (vocab['arg_2'].str.contains('animate=1')==True)]
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
            V = choice(all_p3is_anim_anim_verbs)
            #plural feminine
            if choice([True,False]):
                D = choice(d_fem_pl)
                N1_good = choice(all_animate_pl_nouns_f)
                N1_bad = choice(all_inanimate_pl_nouns_f)
            #plural masculine
            else:
                D = choice(d_masc_pl)
                N1_good = choice(all_animate_pl_nouns_m)
                N1_bad = choice(all_inanimate_pl_nouns_m)
        #sing verb
        else: 
            V = choice(all_p3is_anim_anim_verbs)
            #singular feminine
            if choice([True,False]):
                D = choice(d_fem_sg)
                N1_good = choice(all_animate_sg_nouns_f)
                N1_bad = choice(all_inanimate_sg_nouns_f)
            #singular masculine
            else:
                D = choice(d_masc_sg)
                N1_good = choice(all_animate_sg_nouns_m)
                N1_bad = choice(all_inanimate_sg_nouns_m)
               
            
            
        if choice([True, False]):
            #sing fem
            if choice([True, False]):
                D = choice(d_fem_sg)
                N2 = choice(all_animate_sg_nouns_f)
             #pl fem
            else: 
                D = choice(d_fem_pl)
                N2 = choice(all_animate_pl_nouns_f)
        else:
            #sing masc
             if choice([True, False]):
                D = choice(d_masc_sg)
                N2 = choice(all_animate_sg_nouns_m)
             #pl fem
             else: 
                D = choice(d_masc_pl)
                N2 = choice(all_animate_pl_nouns_m)
                
      

    
        if N2[0] >= 'A' and N2[0] <= 'Z':
                data = {
                        "sentence_good": string_beautify("%s %s %s." % (N1_good, V, N2)),
                                "sentence_bad": string_beautify("%s %s %s." % (N1_bad, V, N2))
                }
        else:
                        data = {
                                "sentence_good": string_beautify("%s %s %s %s." % (N1_good, V, D, N2)),
                                "sentence_bad": string_beautify("%s %s %s %s." % (N1_bad, V, D, N2))  
                       
                        }   
        print(data)
                            
        
sample(10)


