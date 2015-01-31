from . import ALL, ALL_NON_GENERAL_BIGRAMS
import count
import sum
import max

REAL_POSITIVE_POLARITY = 1
REAL_NEGATIVE_POLARITY = 0
NOMINAL_POSITIVE_POLARITY = 'positive'
NOMINAL_NEGATIVE_POLARITY = 'negative'


def start(bow_sentences,
          bow_sentences_ground_polarity,
          count_features=True,
          sum_features=True,
          max_features=True,
          unigrams=True,
          unigrams_ratio=True,
          unigram_type=ALL,
          non_general_unigrams_and_bigrams=True,
          non_general_unigrams_and_bigrams_ratio=True,
          non_general_bigram_type=ALL_NON_GENERAL_BIGRAMS,
          ngrams_count=True,
          general_unigrams_and_bigrams=True,
          general_unigrams_and_bigrams_ratio=True,
          unigrams_and_bigrams_trigram=True,
          unigrams_and_bigrams_trigram_ratio=True):

    features_list = []
    if count_features:
        features_list = features_list + count.all(bow_sentences,
                                                  unigrams_only=unigrams,
                                                  unigrams_only_ratio=unigrams_ratio,
                                                  unigram_type=unigram_type,
                                                  non_general_unigrams_and_bigrams=non_general_unigrams_and_bigrams,
                                                  non_general_unigrams_and_bigrams_ratio=non_general_unigrams_and_bigrams_ratio,
                                                  non_general_bigram_type=non_general_bigram_type,
                                                  ngrams_count=ngrams_count,
                                                  general_unigrams_and_bigrams=general_unigrams_and_bigrams,
                                                  general_unigrams_and_bigrams_ratio=general_unigrams_and_bigrams_ratio,
                                                  unigrams_and_bigrams_trigram=unigrams_and_bigrams_trigram,
                                                  unigrams_and_bigrams_trigram_ratio=unigrams_and_bigrams_trigram_ratio)

    if sum_features:
        features_list = features_list + sum.all(bow_sentences,
                                                unigrams=unigrams,
                                                unigrams_ratio=unigrams_ratio,
                                                unigram_type=ALL,
                                                non_general_unigrams_and_bigrams=non_general_unigrams_and_bigrams,
                                                non_general_unigrams_and_bigrams_ratio=non_general_unigrams_and_bigrams_ratio,
                                                non_general_bigram_type=non_general_bigram_type,
                                                general_unigrams_and_bigrams=general_unigrams_and_bigrams,
                                                general_unigrams_and_bigrams_ratio=general_unigrams_and_bigrams_ratio,
                                                unigrams_and_bigrams_trigram=unigrams_and_bigrams_trigram,
                                                unigrams_and_bigrams_trigram_ratio=unigrams_and_bigrams_trigram_ratio)

    if max_features:
        features_list = features_list + max.all(bow_sentences,
                                                unigrams=unigrams,
                                                unigram_type=ALL,
                                                non_general_unigrams_and_bigrams=non_general_unigrams_and_bigrams,
                                                non_general_bigram_type=non_general_bigram_type,
                                                general_unigrams_and_bigrams=general_unigrams_and_bigrams,
                                                unigrams_and_bigrams_trigram=unigrams_and_bigrams_trigram)

    attributes = []
    data = []

    for fl in features_list:
        attributes.append((fl['name'], 'REAL'))
        data.append(fl['value'])

    polarity_type = 'REAL'
    if type(bow_sentences_ground_polarity) == str:
        polarity_type = ['positive','negative']

    attributes.append(('polarity', polarity_type))
    data.append(bow_sentences_ground_polarity)

    return {'attributes': attributes, 'data': data}
