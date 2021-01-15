import random
import Bin
import Weight 
import Population
import DNA
import pandas as pd
import csv
sample = [263.78, 212.59, 244.1, 248.03]

class Optimizador(object):
    def __init__(self, sample_stocks):
        self.sampleStocks = sample_stocks

    def use_sample(self):
        sample_stocks = [12]
        sample_weights = [2, 2, 3, 3, 3, 3, 4, 4, 4, 6, 7, 7]
        return sample_weights, sample_stocks,

    def use_real_sample(self):
        sample_weights = []
        sample_stocks = [263.78, 212.59, 244.1, 248.03]
        #sample_stocks = [244.1]
        my_file = pd.read_excel("D:/python/1dStockCutting/prueba_py_005.xls", "OPT")
        i = 0
        refName = my_file["REFERENCIA"][0]
        for i in range(len(my_file["LONGITUD"])):
            for eachQty in range(my_file["CANTIDAD"][i]):
                sample_weights.append(my_file["LONGITUD"][i])
        return sample_weights, sample_stocks, refName


    def optimizar(self, aluRef, aluListWeights):
        popMax = 100
        population = Population.Population(popMax, aluListWeights, self.sampleStocks)
        population.create_population()
        for i in range(100):
            population.natural_selection()
            population.generate()
            population.save_best_one()        
            print("calculating...")
        population.print_the_best(aluRef)

