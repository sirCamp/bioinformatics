class BaseAlgorithm(object):

    name = ""
    path = ""

    def __init__(self, name, path):
        self.name = name
        self.path = path


    def getName(self):
        return self.name

    def run(self):
        return None