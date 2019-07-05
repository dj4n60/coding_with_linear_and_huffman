from huffman import HuffmanCoding
from hamilton import Hamiltation
import numpy as np

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



path = input("Give file...\n")
input = input("Run on Debug ? \n")
debug =  True if input == '1' else False

#Compression creating the bin file
h = HuffmanCoding(path,debug)
output_path = h.compress()
########

#### Taking all the bits from the comppressed file
compressed_bytes= make_string_with_bits("test1.bin")
#######

compressed_bytes = compressed_bytes[0:4] #taking all the first 4 for start

###Routine to making the array for the 4 bits
lista = []
for i in compressed_bytes:
    lista.append(int(i))

#####Routine to encode a message of 4 bit
x = Hamiltation( np.array( lista ) )#init the message to the class
encoded = x.encode(debug) #encode it
#####Routine to decode the 8 bit codeword encode is the e
x = Hamiltation( np.array( encoded ) ) # Decoded it
decoded = x.decode(debug)) # the decoded message of 4 bit



h.decompress(output_path) # decopress after the decode you have to give file
