import sys
import pandas as pd

if len(sys.argv) < 3:
    print('please provide original and prediction file:')
    print('python3 check-lyrics.py lyrics-data/metal-lyrics-test-hidden.csv 12345.lyrics.txt')
    exit(1)

tags = {'1980s', '1990s', '2000s', '2010s', '2020s', 'pre-1980s'}

original = pd.read_csv(sys.argv[1])
pred = pd.read_csv(sys.argv[2])

for keyWord in ['Era', 'Lyrics']:
    if keyWord not in original:
        print('ERROR: \'' + keyWord + '\' not found in ' + sys.argv[1])
        exit(1)
    if keyWord not in pred:
        print('ERROR: \'' + keyWord + '\' not found in ' + sys.argv[2])
        exit(1)

if len(original) != 371:
    print('ERROR: ' + sys.argv[1] + ' is not of length 371 anymore')
    exit(1)
if len(pred) != 371:
    print('ERROR: ' + sys.argv[2] + ' is not of length 371 anymore')
    exit(1)

numErrs = 0
for i in range(len(original)):
    if numErrs > 10:
        print('More than 10 errors found, this probably means that you mixed up the order of the file.')
        exit(1)

    if original['Lyrics'][i] != pred['Lyrics'][i]:
        print('ERROR: the lyrics on line ' + str(i+2) + ' do not match in both files.')
        numErrs += 1
    if pred['Era'][i].strip() not in tags:
        print('ERROR: the prediction on line ' + str(i+2) + ' is an invalid label: ' + pred['Era'][i])
        numErrs += 1
    

if numErrs == 0:
    print('Succesfully passed check!')
else:
    print()
    print('Please fix the errors shown above')
