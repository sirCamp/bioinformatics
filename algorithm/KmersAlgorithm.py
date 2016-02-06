from base.BaseAlgorithm import BaseAlgorithm

class KmersAlgorithm(BaseAlgorithm):

    kmersL = 4
    kmerLabel = ""
    kmerMax = 0

    def __init__(self, name, path):
        BaseAlgorithm.__init__(self, name, path)

    def mapping(self, string):

        string = string.replace("A", "W")
        string = string.replace("T", "A")
        string = string.replace("W", "T")

        string = string.replace("C", "W")
        string = string.replace("G", "C")
        string = string.replace("W", "G")
        return string

    def kmersLength(self):
        print "Please insert the desidered length of the kmers ( leave empty to set default value 4 ) :"
        inputVal = raw_input(">>  ")
        try:
            if inputVal == "":
                self.kmersL = 4
            else:
                print inputVal
                self.kmersL = int(inputVal)
        except ValueError:
            print("Error, you must pass a number")

    def checker(self, max,label):
        if(max > self.kmerMax):
            self.kmerMax = max
            self.kmerLabel = label

    def run(self):

        self.lengthOfCoverage()

        self.kmersLength()
        #open the SAM file

        print "Open SAM file...\n"
        kmers = {}

        print "Looking for kmers and it's opposites for "+str(self.kmersL)+" bases long\n"
        with open(self.path) as file:
            for line in file:

                #exclude header lines
                if line.find("@") != -1:
                    continue;

                pieces = line.split("\t")

                read = str(pieces[9])
                padding = 0
                while len(read[padding:padding+self.kmersL]) >= self.kmersL:
                    key = read[padding:padding+self.kmersL]
                    padding += 1
                    # looking for the kmers
                    if kmers.has_key(key):
                        kmers[key] = kmers[key] +1
                        self.checker(kmers[key],key)
                    # looking for the opposite kmers
                    elif kmers.has_key(self.mapping(key)):
                            kmers[self.mapping(key)] = kmers[self.mapping(key)] +1
                            self.checker(kmers[self.mapping(key)],self.mapping(key))
                    # adding new kmers
                    else:
                        kmers.__setitem__(key,1)
                        self.checker(kmers[key],key)

        file = "kmer,quantity\n"
        for i in kmers:
            file += str(i)+","+str(kmers[i])+"\n"

        print "Saving kmers.csv file..."
        targetF = open("kmers.csv","w")
        targetF.truncate()
        targetF.write(file)
        targetF.close()
        print "The max present value is: "+str(self.kmerMax)+" for the kmer: "+self.kmerLabel+"\n"
        print("Done!")