# xyz2POSCAR
This script converts the xyz format files into POSCAR for VASP calculation

Download it and move it to the bin file 

chmod u+x ~/bin/get_POSCAR.py

To use it: 

get_POSCAR.py XXX.xyz POSCAR 

Note: 
1 The script read the second line to get the box parameters of the structure

2 If there are no parameters, it will ask you to type by hand 

3 if you do not want to type by hand, press anykey and it will use the default values of 40 x 40 x 40
#MaxNevo Edit Notes
I could not get this script to run when I needed it. I have made a seris of changes the include:


Fixes:
1 Print for the error text of lattice missing (old python implemnetation I think)

2 Some of the functions didn't call the open file as a global variable, but I decided to jsut pass the file path into those functions

3 Changed indexing varialbes for loops to help avoid confusion



New Features:
1 Looping for all of the .xyz files in the scripts current repository (get_XYZ_files())

2 Prompt to ask the user if they want to add a tag to all of the converted files.
		USE get_POSCAR_MNedits_v2_NO_INPUT TO NOT BE PROMPTED FOR TAGGING





