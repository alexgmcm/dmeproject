### Links
>
- [Official Description](http://www.bbci.de/competition/iii/desc_V.html)


### Sandbox

When checking out the data, please put you scripts into ``sandbox/<name>`` so all can use it.
Form a script in ``sandbox/<name>`` you can access a file with:
>
    data = load('../../data/matlab/data_psd_mat/train_subject1_psd01.mat')

### Folder structure for data

We don't save the data (see .gitignore) on github as it is ~1.2 GB.
Just store your data in the root folder according to following structure:

>
    data/
    ├── ascii
    │   ├── data_psd
    │   │   ├── test_subject1_psd04.asc
    │   │   ├── test_subject2_psd04.asc
    │   │   ├── test_subject3_psd04.asc
    │   │   ├── train_subject1_psd01.asc
    │   │   ├── train_subject1_psd02.asc
    │   │   ├── train_subject1_psd03.asc
    │   │   ├── train_subject2_psd01.asc
    │   │   ├── train_subject2_psd02.asc
    │   │   ├── train_subject2_psd03.asc
    │   │   ├── train_subject3_psd01.asc
    │   │   ├── train_subject3_psd02.asc
    │   │   └── train_subject3_psd03.asc
    │   ├── subject1_ascii
    │   │   ├── test_subject1_raw04.asc
    │   │   ├── train_subject1_raw01.asc
    │   │   ├── train_subject1_raw02.asc
    │   │   └── train_subject1_raw03.asc
    │   ├── subject2_ascii
    │   │   ├── test_subject2_raw04.asc
    │   │   ├── train_subject2_raw01.asc
    │   │   ├── train_subject2_raw02.asc
    │   │   └── train_subject2_raw03.asc
    │   └── subject3_ascii
    │       ├── test_subject3_raw04.asc
    │       ├── train_subject3_raw01.asc
    │       ├── train_subject3_raw02.asc
    │       └── train_subject3_raw03.asc
    ├── matlab
    │   ├── data_psd_mat
    │   │   ├── test_subject1_psd04.mat
    │   │   ├── test_subject2_psd04.mat
    │   │   ├── test_subject3_psd04.mat
    │   │   ├── train_subject1_psd01.mat
    │   │   ├── train_subject1_psd02.mat
    │   │   ├── train_subject1_psd03.mat
    │   │   ├── train_subject2_psd01.mat
    │   │   ├── train_subject2_psd02.mat
    │   │   ├── train_subject2_psd03.mat
    │   │   ├── train_subject3_psd01.mat
    │   │   ├── train_subject3_psd02.mat
    │   │   └── train_subject3_psd03.mat
    │   ├── subject1_mat
    │   │   ├── test_subject1_raw04.mat
    │   │   ├── train_subject1_raw01.mat
    │   │   ├── train_subject1_raw02.mat
    │   │   └── train_subject1_raw03.mat
    │   ├── subject2_mat
    │   │   ├── test_subject2_raw04.mat
    │   │   ├── train_subject2_raw01.mat
    │   │   ├── train_subject2_raw02.mat
    │   │   └── train_subject2_raw03.mat
    │   └── subject3_mat
    │       ├── test_subject3_raw04.mat
    │       ├── train_subject3_raw01.mat
    │       ├── train_subject3_raw02.mat
    │       └── train_subject3_raw03.mat
    └── REMARK
