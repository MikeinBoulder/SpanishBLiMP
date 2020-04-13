# Authors: Alex Warstadt
# Functions for manipulating strings
import re

def verb_cleanup(verb, make_reflex = False):
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

def string_beautify(string):
    """
    :param string: the string of a generated sentence
    :return: the string with whitespace removed and the first character capitalized
    """
    string = remove_extra_whitespace(string)
    string = list(string)
    string[0] = string[0].capitalize()
    string = "".join(string)
    return string

