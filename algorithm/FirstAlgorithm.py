from base.BaseAlgorithm import BaseAlgorithm
import math
import numpy as np
import matplotlib.pyplot as plt

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
                #genome_lenght += 1
                #if genome_lenght == 10000:
                   #break

                if line.find("@") != -1:
                    continue;

                pieces = line.split("\t")

                seven = 0;
                three = 0;
                five = ""
                four = ""
                for index, item in enumerate(pieces, start=0):   # default is zero
                    if index == 7:
                        seven = int(item)

                    if index == 3:
                        three = int(item)
                    if index == 4:
                        four = str(item)

                temp = abs(three - seven);
                if temp > 10000:
                    print four
                    continue
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

        #N = len(data)
       # menMeans = data#(20, 35, 30, 35, 27)
       # menStd = (2, 3, 4, 1, 2)

        #ind = np.arange(N)  # the x locations for the groups
       # width = 0.01       # the width of the bars

        #fig, ax = plt.subplots()
        #rects1 = ax.bar(ind, menMeans, width, color='r')

        #womenMeans = (25, 32, 34, 20, 25)
        #womenStd = (3, 5, 2, 3, 3)
        #rects2 = ax.bar(ind + width, womenMeans, width, color='y', yerr=womenStd)

        # add some text for labels, title and axes ticks
        #ax.set_ylabel('Scores')
        #ax.set_title('Scores by group and gender')
        #ax.set_xticks(ind + width)
       # ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))

        #ax.legend((rects1[0]), ('Men'))



        #plt.show()