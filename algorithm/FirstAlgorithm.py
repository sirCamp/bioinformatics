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


        self.lengthOfCoverage()
        genome_insertion = {}

        ext = 0;
        with open(self.path) as file:
            for line in file:

                if ext == self.length:break;

                if line.find("@") != -1:
                    continue

                pieces = line.split("\t")
                ext += 1
                if ((eval(pieces[1]) & 3) == 3) and (int(pieces[8]) > 0) and int(pieces[8]) <10001:

                    index = 0;
                    while index < len(pieces[9]):


                        key = index + int(pieces[3])
                        index += 1 ;

                        if genome_insertion.has_key(key):
                            #media non standard, e comunque valida e permette di ottimizzare
                            genome_insertion[key] = int(((genome_insertion[key] + int(pieces[8]))/2))
                        else:
                            genome_insertion.__setitem__(key,int(pieces[8]))


        file = "fixedStep chrom=genome start=1 step=1 span=1\n"
        for i in genome_insertion:
            file += str(genome_insertion[i])+"\n"

        print "Saving genome_insertion_lenght.wig file..."
        targetF = open("genome_insertion_lenght.wig","w")
        targetF.truncate()
        targetF.write(file)
        targetF.close()
        print("Done!")




                #genome_lenght += 1
                #if genome_lenght == 100000:
                   #break
                #   f = open("text.wig", 'w')
                #   f.write(final)
                 #  f.close()
                 #  exit(0)

                #if line.find("@") != -1:
                #    continue;

                #pieces = line.split("\t")

                #seven = 0;
                #three = 0;
                #five = ""
                #four = ""
                #if ((eval(pieces[1]) & 3) == 3) and (int(pieces[8]) > 0):
                #    for index, item in enumerate(pieces, start=0):   # default is zero
                #        if index == 7:
                #            seven = int(item)

                #        if index == 3:
                #            three = int(item)
                        #if index == 4:
                        #    four = str(item)

                #    temp = abs(three - seven);
                    #if temp > 10000:
                    #    print four
                    #    continue
                #    lineNumber += 1
                #    sum +=temp
                    #print(temp)
                #    final += str(temp)+"\n"
                    #print str(sum) +" "+str(temp)
                #    data.append(temp)

        #med = sum/lineNumber

        #sum = 0
        #lineNumber = 0
        #for index, item in enumerate(data, start=0):
        #    lineNumber = index
        #    sum += pow((med-item),2);


        #print "media: "+str(med)
       # print "varianza: "+str(sum/lineNumber)
       # print "variazione standard: "+str(math.sqrt(sum/lineNumber))
       # f = open("text.wig", 'w')
       #  f.write(final)
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