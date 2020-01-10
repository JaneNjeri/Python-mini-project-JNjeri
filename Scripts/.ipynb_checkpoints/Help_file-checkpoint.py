#! usr/bin/python

def Help_file():
    """ This function lists all options and displays a brief description of each. """
    
    print(""" The available options:

        R: Enter name of a PDB file 
           This option allows the user to read in PDB files for analysis.
           
        S: Search for PDB files
           This option enables the user to search PDB files that are already loaded for analysis.
           It also, reports glycosylation sites in the protein with a given pattern for the motif.
           
        W: Write out PDB files (PDB files in existence)
           Writes out different portions of PDB files, including atomic coordinates and
           protein sequences in fasta format.
           
        I: Information on PDB files
           Displays information in the PDB files, in terms of the portions defining the file.
           Including, coordinate sequence, SEQRES sequence, alignment sequence, all non-water ligands in 
           the protein (if any).
           
        A: Alignment
           This option extracts SEQRES sequences from two PDB files and aligns the sequences using the local
           alignment algorithm.
           
        H: Help
           Lists all options ands a brief description of each option.
           
        Q: Quit
           Terminates the program.
        """)
    
    Mainmenu()