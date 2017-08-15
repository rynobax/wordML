from os import listdir
from os.path import isfile, join, basename

workDir = './work'
trainingDir = './training'
files = [join(trainingDir, f) for f in listdir(trainingDir) if isfile(join(trainingDir, f))]

words = []
with open(join(workDir, 'words.txt')) as f:
    for word in f:
        if word == '':
            break
        words.append(word.lower().strip())

for f in files:
    total = 0
    countDict = dict()
    for word in words:
        countDict[word.lower().strip()] = 0
    with open(f) as fin:
        for line in fin:
            for word in line.split(' '):
                if word.lower().strip() in countDict:
                    countDict[word.lower().strip()] += 1
                    total += 1
    for word in countDict:
        countDict[word] /= float(total)
    outName = join(workDir, basename(f) + '.count')
    with open(outName, 'w') as fout:
        for word in countDict:
            fout.write(str(countDict[word]) + '\n')
