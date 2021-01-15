import Weight

class Bin(object):
    def __init__(self, id_, size):
        self.id = id_
        self.size = size
        self.remainingSize = size
        self.listOfWeights = []
    
    def addWeight(self, weight):
        # we add weights to our bin and calculate the remaining capacity
        self.listOfWeights.append(weight)
        self.remainingSize -= weight.weight_size

    def __str__(self):
        return 'size of the bin: {}, id of the bin: {}, remainin capacity: {}'.format(self.size, self.id, self.remainingSize)

         
    

