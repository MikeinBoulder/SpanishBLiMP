from Spanish_Utils.vocab_sets import *
import numpy as np
from Spanish_Utils.randomize import choice
from Spanish_Utils.string_utils import *
from Spanish_Utils.vocab_table import *
import random
import pandas as pd


   # The bear has attacked.
        # Subj     Aux V_non_strict
        # The bear has injured.
        # Subj     Aux V_strict
"""
all_strict_transitive_verbs = vocab['expression'].loc[(vocab['category_2'] == "TV")& (vocab['category'] == "(S\\NP)/NP") & (vocab['strict_trans'] =="1")].dropna
all_nonstrict_transitive_verbs = vocab['expression'].loc[(vocab['category_2'] == "TV")& (vocab['category'] == "(S\\NP)/NP") & (vocab['strict_trans'] !="1")].dropna      
 """


import pandas as pd
data = pd.read_csv('./Spanish_Utils/new_combined.csv')

df_V = data[data['pos'] == 'V']
df_non_strict_V = data[(data['category_2'] == "TV")& (data['category'] == "(S\\NP)/NP") & (data['strict_trans'] !="1")]


df_V_arg1 = df_non_strict_V[['arg_1']]


nouns = data['expression'].loc[(data['noun'] == 1) & (data['arg_1'].isin(list(df_V_arg1.arg_1.unique())))].dropna



def sample(max_iter):
        for i in range(max_iter):
            V_non_strict = choice(all_nonstrict_transitive_verbs)
            Subj = choice(nouns)
            #Aux = return_aux(V_non_strict, Subj)
            Aux = "ha"
            V_strict = choice(all_strict_transitive_verbs)

        data = {
            "sentence_good": "%s %s %s." % (Subj, Aux, V_non_strict),
            "sentence_bad": "%s %s %s." % (Subj, Aux, V_strict)
        }
 

        print(data)
sample(10)
