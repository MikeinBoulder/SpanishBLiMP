from Spanish_Utils.randomize import choice
from Spanish_Utils.vocab_sets import *
from Spanish_Utils.string_utils import *
import numpy as np
import random
import sys
#all_singular_count_nouns
#all_trans_p3is
#all_p3is_anim_subj_allowing_verbs
#all_singular_count_nouns_fem
#all_animate_sg_nouns_fem
quantifiers = [("mas que", "al menos"),("menos que", "como mucho")]
numbers = ['dos','tres','quatro','cinco','seis','siete','ocho','nueve']
ningun_masc = 'ningún'
ningun_fem = 'ningúna'
safe_nouns = np.setdiff1d(all_plural_nouns, all_proper_nouns)

def sample(iter, out):
        # No professor graded more than three papers
        # NO N1        V      Q1        Num   N2
        # No professor graded at least four papers
        # NO N1        V      Q2       Num  N2
    for i in range(iter):
        V = verb_cleanup(choice(all_p3is_anim_subj_allowing_verbs))
        if choice([True,False]):
            ningun = ningun_fem
            N1 = choice(all_animate_sg_nouns_fem, all_proper_nouns)
        else:
            ningun = ningun_masc
            N1 = choice(all_animate_sg_nouns_masc, all_proper_nouns)
        N2 = choice(all_plural_count_nouns)
        quants = random.choice(quantifiers)
        Q1 = quants[0]
        Q2 = quants[1]
        Num = choice(numbers)
        data = {
            "sentence_good": string_beautify("%s %s %s %s %s %s." % (ningun, N1, V, Q1, Num, N2)),
            "sentence_bad": string_beautify("%s %s %s %s %s %s." % (ningun, N1, V, Q2, Num, N2)),
        }
        out.write(str(data) + '\n')
try:
    iter = int(sys.argv[1])
    out = open(sys.argv[2], 'w')
    sample(iter, out)
except IndexError:
    print('To run this file:\npython superlative_quantifiers.py <# sentences> <output path>')
