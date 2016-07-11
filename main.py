from Sequence import Sequence
from Graph import Graph
from topsort import topsort
import sys

def main(infileName, outfileName):
    sequences = buildSequences(infileName)
    graph, indexMap = buildGraph(sequences)
    sortedSequence = topsort(graph)
    writeSequenceToFile(sortedSequence, indexMap, outfileName)

def buildSequences(infileName):
    sequences = []
    currentSeq = None
    currentName = None

    with open(infileName, 'r') as infile:
        for line in infile.readlines():
            if '>' in line:
                if currentSeq != None:
                    sequences.append(Sequence(currentName, currentSeq))
                currentName = line.strip('>').strip('\n')
                currentSeq = ''
            else:
                currentSeq = currentSeq + line.strip('\n')
        if currentSeq != None:
            sequences.append(Sequence(currentName, currentSeq))
    return sequences

def buildGraph(sequences):
    graph = Graph()
    indexMap = {}
    for seq in sequences:
        for otherSeq in sequences:
            if seq.name == otherSeq.name:
                continue
            index = seq.canPreceed(otherSeq)
            if index != -1:
                graph.addEdge(seq, otherSeq)
                indexMap[(seq.name, otherSeq.name)] = index
    return (graph, indexMap)

def writeSequenceToFile(sortedList, indexMap, outfileName):
    dna = ''
    for i in range(len(sortedList)-1):
        seq = sortedList[i]
        nextSeq = sortedList[i+1]
        dna = dna + seq.sequence[:indexMap[(seq.name, nextSeq.name)]]
    dna = dna + sortedList[-1].sequence
    print dna
    with open(outfileName, 'w') as outfile:
        outfile.write(dna)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
