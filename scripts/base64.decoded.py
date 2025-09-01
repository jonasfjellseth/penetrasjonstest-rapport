"""
base64_decode.py
----------------
Script brukt i penetrasjonstesten for å dekode Base64-strenger 
(i dette tilfellet "64pw.txt") til klartekst (64pw-decoded.txt).
"""

import base64

input_file = '64pw.txt'
output_file = '64pw-decoded.txt'

def decode_file_from_base64(input_path, output_path):
    with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
        for line in infile:
            line = line.strip()
            try:
                decoded = base64.b64decode(line)
                decoded_str = decoded.decode('utf-8')
                outfile.write(decoded_str + '\n')
            except Exception as e:
                print(f"Error decoding line: {line}")
                print(f"Error: {e}")
    print(f"Base64 decoding complete. Decoded strings are saved in {output_path}")

decode_file_from_base64(input_file, output_file)
