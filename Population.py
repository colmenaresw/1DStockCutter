import random
import Bin
import Weight
import DNA 

class Population(object):
    def __init__(self, sizeOfPopulation, theWeights, theStocks):
        self.sizeOfPopulation = sizeOfPopulation
        self.listOfIndividuals = []
        self.newGeneration = []
        self.matingPool = []
        self.indexedWeights = []
        self.theWeights = theWeights
        self.theStocks = theStocks
        self.listOfPerformance = []
        self.listOfBestByGeneration = []

    def create_population(self):  # here we give to our population the initial state
        self.weight_generator(self.theWeights)
        for i in range(self.sizeOfPopulation):
            random.shuffle(self.indexedWeights)            
            newBorn = DNA.DNA(self.indexedWeights, self.theStocks)
            newBorn.calculate_performance()    
            self.listOfIndividuals.append(newBorn)

    def weight_generator(self, some_weights):
        for i in range(len(some_weights)):
            self.indexedWeights.append(Weight.Weight(some_weights[i], 1000 + i))        

    def natural_selection(self):
        self.matingPool.clear()
        bestOnes = sorted(self.listOfIndividuals, reverse=True, key= lambda x: x.performance)
        for indi in range(len(bestOnes)):
            normal = ((bestOnes[indi].performance - 1) / (bestOnes[0].performance - 1)) * 100
            for n in range(int(normal)):
                self.matingPool.append(bestOnes[indi])

    def generate(self):
        self.listOfIndividuals.clear()
        for individual in range(self.sizeOfPopulation):
            theChild = DNA.DNA()
            parentA = random.choice(self.matingPool)
            parentB = random.choice(self.matingPool)
            theChild.crossover(parentA, parentB)
            theChild.mutate(self.indexedWeights, self.theStocks)
            theChild.calculate_performance()
            self.listOfIndividuals.append(theChild)

    def best_one(self):
        self.listOfPerformance.clear()
        for eachIndividual in self.listOfIndividuals:
            self.listOfPerformance.append(eachIndividual.performance)
        self.listOfPerformance.sort()
        print(self.listOfPerformance[0])
        return self.listOfPerformance[0]

    def save_best_one(self):
        bestOne = sorted(self.listOfIndividuals, reverse=True, key= lambda x: x.performance)
        self.listOfBestByGeneration.append(bestOne[-1])
        
    
    def print_the_best(self, refName):
        bestOne = sorted(self.listOfBestByGeneration, reverse=True, key= lambda x: x.performance)
        print("your performance was: " + str(bestOne[-1].performance))
        bestOne[-1].write_the_csv(refName)
        bestOne[-1].write_the_performance(refName)

        


        