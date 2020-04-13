from Spanish_Utils.vocab_sets import *
import pandas as pd
import numpy as np
from Spanish_Utils.randomize import *
import random

'''
vocab = pd.read_csv("./Spanish_Utils/new_combined.csv")
verbs_p3is = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'SG')]
verbs_p3ip = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'PL')]
n_fem_pl = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['gender'] == 'f') & (vocab['pl'] == 1)]
n_fem_sg = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['gender'] == 'f') & (vocab['sg'] == 1)]
n_masc_pl = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['gender'] == 'm') & (vocab['pl'] == 1)]
n_masc_sg = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['gender'] == 'm') & (vocab['sg'] == 1)]
d_masc_pl = ['los','unos']
d_masc_sg = ['el','un']
d_fem_pl = ['las','unas']
d_fem_sg = ['la','una']
all_reflexives = ["a sí mismo", "a sí misma","a sí mismos", "a sí mismas"]
sg_reflexives = ["a sí mismo", "a sí misma"]
pl_reflexives = ["a sí mismos", "a sí mismas"]

'''

def sample(max_iter):
        for i in range(max_iter):
                #plural verb
                if random.choice([True, False]):
                        V = np.random.choice(verbs_p3ip)
                        #fem pl noun
                        if np.random.choice([True,False]):
                                D = random.choice(d_fem_pl)
                                N = np.random.choice(n_fem_pl)
                                rp_good = pl_reflexives[1]
                                #all_reflexives.remove(rp_good)
                                rp_bad = sg_reflexives[1]
                                #all_reflexives.insert(3, rp_good)
                        else:
                                D = random.choice(d_masc_pl)
                                N = np.random.choice(n_masc_pl)
                                rp_good = pl_reflexives[0]
                                #all_reflexives.remove(rp_good)
                                rp_bad = sg_reflexives[0]
                                #all_reflexives.insert(2, rp_good)

                #singular verb
                else:
        
                        V = np.random.choice(verbs_p3is)
                        #fem sg noun
                        if np.random.choice([True,False]):
                                D = random.choice(d_fem_sg)
                                N = np.random.choice(n_fem_sg)
                                rp_good = sg_reflexives[1]
                                #all_reflexives.remove(rp_good)
                                rp_bad = pl_reflexives[1]
                                #all_reflexives.insert(1, rp_good)
                        else:
                                D = random.choice(d_masc_sg)
                                N = np.random.choice(n_masc_sg)
                                rp_good = sg_reflexives[0]
                                #all_reflexives.remove(rp_good)
                                rp_bad = pl_reflexives[0]
                                #all_reflexives.insert(0,rp_good)
                                                               
                #Verb fix
                if not V.startswith('se', 0, 2):
                        V = 'se ' + V
                                        
                                        
                                        
                if N[0] >= 'A' and N[0] <= 'Z':
                        data = {
                                "sentence_good": "%s %s %s." % (N, V, rp_good),
                                "sentence_bad": "%s %s %s." % (N, V, rp_bad)
                        }
                else:
                        data = {
                                "sentence_good": "%s %s %s %s." % (D, N, V, rp_good),
                                "sentence_bad": "%s %s %s %s." % (D, N, V, rp_bad)
                        }
                print(data)

sample(10)



