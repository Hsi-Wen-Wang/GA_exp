import numpy as np
import csv
import random
import math

#----------------------------OK-----------------------------#
def randInt(min, max):
    x = random.randrange(0, 2147483647) % (max - min + 1)
    return x

#-----------------------------------------------------------#
Type = {'NONE':0, 'A':1, 'B':2}
class Test:
    NONE = 0
    A = 1
    B = 2

# class Test2(Test):
#     def __init__(self,  a, b):
        
#         self.a = a
#         self.b = b

# def randMachine(gene):
#     List = []
#     result = 0

#     List.clear()
    
#     for i in range(len(machineList)):
#         for j in range(len(machineList[i].processCanDo)):
#             if (machineList[i].processCanDo[j])
#     return 0


if __name__ == '__main__':
    ts = Test()
    
    a = [1, 2, 3]
    print()