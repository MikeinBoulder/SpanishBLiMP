# Authors: Alex Warstadt
# Functions for manipulating strings
import re

def de_a_cleanup(verb, refl):
    if verb.endswith('de') and refl.startswith('a'):
        return verb + refl[1:]
    else:
        return verb + ' ' + refl
        

def verb_cleanup(verb, make_reflex = False, remove_se_inf = False):
    if remove_se_inf:
        if verb.endswith('se'):
            return verb[:-2]
    if make_reflex:
        if verb.startswith('se '):
            return verb
        else:
            return 'se ' + verb
    else:
        if verb.startswith('se '):
            return verb[3:]
        else:
            return verb
    
def remove_extra_whitespace(string):
    """
    :param string: the string of a generated sentence
    :return: the string with duplicated whitespace / whitespace before punctuation removed
    """
    string = re.sub(' +', ' ', string).strip()
    string = re.sub(' \.', '.', string)
    string = re.sub(' ,', ',', string)
    string = re.sub(' \?', '?', string)
    return string

def string_beautify(string, question = False):
    """
    :param string: the string of a generated sentence
    :return: the string with whitespace removed and the first character capitalized
    """
    if question:
        string = remove_extra_whitespace(string)
        string = list(string)
        string[0] = string[0].capitalize()
        string = "".join(string)
        string = '¿'+string+'?'
        return string
    else:
        string = remove_extra_whitespace(string)
        string = list(string)
        string[0] = string[0].capitalize()
        string = "".join(string)
        return string

