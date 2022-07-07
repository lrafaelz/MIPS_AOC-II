import math
import mainMemory as memory

bit = 1
byte = 8
Kbyte = 1024

validateBit = 1
LRUbit = 1

# Initial conditions
userSize = 32*bit
ways = 8
word = 4
wordPerBlock = 16
address = 64*bit

# Offsets
byteOffset = math.log(word, 2)
wordOffset = math.log(wordPerBlock, 2)

# Index & tag
block = wordPerBlock*word
setSize = ways*block
sets = userSize*Kbyte / setSize
index = math.log(sets, 2)
tag = address - index - wordOffset - byteOffset

# Total size
overheadperblock = tag + validateBit + LRUbit
overheadPerSet = overheadperblock * ways
cacheOverhead =  overheadPerSet * sets
totalSize = ((cacheOverhead/byte)/Kbyte) + userSize
print("Total size of cache: " + str(totalSize) + "KB\nTotal size of overhead: " + str((cacheOverhead/byte)/Kbyte) + "KB")

memory.DRAM(sets, setSize)