# 1DStockCutter
===============

this is one dimensional bin optimizer that uses a genetic algorithm to find the best combination posible of arragement for the stocks.

in order to use it, you need python: run the script through the console, specify as requested the path were your excel document is and with size of stocklenght you will optimize for.

your excel document must have the following headers:
* "REFERENCIA": that is the name of the bar you are optimizing
* "LONGITUD" : that is the lenght of the bar you are optimizing
* "CANTIDAD": that is the quantity of the bar you are optimizing

this is an example of how the document must be arranged:

![alt text](https://github.com/colmenaresw/1DStockCutter/blob/main/1DstockImages/Captura1.JPG)

Finally, the script will generate two csv documents:

1. optimization: this is where your final optimization is
2. performance: this is where data related to your optimization is, such as: total lenght used, total remaining, performance.


