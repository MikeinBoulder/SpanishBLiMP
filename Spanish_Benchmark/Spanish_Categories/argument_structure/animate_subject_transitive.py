from Spanish_Utils.vocab_sets import *
from Spanish_Utils.randomize import *
from Spanish_Utils.string_utils import *
import pandas as pd
import numpy as np
import random



all_animate_sg_nouns_f = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['sg'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==1) & (vocab['gender'] == 'f')]
all_animate_sg_nouns_m = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['sg'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==1) & (vocab['gender'] == 'm')]

all_animate_pl_nouns_f = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['pl'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==1) & (vocab['gender'] == 'f')]
all_animate_pl_nouns_m = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['pl'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==1) & (vocab['gender'] == 'm')]

all_inanimate_sg_nouns_f = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['sg'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==0)& (vocab['gender'] == 'f')]
all_inanimate_pl_nouns_m = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['pl'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==0)& (vocab['gender'] == 'm')]

all_p3ip_anim_subj_allowing_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'PL') & (vocab['category_2'] == 'TV') & (vocab['arg_1'].str.contains('animate=1')==True)]
all_p3is_anim_subj_allowing_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'SG') & (vocab['category_2'] == 'TV') & (vocab['arg_1'].str.contains('animate=1')==True)]

all_p3ip_inanim_subj_allowing_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'PL') & (vocab['category_2'] == 'TV') & (vocab['arg_2'].str.contains('inanimate=1')==True)]
all_p3is_inanim_subj_allowing_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'SG') & (vocab['category_2'] == 'TV') & (vocab['arg_2'].str.contains('inanimate=1')==True)]


all_p3is_anim_anim_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'SG') & (vocab['category_2'] == 'TV') & (vocab['arg_1'].str.contains('animate=1')==True) & (vocab['arg_2'].str.contains('animate=1')==True)]


all_p3ip_anim_anim_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'PL') & (vocab['category_2'] == 'TV') & (vocab['arg_1'].str.contains('animate=1')==True) & (vocab['arg_2'].str.contains('animate=1')==True)]


all_p3ip_anim_anim_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'PL') & (vocab['category_2'] == 'TV') & (vocab['arg_1'].str.contains('animate=1')==True) & (vocab['arg_2'].str.contains('animate=1')==True)]


a_verbs=['abraza', 'abrazan', 'aburre','aburren','se acerca','se acercan', 'admira', 'admiran', 'agracece', 'agracecen', 'alarma', 'alarman','asombra','asombran', 'asusta', 'asustan', 'ataca', 'atacan', 'ayuda', 'ayudan', 'besa', 'besan', 'boicotea', 'boicotean', 'compra', 'compran', 'confunde', 'confunden', 'conmociona', 'conmocionan', 'conoce', 'conocen', 'corretea', 'corretean', 'cuestiona', 'cuestionan', 'cuida', 'cuidan', 'nota', 'notan', 'observa', 'observan', 'oculta', 'ocultan', 'odia', 'odia', 'ojea', 'ojean', 'pasa', 'pasan', 'se pasa', 'se pasan', 'se pinta', 'se pintan', 'se queja','se quejan', 'sale', 'salen', 'trae', 'traen', 'vende', 'venden', 'se vende', 'se venden', 'se ve', 'se ven', 'vuelve', 'vuelven']


def sample(max_iter):
    for i in range(max_iter):
        # def sample(self):
        # John      talked to the boy
        # N1_good   V1        N2
        # The table talked to the boy
        # N1_bad    V1        N2

        #plural verb
        if choice([True, False]):       
            Verb = choice(all_p3ip_anim_anim_verbs)
            if Verb in a_verbs:
                    V= Verb + ' a'
            else:
                V=Verb
            #plural feminine
            if choice([True,False]):
                D1 = choice(d_fem_pl)
                N1_good = choice(all_animate_pl_nouns_f)
                N1_bad = choice(all_inanimate_pl_nouns_f)
            #plural masculine
            else:
                D1 = choice(d_masc_pl)
                N1_good = choice(all_animate_pl_nouns_m)
                N1_bad = choice(all_inanimate_pl_nouns_m)
        #sing verb
        else: 
            Verb = choice(all_p3is_anim_anim_verbs)
            if Verb in a_verbs:
                    V= Verb + ' a'
            else:
                V=Verb
            #singular feminine
            if choice([True,False]):
                D1 = choice(d_fem_sg)
                N1_good = choice(all_animate_sg_nouns_f)
                N1_bad = choice(all_inanimate_sg_nouns_f)
            #singular masculine
            else:
                D1 = choice(d_masc_sg)
                N1_good = choice(all_animate_sg_nouns_m)
                N1_bad = choice(all_inanimate_sg_nouns_m)
               
            
            
        if choice([True, False]):
            #sing fem
            if choice([True, False]):
                D2 = choice(d_fem_sg)
                N2 = choice(all_animate_sg_nouns_f)
             #pl fem
            else: 
                D2 = choice(d_fem_pl)
                N2 = choice(all_animate_pl_nouns_f)
        else:
            #sing masc
             if choice([True, False]):
                D2 = choice(d_masc_sg)
                N2 = choice(all_animate_sg_nouns_m)
             #pl fem
             else: 
                D2 = choice(d_masc_pl)
                N2 = choice(all_animate_pl_nouns_m)
                
      

    
        #prop subj
        if N1_good[0] >= 'A' and N1_good[0] <= 'Z':
            #prop subj prop obj
            if N2[0] >= 'A' and N2[0] <= 'Z':
                data = {
                        "sentence_good": string_beautify("%s %s %s." % (N1_good, V, N2)),
                        "sentence_bad": string_beautify("%s %s %s." % (N1_bad, V, N2))
                }
            #prop subj inprop obj
            else:
                        data = {
                                "sentence_good": string_beautify("%s %s %s %s." % (N1_good, V, D2, N2)),
                                "sentence_bad": string_beautify("%s %s %s %s." % (N1_bad, V, D2, N2))  
                       
                        }  
                
            
       #inprop subj
        else:
            #inprop subj prop obj
            if N2[0] >= 'A' and N2[0] <= 'Z':
                data = {
                        "sentence_good": string_beautify("%s %s %s %s." % (D1, N1_good, V, N2)),
                                "sentence_bad": string_beautify("%s %s %s %s." % (D1, N1_bad, V, N2))
                }
            #inprop subj inprop obj
            else:
                 
                        data = {
                                "sentence_good": string_beautify("%s %s %s %s %s." % (D1, N1_good, V, D2, N2)),
                                "sentence_bad": string_beautify("%s %s %s %s %s." % (D1, N1_bad, V, D2, N2))
                            }
                            

        print(data)
                            
        
sample(100)

"""
  if Verb == 'abraza' or 'aburre' or 'se acerca' or 'admira' or 'agracece' or 'alarma' or 'asombra' or 'asusta' or 'ataca' or 'ayuda' or 'besa' or 'boicotea' or 'compra' or 'confunde' or 'conmociona' or 'conoce' or 'corretea' or 'cuestiona' or 'cuida' or 'nota' or 'observa' or 'oculta' or 'odia' or 'ojea' or 'pasa' or 'se pasa' or 'se pinta' or 'se queja' or 'sale' or 'trae' or 'vende' or 'se vende' or 'se ve' or 'vuelve'
  V == Verb+ ' a'
  
  a_verbs=['abraza', 'aburre','se acerca', 'admira', 'agracece', 'alarma', 'asombra', 'asusta', 'ataca', 'ayuda', 'besa', 'boicotea', 'compra', 'confunde', 'conmociona', 'conoce', 'corretea', 'cuestiona', 'cuida', 'nota', 'observa', 'oculta', 'odia', 'ojea', 'pasa', 'se pasa', 'se pinta', 'se queja', 'sale', 'trae', 'vende', 'se vende', 'se ve', 'vuelve'
  
  
"""