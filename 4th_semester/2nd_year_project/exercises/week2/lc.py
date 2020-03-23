# imports
import re
import numpy as np
from nltk.corpus import stopwords
from sklearn.linear_model import Perceptron, LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

# variables
train_text = 'data/train.star.txt'
dev_star_text = 'data/dev.star.txt'
dev_star_other_text= 'data/dev.starOther.txt'
dev_other_text = 'data/dev.other.txt'

token_pattern = re.compile('[\(\)]|\[A-Za-z\'-]+|M[rs]\.|\.+|\w+')
m_sws = set(stopwords.words())

def convert_data(fp):
    """
    Convert given file into list of labels, tokens and also return vocab
    """
    labels = list()
    all_tokens = list()
    vocab = set()
    with open(fp) as f:
        for l in f.readlines():
            labels.append(l.split('\t')[0])
            tokens = token_pattern.findall(l.split('\t')[1])
            vocab |= {token for token in tokens if not token.isdigit()}
            all_tokens.append([token for token in tokens if not token.isdigit()])
    return labels, all_tokens, vocab

def lists_to_arrays(labels, tokens, feature_dict):
    """
    Convert lists into labels and feature matrix that can be input for classifier
    """
    X = np.zeros((len(tokens), len(feature_dict)), dtype = np.int16)
    y = np.array([labels,])
    y = y.reshape(-1,1)
    for idx, row in enumerate(tokens):
        for v in row:
            if v in feature_dict:
                X[idx, feature_dict[v]] += 1
    return X, y

if __name__ == '__main__':
    train_labels, train_tokens, train_vocab = convert_data(train_text)
    index_dir = {key: value for (value, key) in enumerate(train_vocab)}
    inversed_index_dir = {value: key for (key, value) in index_dir.items()}
    train_X, train_y = lists_to_arrays(train_labels, train_tokens, index_dir)
    
    # train perceptron
    perceptron = Perceptron(tol = 1e-3, random_state = 42)
    perceptron.fit(train_X, train_y)
    #print(perceptron.score(train_X,train_y))
    
    # train logistic regression
    lr = LogisticRegression(random_state = 42, tol = 1e-4)
    lr.fit(train_X, train_y)
    #print(lr.score(train_X, train_y))
    print('Top words for LR:')
    for coef in lr.coef_:
        print([inversed_index_dir[x] for x in np.argsort(coef)[::-1][:10]])

    print("Top words for Perceptron:")
    for coef in perceptron.coef_:
        print([inversed_index_dir[x] for x in np.argsort(coef)[::-1][:10]])
    
    # read devsets
    for current_dev_set in [dev_star_text, dev_star_other_text, dev_other_text]:
        dev_labels, dev_tokens, _ = convert_data(current_dev_set)
        dev_X, dev_y = lists_to_arrays(dev_labels, dev_tokens, index_dir)
        pred_y = perceptron.predict(dev_X)
        print(current_dev_set)
        print("Perceptron results")
        print(confusion_matrix(dev_y, pred_y))
        print(accuracy_score(dev_y, pred_y))

        print("Logistric Regression results")
        pred_y = lr.predict(dev_X)
        print(confusion_matrix(dev_y, pred_y))
        print(accuracy_score(dev_y, pred_y))
