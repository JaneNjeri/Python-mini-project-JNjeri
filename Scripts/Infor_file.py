#! usr/bin/python

def pdbfile_list():
    """ This function finds all loaded files in the appropriate folder. """
    
    import glob, os
    os.chdir("../Data")
    file_list = []
    for file in glob.glob("*.pdb"):
        file_list.append(file)
    return file_list

def display_cord_seq():
    """ This function displays the coordinate sequence in a give PDB file. """
    
    import os
    choice = input('Enter the name of the file: ')
    filepath = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Data', choice)
    with open(filepath, 'r') as file:
        for line in file:
            if line[:4] == 'ATOM':
                line_split = line.split()[3:4]
                print(line_split)
    return file

def display_seqres_seq():
    """ This function displays the SEQRES sequences on the console, for a given PDB file. """
    
    import os
    choice = input('Enter the name of the file: ')
    filepath = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Data', choice)
    with open(filepath, 'r') as file:
        for line in file:
            if line[:6] == 'SEQRES':
                line_split = line.split()[4:]
                print(line_split)
    return file

def display_algn_seq():
    """ This function displays the alignment sequence of a given PDB file. """
    
    import os
    choice = input('Enter the name of the file: ')
    filepath = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Data', choice)
    with open(filepath,'r') as file:
        seq_list = []
        for line in file:
            if line[:6] == 'SEQRES':
                line_split = line.split()[4:]
                seq_list.append(line_split)
            
    filepath1 = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Results', 'outfile1')
    with open(filepath1, 'w') as outfile:
        for i in seq_list:
            outfile.writelines(i)
    
    filepath2 = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Results', 'outfile2')
    j = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Results', 'outfile1')
    with open(j, 'r') as fil:
        d = {'CYS':'C','ASP':'D','SER':'S','GLN':'Q','LYS':'K','ILE':'I','PRO':'P','THR':'T','PHE':'F','ASN':'N',
             'GLY':'G','HIS':'H','LEU':'L','ARG':'R','TRP':'W','TER':'*','ALA':'A','VAL':'V','GLU':'E','TYR':'Y',
             'MET':'M','XAA':'X'}
        with open(filepath2, 'w') as outf:
            for line in fil:
                if len(line) %3 == 0:
                    upper_seq = line.upper()
                    single_seq = ''
                    for i in range(int(len(upper_seq)/3)):
                        single_seq += d[upper_seq[3*i:3*i+3]]
                        outf.write(single_seq)    
                    return single_seq
                else:
                    print("ERROR: Line was not a factor of 3 in length!") 
                    
def display_all_nonwater_L():
    """ This function displays all non-water ligands in the protein(if any). """
    
    import os
    choice = input('Enter the name of the file: ')
    filepath = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Data', choice)
    with open(filepath, 'r') as file:
        for line in file:
            if line[:6] == 'HETATM' and line[16:21] != 'HOH':
                line_split = line.split()[3:4]
                print(line_split)
#             else:
#                 print('File has no non-water ligands')
#                 break

def Infor_menu():
    """ This function displays the various options on atomic coordinates and sequences extracted
        from a PDB file. """
    
    import sys
    d = ''
    msg = ''    
    while d == '':
        print('\nINFORMATION MENU')
        print('1. Display coordinate sequence')
        print('2. Display SEQRES sequence')
        print('3. Display Alignment sequence')
        print('4. Display all non-water ligands in the protein(if any)')
        print('q. Quit')
        option = input('Select an option: ')
        if option.lower() == 'q':
            sys.exit()
        elif option == '1':
            msg = 'Option 1'
            d = display_cord_seq()
        elif option == '2':
            msg = 'Option 2'
            d = display_seqres_seq()
        elif option == '3':
            msg = 'Option 3'
            d = display_algn_seq()
        elif option == '4':
            msg = 'Option 4'
            d = display_all_nonwater_L()
        else:
            print ('Invalid selection!')
    return msg, d    

# message, action = Infor_menu()

# print ('\nMessage: ', message)
# print ('Action: ', action)

def Infor_file():
    """ This function Displays information in the PDB files, in terms of the portions defining the file.
        Including, coordinate sequence, SEQRES sequence, alignment sequence, all non-water ligands in 
        the protein (if any).
    """
    
    import os
    import sys
    pdbfile_list()

    file_list = pdbfile_list()

    items = os.listdir('/home/njesh/python-mini-project-JaneNjeri/PDB_files/')
    
    file_list = [name for name in items if name.endswith('.pdb')]

    for count, fileName in enumerate(file_list, 0):
        sys.stdout.write("[%d] %s\n\r" % (count, fileName))

    choice = int(input("Select pdb file[0-%s]: " % count))
    print(file_list[choice])
            
    return choice
    choice = infile
    Infor_menu()
                
    Mainmenu()