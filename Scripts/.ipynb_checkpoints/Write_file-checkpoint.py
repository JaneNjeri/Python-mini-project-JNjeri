#! usr/bin/python

def pdbfile_list():
    """ This function finds all loaded files in the appropriate folder. """
    import glob, os
    os.chdir("../Data")
    file_list = []
    for file in glob.glob("*.pdb"):
        file_list.append(file)
    return file_list

def coord_atoms():
    """ This function provides all coordinate atoms in a PDB file, and outputs to a file. """
    
    import os
    choice = input('Enter the name of the file: ')
    filepath = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Data', choice)
    a_list = []
    with open(filepath, 'r') as pdb:
        for line in pdb:
            if line[:4] == 'ATOM':
                line_split = line.split()[6:9]
                a_list.append(line_split)    
    choice1 = input('Enter the name of the outfile: ')
    filepath1 = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Results', choice1)
    with open(filepath1, 'w') as outfile:
        for i in a_list:
            outfile.writelines(i)
        print('Done!')
        print(i)
        
def write_backbone_atoms():
    """ This function write out coordinates for all backbone atoms (CA, C, N, O), in PDB file """
    
    import os
    choice = input('Enter the name of the file: ')
    filepath = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Data', choice)
    backbone_list = []
    with open(filepath, 'r') as pdb:
        for line in pdb:
            if line[12:16] == " CA " and " O " and " N " and " C ":
                line_split = line.split()[6:9]
                backbone_list.append(line_split)
    choice1 = input('Enter the name of the outfile: ')
    filepath1 = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Results', choice1)
    with open(filepath1, 'w') as outfile:
        for i in backbone_list:
            outfile.writelines(i)
        print('Done!')
        print(i)
        
def write_CA_atoms():
    """ This function write out coordinates for all alpha-carbon atoms (CA), in a PDB file. """
    
    import os
    choice = input('Enter the name of the file: ')
    filepath = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Data', choice)
    ca_list = []
    with open(filepath, 'r') as pdb:
        for line in pdb:
            if line[:4] == 'ATOM' and line[12:16] == " CA ":
                line_split = line.split()[6:9]
                ca_list.append(line_split)
    choice1 = input('Enter name of the outfile: ')
    filepath1 = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Results', choice1)
    with open(filepath1, 'w') as outfile:
        for i in ca_list:
            outfile.writelines(i)
        print('Done!')
        print(i)
        
def write_SEQRES_fasta():
    """ This function extracts seqres sequences in a pdb file and outputs it to a fasta file. """
    
    import os
    choice = input('Enter the name of the file: ')
    filepath = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Data', choice)
    with open(filepath,'r') as file:
        seq_list = []
        for line in file:
            if line[:6] == 'SEQRES':
                line_split = line.split()[4:]
                seq_list.append(line_split)
    choice1 = input('Enter name of the outfile: ')            
    filepath1 = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Results', choice1)
    with open(filepath1, 'w') as outfile:
        for i in seq_list:
            outfile.writelines(i)
        print('Sequences successfully written!')
        
    with open(choice, 'r') as myfile:
        header = ''
        for line in myfile:
            if line.startswith("TITLE"): 
                head_split = line.split()
                header = header + ' '.join(head_split[1:])
            
    choice2 = input('Enter output file name with a .fasta extension: ')
    filepath2 = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Results', choice2)
    z = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Results', choice1)
    with open(z, 'r') as file:
        with open(filepath2, 'w') as output:
            for i in file:
                output.writelines('>' + header + '\n' + i)
                print('>' + header + '\n' + i)
        print('Fasta file generated!')
        
def write_coord_seq():
    """ This function write out the sequence of the PDB file in a fasta format,
        based on the coordinates section. """
    
    import os
    choice = input('Enter the name of the file: ')
    filepath = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Data', choice)
    lis = []
    with open(filepath, 'r') as file:
        for line in file:
            if line[:4] == 'ATOM':
                line_split = line.split()
                lis.append(line_split[3:4])
    choice1 = input('Enter name for the output file: ')
    filepath1 = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Results', choice1)
    with open(filepath1, 'w') as myfile:
        for i in lis:
            myfile.writelines(i)
        print('Done!')
        
    with open(choice, 'r') as myfile:
        header = ''
        for line in myfile:
            if line.startswith("TITLE"): 
                head_split = line.split()
                header = header + ' '.join(head_split[1:])
            
    choice2 = input('Enter output file name with a .fasta extension: ')
    filepath2 = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Results', choice2)
    z = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Results', choice1)
    with open(z, 'r') as file:
        with open(filepath2, 'w') as output:
            for i in file:
                output.writelines('>' + header + '\n' + i)
                print('>' + header + '\n' + i)
        print('Fasta file generated!')
        
def write_align_seq():
    """ This function write out a sequence equivalent to the SEQRES section with all the missing
        residues converted to ‘X’ characters, in fasta format. """
    
    import os
    choice = input('Enter the name of the file: ')
    filepath = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Data', choice)
    with open(infile,'r') as file:
        seq_list = []
        for line in file:
            if line[:6] == 'SEQRES':
                line_split = line.split()[4:]
                seq_list.append(line_split)
    choice1 = input('Enter name of the outfile: ')            
    filepath1 = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Results', choice1)
    with open(filepath1, 'w') as outfile:
        for i in seq_list:
            outfile.writelines(i)
        print('Sequences successfully written!')
        
    choice2 = input('Enter name of the alignment sequence: ')
    filepath2 = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Results', choice2)
    j = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Results', choice1)
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
                    print('Done!')
                    return single_seq
                else:
                    print("ERROR: Line was not a factor of 3 in length!")  
        
    with open(choice, 'r') as myfile:
        header = ''
        for line in myfile:
            if line.startswith("TITLE"): 
                head_split = line.split()
                header = header + ' '.join(head_split[1:])
            
    choice3 = input('Enter output file name with a .fasta extension: ')
    filepath3 = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Results', choice3)
    z = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Results', choice2)
    with open(z, 'r') as file:
        with open(filepath3, 'w') as output:
            for i in file:
                output.writelines('>' + header + '\n' + i)
                print('>' + header + '\n' + i)
        print('Fasta file generated!')
        

##sub-options of the main options

def submenu1():
    """ This function calls out the sub-menu for writing out coordinate file. """
    
    p = ''
    while p == '':
        print('\nS U B  M E N U 1')
        print('1. All atom')
        print('2. Backbone atoms')
        print('3. Alpha carbon atoms only')
        print('b. Back')
        print('q. Quit')
        option = input('Select an option: ')
        if option.lower() == 'q':
            sys.exit()
        elif option.lower() == 'b':
            return Write_menu()
        elif option == '1':
            p = coord_atoms()
        elif option == '2':
            p = write_backbone_atoms()
        elif option == '3':
            p = write_CA_atoms()
        else:
            print ('Invalid selection!')
    return p

def submenu2():
    """ This function calls out the sub-menu for writing out sequences in a PDB file, in fasta format. """
    
    j = ''
    while j == '':
        print('\nS U B  M E N U 2')
        print('1. SEQRES sequence')
        print('2. Coordinate sequence')
        print('3. Alignment sequence')
        print('b. Back')
        print('q. Quit')
        option = input('Select an option: ')
        if option.lower() == 'q':
            sys.exit()
        elif option.lower() == 'b':
            return Write_menu()
        elif option == '1':
            j = write_SEQRES_fasta()
        elif option == '2':
            j = write_coord_seq()
        elif option == '3':
            j = write_align_seq()
        else:
            print ('Invalid selection!')
    return j


##main-options
def Write_menu():
    """ This function calls out the write main-menu for writing out PDB files. """
    
    import sys
    d = ''
    msg = ''    
    while d == '':
        print('\nW R I T E   M E N U')
        print('1. Write out coordinate file')
        print('2. Write out sequence(Fasta format)')
        print('q. Quit')
        option = input('Select an option: ')
        if option.lower() == 'q':
            sys.exit()
        elif option == '1':
            msg = 'Option 1'
            d = submenu1()
        elif option == '2':
            msg = 'Option 2'
            d = submenu2()
        else:
            print ('Invalid selection!')
    return msg, d    

# message, action = Write_menu()

# print ('\nMessage: ', message)
# print ('Action: ', action)

#the write function

def Write_file():
    """ Writes out different portions of PDB files, including atomic coordinates and
        protein sequences in fasta format.
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
            
    return choice
    choice = infile
    Write_menu()
    
    Mainmenu()
