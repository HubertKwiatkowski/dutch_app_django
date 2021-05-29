import os
import csv
import random


csvFilePath = os.path.join('.', 'quiz', 'data', 'vocabulary.csv')
vocabulary = []

def openCsv():
    """Read csv file with all words."""
    with open(csvFilePath) as csvf:
        readCsv = csv.reader(csvf)
        csvRow = next(readCsv)
        for line in readCsv:
            vocabulary.append(line)

    return vocabulary


def singleWord():
    """Generate a single word to learn at random."""

    voc = openCsv()
    word = random.sample(voc, 1)
    
    return word