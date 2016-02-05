from base.BaseAlgorithm import BaseAlgorithm
import math
import numpy as np
import matplotlib.pyplot as plt

class FirstAlgorithm(BaseAlgorithm):

    def __init__(self, name, path):
        BaseAlgorithm.__init__(self, name, path)

    def run(self):
        self.lengthOfCoverage()
        genome_insertion = []
        sum = 0;
        sumI = 0;

        ext = 0;
        with open(self.path) as file:
            for line in file:

                if ext == self.length:break;

                if line.find("@") != -1:
                    continue

                pieces = line.split("\t")
                ext += 1
                if int(pieces[8]) > 0 and int(pieces[8]) < 10000:
                    isize = abs(int(pieces[3])-int(pieces[7]))
                    genome_insertion.append(isize)
                    sum += isize
                    sumI += 1


        file = "position,isize\n"
        scatFile = "position,distance\n"

        isizeM = int((sum / sumI))
        tmp = 0
        index = 1
        for i in genome_insertion:
            file += str(index)+","+str(i)+"\n"
            dist = (i-isizeM)
            scatFile += str(dist)+","+str(i)+"\n"
            tmp += math.pow(dist,2) #per la dev standard
            index += 1


        print "Saving genome_insert_csv.csv file..."
        targetF = open("genome_insert_csv.csv","w")
        targetF.truncate()
        targetF.write(file)
        targetF.close()
        print "Saving genome_insert_scat_csv.csv file..."
        targetF = open("genome_insert_scat_csv.csv","w")
        targetF.truncate()
        targetF.write(scatFile)
        targetF.close()
        print "Media: "+str(isizeM)
        print "Standard Dev: "+str(math.sqrt(tmp/(index)))
        print("Done!")