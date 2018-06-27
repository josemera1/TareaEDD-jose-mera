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
    insert(n,l,num,m)
elif a==2:
    print ('ingrese el numero:')
    n=input()
    find(n)
elif a==3:
    print ('ingrese numero a eliminar:')
    n=input()
    delete(n)
elif a==4:
    display()
class Node:
    def __init__(self,name,lname,phone,mail):
        self.left = None
        self.right = None
        self.name = name
        self.lname = lname
        self.phone = phone 
        self.mail = mail
        self.parent = None # Añadimos el atributo parent para facilitar la eliminación de un nodo

class BST:
    def __init__(self):
        self.root = None

    def empty(self):
        return self.root == None

    def _insert(self, node):
        if root.lname[0] < node.lname[0]:
            if node.left == None:
                node.left = Node(node)
                node.left.parent = node
            else:
                self._insert(node.left)
        elif root.lname[0] > node.lname[0]:
            if node.right == None:
                node.right = Node(node)
                node.right.parent = node
            else:
                self._insert(node.right)
        else:
            print("El contacto ya existe")
            
    def insert(self, node):
        if self.empty():
            self.root = Node(node)
        else:
            self._insert(node, self.root)

    def _find(self, lname):
        #suponiendo que busca segun apellido
        if node == None:
            return None
        elif lname == root.lname:
            return node
        elif value < node.lname and node.left != None:
            return self._find(lname, node.left)
        elif value > node.lname and node.right != none:
            return self._find(lname, node.right)

    def find(self, value):
        if self.empty():
            return None
        else:
            return self._find(value, self.root)

    def delete(self, value): #Implementar
        if self.empty():
            return None
        return self.delete_node(self.find(value))

    def delete_node(self, node):
        def min_value_node(n):
            current = n
            while current.left != None:
                current = current.left
            return current
        def number_children(n): # Return the number of childrens of the node to be deleted
            number_children = 0
            if n.left != None:
                number_children += 1
            if n.right != None:
                number_children += 1
            return number_children

        node_parent = node.parent # Get the parent of the node to be deleted
        node_children = number_children(node)

        # Case 1: Deleting a node without childrens
        if node_children == 0:
            if node_parent.left == node:
                node_parent.left = None
            else:
                node_parent.right = None
        # Case 2: Deleting a node with one children
        if node_children == 1:
            # Get the children of the node to be deleted
            if node.left != None:
                child = node.left
            else:
                child = node.right

            # Replace the node to be deleted with its child
            if node_parent.left == node:
                node_parent.left = child
            else:
                node_parent.right = child

            # Change the parent of the child
            child.parent = node_parent
        # Case 3: Deleting a node with two childrens
        if node_children == 2:
            successor = min_value_node(node.right) # Get the inorder successor of the deleted node
            node.value = successor.value # Copy the value
            self.delete_node(successor)

    def display(self,a): #arreglar, metodo in order
         if a == None:
            return None
        else:
            self.display(a.left)
            print(a.dato)
            self.display(a.right)
            


