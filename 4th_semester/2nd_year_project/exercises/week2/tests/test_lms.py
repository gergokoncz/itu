from nose.tools import eq_, assert_almost_equals

from snlp import preproc, lm

def setup_module():
    global x_tr, x_dev
    global vocab
    x_tr = preproc.read_data('data/corpus.csv',preprocessor=preproc.space_tokenizer)
    x_dev = preproc.read_data('data/corpus_dev.csv',preprocessor=preproc.space_tokenizer)


# deliverable 2.1
def test_uniform():
    global x_tr
    eq_(len(x_tr), 7)
    vocab = preproc.create_vocab(x_tr)
    eq_(len(vocab), 15)
    uniformLM = lm.UniformLM(vocab)
    eq_(0.06666666666666667, uniformLM.probability("the"))
    eq_(0.06666666666666667, uniformLM.probability("?"))
    eq_(0.0, uniformLM.probability("notttt")) # make sure to return 0 if word not in vocab
    
    ## we can test the probability distribution
    assert_almost_equals(1.0, sum([uniformLM.probability(w) for w in uniformLM.vocab]))

# deliverable 3.1
def test_unigram():
    global x_tr
    eq_(len(x_tr), 7)
    vocab = preproc.create_vocab(x_tr)
    eq_(len(vocab), 15)
    unigramLM = lm.UnigramLM(vocab, x_tr)
    eq_(2/33, unigramLM.probability("another"))
    eq_(1/33, unigramLM.probability("?"))
    eq_(33, unigramLM._norm[()])

# deliverable 3.3
def test_ppl():
    global x_tr, x_dev
    eq_(len(x_tr), 7)
    eq_(len(x_dev), 1)
    vocab = preproc.create_vocab(x_tr)
    uniformLM = lm.UniformLM(vocab)
    eq_(15, lm.perplexity(uniformLM, x_dev))

    vocab_uni = preproc.create_vocab(x_tr)

    unigramLM = lm.UnigramLM(vocab_uni, x_tr)
    assert_almost_equals(8.25, lm.perplexity(unigramLM, x_dev), places=3)
    
# deliverable 4.1
def test_bigram():
    global x_tr, x_dev
    eq_(len(x_tr), 7)
    eq_(len(x_dev), 1)
    vocab = preproc.create_vocab(x_tr)
    bigramLM = lm.NgramLM(vocab, x_tr, 2)
    eq_(1.0,bigramLM.probability("dog","the"))
    eq_(2, lm.perplexity(bigramLM, x_dev))

