import numpy as np
import pandas as pd
from Spanish_Utils.vocab_sets import *
from Spanish_Utils.randomize import *
from Spanish_Utils.string_utils import * 
import random
import sys

def sample(iter,out):
    for i in range(iter):
        V = choice(all_trans_p3is)
        N1 = choice(all_proper_nouns)
        #fem sg
        demonst_choice = choice(['nfsg','nfpl','nmsg','nmpl'])
        if demonst_choice == 'nfsg':
            demonst_good = choice(all_demonstratives_fem_sg)
            demonst_bad = choice(np.union1d())
            N2 = choice(n_fem_sg, all_proper_nouns)
            N2_bad = choice(all_plural_nouns, all_proper_nouns)
        elif demonst_choice == 'nfpl':
            demonst = choice(all_demonstratives_fem_pl)
            N2_good = choice(n_fem_pl, all_proper_nouns)
            N2_bad = choice(all_singular_nouns, all_proper_nouns)
        elif demonst_choice == 'nmsg':
            demonst = choice(all_demonstratives_masc_sg)
            N2_good = choice(n_masc_sg, all_proper_nouns)
            N2_bad = choice(all_plural_nouns, all_proper_nouns)
        elif demonst_choice == 'nmpl':
            demonst = choice(all_demonstratives_masc_pl)
            N2_good = choice(n_masc_pl, all_proper_nouns)
            N2_bad = choice(all_singular_nouns, all_proper_nouns)
        data = {
            "sentence_good" : string_beautify("%s %s %s %s." % (N1, V, demonst, N2_good)),
            "sentence_bad" : string_beautify("%s %s %s %s." % (N1, V, demonst, N2_bad))
        }
        out.write(str(data)+'\n')

try:
    iter = int(sys.argv[1])
    out = open(sys.argv[2],'w')
    sample(iter,out)
except IndexError:
    print('To run this file use:\npython determiner_noun_agreement_1.py <# of sentences> <output path>')
    sys.exit()
class DetNGenerator(data_generator.BenchmarkGenerator):
    def __init__(self):
        super().__init__(field="morphology",
                         linguistics="determiner_noun_agreement",
                         uid="determiner_noun_agreement_2",
                         simple_lm_method=True,
                         one_prefix_method=False,
                         two_prefix_method=True,
                         lexically_identical=True)
        self.all_null_plural_nouns = get_all("sgequalspl", "1")
        self.all_missingPluralSing_nouns = get_all_conjunctive([("pluralform", ""), ("singularform", "")])
        self.all_irregular_nouns = get_all("irrpl", "1")
        self.all_unusable_nouns = np.union1d(self.all_null_plural_nouns, np.union1d(self.all_missingPluralSing_nouns, self.all_irregular_nouns))
        self.all_pluralizable_nouns = np.setdiff1d(all_common_nouns, self.all_unusable_nouns)

    def sample(self):
        # John cleaned this       table.
        # N1   V1      Dem_match  N2
        # John cleaned these        table.
        # N1   V1      Dem_mismatch N2

        V1 = choice(all_transitive_verbs)
        N1 = N_to_DP_mutate(choice(get_matches_of(V1, "arg_1", all_nouns)))
        N2 = choice(get_matches_of(V1, "arg_2", self.all_pluralizable_nouns))
        Dem_match = choice(get_matched_by(N2, "arg_1", all_demonstratives))
        if Dem_match[0] == "this":
            Dem_mismatch = "these"
        elif Dem_match[0] == "these":
            Dem_mismatch = "this"
        elif Dem_match[0] == "that":
            Dem_mismatch = "those"
        elif Dem_match[0] == "those":
            Dem_mismatch = "that"
        V1 = conjugate(V1, N1)

        data = {
            "sentence_good": "%s %s %s %s." % (N1[0], V1[0], Dem_match[0], N2[0]),
            "sentence_bad": "%s %s %s %s." % (N1[0], V1[0], Dem_mismatch, N2[0]),
            "two_prefix_prefix_good": "%s %s %s" % (N1[0], V1[0], Dem_match[0]),
            "two_prefix_prefix_bad": "%s %s %s" % (N1[0], V1[0], Dem_mismatch),
            "two_prefix_word": N2[0]
        }
        return data, data["sentence_good"]

generator = DetNGenerator()
generator.generate_paradigm(rel_output_path="outputs/benchmark/%s.jsonl" % generator.uid)
