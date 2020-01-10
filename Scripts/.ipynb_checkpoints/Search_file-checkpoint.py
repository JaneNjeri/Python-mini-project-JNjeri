#! usr/bin/python

def pdbfile_list():
    """ This function finds all loaded files in the appropriate folder. """
    import glob, os
    os.chdir("../Data")
    file_list = []
    for file in glob.glob("*.pdb"):
        file_list.append(file)
    return file_list

def Get_seqres():
    """ This function extracts seqres sequences in a pdb file and outputs it to a text file. """
    
    import os
    choice = input('Enter the name of the file: ')
    filepath = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Data', choice)
    seq_list = []
    with open(filepath,'r') as file:
        for line in file:
            if line.startswith('SEQRES'):
                line_split = line.split()[4]
                seq_list.append(line_split)
    
    choice1 = input('Enter the name of the outfile: ')
    filepath1 = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Results', choice1)
    with open(filepath1, 'w') as outfile:
        for i in seq_list:
            outfile.write(i)
        print('Sequences successfully written!')
        
def glyc_sites():
    """ This function finds glycosylation sites given G or Y or L then A then P or F or W the TLVGMI as motifs
    given an amino acid sequence file. """
    
    import re
    import os
    choice = input('Enter the name of the file: ')
    filepath = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Data', choice)
    with open(filepath, 'r') as file:
        for i in file:
            pattern = re.compile(r'[GYL]A[PFW][TLVGMI]')
            matches = pattern.finditer(i)
            for match in matches:
                print(match)  
    return i

def check_glycSites():
    """ This function checks the glycosylation sites of a protein sequence in a given file. """
    
    import os
    choice = input('Enter the name of the file: ')
    filepath = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Data', choice)
    with open(filepath, 'r') as myfile:
        for i in myfile:
            glyc_sites(i)
            
def Search_file():
    """ This function enables the user to search PDB files that are already loaded, for analysis.
        It also, reports glycosylation sites in the protein with a given pattern for the motif.
    """
        
    import os
    import sys
    pdbfile_list()

    file_list = pdbfile_list()
    
    items = os.listdir('/home/njesh/python-mini-project-JaneNjeri/Data/')
    
    file_list = [name for name in items if name.endswith('.pdb')]

    for count, fileName in enumerate(file_list, 0):
        sys.stdout.write("[%d] %s\n\r" % (count, fileName))

    choice = int(input("Select pdb file[0-%s]: " % count))
    print(file_list[choice])
            
    choice = infile
    with open(infile, 'r') as file:
        Get_seqres()
        file = Get_seqres

    with open(file, 'r') as aa_seq:
        check_glycSites()
        
    Mainmenu()