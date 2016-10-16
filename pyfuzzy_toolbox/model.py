import pymongo
import os
import abc
import string
from bson.objectid import ObjectId
from bson.code import Code


class BaseModel(object):

    """docstring for BaseModel class that represents and generic corpora in mongodb"""

    __metaclass__ = abc.ABCMeta

    def __init__(self, database_name, domain='localhost', port=27017):
        super(BaseModel, self).__init__()
        self.client = pymongo.MongoClient(domain, port)
        self.database_name = database_name
        self.database = self.client[database_name]
        self.documents = self.database.documents
        self.REDUCER = Code("""
                function (key, values) {
                  var total = 0;
                  for (var i = 0; i < values.length; i++) {
                    total += values[i];
                  }
                  return total;
                }
                """)

    @abc.abstractmethod
    def read_corpora_source(self):
        """This method should be implemented by each subclass that defines the way of reading each corpora.
        It must returns a list of dictionaries elements.
        """

        pass

    @abc.abstractmethod
    def create_database(self, qtd=None):
        """Creates the mongodb database and its documents"""

        pass

    def __is_field_exists(self, collection_name, field_name):
        collection = self.database[collection_name]
        for e in collection.find():
            for k in e.keys():
                if k == field_name:
                    return True
        return False

    def get_doc_by_name(self, doc_name, collection_name='documents'):
        return self.database[collection_name].find({'name': doc_name})[0]

    def get_doc_by_id(self, doc_id):
        return self.documents.find({'_id': ObjectId(doc_id)})[0]

    def create_or_update_collection_from_file(self, file_name, collection_name):
        """ File must have only a pair of values per line, separated by ; """

        f = open(file_name)
        collection = self.database[collection_name]
        for line in f.readlines():
            values = line.split('\n')[0]
            values = values.split(';')
            adverb = values[0]
            factor = values[1]
            collection.insert({'word': adverb, 'factor': factor})
        f.close()


class TripAdvisorModel(BaseModel):

    """docstring for TripAdvisorModel"""

    def __init__(self, database_name="TripAdvisor"):
        BaseModel.__init__(self, database_name)

    def read_corpora_source(self):

        source_5255 = os.path.abspath(
            os.curdir) + '/resources/corpora/trip_advisor/TripAdvisor_5255.txt'
        source_10508 = os.path.abspath(
            os.curdir) + '/resources/corpora/trip_advisor/TripAdvisor_10508.txt'
        source_file_5255 = open(source_5255, 'r')
        source_file_10508 = open(source_10508, 'r')

        list_of_dict_units = []

        for line in source_file_5255.readlines():
            parts = line.split()
            name = parts[0]
            degree = parts[len(parts) - 1]

            cons = parts[len(parts) - 2]
            cons = cons.decode('Windows-1252').encode('utf-8')

            pros = parts[len(parts) - 3]
            pros = pros.decode('Windows-1252').encode('utf-8')

            text = string.join(parts[1:len(parts) - 3])
            list_of_dict_units.append(
                {'name': name, 'text': text, 'degree': degree, 'pros': pros, 'cons': cons})

        for line in source_file_10508.readlines():
            parts = line.split()
            name = parts[0]
            degree = parts[len(parts) - 1]

            cons = parts[len(parts) - 2]
            cons = cons.decode('Windows-1252').encode('utf-8')

            pros = parts[len(parts) - 3]
            pros = pros.decode('Windows-1252').encode('utf-8')

            text = string.join(parts[1:len(parts) - 3])
            list_of_dict_units.append(
                {'name': name, 'text': text, 'degree': degree, 'pros': pros, 'cons': cons})

        return list_of_dict_units

    def create_database(self, qtd=None):

        docs = self.read_corpora_source()
        pos_count, neg_count = (qtd / 2, qtd / 2) if qtd else (0, 0)
        for d in docs:
            if qtd:
                if pos_count > 0 and int(d['degree']) > 3:
                    self.documents.insert(d)
                    pos_count = pos_count - 1

                if neg_count > 0 and int(d['degree']) < 3:
                    self.documents.insert(d)
                    neg_count = neg_count - 1

                if pos_count == 0 and neg_count == 0:
                    break
            else:
                self.documents.insert(d)

        # search for documents with NULL information and attaches the doc id to
        # turn the name unique
        for ndoc in self.documents.find():
            if 'NULL' in ndoc['name']:
                new_ndoc_name = ndoc['name'] + "_" + str(ndoc['_id'])
                self.documents.update(
                    {'_id': ndoc['_id']}, {'$set': {'name': new_ndoc_name}})


class CornellMoviesModel(BaseModel):

    """docstring for CornellMoviesModel"""

    def __init__(self, database_name="CornellMovies_v2"):
        BaseModel.__init__(self, database_name)

    def read_corpora_source(self):

        POS_DOCS_PATH = os.path.abspath(
            os.curdir) + '/pyfuzzy_toolbox/resources/corpora/cs_cornell_edu/txt_sentoken/pos'
        NEG_DOCS_PATH = os.path.abspath(
            os.curdir) + '/pyfuzzy_toolbox/resources/corpora/cs_cornell_edu/txt_sentoken/neg'
        files_pos = os.listdir(POS_DOCS_PATH)
        files_neg = os.listdir(NEG_DOCS_PATH)
        list_of_dict_units = []

        for fn in files_pos:
            if fn.find('txt') != -1:
                fn_name = POS_DOCS_PATH + '/' + fn
                doc = {'name': fn,
                       'text': open(fn_name).read(),
                       'polarity': 1}
                list_of_dict_units.append(doc)

        for fn in files_neg:
            if fn.find('txt') != -1:
                fn_name = NEG_DOCS_PATH + '/' + fn
                doc = {'name': fn,
                       'text': open(fn_name).read(),
                       'polarity': 0}

                list_of_dict_units.append(doc)

        return list_of_dict_units

    def create_database(self):

        docs = self.read_corpora_source()
        # inserts documents into collection
        for d in docs:
            self.documents.insert(d)


class Epinions_1(BaseModel):

    """docstring for Epinions datasets"""

    def __init__(self, dataset_name):
        self.dataset_name = dataset_name
        BaseModel.__init__(self, database_name="Epinions_1_" + dataset_name)

    def read_corpora_source(self):
        DOCS_PATH = os.path.abspath(
            os.curdir) + '/resources/corpora/sfu_review_corpus_raw/' + self.dataset_name
        files = os.listdir(DOCS_PATH)
        list_of_dict_units = []

        for fn in files:
            if fn.find('txt') != -1:
                polarity = 0 if 'no' in fn else 1
                fn_name = DOCS_PATH + '/' + fn
                text = open(fn_name).read()
                text = text.decode('Windows-1252').encode('utf-8')
                doc = {'name': fn,
                       'text': text,
                       'polarity': polarity}
                list_of_dict_units.append(doc)
        return list_of_dict_units

    def create_database(self):
        docs = self.read_corpora_source()
        for d in docs:
            self.documents.insert(d)


class Amazon(BaseModel):

    """docstring for Amazon datasets for MP3, USB, GPS, Wifi and camera products"""

    def __init__(self, database_name='Amazon_Train_MP3_USB_GPS_WIFI_CAMERA', num_docs=2000):
        BaseModel.__init__(self, database_name)
        self.num_docs = num_docs

    def read_corpora_source(self):
        file = os.path.abspath(
            os.curdir) + '/pyfuzzy_toolbox/resources/corpora/amazon_corpus/train+validation-reviews_MP3-USB-GPS-802.11-Camera-Phone.txt'
        file = open(file, 'r')
        list_of_dict_units = []

        for line in file.readlines():
            line_parts = line.split()
            name = line_parts[0]
            text = string.join(line_parts[1:len(line_parts) - 2])
            star = int(line_parts[len(line_parts) - 1])
            if star < 3 or star > 3:
                polarity = 0 if star < 3 else 1
                doc = {'name': name,
                       'text': text,
                       'polarity': polarity}
                list_of_dict_units.append(doc)

        return list_of_dict_units

    def create_database(self):
        docs = self.read_corpora_source()
        num_pos_docs = self.num_docs / 2
        num_neg_docs = num_pos_docs
        for d in docs:
            if d['polarity'] == 0 and num_neg_docs > 0:
                self.documents.insert(d)
                if num_neg_docs > 0:
                    num_neg_docs -= 1
                else:
                    num_neg_docs = 0

            if d['polarity'] == 1 and num_pos_docs > 0:
                self.documents.insert(d)
                if num_pos_docs > 0:
                    num_pos_docs -= 1
                else:
                    num_pos_docs = 0

            if num_neg_docs == 0 and num_pos_docs == 0:
                break
