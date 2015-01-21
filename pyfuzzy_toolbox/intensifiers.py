from textblob import Word
from textblob.wordnet import ADV
from addict import Dict
import networkx as nx
import json

# Intensifiers and Downtoners - From Taboada et al. (2011)

# -- Seeds

# Intensifiers | Modifiers (%50)
# slightly | -50 -> LOWEST
# somewhat | -30 -> VERY LOW
# pretty | -10 -> LOW
# really | +15 -> HIGH
# very | +25 -> VERY HIGH
# extraordinarily | +50 -> HIGHEST
# (the) most | +100 -> MOST HIGHEST

intensifiers = Dict()
intensifiers.low.seed = 'pretty'
intensifiers.low.words = []
intensifiers.low.modifier = -10

intensifiers.very_low.seed = 'somewhat'
intensifiers.very_low.words = []
intensifiers.very_low.modifier = -30

intensifiers.lowest.seed = 'slightly'
intensifiers.lowest.words = []
intensifiers.lowest.modifier = -50

intensifiers.high.seed = 'really'
intensifiers.high.words = []
intensifiers.high.modifier = 15

intensifiers.very_high.seed = 'very'
intensifiers.very_high.words = []
intensifiers.very_high.modifier = 25

intensifiers.highest.seed = 'extraordinarily'
intensifiers.highest.words = []
intensifiers.highest.modifier = 50

intensifiers.most_highest.seed = 'most'
intensifiers.most_highest.words = []
intensifiers.most_highest.modifier = 100

intensifiers.unknown = []


def expand_words():
    list_of_adverbs = open('resources/adverbs/list_of_adverbs_and_wordnet.txt')
    G = read_adverbs_graph()
    greater_similarity_key = None
    greater_similarity_value = -1
    seeds = [intensifiers.low.seed, intensifiers.very_low.seed,
             intensifiers.lowest.seed, intensifiers.high.seed,
             intensifiers.very_high.seed, intensifiers.highest.seed,
             intensifiers.most_highest.seed]

    # log = open('log.txt', 'w')
    for adverb in list_of_adverbs.readlines():
        adv = adverb.strip()
        if adv not in seeds:
            greater_similarity_key = 'low'
            greater_similarity_value = multiple_adverbs_similarity(
                G, adv, [intensifiers.low.seed] + intensifiers.low.words)

            # log.write('adv: ' + adv + ' - seed + words: ' +
            #           str([intensifiers.low.seed] + intensifiers.low.words) + ' ### greater_similarity_key: ' + greater_similarity_key +
            #           ' - greater_similarity_value: ' + str(greater_similarity_value) + '\n')

            very_low_distance = multiple_adverbs_similarity(
                G, adv, [intensifiers.very_low.seed] + intensifiers.very_low.words)
            if greater_similarity_value == -1 or \
                    (greater_similarity_value > 0 and
                     (very_low_distance < greater_similarity_value and
                      very_low_distance != -1)):

                greater_similarity_value = multiple_adverbs_similarity(
                    G, adv, [intensifiers.very_low.seed] + intensifiers.very_low.words)
                greater_similarity_key = 'very_low'

                # log.write('adv: ' + adv + ' - seed + words: ' +
                #           str([intensifiers.very_low.seed] + intensifiers.very_low.words) + ' ###  greater_similarity_key: ' + greater_similarity_key +
                #           ' - greater_similarity_value: ' + str(greater_similarity_value) + '\n')

            lowest_distance = multiple_adverbs_similarity(
                G, adv, [intensifiers.lowest.seed] + intensifiers.lowest.words)
            if greater_similarity_value == -1 or \
                    (greater_similarity_value > 0 and
                     (lowest_distance < greater_similarity_value and
                      lowest_distance != -1)):

                greater_similarity_value = lowest_distance
                greater_similarity_key = 'lowest'

                # log.write('adv: ' + adv + ' - seed + words: ' +
                #           str([intensifiers.lowest.seed] + intensifiers.lowest.words) + ' ### greater_similarity_key: ' + greater_similarity_key +
                #           ' - greater_similarity_value: ' + str(greater_similarity_value) + '\n')

            high_distance = multiple_adverbs_similarity(
                G, adv, [intensifiers.high.seed] + intensifiers.high.words)
            if greater_similarity_value == -1 or \
                    (greater_similarity_value > 0 and
                     (high_distance < greater_similarity_value and
                      high_distance != -1)):

                greater_similarity_value = high_distance
                greater_similarity_key = 'high'

                # log.write('adv: ' + adv + ' - seed + words: ' +
                #           str([intensifiers.high.seed] + intensifiers.high.words) + ' ### greater_similarity_key: ' + greater_similarity_key +
                #           ' - greater_similarity_value: ' + str(greater_similarity_value) + '\n')

            very_high_distance = multiple_adverbs_similarity(
                G, adv, [intensifiers.very_high.seed] + intensifiers.very_high.words)
            if greater_similarity_value == -1 or \
                    (greater_similarity_value > 0 and
                     (very_high_distance < greater_similarity_value and
                      very_high_distance != -1)):

                greater_similarity_value = very_high_distance
                greater_similarity_key = 'very_high'

                # log.write('adv: ' + adv + ' - seed + words: ' +
                #           str([intensifiers.very_high.seed] + intensifiers.very_high.words) + ' ### greater_similarity_key: ' + greater_similarity_key +
                #           ' - greater_similarity_value: ' + str(greater_similarity_value) + '\n')

            highest_distance = multiple_adverbs_similarity(
                G, adv, [intensifiers.highest.seed] + intensifiers.highest.words)
            if greater_similarity_value == -1 or \
                    (greater_similarity_value > 0 and
                     (highest_distance < greater_similarity_value and
                      highest_distance != -1)):

                greater_similarity_value = highest_distance
                greater_similarity_key = 'highest'

                # log.write('adv: ' + adv + ' - seed + words: ' +
                #           str([intensifiers.highest.seed] + intensifiers.highest.words) + ' ### greater_similarity_key: ' + greater_similarity_key +
                #           ' - greater_similarity_value: ' + str(greater_similarity_value) + '\n')

            most_highest_distance = multiple_adverbs_similarity(
                G, adv, [intensifiers.most_highest.seed] + intensifiers.most_highest.words)
            if greater_similarity_value == -1 or \
                    (greater_similarity_value > 0 and
                     (most_highest_distance < greater_similarity_value and
                      most_highest_distance != -1)):

                greater_similarity_value = most_highest_distance
                greater_similarity_key = 'most_highest'

                # log.write('adv: ' + adv + ' - seed + words: ' + str(
                #     [intensifiers.most_highest.seed] + intensifiers.most_highest.words) + ' ### greater_similarity_key: ' + greater_similarity_key +
                #     ' - greater_similarity_value: ' + str(greater_similarity_value) + '\n')

            if greater_similarity_key is not None and greater_similarity_value != -1:
                intensifiers[greater_similarity_key].words.append(adv)
                # log.write('ADDED adv: ' + adv + ' ### greater_similarity_key: ' + greater_similarity_key +
                #           ' - greater_similarity_value: ' + str(greater_similarity_value) + '\n')
            else:
                intensifiers.unknown.append(adv)
                # log.write('UNKNOWN adv: ' + adv + '\n')

        # log.write(
        #     '----------------------------------------------------------------------------- \n')
    with open('intensifiers.json', 'w') as adv_file:
        json.dump(intensifiers.to_dict(), adv_file,
                  sort_keys=True, indent=4, separators=(',', ': '))


def create_adverbs_graph(format='graphml'):
    G = nx.Graph()
    list_of_adverbs = open('resources/adverbs/list_of_adverbs_and_wordnet.txt')
    for adverb in list_of_adverbs.readlines():
        adv = adverb.strip()
        adv_synsets = Word(adv).get_synsets(pos=ADV)
        G.add_node(adv)
        for synset in adv_synsets:
            word = synset._name.split('.')[0]
            sense = synset._name.split('.')[2]
            if word != adv:
                G.add_edge(adv, word, weight=int(sense))

    nx.write_graphml(G, "resources/adverbs/wordnet_adverbs_graph.graphml")


def read_adverbs_graph(format='graphml'):
    return nx.read_graphml("resources/adverbs/wordnet_adverbs_graph.graphml")


def simple_adverbs_similarity(G, source, target):
    length_similarity = -1
    try:
        length_similarity = nx.dijkstra_path_length(
            G, source, target, weight='weight')
    except:
        pass
    return length_similarity


def multiple_adverbs_similarity(G, source, list_of_targets, evaluation='sum'):
    length_similarities = []
    for target in list_of_targets:
        length_similarity = simple_adverbs_similarity(G, source, target)
        if length_similarity > 0:
            length_similarities.append(length_similarity)

    if len(length_similarities) == 0:
        return -1

    if evaluation == 'sum':
        return sum(length_similarities)
    else:
        return min(length_similarities)
