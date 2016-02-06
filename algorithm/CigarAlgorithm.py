from base.BaseAlgorithm import BaseAlgorithm

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

                #exclude all reads that no have H or S inside CIGAR field
                if pieces[5].find("H") == -1 and pieces[5].find("S") == -1:

                    continue
                else:
                    index = int(pieces[3])
                    length = (int(pieces[3]) + int(pieces[8]))
                    while(index < length ):

                        if genome_change.has_key(index):
                            genome_change[index] = genome_change[index] + 1
                        else:
                            genome_change.__setitem__(index,1)

                        index += 1

        file += "fixedStep chrom=genome start=1 step=1 span=1\n"

        coverage = 0

        for i in genome_change:
            coverage = genome_change[i];
            file += str(coverage)+"\n"

        print "Saving cigar.wig file..."
        targetF = open("cigar.wig","w")
        targetF.truncate()
        targetF.write(file)
        targetF.close()
        print("Done!")