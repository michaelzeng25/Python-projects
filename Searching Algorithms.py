from random import randint
import time
import random


class Search:
    def __init__(self, list):
        self.list = list

    def sequential_search(self, target):

        for i in range(len(list)):
            if (list[i] == target):
                print('The number ',target,'is found at the index number: ',i)
                break
            elif(list[i] != target and i == len(list)-1):
                print("The target number is not found in the list")
                break

    def binary_search(self,target):
        # the list must be sorted in binary search.
        sorted_list = list.sort()
        first = 0
        last = len(list)-1
        while(first<= last):
            mid = (last+first) //2
            if(list[mid] == target):
                print("Found the number at index: ",mid)
                break

            else:
                if(list[mid] > target):
                    last = mid - 1
                else:
                    first = mid + 1

            if(first == last and list[first] != target):
                print('The number is not found in the list')
                break


list = [random.randint(0,2000) for x in range(1000)]
target = randint(0,2000)
print('The list contains: ',len(list),' numbers.')
print('The target number is',target)
print('\n')

result = Search(list)

start = time.time()
result.sequential_search(target)
end = time.time()
print('Seqiential search took ',round(end-start,5),'seconds.')
print('\n')

start = time.time()
result.binary_search(target)
end = time.time()
print('binary search took ',round(end-start,5),'seconds.')

