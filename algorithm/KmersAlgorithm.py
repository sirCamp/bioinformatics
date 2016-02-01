from base.BaseAlgorithm import BaseAlgorithm
import sys
import string
import os
import errno

class KmersAlgorithm(BaseAlgorithm):



    def __init__(self, name, path):
        BaseAlgorithm.__init__(self, name, path)

    def mapping(self, string):

        string = string.replace("A", "W")
        string = string.replace("T", "A")
        string = string.replace("W", "T")

        string = string.replace("C", "W")
        string = string.replace("G", "C")
        string = string.replace("W", "G")
        return string

    def run(self):

        self.lengthOfCoverage()
        #genome_change = [0] * self.length

        #open the SAM file
        print "Open SAM file..."
        kmers = {}
        index = 0
        print "Looking for kmers and it's opposites for "+str(self.length)
        with open(self.path) as file:
            for line in file:

                if index == self.length:
                    break;

                index += 1
                #exclude header lines
                if line.find("@") != -1:
                    continue;

                pieces = line.split("\t")

                read = str(pieces[9])
                padding = 0
                while len(read[padding:padding+4]) >= 4:
                    key = read[padding:padding+4]
                    padding += 1
                    if kmers.has_key(key):
                        kmers[key] = kmers[key] +1

                    elif kmers.has_key(self.mapping(key)):
                            kmers[self.mapping(key)] = kmers[self.mapping(key)] +1
                    else:
                        kmers.__setitem__(key,1)

        file = "";

        for i in kmers:
            file += str(i)+","+str(kmers[i])+"\n"

        print "Saving kmers.csv file..."
        targetF = open("kmers.csv","w")
        targetF.truncate()
        targetF.write(file)
        targetF.close()
        print("Done!")