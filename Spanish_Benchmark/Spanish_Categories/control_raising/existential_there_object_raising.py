from Spanish_Utils.vocab_sets import *
import numpy as np
from Spanish_Utils.randomize import choice
from Spanish_Utils.string_utils import *
import random
import sys


class Generator(data_generator.BenchmarkGenerator):
    def __init__(self):
        super().__init__(field="syntax_semantics",
                         linguistics="control_raising",
                         uid="existential_there_object_raising",
                         simple_lm_method=True,
                         one_prefix_method=False,
                         two_prefix_method=True,
                         lexically_identical=False)
        good_quantifiers_sg_str = ["a", "an", ""]
        good_quantifiers_pl_str = ["no", "some", "few", "fewer than three", "more than three", "many", "a lot of", ""]
        self.good_quantifiers_sg = reduce(np.union1d, [get_all("expression", s, all_quantifiers) for s in good_quantifiers_sg_str])
        self.good_quantifiers_pl = reduce(np.union1d, [get_all("expression", s, all_quantifiers) for s in good_quantifiers_pl_str])
        bad_emb_subjs = reduce(np.union1d, (all_relational_poss_nouns, all_proper_names, get_all("category", "NP")))
        self.safe_emb_subjs = np.setdiff1d(all_nominals, bad_emb_subjs)
        self.raising_verbs = get_all("category_2", "V_raising_object")
        self.control_verbs = get_all("category_2", "V_control_object")
       
    """ 
past_3is_ipfv_raising_animate_verbs= vocab['expression'].loc[(vocab['category'] == 'V') & (vocab['category_2'] == 'V_raising_object') & (vocab['animate'] ==1) & (vocab['tense'] == 'PST') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'SG') & (vocab['aspect'] == 'IPFV')
past_3is_ipfv_control_animate_verbs= vocab['expression'].loc[(vocab['category'] == 'V') & (vocab['category_2'] == 'V_control_object') & (vocab['animate'] ==1) & (vocab['tense'] == 'PST') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'SG') & (vocab['aspect'] == 'IPFV')
   
all_animate_sg_nouns_f = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['sg'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==1) & (vocab['gender'] == 'f')]
all_animate_sg_nouns_m = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['sg'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==1) & (vocab['gender'] == 'm')] 
   
  
all_relational_poss_nouns = vocab['expression'].loc[(vocab['category'] == 'N\\NP[poss]') & (vocab['sg'] ==1)]
all_relational_poss_nouns = vocab['expression'].loc[(vocab['category'] == 'N\\NP[poss]') & (vocab['sg'] ==1)]
all_proper_nouns = vocab['expression'].loc[(vocab['properNoun'] == 1)]

n_fem_sg = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['gender'] == 'f') & (vocab['sg'] == 1)]
n_masc_sg = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['gender'] == 'm') & (vocab['sg'] == 1)]

bad_emb_subj == (all_relational_poss_nouns, all_proper_names)
safe_fem_emb_subjs = np.setdiff1d(n_fem_sg, bad_emb_subjs)
safe_masc_emb_subjs = np.setdiff1d(n_masc_sg, bad_emb_subjs)
   """     
        

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
                V_raise = past_3is_ipfv_raising_animate_verbs
                V_control = past_3is_ipfv_control_animate_verbs
                D = choice(d_fem_sg)
                emb_subj = choice(safe_fem_emb_subjs)
            else:
                N = choice(all_proper_nouns)
                V_raise = past_3is_ipfv_raising_animate_verbs
                V_control = past_3is_ipfv_control_animate_verbs
                D = choice(d_masc_sg)
                emb_subj = choice(safe_masc_emb_subjs)
     
      
        data = {
            "sentence_good": "%s %s que había pasando %s %s %s." % (N, V_raise, D, emb_subj),
            "sentence_bad": "%s %s que había pasando %s %s." % (N, V_control, D, emb_subj),
   
        }
        return data, data["sentence_good"]

print(data)