from base.BaseAlgorithm import BaseAlgorithm

class PhysicalCoverageAlgorithm(BaseAlgorithm):

    leght = 0;

    def __init__(self, name, path):
        BaseAlgorithm.__init__(self, name, path)

    def run(self):

        self.lengthOfCoverage()
        genome_change = [0] * self.length

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

        file += "fixedStep chrom=genome start=1 step=1 span=1\n"
        currentC = 0

        for i in range:
            currentC += genome_change[i];
            file += str(currentC)+"\n"

        print "Saving to physical_coverage.wig "
        targetF = open("physical_coverage.wig","w")
        targetF.truncate()
        targetF.write(file)
        targetF.close()
        print("Done!")