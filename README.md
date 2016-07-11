# Merging DNA Fragments

### How to run
```
python main.py <FASTA input file> <Sequence output file>
```
See sample output in `data/fasta_output.txt`.

### How it works
*Step 1*: Build a directed graph going from fragment to fragment. Fragment A points to Fragment B if A can validly preceed B.

*Step 2*: Perform a topological sort on our graph to get the fragments in order.

*Step 3*: Write sorted fragments to a file.

### Assumptions
1. If 2 sequences overlap by more than half of either sequence, then they are sequential.
2. There is only one unique way to order the DNA sequence fragments.
3. There are no input sequence of less than 1/2 the length of the next smallest sequence.

*Note*: The code as written has the benefit of checking our assumptions and making sure that the input data holds follows those assumptions, specifically Assumption #2. If there is more than one way to sequence our fragments, then the code will warn us and throw an exception.
