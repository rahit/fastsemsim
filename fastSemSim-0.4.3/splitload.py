#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""This program determines the distribution of semantic similarity scores for sets of proteins
"""
__author__="Marco Mina"
__email__="marco.mina.85@gmail.com"

import sys
import os
import math

def det_total(A,B,N):
	if A > B:
		return 0
	if B > N - 1:
		return 0
	T = (N - 1)*(B - A + 1) - ((B*(B+1))/2 - ((A-1)*A)/2)
	return int(T)

if __name__ == "__main__":
	N = int(sys.argv[1])
	P = int(sys.argv[2])
	T = N * (N - 1) / 2
	F = int(math.ceil(T / P))
	A = 0
	B = 0
	print("N: " + str(N))
	print("P: " + str(P))
	print("T: " + str(T))
	print("F: " + str(F))
	print("A: " + str(A))
	print("B: " + str(B))
	print("Total: " + str(det_total(A,B,N)))
	
	intervals = []
	nexti = 1
	while B < N - 1:
		B = A
		while det_total(A,B,N) < F:
			B += 1
			if(B == N - 1):
				break
		intervals.append((nexti, A,B, det_total(A,B,N)))
		A = B + 1
		nexti += 1
	tota = 0
	for i in intervals:
		print(str(i))
		tota += i[3]
	print(str(tota))
