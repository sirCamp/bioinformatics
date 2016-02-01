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
        genome_change = [0] * self.length

        #open the SAM file
        print "Analising SAM file..."
        with open(self.path) as file:
            for line in file:

                #exclude header lines
                if line.find("@") != -1:
                    continue;

                pieces = line.split("\t")


                if pieces[5].find("H") == -1 and pieces[5].find("S") == -1:
                    continue;
                #else:
                #    print pieces[5]

                index = 0
                for x in xrange(0,len(str(pieces[9]))):
                        genome_change[int(pieces[3])+index] = genome_change[int(pieces[3])+index] + 1
                        index +=1


                #if (int(pieces[8]) > 0):
                 #   index = 0

                #    for x in xrange(0,len(str(pieces[9]))):
                #        genome_change[int(pieces[3])+index] = genome_change[int(pieces[3])+index] + 1
                #        index +=1
                #else:
                #    index = 0
                #    if int(pieces[8]) < 0:
                #       for x in xrange(0,len(str(pieces[9]))):
                #        genome_change[int(pieces[3])-index] = genome_change[int(pieces[3])-index] + 1
                #        index +=1
                    #genome_change[int(pieces[7]) ] = (genome_change[int(pieces[7])]) -1
                #genome_change[int(pieces[3])] = genome_change[int(pieces[3])] + 1

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