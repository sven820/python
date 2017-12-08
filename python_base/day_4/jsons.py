__author__ = "JJ.sven"

import json
import pickle

'''
dic = {
    'name': 'jj',
    'age': 99
}
json_str = json.dumps(dic)

file = open('test_json', 'r', encoding='utf-8')
# json.dump(dic, file)

print(json_str)

dic_from = json.loads(json_str)
dic_from_jsontext = json.loads(file)

print(dic_from, type(dic_from), dic_from_jsontext)

file.close()

'''


# pickle
# 可以序列化所有对象
# '''
def test():
    print('test')
    pass


dic = {
    'name': 'jj',
    'age': 99,
    'func': test
}

file = open('pickle_test', 'rb')

to = pickle.dumps(dic)
# pickle.dump(dic, file)
print(to)

load_dic = pickle.load(file)
print(load_dic)
load_dic['func']()

file.close()
# '''
