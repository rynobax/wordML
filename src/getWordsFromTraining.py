from multiprocessing import Pool
from os import listdir
from os.path import isfile, join

dataDir = './training'
files = [join(dataDir, f) for f in listdir(dataDir) if isfile(join(dataDir, f))]

def main():
  pool = Pool()
  fileWords = pool.map(getWordsFromFile, files)
  masterWords = dict()
  for words in fileWords:
    for word in words:
      if not word in masterWords:
        masterWords[word] = words[word]
      else:
        masterWords[word] += words[word]
  with open('./work/words.txt', 'w') as f:
    for word in masterWords:
      f.write(word + '\n')

def getWordsFromFile(fname):
  words = dict()
  with open(fname) as f:
    for line in f:
      split = line.split(' ')
      for word in split:
        if word == '':
          continue
        if not word in words:
          words[word] = 1
        else:
          words[word] += 1
  return words

if __name__ == '__main__':
  main()
