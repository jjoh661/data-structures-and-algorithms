# O(n) time | O(1) space - where n is the length of the array
def isValidSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)

array1 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence1 = [1, 6, -1, 10]

print(isValidSubsequence(array1, sequence1))
