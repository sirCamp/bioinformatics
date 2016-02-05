from base.BaseAlgorithm import BaseAlgorithm
import sys
import string
import os
import errno

class CigarAlgorithm(BaseAlgorithm):



    def __init__(self, name, path):
        BaseAlgorithm.__init__(self, name, path)

    def run(self):

        self.lengthOfCoverage()
        genome_change = {}

        #open the SAM file
        print "Analising SAM file..."
        with open(self.path) as file:
            for line in file:

                #exclude header lines
                if line.find("@") != -1:
                    continue;

                pieces = line.split("\t")


                if pieces[5].find("H") == -1 and pieces[5].find("S") == -1:

                    continue
                else:
                    index = int(pieces[3])

                    while index < (int(pieces[3])+int(pieces[8])):

                        key = index
                        #genome_change[int(pieces[3])+index] = genome_change[int(pieces[3])+index] + 1
                        #index +=1
                        if genome_change.has_key(key):
                            genome_change[key] = genome_change[key] +1
                        else:
                            genome_change.__setitem__(key,1)
                        index += 1



        file = "";
        file += "fixedStep chrom=genome start=1 step=1 span=1\n"

        coverage = 0

        for i in genome_change:
            coverage = genome_change[i];
            print i
            file += str(i)+"\n"

        print "Saving sequence_coverage.wig file..."
        targetF = open("cigar.wig","w")
        targetF.truncate()
        targetF.write(file)
        targetF.close()
        print("Done!")