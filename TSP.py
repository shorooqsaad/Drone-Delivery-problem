class TSP:
 distances={}
 initalNode=""
 def __init__(self,distances,initalNode):
 self.distances=distances
 self.initalNode=initalNode
 def swap(self,arr,first,second):
 temp=arr[first]
 arr[first]=arr[second]
 arr[second]=temp
 def allPermutationsHelper(self,permutation,permutations,n):
 if(n<=0):
 if(permutation[0] == self.initalNode):
 permutations.append(permutation)
 return
 tempPermutation=permutation+[]
 
 for i in range(n):
 self.swap(tempPermutation, i , n-1)
 
 self.allPermutationsHelper(tempPermutation,permutations,n-1)
 
 self.swap(tempPermutation,i,n-1)
 def permutations(self, original):
 permutations=[]
 
 self.allPermutationsHelper(original,permutations, len(original))
 
 return permutations
 
 def pathDistance(self, path):
 last=path[0]
 distance = 0
 
 for i in path[1:]:
 
 distance+=self.distances[last][i]
 last = i 
 return distance
 def findShortestPath(self):
 cities=list(self.distances.keys())
 paths=self.permutations(cities)
 shortestpath=None
10
 miniDistance=float ('inf')
 
 
 for path in paths:
 distance=self.pathDistance(path)
 distance+=self.distances[path[len(path)-1]][path[0]]
 if(distance<miniDistance):
 miniDistance=distance
 shortestpath=path
 return shortestpath
 def GoToDepote(self,path):
 LastHouse=path[len(path)-1] #path[len(path)-1:len(path)]
 if(LastHouse == "H1"):
 return 1
 if(LastHouse == "H2"):
 return 2
 if(LastHouse == "H3"):
 return 3
 if(LastHouse == "H4"):
 return 4
 
 def NewPath(self,path):
 path.append("D")
 return path