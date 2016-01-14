from base.BaseAlgorithm import BaseAlgorithm
import sys
import string
import os
import errno

class SequenceCoverageAlgorithm(BaseAlgorithm):

    leght = 0;

    def __init__(self, name, path):
        BaseAlgorithm.__init__(self, name, path)
        self.lenght = 0