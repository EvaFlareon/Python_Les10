# -*- coding: utf-8 -*-

import chardet
import operator


def list_to_dict(txt_list):
    dict_word = {}
    for item in txt_list:
        dict_word[item] = 0
        for len_word in txt_list:
            if item == len_word:
                dict_word[item] += 1
    return dict_word


def max_word(new_dict):
    sorted_dict = sorted(new_dict.items(), key=operator.itemgetter(1))
    sorted_dict.reverse()
    i = 0
    while i < 10:
        print('Слово:', sorted_dict[i][0], 'количество повторов:', sorted_dict[i][1])
        i += 1


def search_word(file_name):
    with open(file_name, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        s = data.decode(result['encoding'])
        list_file = s.split(' ')
        list_file.sort()
        new_list = []
        for word in list_file:
            if len(word) > 6 and ord(word[0]) != 10:
                new_list.append(word)
        new_dict = list_to_dict(new_list)
        print(file_name)
        max_word(new_dict)


search_word('newsafr.txt')
search_word('newscy.txt')
search_word('newsfr.txt')
search_word('newsit.txt')
