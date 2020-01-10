#! usr/bin/python

def pdbfile_list():
    """ This function finds all loaded files in the appropriate folder. """
    import glob, os
    os.chdir("../Data")
    file_list = []
    for file in glob.glob("*.pdb"):
        file_list.append(file)
    return file_list

def extract_SEQRES_seq():
    """ This function extracts seqres sequences in a pdb file. """
    
    import os
    choice = input('Enter the name of the file: ')
    filepath = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Data', choice)
    with open(filepath,'r') as file:
        seq_list = []
        for line in file:
            if line[:6] == 'SEQRES':
                line_split = line.split()[4:]
                seq_list.append(line_split)
    choice1 = input('Enter name of the outfile, to keep sequences for alignment: ')            
    filepath1 = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Results', choice1)
    with open(filepath1, 'w') as outfile:
        for i in seq_list:
            outfile.writelines(i)
        print('Sequences successfully written!')
        
def Align_2files():
    """ This function aligns two PDB files using local alignment algorithm,
        selected by user and outputs the results to a file. """
    
    import os
    import sys
    pdbfile_list()
    
    file_list = pdbfile_list()
    
    items = os.listdir('/home/njesh/python-mini-project-JaneNjeri/Data/')
    
    file_list = [name for name in items if name.endswith('.pdb')]

    for count, fileName in enumerate(file_list, 0):
        sys.stdout.write('[%d] %s\n\r' % (count, fileName))

    choice = int(input('Select the first pdb file[0-%s]: ' % count))
    print(file_list[choice])
    choice2 = int(input('Select the second pdb file[0-%s]: ' % count))
    print(file_list[choice2])
            
    #extracting seqres sequences
    print('Please enter the names of the files, starting with the first one.')
    choice = extract_SEQRES_seq()

    choice2 = extract_SEQRES_seq()
            
    #building global alignment
    from Bio import pairwise2
    from Bio.pairwise2 import format_alignment
            
    choice = input('Enter the name of the first outfile with the extracted sequences: ')
    filepath = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Results', choice)
    with open(filepath,'r') as file:
        for line in file:
            X = line
            break
                          
    choice2 = input('Enter the name of the second outfile with the extracted sequences: ')
    filepath2 = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Results', choice2)
    with open(filepath2,'r') as file:
        for line in file:
            Y = line
            break
                    
    alignments = pairwise2.align.localxx(X, Y)
    for a in alignments:
        print(format_alignment(*a))
        break
#         Z = format_alignment(*a)
                
    choice3 = input('Enter the name of the outfile with the alignment: ')
    filepath3 = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Results', choice3)
    with open(filepath3, 'w') as outfile:
        for i in format_alignment(*a):
            outfile.writelines(i)
            print('All done!')
    Mainmenu()