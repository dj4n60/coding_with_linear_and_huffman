#!/usr/bin/python3
from os import path as path_
import json
from huffman import HuffmanCoding
from hamilton import Hamiltation
import numpy as np
from os import path as path_
import base64


#Taking a json
path = input("Give json file...\n")
while path_.exists(path) ==  False:
    print("No such file exist")
    path = input("Give json file...\n")
deb_input = input("Run on Debug ? \n")
debug =  True if deb_input == '1' else False


with open(path) as json_file:
    data = json.load(json_file)

h = HuffmanCoding(path,debug)
h.set_reverse_mapping(data["reverse_mapping"])# The statics from the huffman compression

received_message = data["Messagebase64"]
received_message = bytes(received_message[2:-1],'utf-8') #Make it back to base64 bytes

income_message = str(base64.b64decode(received_message))
income_message = income_message[2:-1] #We take only what we need


dec_out = ''
i = 0
k = 7
while k <= len(income_message):
    input = income_message[i:k] # Do hamilton for input = income_message[i:k]
    lista = [] #make a list so i can make an numpy array
    for bit in input:
        lista.append(int(bit))

    y = Hamiltation( np.array( lista ) ) # Decoded it
    decoded = y.decode(debug) # the decoded message of 4 bit
    dec_out += str(decoded)
    i += 7
    k += 7

dec_out = ''.join(c for c in dec_out if c not in ' []') #clear the message
h.decompress_string(dec_out) # Finally it is making a new file with suffix "_decompressed.txt"
