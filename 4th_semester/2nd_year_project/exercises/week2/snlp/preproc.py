from collections import Counter

import pandas as pd
import numpy as np

# deliverable 1.1
def space_tokenizer(text):
    '''
    space tokenizer

    :param text: a document, as a single string (here just a sentence)
    :returns: a list of words
    :rtype: list
    '''
    raise NotImplementedError
    

# deliverable 1.2
def create_vocab(tokenized_texts):
    '''
    Extracts the vocabulary from a list of tokenized documents
    
    :param texts: a list of tokenized documents
    :returns: a vocab (a set of words)
    :rtype: set
    '''
   
    raise NotImplementedError




### helper code

def read_data(filename,label=None,preprocessor=space_tokenizer):
    """
    Code to read in the data
    :param filename:  path
    :param label: None (as we do not use classification yet)
    :param preprocessor: your metho
    :return: list of preprocessor output
    """
    df = pd.read_csv(filename)
    return [preprocessor(string) for string in df['sentences'].values]
