#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
	prvi = 0
	drugi = 0
	for l in list(zip(a,b)):
		if l[0]>l[1]:
			prvi+=1

		elif l[1]>l[0]:
			drugi+=1


	return [prvi,drugi]
def main():
    a = list(map(int, input().rstrip().split()))
    print(a)
    b = list(map(int, input().rstrip().split()))
    print(b)
    result = compareTriplets(a, b)
    print(result)

if __name__ == '__main__':
	main()
    


    
