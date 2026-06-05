#! /usr/bin/env python
import sys
import re

def read_xyz(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    coords = []
    for i, line in enumerate(lines[2:]): 
        parts = line.split()
        if len(parts) == 4:  
            atom_index = i + 1
            atom_type = parts[0]
            x = float(parts[1])
            y = float(parts[2])
            z = float(parts[3])
            
            if atom_index < 10:

                formatted_line = f"{atom_index}   {atom_type:<2} {x:20.12f} {y:20.12f} {z:20.12f}\n"
            else:

                formatted_line = f"{atom_index}  {atom_type:<2} {x:20.12f} {y:20.12f} {z:20.12f}\n"
            
            coords.append(formatted_line)
    return coords

def read_out(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    ej_ei_value = None
    gradient_data = []
    read_gradient = False
    
    for line in lines:
        if "wI0 =" in line or "wJI =" in line:
            match = re.search(r'(wI0|wJI)\s*=\s*([\d.-]+[eE][+-]?\d+|\d+\.\d+)', line)
            if match:
                ej_ei_value = float(match.group(2))
        
        if "Gradient contribution from Final-NAC(S)-Escaled" in line:
            read_gradient = True
            continue
        
        if "Sum of gradient contribution from Final-NAC(S)-Escaled" in line:
            break
        
        if read_gradient:
            if line.strip(): 
                gradient_data.append(line)
    
    return ej_ei_value, gradient_data

def write_output(coords, ej_ei_value, gradient_data, output_path):

    with open(output_path, 'w') as f:
        f.write("Inc., Pleasanton\n")
        f.write("             Standard Nuclear Orientation (Angstroms)\n\n\n") 
        for coord in coords:
            f.write(coord)
        f.write("--\n")
        f.write("CIS Derivative Couplings\n")
        f.write(f"Ej-Ei = {ej_ei_value:.6f}\n")  
        f.write("DC between ground and excited states with ETF\n\n\n")  
        for line in gradient_data:
            f.write(line)

def main(xyz_file, out_file, output_file):

    coords = read_xyz(xyz_file)
    ej_ei_value, gradient_data = read_out(out_file)
    write_output(coords, ej_ei_value, gradient_data, output_file)

if __name__ == "__main__":
    xyz_file = sys.argv[1]  
    out_file = sys.argv[2]  
    output_file = sys.argv[3] 
    main(xyz_file, out_file, output_file)

