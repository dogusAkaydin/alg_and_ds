#! /home/ubt/anaconda3/bin/python
import sys
import lru

# Create the cache with size 3
myLRU = lru.LRU(5)
myLRU.showList()
myLRU.showDict()
print("1-5: Put n_max items")
myLRU.put('a', 100)
myLRU.put('b', 200)
myLRU.put('c', 300)
myLRU.put('d', 400)
myLRU.put('e', 500)
myLRU.showList()
myLRU.showDict()
print('-'*80)

print("6: Put one more")
myLRU.put('f', 600)
myLRU.showList()
myLRU.showDict()
print('-'*80)

print("7: Put one more")
myLRU.put('g', 700)
myLRU.showList()
myLRU.showDict()
print('-'*80)

print("8: Put one more")
myLRU.put('h', 800)
myLRU.showList()
myLRU.showDict()
print('-'*80)

print("9: Put one more")
myLRU.put('i', 900)
myLRU.showList()
myLRU.showDict()
print('-'*80)

print("10: Put one more. The first 5 items should all be gone now.")
myLRU.put('j', 1000)
myLRU.showList()
myLRU.showDict()
print('-'*80)

print("11: Update the value of a non-MRU/LRU key")
myLRU.put('h', 801)
myLRU.showList()
myLRU.showDict()
print('-'*80)

print("12: Update the value of the MRU key")
myLRU.put('h', 802)
myLRU.showList()
myLRU.showDict()
print('-'*80)

print("13: Update the value of the LRU key")
myLRU.put('f', 601)
myLRU.showList()
myLRU.showDict()
print('-'*80)

print("14: Check the value of a non-MRU/LRU key")
val = myLRU.get('j')
print('***',val,'***')
myLRU.showList()
myLRU.showDict()
print('-'*80)

print("15: Check the value of the MRU key")
val = myLRU.get('j')
print('***',val,'***')
myLRU.showList()
myLRU.showDict()
print('-'*80)

print("16: Check the value of the LRU key")
val = myLRU.get('g')
print('***',val,'***')
myLRU.showList()
myLRU.showDict()
print('-'*80)

sys.exit()


