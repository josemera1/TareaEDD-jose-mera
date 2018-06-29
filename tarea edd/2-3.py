print ("Selecciona una opción")
print ("\t1 - Insertar:")
print ("\t2 - Buscar:")
print ("\t3 - Eliminar")
print ("\t4 - Imprimir")
a = input()
if a==1:
    print ('ingrese nombre, apellido, numero y mail:')
    n=input()
    l=input()
    num=input()
    m=input()
    insert_first(n,l,num,m)
elif a==2:
    print ('ingrese el numero:')
    n=input()
    buscar(n)
elif a==3:
    print ('ingrese numero a eliminar:')
    n=input()
    remover(n)

# 2-3 Tree
# balanced tree data structure with up to 2 data items per node

class Node:
	def __init__(self, data, par = None):
		#print ("Node __init__: " + str(data))
		self.data = list([data])
		self.parent = par
		self.child = list()
		
	def __str__(self):
		if self.parent:
			return str(self.parent.data) + ' : ' + str(self.data)
		return 'Root : ' + str(self.data)
	
	def __lt__(self, node):
		return self.data[0] < node.data[0]
		
	def _isLeaf(self):
		return len(self.child) == 0
			
	# merge new_node sub-tree into self node
	def _add(self, new_node):
		# print ("Node _add: " + str(new_node.data) + ' to ' + str(self.data))
		for child in new_node.child:
			child.parent = self
		self.data.extend(new_node.data)
		self.data.sort()
		self.child.extend(new_node.child)
		if len(self.child) > 1:
			self.child.sort()
		if len(self.data) > 2:
			self._split()
	
	# find correct node to insert new node into tree
	def _insert(self, new_node):
		# print ('Node _insert: ' + str(new_node.data) + ' into ' + str(self.data))
		
		# leaf node - add data to leaf and rebalance tree
		if self._isLeaf():
			self._add(new_node)
			
		# not leaf - find correct child to descend, and do recursive insert
		elif new_node.data[0] > self.data[-1]:
			self.child[-1]._insert(new_node)
		else:
			for i in range(0, len(self.data)):
				if new_node.data[0] < self.data[i]:
					self.child[i]._insert(new_node)
					break
	
	# 3 items in node, split into new sub-tree and add to parent	
	def _split(self):
		# print("Node _split: " + str(self.data))
		left_child = Node(self.data[0], self)
		right_child = Node(self.data[2], self)
		if self.child:
			self.child[0].parent = left_child
			self.child[1].parent = left_child
			self.child[2].parent = right_child
			self.child[3].parent = right_child
			left_child.child = [self.child[0], self.child[1]]
			right_child.child = [self.child[2], self.child[3]]
					
		self.child = [left_child]
		self.child.append(right_child)
		self.data = [self.data[1]]
		
		# now have new sub-tree, self. need to add self to its parent node
		if self.parent:
			if self in self.parent.child:
				self.parent.child.remove(self)
			self.parent._add(self)
		else:
			left_child.parent = self
			right_child.parent = self
			
	# find an item in the tree; return item, or False if not found		
	def _find(self, item):
		# print ("Find " + str(item))
		if item in self.data:
			return item
		elif self._isLeaf():
			return False
		elif item > self.data[-1]:
			return self.child[-1]._find(item)
		else:
			for i in range(len(self.data)):
				if item < self.data[i]:
					return self.child[i]._find(item)
		
	def _remove(self, item):
		pass
		
	# print preorder traversal		
	def _preorder(self):
		print (self) 
		for child in self.child:
			child._preorder()
	
class Tree:
	def __init__(self):
		print("Tree __init__")
		self.root = None
		
	def insert(self, item):
		print("Tree insert: " + str(item))
		if self.root is None:
			self.root = Node(item)
		else:
			self.root._insert(Node(item))
			while self.root.parent:
				self.root = self.root.parent
		return True
	
	def find(self, item):
		return self.root._find(item)
		
	def remove(self, item):
		self.root.remove(item)
		
	def printTop2Tiers(self):
		print ('----Top 2 Tiers----')
		print (str(self.root.data))
		for child in self.root.child:
			print (str(child.data), end=' ')
		print(' ')
		
	def preorder(self):
		print ('----Preorder----')
		self.root._preorder()