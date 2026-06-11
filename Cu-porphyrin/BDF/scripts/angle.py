#!/usr/bin/env python3
import math
import sys
import os

def angle_between_vectors(a, b):
    """
    计算两个向量的夹角（返回弧度和角度）
    a, b: 列表或元组，例如 [1,2,3]
    """

    # 点积
    dot = sum(ai * bi for ai, bi in zip(a, b))
    #print(dot)

    # 模长
    norm_a = math.sqrt(sum(ai**2 for ai in a))
    norm_b = math.sqrt(sum(bi**2 for bi in b))
    #print(norm_a,norm_b)

    # 余弦值
    cos_theta = dot / (norm_a * norm_b)

    # 修正浮点误差，避免超出 [-1, 1]
    cos_theta = max(-1.0, min(1.0, cos_theta))

    # 夹角（弧度）
    theta_rad = math.acos(cos_theta)

    # 转成角度
    theta_deg = math.degrees(theta_rad)

    return theta_rad, theta_deg


filename = sys.argv[1]

f = open("{}".format(filename))

# 返回一个列表
f1 = f.readlines()
f.close()

square = int(0)

#print(f1)
a = []
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
#       print(l)
        a.append(float(l))
#print(a)

filename = sys.argv[2]

f = open("{}".format(filename))

# 返回一个列表
f1 = f.readlines()
f.close()

square = int(0)

#print(f1)
b = []
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
#       print(l)
        b.append(float(l))

########例子####
# a = [1,2,3]
# b = [4,5,6]

rad, deg = angle_between_vectors(a, b)
#print("夹角（弧度）:", rad)
print("夹角（度）:", deg)


