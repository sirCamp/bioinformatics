from base.BaseAlgorithm import BaseAlgorithm
import math

class FirstAlgorithm(BaseAlgorithm):

    def __init__(self, name, path):
        BaseAlgorithm.__init__(self, name, path)

    def run(self):
        genome_lenght  = 0
        data = []
        sum = 0;
        lineNumber = 0;
        with open(self.path) as file:
            for line in file:
                genome_lenght += 1
                #if genome_lenght == 7:
                #    exit(0)

                if line.find("@") != -1:
                    continue;

                pieces = line.split("\t")

                seven = 0;
                three = 0;

                for index, item in enumerate(pieces, start=0):   # default is zero
                    if index == 7:
                        seven = int(item)

                    if index == 3:
                        three = int(item)

                temp = abs(three - seven);
                lineNumber += 1
                sum +=temp
                #print str(sum) +" "+str(temp)
                data.append(temp)

        med = sum/lineNumber

        sum = 0
        lineNumber = 0
        for index, item in enumerate(data, start=0):
            lineNumber = index
            sum += pow((med-item),2);


        print "media: "+str(med)
        print "varianza: "+str(sum/lineNumber)
        print "variazione standard: "+str(math.sqrt(sum/lineNumber))