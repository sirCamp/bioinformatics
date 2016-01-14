from base.BaseAlgorithm import BaseAlgorithm
import sys
import string
import os
import errno

class PhysicalCoverageAlgorithm(BaseAlgorithm):

    leght = 0;

    def __init__(self, name, path):
        BaseAlgorithm.__init__(self, name, path)
        self.lenght = 0


    def lengthOfCoverage(self):
        os.system('clear')

        print "Please insert the desidered length of physical coverage ( leave empty for wole genome ) :"
        print "\n"
        inputVal = raw_input(">>  ")
        try:
           self.lenght = int(inputVal)
        except ValueError:
           print("Error, you must pass a number")
           self.lengthOfCoverage()


    def run(self):

        self.lengthOfCoverage()
        if self.lenght  == 0:
            print "physical coverage of whole genome"
        else:
            print "physical coverage of "+str(self.lenght)+" of genome"


        line = ""
        lineNumber = 0;
        genome_change = []
        range = []
        if self.lenght == 0:
            range  = xrange(0, 3079196)
        else:
            range = xrange(0, self.lenght)

        for i in range:
            genome_change.append(0)

        with open(self.path) as file:
            for line in file:
                if line.find("@") != -1:
                    continue;

                pieces = line.split("\t")

                if ((eval(pieces[1]) & 3) == 3) and (int(pieces[8]) > 0):
                    genome_change[int(pieces[3])] = genome_change[int(pieces[3])] + 1

                    genome_change[int(pieces[7]) + len(str(pieces[9]))] = (genome_change[int(pieces[7]) + len(str(pieces[9]))]) - 1

        file = "";
        file += "fixedStep chrom=genome start=1 step=1 span=1\n"
        currentC = 0



        for i in range:
            currentC += genome_change[i];
            file += str(currentC)+"\n"

        print "Saving to "
        targetF = open("physical_coverage.wig","w")
        targetF.truncate()
        targetF.write(file)
        targetF.close()
        print("file is written")