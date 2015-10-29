#!/usr/bin/python
#-*- coding: utf8 -*-

import pickle
import sys
import time
import re

def readFile(fileName):
	with open(fileName, "rt") as in_file:
		text = in_file.read()
	return text

if __name__ == '__main__':
	time1 = time.time()
	input_file = open("wordquery.pkl", 'rb')
	word_dict = pickle.load(input_file)
	input_file.close()
	time2 = time.time()
	
	_str = ""
	text = readFile(sys.argv[1])
	word_list = re.findall(r'[a-zA-Z]+', text)
	index_list = []
	for word in word_list:
		tmp_word = word.lower()
		index_list = word_dict[tmp_word]
		length = len(index_list)
		for i in range(0, length - 1):
			sys.stdout.write("%d" % index_list[i])
			sys.stdout.write(',')
		sys.stdout.write("%d" % index_list[length - 1])
		sys.stdout.write('\n')
	
	time3 = time.time()
	#print(time2 - time1)
	#print(time3 - time2)
	print(time3 - time1)
	
