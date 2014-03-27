import sys

def extractHeader(fileInName):
    header = [];
    for line in file(fileInName, 'r').readlines():
        header.append(line)
        if(line.strip() == '@data'):
            return header


def extractData(fileInName):
    readingHeader = True
    data = [];
    for line in file(fileInName, 'r').readlines():
        if not readingHeader:
            data.append(line)

        if(line.strip() == '@data'):
            readingHeader = False
    return data

def mergeFiles(fileInNames, fileOutName):
    outFile = file(fileOutName, 'w')

    outFile.writelines(extractHeader(fileInNames[0]))

    for fileName in fileInNames:
        outFile.writelines(extractData(fileName))


if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) < 1:
        print "missing input file(s) as arguments"
        exit(1)

    filesIn = args

    mergeFiles(filesIn, 'out')

