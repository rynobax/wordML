from multiprocessing import Pool
from os import listdir
from os.path import isfile, join

dataDir = './data'
files = [join(dataDir, f)  for f in listdir(dataDir) if isfile(join(dataDir, f))]

def main():
  pool = Pool()
  pool.map(getWordsFromFile, files)

def getWordsFromFile(fname):
  words = dict()
  with open(fname) as f:
    for line in f:
      split = line.split('\t')
      word = split[0]
      year = split[1]
      count = split[2]

      if not word in words:
        words[word] = count
      else:
        words[word] += count

main()
