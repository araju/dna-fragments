# infileName = 'data/fasta.txt'
# sequences = []
# currentSeq = None
#
# with open(infileName, 'r') as infile:
#     for line in infile.readlines():
#         if '>' in line:
#             if currentSeq != None:
#                 sequences.append(currentSeq)
#             currentSeq = ''
#         else:
#             currentSeq = currentSeq + line.strip('\n')
#
# for seq in sequences:
#     print len(seq)

from Sequence import Sequence

s1 = Sequence('s1','BABCDAFGHIJB')
s2 = Sequence('s2','DAFGHIJBCDEF')

print s1.canPreceed(s2)
print s1.canPreceed(s1)
print s2.canPreceed(s1)
