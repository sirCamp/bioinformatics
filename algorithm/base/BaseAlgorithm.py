import os

class BaseAlgorithm(object):

    name = ""
    path = ""
    length = 0;

    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.length = 0


    def getName(self):
        return self.name

    def run(self):
        return None

    def lengthOfCoverage(self):
        os.system('clear')

        print "Please insert the desidered length of sequence coverage ( leave empty for wole genome ) :"
        print "\n"
        inputVal = raw_input(">>  ")
        try:
            if inputVal == "":

                infile = open(self.path, 'r')
                headers = infile.readline().split("\t")
                lengths = headers[2].split(":")
                self.length = int(lengths[1])
            else:
                print inputVal
                self.length = int(inputVal)
        except ValueError:
           print("Error, you must pass a number")
           self.lengthOfCoverage()

        print "The slected Genome lenght is: "+str(self.length)