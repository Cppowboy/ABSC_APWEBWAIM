from absl import flags
import time
import datetime
import os

flags.DEFINE_string('model', 'ram', 'ram model')
# data input files
flags.DEFINE_string('dataset', 'lap', 'the dataset to use for train and test, lap/res/res_cat')
flags.DEFINE_string('laptop_train_xml', 'data/laptop/Laptop_Train_v2.xml', 'laptop dataset, train xml file path')
flags.DEFINE_string('laptop_test_xml', 'data/laptop/Laptops_Test_Gold.xml',
                    'laptop dataset, test gold xml file path')
flags.DEFINE_string('restaurant_train_xml', 'data/restaurant/Restaurants_Train_v2.xml',
                    'restaurant dataset, train xml file path')
flags.DEFINE_string('restaurant_test_xml', 'data/restaurant/Restaurants_Test_Gold.xml',
                    'restaurant dataset, test gold xml file path')
flags.DEFINE_string('twitter_train_xml', 'data/twitter/train.xml', '')
flags.DEFINE_string('twitter_test_xml', 'data/twitter/test.xml', '')
flags.DEFINE_string('glove_file', 'data/glove/glove.840B.300d.txt', 'glove embedding file path')
# data output files
flags.DEFINE_string('train_data', 'train.json', 'save train examples in this file')
flags.DEFINE_string('train_examples', 'train_examples.json', 'save train examples in this file')
flags.DEFINE_string('test_data', 'test.json', 'save test data in this file')
flags.DEFINE_string('test_examples', 'test_examples.json', 'save test examples in this file')
flags.DEFINE_string('word2id_file', 'word2id.json', 'word2id dict file')
flags.DEFINE_string('wordmat_file', 'wordmat.txt', 'word embedding file')
# data params
flags.DEFINE_integer('word_limit', -1, 'word appears over word_limit times will be put into the word dict')
flags.DEFINE_integer('sent_limit', 50, 'max length of sentence')
flags.DEFINE_integer('aspect_limit', 5, 'max length of')
# save params
flags.DEFINE_string('log_save', 'logs', 'save the events in this directory')
flags.DEFINE_string('model_save', 'ckt', 'save the models in this directory')
flags.DEFINE_string('result_save', 'result', 'save result here')
flags.DEFINE_string('timestr', datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
                    'time str of current time, %Y%m%d%H%M%S')
# train params
flags.DEFINE_string('device', 'cuda', 'which device to use, cuda or cpu')
flags.DEFINE_integer('seed', int(1000 * time.time()), 'random seed')
flags.DEFINE_string('optimizer', 'adam', 'which kind of optimizer to use')
flags.DEFINE_float('lr', 0.0002, 'initial learning rate')
flags.DEFINE_float('weight_decay', 0, 'weigth decay')
flags.DEFINE_integer('max_epoch', 50, 'max train epoch')
flags.DEFINE_integer('batch', 32, 'batch size value')
flags.DEFINE_float('dropout_rate', 0.5, 'dropout rate')
# model params
flags.DEFINE_integer('dim_word', 300, 'word embedding dimension')
flags.DEFINE_integer('dim_hidden', 200, 'hidden state dimension of lstm')
flags.DEFINE_integer('dim_episode', 200, 'episode vector dimension')
flags.DEFINE_integer('num_layer', 2, 'number of attention layer')
flags.DEFINE_integer('C', 40, 'C constant to calculate the position weights')
flags.DEFINE_integer('num_class', 3, 'number of classes')
flags.DEFINE_list('class_weight', [3, 1, 3], 'class weight for loss')
# params
flags.DEFINE_string('mode', 'train', 'run prepro/train/test')
config = flags.FLAGS
