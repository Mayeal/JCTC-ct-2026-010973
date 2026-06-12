#!/usr/bin/env python3

import sys
import os

filename = sys.argv[1]

f = open("{}".format(filename))

# 返回一个列表
f1 = f.readlines()
f.close()

square = int(0)

#print(f1)
list1 = []
for i, inp1 in enumerate(f1):
	if ' Gradient contribution from Final-NAC(S)-Escaled' in inp1:
		atom_1 = i+1
	if "Sum of gradient contribution from Final-NAC(S)-Escaled" in inp1:
		atom_n = i-1
		nacme = f1[atom_1:atom_n]
#print(nacme)
for j in nacme:
	k = j.split( )[1:4]
	#print(k)
	
	for l in k:
#		print(l)
		list1.append(l)
		square += float(l)**2
#		print(square)
norm = square ** 0.5
print('模 = ', norm)
matrix = ','.join(list1)
#print('取出的矩阵元 = ', matrix)

