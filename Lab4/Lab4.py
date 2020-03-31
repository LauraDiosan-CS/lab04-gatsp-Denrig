from Utils import *
from GA import *

#problParam=test1('hugeMatrix.txt')
problParam=readMatrix("hardE.txt")
problParam['function']=lenPath
gaParam = {'popSize' : 150, 'noGen' : 200, 'pc' : 0.8, 'pm' : 0.1}

ga = GA(gaParam, problParam)
ga.initialisation()
ga.evaluation()

solution=None
bestFitness=99999999999999

for g in range(gaParam['noGen']):
        ga.oneGeneration()
        bestChromo = ga.bestChromosome()
        if(bestChromo.fitness<bestFitness):
            bestFitness=bestChromo.fitness
            solution=bestChromo
        print(str(bestChromo))
print("Best Chromo in all generations",solution)

