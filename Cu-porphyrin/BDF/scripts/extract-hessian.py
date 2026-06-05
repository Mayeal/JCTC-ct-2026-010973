#!/usr/bin/env python3

import sys
import os
import subprocess

def extract_hessian_data(input_file):
    """
    Extract Hessian data from the input file starting from a specific marker line
    until another specific marker line is encountered.
    """
    start_marker = "Molecular Hessian - Numerical Hessian (BDFOPT)"
    start_marker1 = "Molecular Hessian - Analytic Hessian (BDFOPT)"
    end_marker = "Entering thermochemistry analysis..."
    data_started = False
    data_lines = []

    try:
        with open(input_file, 'r') as infile:
            for line in infile:
                if start_marker in line or start_marker1 in line:
                    data_started = True
                    continue  # Skip the start marker line

                if data_started and end_marker in line:
                    break

                if data_started and line.strip():  # Ensure we are not collecting empty lines
                    data_lines.append(line.rstrip())
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    return data_lines

def extract_coordinates(filename):
    """
    Extract the molecular coordinates from the specified section of the input file.
    """
    linux_command = f"sed -n '/Good Job/,/Force-RMS/p' {filename} | head -n -2 | tail -n +4 | cut -d ' ' -f 7-"
    try:
        process = subprocess.Popen(linux_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()
        if process.returncode != 0:
            print(f"Error: {error}")
            sys.exit(1)
    except Exception as e:
        print(f"An error occurred while extracting coordinates: {e}")
        sys.exit(1)

    return output.strip().split('\n')

def format_coordinates(coordinate_lines):
    """
    Format the extracted coordinates to include an index number and ensure
    they have six decimal places with a specific spacing.
    """
    formatted_lines = []
    for index, line in enumerate(coordinate_lines):
        parts = line.split()
        atom_type = parts[0]
        coordinates = '  '.join([f"{float(coord):11.6f}" for coord in parts[1:]])
        formatted_line = f"{index + 1:<3} {atom_type:<1} {coordinates}"
        formatted_lines.append(formatted_line)
    return formatted_lines

def extract_cartesian_coordinates(input_file):
    """
    Extract Cartesian coordinates and mass information from the input file.
    """
    start_marker = "Cartesian coordinates (Angstrom)"
    coordinates_started = False
    cartesian_data = []

    mass_mapping = {
        'C': '11.99670',
        'H': '1.00730',
        'N': '14.00310',
        'Cu': '62.92980'
    }

    try:
        with open(input_file, 'r') as infile:
            for line in infile:
                if start_marker in line:
                    coordinates_started = True
                    continue  # Skip the start marker line

                if coordinates_started:
                    if line.strip() == '|--------------------------------------------------------------------------------|':
                        continue  # Skip the separator line
                    elif line.strip() and not line.startswith('|'):
                        parts = line.split()
                        if len(parts) >= 7:  # Ensure line contains expected number of parts
                            try:
                                atom_number = int(parts[0])
                                element = parts[1]
                                # Use fixed mass values
                                mass = mass_mapping.get(element, '0.00000')
                                formatted_line = f"  Atom {atom_number:>4}  Element {element:<2}  Has Mass {mass}"
                                cartesian_data.append(formatted_line)
                            except ValueError:
                                continue  # Skip lines with non-numeric data
                    elif not line.strip():
                        break  # End of Cartesian coordinates
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    return cartesian_data

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: extract_hessian_data.py <filename>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = os.path.splitext(input_file)[0] + "_output.txt"

    # Extract data and coordinates
    hessian_data = extract_hessian_data(input_file)
#    print(hessian_data)
    coordinates = extract_coordinates(input_file)
    formatted_coordinates = format_coordinates(coordinates)
    cartesian_data = extract_cartesian_coordinates(input_file)

    # Fixed header text
    header_text = "Inc., Pleasanton\nStandard Nuclear Orientation (Angstroms)\n\n\n"

    # Footer text
    footer_text = "--\nFinal Hessian\n"

    try:
        # Write to output file
        with open(output_file, 'w') as outfile:
            outfile.write(header_text)  # Write fixed header text
            for line in formatted_coordinates:
                outfile.write(line + '\n')
            outfile.write(footer_text)  # Write footer text
            for line in hessian_data:
                outfile.write(line + '\n')
            for line in cartesian_data:
                outfile.write(line + '\n')

        print(f"Data extraction completed. Output saved to '{output_file}'.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
