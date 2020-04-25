from Spanish_Utils.vocab_sets import *
import numpy as np
from Spanish_Utils.randomize import choice
from Spanish_Utils.string_utils import *
import random
import sys



    #def sample(self):
        # John   believed there to be a party    happening
        # m_subj V_raise  THERE TO BE D emb_subj VP
        # John   persuaded there to be a party    happening
        # m_subj V_control THERE TO BE D emb_subj VP

def sample(iter,out):
        for i in range(iter):
            #fem sg emb_subj
            if choice([True,False]):
                N = choice(all_proper_nouns)
                V_raise = choice(past_3is_ipfv_raising_verbs)
                V_control = choice(past_3is_ipfv_control_verbs)
                D = choice(d_fem_sg)
                emb_subj = choice(safe_fem_emb_subjs)
            else:
                N = choice(all_proper_nouns)
                V_raise = choice(past_3is_ipfv_raising_verbs)
                V_control = choice(past_3is_ipfv_control_verbs)
                D = choice(d_masc_sg)
                emb_subj = choice(safe_masc_emb_subjs)
     
      
            data = {
                "sentence_good": "%s %s que había %s %s." % (N, V_raise, D, emb_subj),
                "sentence_bad": "%s %s que había %s %s." % (N, V_control, D, emb_subj),
   
            }
            
            out.write(str(data)+'\n')
            
iter = int(sys.argv[1])
out = sys.argv[2]
print(iter,out)
out = open(out,'w')
sample(iter,out)
#except IndexError:
#        print('To run this file use:\npython anaphor_number_agreement.py <# of sentences> <output path>')
#        sys.exit()
