from nose.tools import eq_

from snlp import preproc

def setup_module():
    global x_tr, x_dv
    global vocab
    x_tr = preproc.read_data('data/corpus.csv',preprocessor=preproc.space_tokenizer)


def test_space_tok():
    global x_tr
    eq_(len(x_tr), 7)
    eq_(x_tr[1][2], 'a')
    eq_(x_tr[6][4], '?')


def test_create_vocab():
    global x_tr
    vocab = preproc.create_vocab(x_tr)

    eq_(len(vocab), 15)



