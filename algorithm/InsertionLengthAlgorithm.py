from base.BaseAlgorithm import BaseAlgorithm
import math

class InsertionLengthAlgorithm(BaseAlgorithm):

    def __init__(self, name, path):
        BaseAlgorithm.__init__(self, name, path)

    def run(self):
        self.lengthOfCoverage()
        genome_insertion = []
        sum = 0;
        sumI = 0;

        with open(self.path) as file:
            for line in file:

                if line.find("@") != -1:
                    continue

                pieces = line.split("\t")

                if int(pieces[8]) > 0 and int(pieces[8]) < 10000:
                    isize = abs(int(pieces[3])-int(pieces[7]))
                    genome_insertion.append(isize)
                    sum += isize
                    sumI += 1


        file = "position,isize\n"

        isizeM = int((sum / sumI))
        tmp = 0
        index = 1
        for i in genome_insertion:
            file += str(index)+","+str(i)+"\n"
            dist = (i-isizeM)
            # needs for the standard deviation
            tmp += math.pow(dist,2)
            index += 1


        print "Saving genome_insert_csv.csv file..."
        targetF = open("genome_insert_csv.csv","w")
        targetF.truncate()
        targetF.write(file)
        targetF.close()
        print "Media: "+str(isizeM)
        print "Standard Dev: "+str(format(math.sqrt(tmp/(index)),'.2f'))
        print("Done!")