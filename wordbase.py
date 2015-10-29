#!/usr/bin/python
#-*- coding: utf8 -*-

import trie_tree_linklist
import pickle
import sys
import re
import time

def readFile(fileName):
	with open(fileName, "rt") as in_file:
		text = in_file.read()
	return text

if __name__ == '__main__':
	time1 = time.time()
	text = readFile(sys.argv[1])
	word_list = re.findall(r'[a-zA-Z]+', text)
	word_dict = {}
	i = 1
	for word in word_list:
		lower_word = word.lower()
		if lower_word not in word_dict:
			word_dict[lower_word] = [i]
		else:
			word_dict[lower_word].append(i)
		i = i + 1
	output = open('wordquery.pkl', 'wb')
	pickle.dump(word_dict, output)
	output.close()
	time2 = time.time()
	print(time2 - time1)
	
