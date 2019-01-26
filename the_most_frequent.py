#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 00:58:37 2019

@author: annhuang
"""

"""
determine the most frequent strings in the sequence
"""
import collections

sequence = ['a','b','c','a','b','a']
sequence = ['a','a','bi','bi','bi']


#slow solution -> N^2 
#def most_frequent(sequence):
#    ls_count = [sequence.count(item) for item in sequence]
#    return sequence[ls_count.index(max(ls_count))]


def most_frequent(sequence):
    return collections.Counter(sequence).most_common(1)[0][0]

most_frequent(sequence)        
