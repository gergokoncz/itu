import abc

import numpy as np
import math
import collections


# ===== helper classes and functions ====
# DO NOT EDIT this section -- see below
# =======================================

class LanguageModel(metaclass=abc.ABCMeta):
    """
    Abstract class for a language model
    Args:
        docs: the texts. Should be a list of documents (list of words).
        order: history length (-1).
    Creates:
        vocab: the vocabulary underlying this language model. Should be a set of words.
    """

    def __init__(self, vocab, order):
        self.vocab = vocab
        self.order = order
        self.START_SYMBOL = "<START>"
        self.STOP_SYMBOL = "<STOP>"

    @abc.abstractmethod
    def probability(self, word, *history):
        """
        Args:
            word: the word we need the probability of
            history: words to condition on.

        Returns:
            the probability p(w|history)
        """
        pass


class CountLM(LanguageModel):
    """
    A Language Model that uses counts of events and histories
    to calculate probabilities of words in context.
    """

    @abc.abstractmethod
    def counts(self, word_and_history):
        pass

    @abc.abstractmethod
    def norm(self, history):
        pass

    def probability(self, word, *history):
        sub_history = tuple(history[-(self.order - 1):]) if self.order > 1 else () #empty history
        return self.counts((word,) + sub_history) / self.norm(sub_history)

def sample(lm, init, amount):
    """
    Sample from a language model.
    Args:
        lm: the language model
        init: the initial sequence of words to condition on
        amount: how long should the sampled sequence be
    """
    words = list(lm.vocab)
    result = []
    result += init
    for _ in range(0, amount):
        history = result[-(lm.order - 1):]
        probs = [lm.probability(word, *history) for word in words]
        sampled = np.random.choice(words, p=probs)
        result.append(sampled)
    return result


def perplexity(lm, data):
    """
    Calculate the perplexity of the language model given the provided data.
    Args:
        lm: a language model.
        data: the data to calculate perplexity on.

    Returns:
        the perplexity of `lm` on `data`.

    """
    log_prob = 0.0
    history_order = lm.order - 1

    # flatten data
    sdata = [word for sentence in data for word in sentence]
    for i in range(history_order, len(sdata)):
        history = sdata[i - history_order: i]
        word = sdata[i]
        p = lm.probability(word, *history)
        log_prob += math.log(p) if p > 0.0 else float("-inf")
    return math.exp(-log_prob / (len(sdata) - history_order))


# === end helper classes and functions ===
# =======================================


class UniformLM(LanguageModel):
    """
    A uniform language model that assigns the same probability to each word in the vocabulary.
    """

    def __init__(self, vocab):
        super().__init__(vocab, 1)

    # deliverable 2.1
    def probability(self, word, *history):
        """
        return the probability of a word under the uniform LM assumption and zero if it is not in the vocab
        *history: not used here
        """
        raise NotImplementedError
        
        

# ======


class UnigramLM(CountLM):
    """
    A unigram language model
    """

    ## deliverable 1.4
    def __init__(self, vocab, train):
        """
        Create an unigram language model.
        Args:
            train: list of training tokens.
            order: order of the LM.
        """
        super().__init__(vocab, 1)
        self._counts = collections.defaultdict(float)
        self._norm = collections.defaultdict(float)
        self.vocab.add(self.START_SYMBOL)
        self.vocab.add(self.STOP_SYMBOL)

        for sentence in train:
            # augment sentence with special symbols
            sentence = [self.START_SYMBOL] * (self.order-1) + sentence + [self.STOP_SYMBOL] * (self.order-1)
            ## deliverable 3.1 - complete this to populate _counts and _norm[()] (here it is an empty history)
            ## note, we use i to get a word at position i 
            ## we store a word in the _counts dictionary as a tuple (word,) -- no history here
            for i in range(0, len(sentence)):
                # populate counts and norm
                raise NotImplementedError
                
 

    def counts(self, word_and_history):
        return self._counts[word_and_history]

    def norm(self, history):
        return self._norm[history]


class NgramLM(CountLM):
    """
    A unigram language model
    """
    ## deliverable 4.1
    def __init__(self, vocab, train, order):
        """
        Create a bigram language model (try to make this code as general as possible, to handle also higher order n-grams)
        Args:
            train: list of training tokens.
            order: order of the LM.
        """
        super().__init__(vocab, order)
        self._counts = collections.defaultdict(float)
        self._norm = collections.defaultdict(float)
        self.vocab.add(self.START_SYMBOL)
        self.vocab.add(self.STOP_SYMBOL)

        for sentence in train:
            sentence = [self.START_SYMBOL] * (self.order-1) + sentence + [self.STOP_SYMBOL] * (self.order-1)
            ## deliverable 1.5 - make the model more general
            for i in range(self.order-1, len(sentence)):
                history = tuple(sentence[i - self.order + 1: i])
               
                raise NotImplementedError
                

    def counts(self, word_and_history):
        return self._counts[word_and_history]

    def norm(self, history):
        return self._norm[history]



if __name__ == "__main__":
    x = [['the', 'dog', 'barks'],
         ['this', 'is', 'a', 'test', 'dog', '.'],
       ]
    import preproc
    vocab = preproc.create_vocab(x)
    unigram = UnigramLM(vocab, x)
    w = "dog"
    print(w, unigram.probability(w), unigram._counts[(w,)])

