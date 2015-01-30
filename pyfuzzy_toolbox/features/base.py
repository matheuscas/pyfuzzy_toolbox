from . import ALL, ALL_NON_GENERAL_BIGRAMS
import count


def start(bow_sentences,
          bow_sentences_ground_polarity=1,
          count_features=True,
          unigrams_only=True,
          unigrams_only_ratio=True,
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
                                                  unigrams_only=unigrams_only,
                                                  unigrams_only_ratio=unigrams_only_ratio,
                                                  unigram_type=unigram_type,
                                                  non_general_unigrams_and_bigrams=non_general_unigrams_and_bigrams,
                                                  non_general_unigrams_and_bigrams_ratio=non_general_unigrams_and_bigrams_ratio,
                                                  non_general_bigram_type=non_general_bigram_type,
                                                  ngrams_count=ngrams_count,
                                                  general_unigrams_and_bigrams=general_unigrams_and_bigrams,
                                                  general_unigrams_and_bigrams_ratio=general_unigrams_and_bigrams_ratio,
                                                  unigrams_and_bigrams_trigram=unigrams_and_bigrams_trigram,
                                                  unigrams_and_bigrams_trigram_ratio=unigrams_and_bigrams_trigram_ratio)

    attributes = []
    data = []

    for fl in features_list:
        attributes.append((fl['name'], 'REAL'))
        data.append(fl['value'])

    return {'attributes': attributes, 'data': data}
