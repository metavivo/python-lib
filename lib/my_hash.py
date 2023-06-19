#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Alessandro Valitutti

# Last version date: 19/06/23

##############################################################################
#                      IMPORT

import input_output
import my_regexp

##############################################################################
#                     GLOBAL VARIABLES

##############################################################################
#                      PARAMETERS

##############################################################################
#                      CLASSES

##############################################################################
#                      FUNCTIONS
#*****************************************************************************
#                  merge_hash

# Merges two dictionaries in a single one without changing the two ones.

def merge_hash(hash1, hash2):
    """Merges two dictionaries in a single one without changing the two ones.

    :param hash1: first dictionary
    :type hash1: dictionary
    :param hash2: second dictionary
    :type hash2: dictionary
    :returns: dictionary -- the dictionary with all values from the two input ones    

    :examples:

      >>> hash1 = {'a': 1, 'b': 2}
      >>> hash2 = {'b': 3, 'c': 4}
      >>> out_hash = merge_hash(hash1, hash2)
      >>> out_hash
      {'a': 1, 'c': 4, 'b': 3}

      >>> hash1 = {'a': 1, 'b': 2}
      >>> hash2 = {'c': 3, 'd': 4}
      >>> out_hash = merge_hash(hash1, hash2)
      >>> out_hash
      {'a': 1, 'c': 3, 'b': 2, 'd': 4}


    """ 
    out_hash = hash1.copy()
    out_hash.update(hash2)
    return out_hash

#************************************************************************
#                       load_hash

def load_hash(filename, sep):
    """Loads a data frame as a dictionary
    
    :param filename: data file
    :type filename: file
    :param sep: separator
    :type sep: string
    :returns: dictionary -- the dictionary with all values from the data file    

    """ 
    step1 = input_output.read_file_to_list(filename)
    step2 = step1[1:]
    out = {}
    for x in step2:
        step3 = my_regexp.split_regexp(sep, x)
        out[step3[0]] = step3[1]
    return out

#************************************************************************
#                       get_hash_value

def get_hash_value(key, hash_table):
    """Checks the key in a dictionary and, if founds it, returns the value
    
    :param key: dict key
    :type key: string
    :param hash_table: dictionary
    :type type: dictionary
    :returns: value -- the vale corresponding to the input key    

    """ 
    if key in hash_table.keys():
        return hash_table[key]
    else:
        return None

##############################################################################
#                      INSTRUCTIONS

#-----------------------------------------------------------------------------
