# 1DStockCutter
  -------------

this is a one-dimensional bin optimizer that uses a genetic algorithm to find the best combination possible of arrangement for the items.

To use it, you need python: run the "main" script through the console, specify as requested the path where your excel document is, and with a size of stock lenght you will optimize for.

your excel document must have the following headers:
* "REFERENCIA": that is the name of the bar you are optimizing
* "LONGITUD" : that is the lenght of the bar you are optimizing
* "CANTIDAD": that is the quantity of the bar you are optimizing

this is an example of how the document must be arranged:

![alt text](https://github.com/colmenaresw/1DStockCutter/blob/main/1DstockImages/Captura1.JPG)

Finally, the script will generate two csv documents:

1. optimization: this is where your final optimization is
2. performance: this is where data related to your optimization is, such as: total lenght used, total remaining, performance.

Thanks to: 
* **the nature of code: Daniel Shiffman**
* **A Hybrid Grouping Genetic Algorithm for Bin Packing by Emanuel Falkenauer**
