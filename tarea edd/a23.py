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

class Node:
    def __init__(self,name,lname,phone,mail):
        self.left = None
        self.right = None
        self.name = name
        self.lname = lname
        self.phone = phone 
        self.mail = mail
        self.parent = None # Añadimos el atributo parent para facilitar la eliminación de un nodo

class TREE:
    def __init__ (self):
        
