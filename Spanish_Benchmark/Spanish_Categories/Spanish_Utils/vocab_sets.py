#from randomize import *
#from functools import reduce
import numpy as np
import pandas as pd


vocab = pd.read_csv('./Spanish_Utils/vocab.csv')
#FUNCTIONS
def get_corresponding_pastpret(verb,number):
    inf = np.random.choice(vocab['infinitive'].loc[(vocab['expression'].str.contains(verb) == True)])
    to_ret = vocab['expression'].loc[(vocab['infinitive'].str.contains(inf) == True) & (vocab['pos'] == 'V') & (vocab['mood'] == 'IND') & (vocab['tense'] == 'PST') & (vocab['person'] == 3) & (vocab['number'] == number) & (vocab['aspect'] == 'PFV')]
    if len(to_ret) > 0:
        return np.random.choice(to_ret)
    else:
        return inf


#NOUNS
all_nouns = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['frequent'] ==1)]
all_singular_nouns = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['frequent'] ==1) & (vocab['sg'] == 1)]
all_singular_count_nouns = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['frequent'] ==1) & (vocab['sg'] == 1) & (vocab['mass'] == 0)]
all_plural_count_nouns = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['frequent'] ==1) & (vocab['pl'] == 1) & (vocab['mass'] == 0)]
all_singular_count_nouns = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['frequent'] ==1) & (vocab['pl'] == 1) & (vocab['mass'] == 0)]
all_singular_count_nouns_masc = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['frequent'] ==1) & (vocab['sg'] == 1) & (vocab['mass'] == 0) & (vocab['gender'] == 'm')]
all_singular_count_nouns_fem = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['frequent'] ==1) & (vocab['sg'] == 1) & (vocab['mass'] == 0) & (vocab['gender'] == 'f')]
all_animate_nouns = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['frequent'] ==1) & (vocab['animate'] ==1)]
all_animate_sg_nouns = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['sg'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==1)]
all_animate_sg_nouns_fem = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['sg'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==1) & (vocab['gender'] == 'f')]
all_animate_sg_nouns_masc = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['sg'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==1) & (vocab['gender'] == 'm')]
all_animate_pl_nouns = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['pl'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==1)]
all_animate_pl_nouns_fem = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['pl'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==1) & (vocab['gender'] == 'f')]
all_animate_pl_nouns_masc = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['pl'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==1) & (vocab['gender'] == 'm')]
all_inanimate_nouns = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['frequent'] ==1) & (vocab['animate'] ==0)]
all_inanimate_sg_nouns = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['sg'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==0)]
all_inanimate_pl_nouns = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['pl'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==0)]
all_inanimate_sg_nouns_fem = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['sg'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==0)& (vocab['gender'] == 'f')]
all_inanimate_sg_nouns_masc = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['sg'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==0)& (vocab['gender'] == 'm')]
all_inanimate_pl_nouns_fem = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['pl'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==0)& (vocab['gender'] == 'f')]
all_inanimate_pl_nouns_masc = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['pl'] ==1) & (vocab['frequent'] ==1) & (vocab['animate'] ==0)& (vocab['gender'] == 'm')]
all_documents = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['document'] ==1)]
all_gendered_nouns = vocab['expression'].loc[(vocab['gender'] == 'm') | (vocab['gender'] == 'f')]
all_singular_neuter_animate_nouns = all_documents = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['sg'] ==1) & (vocab['animate'] ==1) & (vocab['gender'] == 'n')]
all_plural_nouns = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['frequent'] ==1) & (vocab['pl'] == 1)] 
all_plural_animate_nouns = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['frequent'] ==1) & (vocab['animate'] ==1) & (vocab['category'] == 'N') & (vocab['frequent'] ==1) & (vocab['pl'] == 1)]
all_common_nouns = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['properNoun'] == 0)]
all_animate_common_nouns = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['properNoun'] == 0) & (vocab['animate'] ==1)]
all_singular_animate_common_nouns = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['properNoun'] == 0) & (vocab['animate'] ==1) & (vocab['sg'] ==1)]
all_relational_nouns = vocab['expression'].loc[(vocab['category'] == 'N/NP')]
all_nominals = vocab['expression'].loc[(vocab['noun'] == 1) & (vocab['frequent'] ==1)]
all_relational_poss_nouns = vocab['expression'].loc[(vocab['category'] == 'N\\NP[poss]') & (vocab['sg'] ==1)]
all_proper_nouns = vocab['expression'].loc[(vocab['properNoun'] == 1)]
all_animate_proper_nouns = vocab['expression'].loc[(vocab['category'] == 'N') & (vocab['properNoun'] == 1) & (vocab['animate'] ==1)]
all_null_plural_nouns = vocab['expression'].loc[(vocab['sgequalspl'] == 1)]
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
all_irrpl = vocab['expression'].loc[vocab['irrpl'] == 1]
proper_nouns_fem = vocab['expression'].loc[(vocab['properNoun'] == 1 ) & (vocab['gender'] == 'f')]
proper_nouns_masc = vocab['expression'].loc[(vocab['properNoun'] == 1 ) & (vocab['gender'] == 'm')]
all_relational_poss_nouns = vocab['expression'].loc[(vocab['category'] == 'N\\NP[poss]') & (vocab['sg'] ==1)]
all_relational_poss_nouns = vocab['expression'].loc[(vocab['category'] == 'N\\NP[poss]') & (vocab['sg'] ==1)]
all_proper_nouns = vocab['expression'].loc[(vocab['properNoun'] == 1)]
bad_emb_subj = np.union1d(all_relational_poss_nouns, all_proper_nouns)
safe_fem_emb_subjs = np.setdiff1d(n_fem_sg, bad_emb_subj)
safe_masc_emb_subjs = np.setdiff1d(n_masc_sg, bad_emb_subj)
#bad_emb_subj == (all_relational_poss_nouns, all_proper_names)
#safe_emb_subjs = np.setdiff1d(all_nominals, bad_emb_subjs)

#VERBS

all_verbs = vocab['expression'].loc[(vocab['pos'] == "V")]
all_p3is_anim_anim_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'SG') & (vocab['category_2'] == 'TV') & (vocab['arg_1'].str.contains('animate=1')==True) & (vocab['arg_2'].str.contains('animate=1')==True)]
all_action_verbs = vocab['expression'].loc[(vocab['pos'] == "V") & (vocab['bare']==1)]
#all_coverb = vocab['expression'].loc[(vocab['coverb'] == 1)]
all_verbs_bare = vocab['expression'].loc[(vocab['pos'] == 1) & (vocab['bare']==1)]
all_transitive_verbs = vocab['expression'].loc[(vocab['category_2'] == "TV")& (vocab['category'] == "(S\\NP)/NP")]#& ((vocab['past']==1)|(vocab['ing']==1))]
all_strict_transitive_verbs = vocab['expression'].loc[(vocab['category_2'] == "TV")& (vocab['category'] == "(S\\NP)/NP") & (vocab['strict_trans'] =="1")].dropna
all_nonstrict_transitive_verbs = vocab['expression'].loc[(vocab['category_2'] == "TV")& (vocab['category'] == "(S\\NP)/NP") & (vocab['strict_trans'] !="1")].dropna  
all_transitive_verbs_bare = vocab['expression'].loc[(vocab['category_2'] == "TV")&(vocab['category'] == "(S\\NP)/NP")& (vocab['bare']==1)]
#all_transitive_verbs_bare_VC = vocab['expression'].loc[(vocab['category_2'] == "TV")&(vocab['category'] == "(S\\NP)/NP")& (vocab['bare']==1)]
all_transitive_verbs_past = vocab['expression'].loc[(vocab['category_2'] == "TV")&(vocab['category'] == "(S\\NP)/NP")& (vocab['past']==1)]
# all_intransitive_verbs = get_all("category", "S\\NP")
all_intransitive_verbs = vocab['expression'].loc[(vocab['category_2'] == "IV")&(vocab['category'] == "S\\NP")]
all_intransitive_verbs_bare = vocab['expression'].loc[(vocab['category_2'] == "IV")&(vocab['category'] == "S\\NP")& (vocab['bare']==1)]
all_intransitive_verbs_past = vocab['expression'].loc[(vocab['category_2'] == "IV")&(vocab['category'] == "S\\NP")& (vocab['tense']=='PST')]
all_non_recursive_verbs = vocab['expression'].loc[(vocab['category'] == "(S\\NP)/NP") | (vocab['category'] == "S\\NP")]
all_finite_verbs = vocab['expression'].loc[(vocab['verb'] == 1) & (vocab['finite'] == 1)]
all_non_finite_verbs = vocab['expression'].loc[(vocab['pos'] == "V") & (vocab['mood'] == 'NFIN')]
# all_ing_verbs = get_all("ing", "1", all_verbs)
# all_en_verbs = get_all("en", "1", all_verbs)
#all_bare_verbs = get_all("bare", "1", all_verbs)
all_intrans_p3ip_anim_subj_allowing_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'PL') & (vocab['category'] == 'S\\NP') & (vocab['arg_1'].str.contains('animate=1')==True)]
all_intrans_p3is_anim_subj_allowing_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'SG') & (vocab['category'] == 'S\\NP') & (vocab['arg_1'].str.contains('animate=1')==True)]

all_p3ip_anim_subj_allowing_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'PL') & (vocab['category_2'] == 'TV') & (vocab['arg_1'].str.contains('animate=1')==True)]
all_p3is_anim_subj_allowing_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'SG') & (vocab['category_2'] == 'TV') & (vocab['arg_1'].str.contains('animate=1')==True)]
all_anim_anim_verbs = vocab['expression'].loc[(vocab['arg_1'].str.contains('animate=1')==True) & (vocab['arg_2'].str.contains('animate=1')==True)]# & ((vocab['past']==1)|(vocab['ing']==1))]
all_p3is_anim_anim_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'SG') & (vocab['category_2'] == 'TV') &(vocab['arg_1'].str.contains('animate=1')==True) & (vocab['arg_2'].str.contains('animate=1')==True)]
all_p3ip_anim_anim_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'PL') & (vocab['category_2'] == 'TV') & (vocab['arg_1'].str.contains('animate=1')==True) & (vocab['arg_2'].str.contains('animate=1')==True)]
all_p3ip_anim_subj_allowing_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'PL') & (vocab['category_2'] == 'TV') & (vocab['arg_1'].str.contains('animate=1')==True)]
all_p3is_anim_subj_allowing_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'SG') & (vocab['category_2'] == 'TV') & (vocab['arg_1'].str.contains('animate=1')==True)]
all_anim_anim_verbs_3is_pst = vocab['expression'].loc[(vocab['arg_1'].str.contains('animate=1')==True) & (vocab['arg_2'].str.contains('animate=1')==True) & (vocab['tense'] == 'PST') & (vocab['pos'] == 'V') & (vocab['person'] == 3) & (vocab['number'] =='SG') & (vocab['mood'] == 'IND') & (vocab['aspect'] == 'PFV')]
all_anim_anim_verbs_3ip_pst = vocab['expression'].loc[(vocab['arg_1'].str.contains('animate=1')==True) & (vocab['arg_2'].str.contains('animate=1')==True) & (vocab['tense'] == 'PST') & (vocab['pos'] == 'V') & (vocab['person'] == 3) & (vocab['number'] =='PL') & (vocab['mood'] == 'IND') & (vocab['aspect'] == 'PFV')]
all_doc_doc_verbs = vocab['expression'].loc[(vocab['arg_1'].str.contains('document=1')==True) & (vocab['arg_2'].str.contains('document=1')==True)]#& ((vocab['past']==1)|(vocab['ing']==1))]
all_refl_nonverbal_predicates = vocab[vocab['arg_1'] == vocab['arg_2']]
all_refl_preds = pd.concat([all_anim_anim_verbs,all_doc_doc_verbs]).drop_duplicates().reset_index(drop=True)
all_non_plural_transitive_verbs = vocab['expression'].loc[(vocab['pos']=='V') & (vocab['category_2'] == "TV")& (vocab['category'] == "(S\\NP)/NP") & (vocab['number'] == 'SG')]
all_strictly_plural_verbs = vocab['expression'].loc[(vocab['tense'] == "PRS") & (vocab['number'] == 'PL')]
all_strictly_singular_verbs = vocab['expression'].loc[(vocab['tense'] == "PRS") & (vocab['number'] == 'SG')]
all_strictly_plural_transitive_verbs = vocab['expression'].loc[(vocab['tense'] == "PRS") & (vocab['number'] == 'PL') & (vocab['category_2'] == 'TV')]
all_strictly_singular_transitive_verbs = vocab['expression'].loc[(vocab['tense'] == "PRS") & (vocab['number'] == 'SG') & (vocab['category_2'] == "TV") & (vocab['category'] == "(S\\NP)/NP")]
all_possibly_plural_verbs = vocab['expression'].loc[(vocab['pos'] == "V") & (vocab['tense'] == "PRS") & (vocab['number'] != 'SG')]
all_possibly_singular_verbs = vocab['expression'].loc[(vocab['pos'] == "V") & (vocab['tense'] == "PRS") & (vocab['number'] != 'PL')]
all_non_finite_transitive_verbs = vocab['expression'].loc[(vocab['pos'] == "V") & (vocab['mood'] == 'NFIN') & (vocab['category_2'] == 'TV')]
all_non_finite_intransitive_verbs = vocab['expression'].loc[(vocab['category'] == "S\\NP") & (vocab['mood'] == 'NFIN')]
all_modals_auxs = vocab['expression'].loc[vocab['category'] == "(S\\NP)/(S[bare]\\NP)"]
all_modals = vocab['expression'].loc[vocab['category_2'] == "modal"]
all_negated_modals_auxs = vocab['expression'].loc[(vocab['category'] == "(S\\NP)/(S[bare]\\NP)") & (vocab['negated'] == "1")]
all_non_negated_modals_auxs = vocab['expression'].loc[(vocab['category'] == "(S\\NP)/(S[bare]\\NP)") & (vocab['negated'] == "0")]
all_negated_modals = vocab['expression'].loc[(vocab['negated'] == "1") & (vocab['category_2'] == 'modal')]
all_non_negated_modals = vocab['expression'].loc[(vocab['negated'] == "0") & (vocab['category_2'] == 'modal')]
all_auxs = vocab['expression'].loc[vocab['category_2'] == "aux"]
all_auxiliaries_no_null = vocab["expression"].loc[(vocab['expression'] == "") & (vocab['category_2'] == 'aux')]
all_negated_auxs = vocab['expression'].loc[(vocab['negated'] == "1") & (vocab['category_2'] == 'aux')]
all_non_negated_auxs = vocab['expression'].loc[(vocab['category_2'] == 'aux') & (vocab['negated']== "0")]
all_copulas = vocab['expression'].loc[vocab["category_2"] == "copula"]
all_finite_copulas = vocab['expression'].loc[(vocab["bare"]== "1") & (vocab['category_2'] == 'aux')]
verbs_p3is = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'SG')]
verbs_p3ip = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'PL')]
all_trans_p3ip =  vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'PL') & (vocab['category_2'] == 'TV') ]
all_trans_p3is = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['tense'] == 'PRS') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'SG') & (vocab['category_2'] == 'TV') ]
all_intransitive_verbs_p3is = vocab['expression'].loc[(vocab['pos'] == 'V') & ((vocab['category_2'] == "IV") | (vocab['category_2'] == 'IV_ag')) & (vocab['person'] == 3) & (vocab['tense'] == 'PRS') & (vocab['mood'] == 'IND') & (vocab['number'] == 'SG')]
all_inchoative_p3is = vocab['expression'].loc[(vocab['inchoative'] == 1) & (vocab['person'] == 3) & (vocab['tense'] == 'PRS') & (vocab['mood'] == 'IND') & (vocab['number'] == 'SG')]
all_causative_p3is = vocab['expression'].loc[(vocab['causative'] == 1) & (vocab['person'] == 3) & (vocab['tense'] == 'PRS') & (vocab['mood'] == 'IND') & (vocab['number'] == 'SG')]
alternating_verbs = np.union1d(all_inchoative_p3is, all_causative_p3is)
all_trans_ptcp_for_pres_perf = vocab['expression'].loc[(vocab['pos'] =='V.PTCP') & (vocab['gender'] == 'm') & (vocab['number'] == 'SG') & (vocab['category_2'] == 'TV') & (vocab['category'] == '(S\\NP)/NP')]
all_intrans_ptcp_for_pres_perf = vocab['expression'].loc[(vocab['pos'] =='V.PTCP') & (vocab['gender'] == 'm') & (vocab['number'] == 'SG') & (vocab['category'] == 'S\\NP') & ((vocab['category_2'] == 'IV') | (vocab['category_2'] =='IV_sg'))]
past_pret_3s = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['mood'] == 'IND') & (vocab['tense'] == 'PST') & (vocab['person'] == 3) & (vocab['number'] == 'SG') & (vocab['aspect'] == 'PFV')]
past_pret_3p = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['mood'] == 'IND') & (vocab['tense'] == 'PST') & (vocab['person'] == 3) & (vocab['number'] == 'PL') & (vocab['aspect'] == 'PFV')]
all_transitive_gerunds = vocab['expression'].loc[(vocab['pos'] == "V.CVB") & (vocab['category_2'] == 'TV')]
past_3is_ipfv_raising_verbs = vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['category_2'].str.contains('V_raising_object')==True) & (vocab['tense'] == 'PST') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'SG') & (vocab['aspect'] == 'IPFV')]
past_3is_ipfv_control_verbs= vocab['expression'].loc[(vocab['pos'] == 'V') & (vocab['category_2'].str.contains('V_control_object')==True)& (vocab['tense'] == 'PST') & (vocab['person'] == 3) & (vocab['mood'] == 'IND') & (vocab['number'] == 'SG') & (vocab['aspect'] == 'IPFV')]
all_p3is_anim_subj_allowing_verbs_ptcp = vocab['expression'].loc[(vocab['pos'] == 'V.PTCP') & (vocab['category_2'] == 'TV') & (vocab['arg_1'].str.contains('animate=1')==True)]


#NOT SURE ABOUT SOME OF THESE TAGS

# all_rogatives = get_all("category", "(S\\NP)/Q")
# all_agreeing_aux = np.setdiff1d(all_auxs, get_all("arg_1", "sg=1;sg=0"))
# all_non_negative_agreeing_aux = get_all("negated", "0", all_agreeing_aux)
# all_negative_agreeing_aux = get_all("negated", "1", all_agreeing_aux)
# all_auxiliaries_no_null = np.setdiff1d(all_auxs, get_all("expression", ""))
# all_non_negative_copulas = get_all("negated", "0", all_finite_copulas)
# all_negative_copulas = get_all("negated", "1", all_finite_copulas)


#OTHERS
que_quien = ['qué','quién']
# all_quantifiers = get_all("category", "(S/(S\\NP))/N")
all_quantifiers = vocab['expression'].loc[vocab['category'] == "(S/(S\\NP))/N"]
# all_frequent_quantifiers = get_all("frequent", "1", all_quantifiers)
all_frequent_quantifiers = vocab['expression'].loc[(vocab['category'] == "(S/(S\\NP))/N") & (vocab['frequent'] == 1)]
# all_common_dets = np.append(get_all("expression", "the"), np.append(get_all("expression", "a"), get_all("expression", "an")))
all_common_dets = vocab['expression'].loc[(vocab['expression'] == "the" )| (vocab['expression'] == 'a') | (vocab['expression'] == 'an')]
# all_relativizers = get_all("category_2", "rel")
all_relativizers = vocab['expression'].loc[vocab['category_2'] == "rel"]
# all_reflexives = get_all("category_2", "refl")
all_reflexives = vocab['expression'].loc[vocab['category_2'] == "refl"]
# all_ACCpronouns = get_all("category_2", "proACC")
all_ACCpronouns = vocab['expression'].loc[vocab['category_2'] == "proACC"]
# all_NOMpronouns = get_all("category_2", "proNOM")
all_ACCpronouns = vocab['expression'].loc[vocab['category_2'] == "proNOM"]
# all_embedding_verbs = get_all("category_2", "V_embedding")
all_embedding_verbs = vocab['expression'].loc[vocab['category_2'] == "V_embedding"]
# all_wh_words = get_all("category", "NP_wh")
all_wh_words =vocab['expression'].loc[vocab['category'] == "NP_wh"]

# all_demonstratives = np.append(get_all("expression", "this"), np.append(get_all_conjunctive([("category_2", "D"),("expression", "that")]),np.append(get_all("expression", "these"), get_all("expression", "those"))))
all_demonstratives = vocab['expression'].loc[(vocab['category_2'] == "D")]
all_demonstratives_masc_sg = vocab['expression'].loc[(vocab['category_2'] == "D") & (vocab['sg'] == 1) & (vocab['gender'] == 'm')]
all_demonstratives_masc_pl = vocab['expression'].loc[(vocab['category_2'] == "D") & (vocab['pl'] == 1) & (vocab['gender'] == 'm') ]
all_demonstratives_fem_sg = vocab['expression'].loc[(vocab['category_2'] == "D") & (vocab['sg'] == 1) & (vocab['gender'] == 'f')]
all_demonstratives_fem_pl = vocab['expression'].loc[(vocab['category_2'] == 'D') & (vocab['pl'] == 1) & (vocab['gender'] == 'f')]
# all_adjectives = np.append(get_all("category_2", "adjective"), get_all("category_2", "Adj"))
all_adjectives = vocab['expression'].loc[(vocab['category_2'] == 'adjective') | (vocab['category_2'] == 'Adj') | (vocab['category_2'] == 'Adj-neg') | (vocab['category_2'] == 'Adj_comp') | (vocab['category_2'] == 'Adj_comp_than') | (vocab['category_2'] == 'Adj_clausal') | (vocab['category_2'] == 'Adj_control_subj') | (vocab['category_2'] == 'Adj_raising_subj') | (vocab['category_2'] == 'Adj_tough')]
all_adj_pl_fem = vocab['expression'].loc[(vocab['category_2'] == 'adjective') | (vocab['category_2'] == 'Adj') | (vocab['category_2'] == 'Adj-neg') | (vocab['category_2'] == 'Adj_comp') | (vocab['category_2'] == 'Adj_comp_than') | (vocab['category_2'] == 'Adj_clausal') | (vocab['category_2'] == 'Adj_control_subj') | (vocab['category_2'] == 'Adj_raising_subj') | (vocab['category_2'] == 'Adj_tough') & (vocab['gender'] == 'f') & (vocab['pl'] == 1)]
all_adj_sg_fem = vocab['expression'].loc[(vocab['category_2'] == 'adjective') | (vocab['category_2'] == 'Adj') | (vocab['category_2'] == 'Adj-neg') | (vocab['category_2'] == 'Adj_comp') | (vocab['category_2'] == 'Adj_comp_than') | (vocab['category_2'] == 'Adj_clausal') | (vocab['category_2'] == 'Adj_control_subj') | (vocab['category_2'] == 'Adj_raising_subj') | (vocab['category_2'] == 'Adj_tough') & (vocab['gender'] == 'f') & (vocab['sg'] == 1)]
all_adj_sg_masc = vocab['expression'].loc[(vocab['category_2'] == 'adjective') | (vocab['category_2'] == 'Adj') | (vocab['category_2'] == 'Adj-neg') | (vocab['category_2'] == 'Adj_comp') | (vocab['category_2'] == 'Adj_comp_than') | (vocab['category_2'] == 'Adj_clausal') | (vocab['category_2'] == 'Adj_control_subj') | (vocab['category_2'] == 'Adj_raising_subj') | (vocab['category_2'] == 'Adj_tough') & (vocab['gender'] == 'm') & (vocab['sg'] == 1)]
all_adj_pl_masc = vocab['expression'].loc[(vocab['category_2'] == 'adjective') | (vocab['category_2'] == 'Adj') | (vocab['category_2'] == 'Adj-neg') | (vocab['category_2'] == 'Adj_comp') | (vocab['category_2'] == 'Adj_comp_than') | (vocab['category_2'] == 'Adj_clausal') | (vocab['category_2'] == 'Adj_control_subj') | (vocab['category_2'] == 'Adj_raising_subj') | (vocab['category_2'] == 'Adj_tough') & (vocab['gender'] == 'm') & (vocab['pl'] == 1)]
all_adj_sg_neuter = vocab['expression'].loc[(vocab['category_2'] == 'adjective') | (vocab['category_2'] == 'Adj') | (vocab['category_2'] == 'Adj-neg') | (vocab['category_2'] == 'Adj_comp') | (vocab['category_2'] == 'Adj_comp_than') | (vocab['category_2'] == 'Adj_clausal') | (vocab['category_2'] == 'Adj_control_subj') | (vocab['category_2'] == 'Adj_raising_subj') | (vocab['category_2'] == 'Adj_tough') & (vocab['gender'] == 'n') & (vocab['sg'] == 1)]
all_adj_pl_neuter = vocab['expression'].loc[(vocab['category_2'] == 'adjective') | (vocab['category_2'] == 'Adj') | (vocab['category_2'] == 'Adj-neg') | (vocab['category_2'] == 'Adj_comp') | (vocab['category_2'] == 'Adj_comp_than') | (vocab['category_2'] == 'Adj_clausal') | (vocab['category_2'] == 'Adj_control_subj') | (vocab['category_2'] == 'Adj_raising_subj') | (vocab['category_2'] == 'Adj_tough') & (vocab['gender'] == 'n') & (vocab['pl'] == 1)]
# all_frequent = get_all("frequent", "1")
all_frequent = vocab['expression'].loc[vocab['frequent'] == 1]
all_vehicles = vocab['expression'].loc[vocab['vehicle']==1]








