import numpy as np
import pandas as pd
from Spanish_Utils.vocab_sets import *
from Spanish_Utils.randomize import *
from Spanish_Utils.string_utils import * 
import random

'''

class DetNGenerator(data_generator.BenchmarkGenerator):
    def __init__(self):
        super().__init__(field="morphology",
                         linguistics="determiner_noun_agreement",
                         uid="determiner_noun_agreement_1",
                         simple_lm_method=True,
                         one_prefix_method=True,
                         two_prefix_method=False,
                         lexically_identical=True)
        self.all_null_plural_nouns = get_all("sgequalspl", "1")
        self.all_missingPluralSing_nouns = get_all_conjunctive([("pluralform", ""), ("singularform", "")])
        self.all_irregular_nouns = get_all("irrpl", "1")
        self.all_unusable_nouns = np.union1d(self.all_null_plural_nouns, np.union1d(self.all_missingPluralSing_nouns, self.all_irregular_nouns))
        self.all_pluralizable_nouns = np.setdiff1d(all_common_nouns, self.all_unusable_nouns)

'''

def sample(max_iter):
        # John cleaned this table.
        # N1   V1      Dem  N2_match

        # John cleaned this tables.
        # N1   V1      Dem  N2_mismatch
    for i in range(max_iter):
        #plural verb
        V = verb_cleanup(choice(all_trans_p3is))
        N1 = choice(all_proper_nouns)
        #fem sg
        n_choice = choice(['nfsg','nfpl','nmsg','nmpl'])
        if n_choice == 'nfsg':
            demonst = choice(all_demonstratives_fem_sg)
            N2_good = choice(n_fem_sg, all_proper_nouns)
            N2_bad = choice(all_plural_nouns, all_proper_nouns)
        elif n_choice == 'nfpl':
            demonst = choice(all_demonstratives_fem_pl)
            N2_good = choice(n_fem_pl, all_proper_nouns)
            N2_bad = choice(all_singular_nouns, all_proper_nouns)
        elif n_choice == 'nmsg':
            demonst = choice(all_demonstratives_masc_sg)
            N2_good = choice(n_masc_sg, all_proper_nouns)
            N2_bad = choice(all_plural_nouns, all_proper_nouns)
        elif n_choice == 'nmpl':
            demonst = choice(all_demonstratives_masc_pl)
            N2_good = choice(n_masc_pl, all_proper_nouns)
            N2_bad = choice(all_singular_nouns, all_proper_nouns)
        data = {
            "sentence_good" : string_beautify("%s %s %s %s." % (N1, V, demonst, N2_good)),
            "sentence_bad" : string_beautify("%s %s %s %s." % (N1, V, demonst, N2_bad))
        } 
        print(data)

sample(100)
        
