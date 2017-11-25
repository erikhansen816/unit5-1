#Sam Smedinghoff
#11/15/17
#sorting.py - code to test a sorting function

from random import randint
from time import time

N = 100 #how many numbers will be sorted

def mySort(L):
    
    return L

if __name__ == '__main__':
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
        
    pythonSort = sorted(numbers) #Python's sort
    
    t1 = time()
    numbers = mySort(numbers)
    t2 = time()
        
    try:
        assert(numbers == pythonSort)
        print(t1-t2)
    except:
        print('Your sort did not work')
    