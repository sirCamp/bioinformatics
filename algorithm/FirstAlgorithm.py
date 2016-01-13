from base.BaseAlgorithm import BaseAlgorithm

class FirstAlgorithm(BaseAlgorithm):

    def __init__(self, name, path):
        BaseAlgorithm.__init__(self, name, path)

    def run(self):
        genome_lenght  = 0
        with open(self.path) as file:
            for line in file:
                genome_lenght += 1
                if genome_lenght == 7:
                    exit(0)

                if line.find("@") != -1:
                    continue;

                pieces = line.split("\t")
                print len(pieces)

