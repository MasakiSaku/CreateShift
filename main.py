import random

from deap import base
from deap import creator
from deap import tools

class Person(object):
    def __init__(self,no,name,time,TakeOff):
        #従業員の番号、あんまり必要ないかも？
        self.no = no
        self.name = name
        #出勤の時間帯、0が朝、１が昼、２が夜
        self.time = time
        #希望休
        self.TakeOff = TakeOff
    
    def get_TakeOff(self):
        return self.TakeOff
    
    def get_time(self):
        return self.time


#適応度の適宜
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
#個体の定義
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
#遺伝子を作成する関数
toolbox.register("attr_bool", random.randint, 0, 1)
#個体を作成する関数
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, 100)
#世代を生成する関数
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

#評価関数
def evalOneMax(individual):
    return sum(individual),

toolbox.register("evaluate", evalOneMax)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)


def main():
    #従業員の情報
    e0 = Person(0,"mg",[0,1],[23,30,20])
    e1 = Person(1,"mi",[0],[25,4])
    e2 = Person(2,"sm",[0,1],[])
    e3 = Person(3,"nd",[0,1],[])
    e4 = Person(4,"ms",[0],[29,5,20])
    e5 = Person(5,"me",[2],[22,23,27,30,31,1,2,3,4,5,6,7])

    employees = [e0,e1,e2,e3,e4,e5]

    #random.seed(64)

    #300個体生成
    pop = toolbox.population(n=300)

    #交叉率、突然変異率
    CXPB, MUTPB = 0.5, 0.2

    print("Start of evolution")

    #初期世代の個体の適応度
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    print("  Evaluated %i individuals" % len(pop))

    #全ての個体の適応度のリスト
    fits = [ind.fitness.values[0] for ind in pop]

    g = 0

    while max(fits) < 100 and g < 1000:
        g = g + 1
        print("-- Generation %i --" % g)

        offspring = toolbox.select(pop, len(pop))
        offspring = list(map(toolbox.clone, offspring))

        for child1, child2 in zip(offspring[::2], offspring[1::2]):

            if random.random() < CXPB:
                toolbox.mate(child1, child2)

                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:

            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        print("  Evaluated %i individuals" % len(invalid_ind))

        pop[:] = offspring

        fits = [ind.fitness.values[0] for ind in pop]

        length = len(pop)
        mean = sum(fits) / length
        sum2 = sum(x*x for x in fits)
        std = abs(sum2 / length - mean**2)**0.5

        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))
        print("  Avg %s" % mean)
        print("  Std %s" % std)

    print("-- End of (successful) evolution --")

    best_ind = tools.selBest(pop, 1)[0]
    print("Best individual is %s, %s" % (best_ind, best_ind.fitness.values))


if __name__ == '__main__':
    main()