import random

ebeveyin1 = [1,4,5,2,7,3,6]

potansiyelEbeveyinler = [([3, 1, 7, 2, 6, 4, 5], 3),
                         ([5, 7, 1, 4, 3, 2, 6], 2),
                         ([6, 4, 2, 7, 5, 1, 3], 1)]


def tournament_selection(potansiyelEbeveyinler, tournament_size=2):

    increment = 0
    increment1 = 1

    for i in range(len(potansiyelEbeveyinler)):
        if potansiyelEbeveyinler[increment][1] > potansiyelEbeveyinler[increment1][1]:
            ebeveyin2 = potansiyelEbeveyinler[increment][0]
        elif potansiyelEbeveyinler[increment][1] < potansiyelEbeveyinler[increment1][1]:
            ebeveyin2 = potansiyelEbeveyinler[increment1][0]
        else:

            choice_list = [potansiyelEbeveyinler[increment][0], potansiyelEbeveyinler[increment1][0]]
            ebeveyin2 = random.choice(choice_list)

        increment += 1
        increment1 += 1

        return ebeveyin2

ebeveyin2 = tournament_selection(potansiyelEbeveyinler, tournament_size=2)

def crossover(ebeveyin1, ebeveyin2,çaprazlamaNoktası=3):
    gen1 = ebeveyin1[:çaprazlamaNoktası]
    gen2 = ebeveyin2[çaprazlamaNoktası:]
    çocuk = gen1 + gen2
    return çocuk

çocuk = crossover(ebeveyin1, ebeveyin2, çaprazlamaNoktası=3)
def mutate(çocuk, mutation_rate=0.05):
    if random.random() < mutation_rate:
        değişenGenSayı1 = random.randint(0, len(çocuk) - 1)
        değişenGenSayı2 = random.randint(0, len(çocuk) - 1)

        while değişenGenSayı1 == değişenGenSayı2:
            değişenGenSayı2 = random.randint(0, len(çocuk) - 1)

        çocuk[değişenGenSayı1], çocuk[değişenGenSayı2] = çocuk[değişenGenSayı2], çocuk[değişenGenSayı1]

    return çocuk

çocuk = mutate(çocuk, mutation_rate=0.05)

print(f"1.ebeveyin: {ebeveyin1} ")
print(f"2.ebeveyin: {ebeveyin2}")
print(f"çocuk: {çocuk}")