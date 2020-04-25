from Spanish_Utils.vocab_sets import *
from Spanish_Utils.randomize import *
from Spanish_Utils.string_utils import *
import pandas as pd
import numpy as np
import random

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
                N1_good = choice(all_animate_pl_nouns_fem)
                N1_bad = choice(all_inanimate_pl_nouns_fem)
            #plural masculine
            else:
                D1 = choice(d_masc_pl)
                N1_good = choice(all_animate_pl_nouns_masc)
                N1_bad = choice(all_inanimate_pl_nouns_masc)
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
                N1_good = choice(all_animate_sg_nouns_fem)
                N1_bad = choice(all_inanimate_sg_nouns_fem)
            #singular masculine
            else:
                D1 = choice(d_masc_sg)
                N1_good = choice(all_animate_sg_nouns_masc)
                N1_bad = choice(all_inanimate_sg_nouns_masc)
               
            
            
        if choice([True, False]):
            #sing fem
            if choice([True, False]):
                D2 = choice(d_fem_sg)
                N2 = choice(all_animate_sg_nouns_fem)
             #pl fem
            else: 
                D2 = choice(d_fem_pl)
                N2 = choice(all_animate_pl_nouns_fem)
        else:
            #sing masc
             if choice([True, False]):
                D2 = choice(d_masc_sg)
                N2 = choice(all_animate_sg_nouns_masc)
             #pl fem
             else: 
                D2 = choice(d_masc_pl)
                N2 = choice(all_animate_pl_nouns_masc)
                
      

    
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

