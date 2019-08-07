#!/usr/bin/python3
from huffman import HuffmanCoding
from hamilton import Hamiltation
import numpy as np
from os import path as path_
import base64
import json
import os


def make_string_with_bits(file):
    with open(file, 'rb') as file:
        bit_string = ""
        byte = file.read(1)
        while(len(byte) > 0):
            byte = ord(byte)
            bits = bin(byte)[2:].rjust(8, '0')
            bit_string += bits
            byte = file.read(1)
        return bit_string

def add_noise(noise,message):
    lenght = len(message) - 1
    lista = []
    for i in message:
        lista.append(i)
    while noise != 0:
        lista[lenght-1] = str ( (int(lista[lenght-1]) + 1 ) % 2  )
        noise += -1

    noisy_message = ''.join(c for c in str(lista) if c not in " [],''" )
    return noisy_message




finale_message = ""
path = input("Give file...\n")
while path_.exists(path) ==  False:
    print("No such file exist")
    path = input("Give file...\n")
deb_input = input("Run on Debug ? \n")
noise = input("Give Noise...\n")
debug =  True if deb_input == '1' else False





#Compression creating the bin file
h = HuffmanCoding(path,debug)
output_path = h.compress()
########

#### Taking all the bits from the comppressed bin file
compressed_bytes= make_string_with_bits(path + ".bin")
#######

i = 0
k = 4
while k <= len(compressed_bytes):
    input = compressed_bytes[i:k] # Do hamilton for input = compressed_bytes[i:k]
    lista = [] #make a list so i can make an numpy array
    for bit in input:
        lista.append(int(bit))
    x = Hamiltation( np.array( lista ) ) #init the message to the class
    encoded =x.encode(debug)  #encode it
    finale_message += str(encoded)
    i += 4
    k += 4

finale_message = ''.join(c for c in finale_message if c not in ' []')#Finale messange to send
noisy_message = add_noise(int(noise),finale_message)
if debug == True:
    print("Bits to send in binary: " + str(finale_message))
    print("Noisy: " + add_noise(1,finale_message))

finale_message = noisy_message #make the finale_message noisy
finale_message = base64.b64encode(bytes(finale_message, 'utf-8')) #Covert to base64

if debug == True:
    print("Bits to send in base64: " + str(finale_message))

####Make the json data
data = {}
data['compression_algorithm'] = 'Hufffman'
data['code'] = 'Linear'
data['Messagebase64'] = str(finale_message)
data['reverse_mapping'] = h.get_reverse_mapping()


json_data = json.dumps(data)
if debug == True:
    rever_data = json_data
    print(rever_data)

json_path = path + "_json"
with open(json_path, 'w') as output:
    json.dump(data, output)
#The result is a json file with the suffix "_json" which is use on the receive.py
file_size = os.path.getsize(path)
compfile_size = os.path.getsize(path + ".bin")
print("The file original was: " + str(file_size) + " bytes," + " After the comppression: " + str(compfile_size) + " bytes, " + "And on the final message was added: " + str( int(compfile_size * 8 / 4 * 3)  ) + " bits")
