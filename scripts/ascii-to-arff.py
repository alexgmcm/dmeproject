
import sys
import os

def psd_head(is_train=True):
    channels = ['C3', 'Cz', 'C4', 'CP1', 'CP2', 'P3', 'Pz', 'P4']
    head ='% The psd data\n\n'
    head = head + '@relation eeg\n\n'
    for channel in channels:
        for hz in range(8, 32, 2):
            head = head + '@attribute ' + channel+'-'+str(hz)+' numeric\n'
        head = head + '\n'

    #if is_train:
    head = head + '@attribute class {2,3,7}'

    head = head + '\n\n'

    return head

def raw_head(is_train=True):
    channels = ['C3', 'Cz', 'C4', 'CP1', 'CP2', 'P3', 'Pz', 'P4']
    channels = ['Fp1', 'AF3', 'F7', 'F3', 'FC1', 'FC5', 'T7', 'C3', 'CP1', 'CP5', 'P7', 'P3', 'Pz', 'PO3', 'O1', 'Oz', 'O2', 'PO4', 'P4', 'P8', 'CP6', 'CP2', 'C4', 'T8', 'FC6', 'FC2', 'F4', 'F8', 'AF4', 'Fp2', 'Fz', 'Cz']

    head ='% The raw data\n\n'
    head = head + '@relation eeg-raw\n\n'
    for channel in channels:
        head = head + '@attribute ' + channel+' numeric\n'

    #if is_train:
    head = head + '@attribute class {2,3,7}'

    head = head + '\n\n'

    return head


def transformPSD(file_in, file_out, is_train=True):
    out = open(file_out, 'w');
    out.write(psd_head(is_train))       # prepend head
    out.write('@data\n')        # fillow with the data...

    for line in open(file_in, 'r'):
        vals = line.strip().split()
        if is_train:
            vals[len(vals)-1] = vals[len(vals)-1].split('.')[0]
        if not is_train:
            vals = vals + ['?']

        out.write(','.join(vals))
        out.write('\n')
    out.close()

def transformRAW(file_in, file_out, is_train=True):
    out = open(file_out, 'w');
    out.write(raw_head(is_train))       # prepend head
    out.write('@data\n')        # fillow with the data...

    for line in open(file_in, 'r'):
        vals = line.strip().split()
        if is_train:
            vals[len(vals)-1] = vals[len(vals)-1].split('.')[0]
        if not is_train:
            vals = vals + ['?']

        out.write(','.join(vals))
        out.write('\n')
    out.close()



def transformAllPDF():
    file_in = '../data/ascii/data_psd/train_subject{subj#}_psd0{#}.asc'
    file_out = '../data/weka/data_psd/train_subject{subj#}_psd0{#}.arff'
    targetDir = '../data/weka/data_psd/';
    if not os.path.exists(targetDir):
        os.makedirs(targetDir)

    # first handle training data
    for subject in [str(s) for s in range(1,4)]:
        for session in [str(s) for s in range(1, 4)]:
            transformPSD(file_in.replace('{subj#}', subject).replace('{#}', session), file_out.replace('{subj#}', subject).replace('{#}', session))



    # then handle test data
    file_in = '../data/ascii/data_psd/test_subject{subj#}_psd04.asc'
    file_out = '../data/weka/data_psd/test_subject{subj#}_psd04.arff'

    for subject in [str(s) for s in range(1,4)]:
        transformPSD(file_in.replace('{subj#}', subject), file_out.replace('{subj#}', subject), is_train=False)

def transformAllRAW():
    file_in = '../data/ascii/subject{subj#}_ascii/train_subject{subj#}_raw0{#}.asc'
    file_out = '../data/weka/subject{subj#}_arff/train_subject{subj#}_psd0{#}.arff'

    # first handle training data
    for subject in [str(s) for s in range(1,4)]:
        targetDir = '../data/weka/subject{subj#}_arff/'.replace('{subj#}', subject)
        if not os.path.exists(targetDir):
            os.makedirs(targetDir)
        for session in [str(s) for s in range(1, 4)]:
            transformRAW(file_in.replace('{subj#}', subject).replace('{#}', session), file_out.replace('{subj#}', subject).replace('{#}', session))



    # then handle test data
    file_in = '../data/ascii/subject{subj#}_ascii/test_subject{subj#}_raw04.asc'
    file_out = '../data/weka/subject{subj#}_arff/test_subject{subj#}_psd04.arff'

    for subject in [str(s) for s in range(1,4)]:
        transformRAW(file_in.replace('{subj#}', subject), file_out.replace('{subj#}', subject), is_train=False)




if __name__ == '__main__':
    args = sys.argv[1:]

    transformAllPDF()
    transformAllRAW()

#    file_in = '../data/ascii/data_psd/train_subject1_psd01.asc'
#    file_out = '../data/weka/data_psd/train_subject1_psd01.arff'
#    if len(args) >= 1:
#        file_in = args[0]
#    if len(args) >= 2:
#        file_in = args[1]
#
#    transformPSD(file_in, file_out)

