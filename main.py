# the main goal here is to: from one file create an optimization of each
# aluminum reference

import pandas as pd
import Optimizador as opt
import os

try:
    os.remove("optimization.csv")
    os.remove("performance.csv")
except:
    pass


my_route = input("please specify the path of your document: ")
input_stocks = float(input("please specify your bin stocklenght: "))
my_file = pd.read_excel(my_route, "OPT")
sample_stocks = []
sample_stocks.append(input_stocks)
theOptimizer = opt.Optimizador(sample_stocks)
sample_weights = []


for i in range(len(my_file["REFERENCIA"])):    
    try:
        for eachQty in range(my_file["CANTIDAD"][i]):
            sample_weights.append(my_file["LONGITUD"][i])

        if (my_file["REFERENCIA"][i] != my_file["REFERENCIA"][i + 1]):
            ref = my_file["REFERENCIA"][i]
            theOptimizer.optimizar(ref, sample_weights)
            print("split")
            sample_weights.clear()        
    except:
        if sample_weights != []:
            ref = my_file["REFERENCIA"][i]
            theOptimizer.optimizar(ref, sample_weights)
        print("finished")

#print(my_file["REFERENCIA"])