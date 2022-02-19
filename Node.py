import math
class Node: 
 def __init__(self, row, col): 
 self.row = row
 self.col = col
 self.neighbors = []
 
 def addBranch(self, weight, node): 
 newEdge = Edge(self,node, weight)
 self.neighbors.append(newEdge)
 def toString(self):
 return "Node{" + "row=" + str(self.row) + ", col=" + str(self.col) + " neighbors: " + 
str(self.neighbors)
 def getRow(self): 
 return self.row
 def setRow(self, row): 
 self.row = row
 def getCol(self): 
11
 return self.col
 def setCol(self, col): 
 self.col = col
 def getNeighbor(self): 
 return self.neighbors
 #//////////////////////////////////////////////////////////
class Edge(Node): 
 DigonalCost = 2
 EculedianCost = 1
 def __init__(self, node1,node, g): 
 self.node = node
 self.g = g
 self.node1=node1
 self.Dh = self.calculate_Digonal_Heuristic(node1)
 self.setDf(self.Dh)
 self.Eh = self.calculate_Euclidean_Heuristic(node1)
 self.setEf(self.Eh)
 self.Mh = self.calculate_Manhattan_Heuristic(node1)
 self.setMf(self.Mh)
 def setMf(self, Mh): 
 self.Mf = self.Mh + self.g
 def setEf(self, Eh): 
 self.Ef = self.Eh + self.g
 def setDf(self, Dh): 
 self.Df = self.Dh + self.g
 def calculate_Manhattan_Heuristic(self,node1): 
 self.Mh = abs(self.node.getRow() - self.node1.getRow()) + abs(self.node.getCol() -
self.node1.getCol())
 return self.Mh
 def calculate_Euclidean_Heuristic(self,node1): 
 x = math.pow(abs(self.node1.getRow() - self.node.getRow()), 2)
 y = math.pow(abs(self.node1.getCol() - self.node.getCol()), 2)
 self.Eh = self.EculedianCost * math.sqrt(x + y)
 return self.Eh
 def calculate_Digonal_Heuristic(self,node1): 
 dx = abs(self.node1.getRow() - self.node.getRow())
 dy = abs(self.node1.getCol() - self.node.getCol())
 self.Eh = self.DigonalCost * max(dx, dy)
 return self.Eh