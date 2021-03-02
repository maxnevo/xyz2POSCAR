#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 2021

Origonal author: lqcata
    Found at: https://github.com/lqcata/xyz2POSCAR.git

Author: Max Neveau
"""
import sys
import os

script = sys.argv 

xyz_file = sys.argv 

out_file = sys.argv 

####################################### DEFINED FUNCTIONS Do Not Touch ##################################################################
def get_box(xyz_file):
    with open(xyz_file) as in_xyz:
        line1 = in_xyz.readlines()[1] 
        if 'Lattice="' in line1:  # Lattice="40.0 0.0 0.0 0.0 40.0 0.0 0.0 0.0 40.0"
            box =  line1.rstrip().split('"')[1].split()
            a = box[0:3]
            b = box[3:6]
            c = box[6:]
        else:
            print('OOPS, it seems that there are no box parametrs in xyz file',
                  'Do you want to type by hand or use the default vaules ( 40 x 40 x 40) ?',
                  'Please enter  y or Y for tying by hand  and press any other keys for using the default value.')
            
            check = input('Please type y or Y or press other keys: >> ')
            if  check == 'y' or check == 'Y':
                a = [input('please enter a direction: '), '0.0', '0.0']
                b = ['0.0', input('please enter b direction: '), '0.0']
                c = ['0.0', '0.0',input('please enter c direction: ') ]
            else:
                a = ['40.0', '0.0', '0.0'] 
                b = ['0.0', '40.0', '0.0'] 
                c = ['0.0', '0.0', '40.0'] 
    return a, b, c 

# get the elements list 
def get_total_ele(xyz_file):
    ele_list = []
    with open(xyz_file) as in_xyz:
        in_file = in_xyz.readlines()[2:]
        for line in in_file:
            ele_list.append(line.rstrip().split()[0])
    return list(set(ele_list))

# get the coordination for one specifix element 
def get_coordinations(ele, xyz_file):
    line_list = []
    with open(xyz_file) as in_xyz:
        in_file = in_xyz.readlines()[2:]
        for line in in_file:
            line_s = line.rstrip().split()[0:4]
            if ele in line_s:
                line_list.append(line_s)
    return line_list

# Get the number of each element 
def get_num_ele(ele, xyz_file):
    total_num = get_coordinations(ele, xyz_file)
    return str(len(total_num))

def get_XYZ_files():
    (_, _, files_in_dir) = next(os.walk(os.path.dirname(os.path.realpath(__file__))))
    files_in_dir.sort()
    correct_files = []
    for file_test in files_in_dir:
        if file_test[-4:] == '.xyz':
            correct_files.append(file_test)
    return correct_files
#########################################################################################################################


file_converted = ''

#Pulls the files that start with filename variable and are .xyz files
correct_files = get_XYZ_files()

for file in correct_files: # Runs through the number of files you have
        
        poscar = open(file[:-4] + file_converted + '.POSCAR' , 'w') #creates a new file for converted poscar
        poscar.write('Converted POSCAR with Python Script ' + os.path.basename(__file__) + '\n1\n') #Adds POSCAR conversion tag
        
        #Pulls lattice parameters from .xyz
        for j in get_box(file):  
            poscar.write('%s %s %s\n' %(j[0], j[1], j[2]))

        # Write Elements line 
        for k in get_total_ele(file):
            poscar.write(k + ' ')
            poscar.write('\n')

        # Write elements numbers line 
        for m in get_total_ele(file):
            poscar.write((get_num_ele(m, file))+' ')

        # Write Cartesian line 
        poscar.write('\nCartesian\n')

        # Write Cooridination part 
        for n in get_total_ele(file):
            for o in get_coordinations(n, file): 
                poscar.write('%s %s %s\n' %(o[1], o[2], o[3]))
        poscar.close()
        print('Done! the POSCAR is named as %s' %(file[:-4] + file_converted + '.POSCAR'))

