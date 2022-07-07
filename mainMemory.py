import csv


class DRAM:
    def __init__(self, sets, setSize):
        mainMemorySets = []
        with open('memory/mainMemory.csv', 'w') as f:
            writer = csv.writer(f)
            for i in range(0, int(sets)):
                row = []
                for j in range(0, setSize):
                    row.append(0)
                writer.writerow(row)
                mainMemorySets.append(row)
    
    def writeDRAM(self, set, toWrite):
        self.mainMemorySets[set] = toWrite
    
    def readDRAM(self, set):
        return self.mainMemorySets[set]


# print(str(mainMemorySets) + '\n')
