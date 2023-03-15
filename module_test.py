class WorkCost:
    def __init__(self, time):
        self.time = time

# class Type(Enum):
#     NONE = 0
#     A = 1
#     B = 2

# class Process(Type, WorkCost):
#     def __init__(self, ID):
#         self.ID = ID


class Machine:
    def __init__(self, processCanDo, name, waitQueue, time):
        self.processCanDo = processCanDo
        self.name = name
        self.waitQueue = waitQueue
        self.time = time

# class ProcessIndex(Type):
#     def __init__(self, order, current, process):
#         self.order = order
#         self.current = current
#         self.process = process

class Order:
    def __init__(self, end, current, time):
        self.end = end
        self.current = current
        self.time = time

# class Gene(ProcessIndex):
#     def __init__(self, machine):
#         self.machine = machine

class Chromosome:
    def __init__(self, gene, rfitness, cfitness, fitness):
        self.gene = gene
        self.rfitness = rfitness
        self.cfitness = cfitness
        self.fitness = fitness


class Population(Chromosome):
    pass

class Type:
    Type = {'NONE':0, 'A':1, 'B':2}
class Test:
    def __init__(self, a = Type()):
        self.a = a

        

if __name__ == '__main__':
    ts = Test()
    print(ts.a.Type['A'])