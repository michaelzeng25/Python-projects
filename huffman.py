
#1.heapq is a built in priority queu available in Python
import heapq

#2.The queue will be built from tuples ordered by the first component of the tuple

def makeHuffTree(symbolTupleList):
   trees = list(symbolTupleList)
   heapq.heapify(trees)
#3. each step of the way the two smallest elements
# will be removed merged and placed back in the heap 
   while len(trees) > 1:
      childR, childL = heapq.heappop(trees), heapq.heappop(trees)
      parent = (childL[0] + childR[0], childL, childR)
      heapq.heappush(trees, parent)
   return trees[0]

#4. No code contains another as its prefix
#5.this recursive function will display the codes of the symbols

def printHuffTree(huffTree, prefix = ''):
   if len(huffTree) == 2:
      print( huffTree[1], prefix)
   else:
      printHuffTree(huffTree[1], prefix + '0')
      printHuffTree(huffTree[2], prefix + '1')
    
#6. The more frequent a symbol appears the shorter its code.
# This on a random file this would not be a effective method of compression.

#Some test cases
exampleData1 = [
  (0.124167  , 'e'),   
  (0.0969225 , 't'),   
  (0.0820011 , 'a'),   
  (0.0768052 , 'i'),   
  (0.0764055 , 'n'),   
  (0.0714095 , 'o'),   
  (0.0706768 , 's'),   
  (0.0668132 , 'r'),   
  (0.0448308 , 'l'),   
  (0.0363709 , 'd'),   
  (0.0350386 , 'h'),   
  (0.0344391 , 'c'),   
  (0.028777  , 'u'),   
  (0.0281775 , 'm'),   
  (0.0235145 , 'f'),   
  (0.0203171 , 'p'),   
  (0.0189182 , 'y'),   
  (0.0181188 , 'g'),   
  (0.0135225 , 'w'),   
  (0.0124567 , 'v'),   
  (0.0106581 , 'b'),   
  (0.00393019, 'k'),   
  (0.00219824, 'x'),   
  (0.0019984 , 'j'),   
  (0.0009325 , 'q'),   
  (0.000599  , 'z')   
]
exampleData2 = [(.75,'a'),(.05,'b'),(.05,'c'),(.15,'d')]

exampleData3 = [(.25,'a'),(.25,'b'),(.25,'c'),(.25,'d')]


huffTree = makeHuffTree(exampleData1)
printHuffTree(huffTree)


