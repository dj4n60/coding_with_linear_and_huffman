import numpy as np
import itertools

"""
Εφαρμογή για Hamilton Coding for 4 bits
"""

class Hamiltation:

    def __init__(self, input):
        self.input = np.array(input)
        self.output = None
        self.encoded = np.array(input)
        self.G = np.array( [[1,0,0,0,1,0,1] , [0,1,0,0,1,1,0 ], [0,0,1,0,1,1,1] , [0,0,0,1,0,1,1]] ) # Generator Matrix
        self.H = np.array([[1,1,1,0,1,0,0] , [0,1,1,1,0,1,0 ], [1,0,1,1,0,0,1] ] )  # parity Matrix
        self.E = np.array( [ [0,0,0,0,0,0,0] , [0,0,0,0,0,0,1] , [0,0,0,0,0,1,0] , [0,0,0,1,0,0,0] , [ 0,0,0,0,1,0,0 ] , [1,0,0,0,0,0,0] , [1,0,0,0,0,0,0] , [ 0,0,1,0,0,0,0] ] ) #error correction


    """
    Makes the binary numbering to decimal
    """
    def binary_counting(self,array):
        count=0

        range = 1
        array_list = list(array)
        k = 0
        y = len(array) - 1
        while k < len(array):
            count += (2 ** k) * array[y]
            k += 1
            y += -1
        return count

    """
    Encode the input
    """
    def encode(self,debug):
        self.output = np.matmul(self.input,self.G) #generate codeword
        self.output = self.output[0:] % 2 #all the calculation is in modulo 2
        if debug == True:
            print( "The input: " + str(self.input) )
            print( "Finale encoding: " + str(self.output))
            return self.output
        else:
            return self.output

    """
    Fix the encoded messange and return the original
    """
    def decode(self,debug):

        syndrome = np.matmul(self.H,self.encoded)# Calculate Syndrome
        syndrome = syndrome[0:] % 2 #all the calculation is in modulo 2

        error = self.binary_counting(syndrome) # make the syndrome to number to intersect with the E array

        self.output = np.subtract(self.encoded,self.E[error]) # Fix the encoded input

        if debug == True:
            print( "The error is : " + str(error) + " So I am using " + str(self.E[error]) )
            print( "The output is : " + str(self.output[0:4]) )
            return str(self.output[0:4])
        else:
            return str(self.output[0:4])


    def get_input(self):
        return self.input

"""
examples
x = Hamiltation( np.array( [0,1,0,1] ) )
print(x.encode(False))
x = Hamiltation( np.array( [0, 1, 0, 1, 1, 0, 1] ) )
print(x.decode(False))

"""
