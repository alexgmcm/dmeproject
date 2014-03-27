import random
import sys

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def shuffleLines(fileInName, fileOutName):
    numLines = file_len(fileInName)

    fileInLines = open(fileInName, 'r').readlines()
    fileOut = open(fileOutName, 'w')

    randLines = range(numLines)

    # preserve all lines before the @data flag
    offset = 0
    for randLine in randLines:
        line = fileInLines[randLine]
        offset = offset + 1
        fileOut.write(line)
        if line.strip() == '@data':
            break
    randLines = randLines[offset:]

    # random order of lines
    random.shuffle(randLines)


    for randLine in randLines:
        line = fileInLines[randLine]
        fileOut.write(line)

if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) < 2:
        print "missing input and/or output file as arguments"
        exit(1)

    fileIn = args[0]
    fileOut = args[1]

    shuffleLines(fileIn, fileOut)
