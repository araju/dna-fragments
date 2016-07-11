class Sequence(object):
    """represents a DNA sequence"""
    def __init__(self, name, seq):
        self.name = name
        self.sequence = seq
        self.startHalf = seq[:len(seq)/2]
        self.endHalf = seq[len(seq)/2:]

    def canPreceed(self, otherSeq):
        # Ex. seq 1: BABCDA | FGHIJB
        # Ex. seq 2: DAFGHI | JBCDEF
        # look for first half of other seq in this.
        # if exists, then look for whatever comes after the half in this,
        # and make sure that the other seq's second half begins with those chars.
        # if not, return false
        idx = self.sequence.find(otherSeq.startHalf)
        if idx >= 0:
            remaining = self.sequence[idx + len(otherSeq.startHalf):]
            if otherSeq.endHalf.find(remaining) == 0:
                return idx
        return -1
