from Spanish_Utils.string_utils import *
from Spanish_Utils.randomize import choice
from Spanish_Utils.vocab_sets import *
import numpy as np
import sys

good_quantifiers_pl_masc = np.union1d(d_masc_pl,['pocos','muchos'])
good_quantifiers_pl_fem = np.union1d(d_fem_pl,['pocas','muchas']) 
bad_quantifiers_gen = ['muy','bastante']#, 'no','cada']

def sample(iter, out):
    for i in range(iter):
        #plural noun
        if choice([True,False]):
            if choice([True,False]):
                q_good = choice(good_quantifiers_pl_fem, ['las'])
                q_bad = choice(np.union1d(bad_quantifiers_gen, ['todas']))
                N = choice(all_animate_pl_nouns_fem)
            else:
                q_good = choice(good_quantifiers_pl_masc, ['los'])
                q_bad = choice(np.union1d(bad_quantifiers_gen, ['todos']))
                N = choice(all_animate_pl_nouns_masc)
        #Singular noun
        else:
            if choice([True,False]):
                q_good = choice(d_fem_sg,['la'])
                q_bad = choice(np.union1d(bad_quantifiers_gen, ['toda']))
                N = choice(all_animate_sg_nouns_fem, all_proper_nouns)
            else:
                q_good = choice(d_masc_sg,['el'])
                q_bad = choice(np.union1d(bad_quantifiers_gen, ['todo']))
                N = choice(all_animate_sg_nouns_masc, all_proper_nouns)
        V = verb_cleanup(choice(all_transitive_gerunds), remove_se_inf = True)
        #Same as above for object
        if choice([True,False]):
            #plural
            if choice([True,False]):
                D = choice(d_fem_pl)
                Obj = choice(n_fem_pl, all_proper_nouns)
            else:
                D = choice(d_masc_pl)
                Obj = choice(n_masc_pl, all_proper_nouns)
        #Singular noun
        else:
            if choice([True,False]):
                D = choice(d_fem_sg)
                Obj = choice(n_fem_sg, all_proper_nouns)
            else:
                D = choice(d_masc_sg)
                Obj = choice(n_masc_sg, all_proper_nouns)
        
        data = {
            'sentence_good' : string_beautify('%s %s %s %s %s %s.' % ('Hay',q_good,N,V,D,Obj)),
            'sentence_bad' :  string_beautify('%s %s %s %s %s %s.' % ('Hay',q_bad,N,V,D,Obj))
        }
        out.write(str(data) + '\n')

try:
    iter = int(sys.argv[1])
    out = open(sys.argv[2], 'w')
    sample(iter,out)
except IndexError:
    print('To run this file:\npython existential_there_quantifers_1.py <# sentences> <output path>')
    sys.exit()
