# the DNA in this case is a list of bins
import Bin
import random
import Weight
import csv

class DNA(object):
    def __init__(self, weights = 0, stocks = []):
        self.listOfBins = []
        self.performance = 0
        self.tempWeightList = []
        self.lineOfText = 0
        self.totalRemaining = 0
        self.totalBins = 0
        if len(stocks) > 0:
            self.born(weights, stocks)
    
    def crossover(self, theFather, theMother):
        
        midpoint = round(len(theFather.listOfBins) / 2, 0)
        for point in range(int(midpoint)):
            self.listOfBins.append(theFather.listOfBins[point])        

        # we make a list of indexed weight already existing within the child
        self.calculate_currrent_weights()

        # now we check if the current mother bin has no weight repetition with the child
        for eachBin in theMother.listOfBins:
            repetition = False
            for eachWeight in eachBin.listOfWeights:
                if eachWeight.id in self.tempWeightList:
                    repetition = True
                    break
            if not(repetition):
                self.listOfBins.append(eachBin)      

    def calculate_currrent_weights(self):
        # we calculate the current weights that are existing within the DNA
        self.tempWeightList.clear()
        for eachBin in self.listOfBins:
            for eachWeight in eachBin.listOfWeights:
                self.tempWeightList.append(eachWeight.id)
        return None        

    def mutate(self, indexedWeights, stocks):
        self.listOfBins.pop(-1)
        remainingWeights = []
        # we check if there's is any indexed weight out of the child's bins
        self.calculate_currrent_weights()
        for eachIndexedWeight in indexedWeights:
            if not(eachIndexedWeight.id in self.tempWeightList):
                remainingWeights.append(eachIndexedWeight)
        
        # now we fill bins with the remaining weights if applicable
        self.born(remainingWeights, stocks) 
    
    def born(self, indexedWeights, allowedStocks):
        # we create a new DNA individual which will contain a list of filled bins and a
        # performance        
        usedBins = []  # a list of Bin objects
        randomSortedWeights = indexedWeights
        random.shuffle((randomSortedWeights))
        for randomWeight in randomSortedWeights:
            isIn = False
            while not isIn:
                # first we check if we can fit the weight into an existing bin
                if len(usedBins) > 0:
                    for bin_index in range(len(usedBins)):
                        if usedBins[bin_index].remainingSize >= randomWeight.weight_size:
                            usedBins[bin_index].addWeight(randomWeight)
                            isIn = True
                            break
                if isIn:
                    break
                # if we could'nt fit in we create a new random bin a put our weight in
                # indexing this new used bin to our used bins list
                newBinSize = 0  # we make a new scratch bin
                while newBinSize < randomWeight.weight_size:  # we pick a random bin size until we find a one that is usefull
                    newBinSize = random.choice(allowedStocks)
                newBin = Bin.Bin(id_ = len(usedBins), size = newBinSize)
                newBin.addWeight(randomWeight)
                usedBins.append(newBin)
                isIn = True        
        
        # we fill the bins of our DNA
        for eachUsedBin in usedBins:
            self.listOfBins.append(eachUsedBin)         

    def calculate_performance(self):
        # with the list of bins of the DNA we calculate the performance of the subject
        self.totalRemaining = 0
        self.totalBins = 0
        for eachBin in self.listOfBins:
            self.totalRemaining += eachBin.remainingSize
            self.totalBins += eachBin.size
        self.performance = self.totalRemaining / self.totalBins
        return None

    def __str__(self):
        theFinalList = ""
        i = 0
        for eachBin in self.listOfBins:
            a = 'the current bin is: {}'.format(i)
            a2 = ' the bin size is: {}'.format(eachBin.size)
            for eachWeight in eachBin.listOfWeights:
                b = ' weight is: {}'.format(eachWeight.weight_size)
                c = ' its id is: {}'.format(eachWeight.id)
                theFinalList += " " + a + a2 + b + c + "\n"
            i += 1
        return theFinalList
    
    def write_the_csv(self, refName):
        theFinalList = [0, 1, 2, 3, 4]        
        i = 0
        with open('optimization.csv', 'a', newline = '') as new_file:
            csv_writer = csv.writer(new_file)
            if self.lineOfText == 0:
                field_names = ['bin id', 'bin size', 'bin weight', 'weight id', 'ref']            
                csv_writer.writerow(field_names)
            i = 0
            for eachBin in self.listOfBins:
                theFinalList[0] = i
                theFinalList[1] = eachBin.size
                for eachWeight in eachBin.listOfWeights:
                    theFinalList[2] = eachWeight.weight_size
                    theFinalList[3] = eachWeight.id
                    theFinalList[4] = refName
                    csv_writer.writerow(theFinalList)
                    self.lineOfText += 1
                i += 1

    def write_the_performance(self, refName):
        theFinalList = [0, 1, 2, 3]
        with open('performance.csv', 'a', newline = '') as new_file:
            csv_writer = csv.writer(new_file)            
            #if self.lineOfText == 0:
            field_names = ['total lenght used', 'total remaining', 'performance', 'reference']
            csv_writer.writerow(field_names)
            theFinalList[0] = self.totalBins
            theFinalList[1] = self.totalRemaining
            theFinalList[2] = self.performance
            theFinalList[3] = refName
            csv_writer.writerow(theFinalList)

            

            





         

