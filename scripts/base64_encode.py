"""
base64_encode.py
----------------
Script brukt i penetrasjonstesten for å konvertere passordlisten rockyou.txt
til en Base64-kodet versjon (rockyou64.txt) for fuzzing av innlogging.
"""

import base64

input_file = 'rockyou.txt'
output_file = 'rockyou64.txt'

def encode_file_to_base64(input_path, output_path):
    with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
        for line in infile:
            line = line.strip()
            encoded = base64.b64encode(line.encode('utf-8')).decode('utf-8')
            outfile.write(encoded + '\n')
    print(f"Base64 encoding complete. Encoded strings are saved in {output_path}")

encode_file_to_base64(input_file, output_file)
