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
elif a==4:
    print_list()
class Node:
    def __init__(self, name,lname,phone,mail):
        self.name = name
        self.lname = lname
        self.phone = phone
        self.mail = mail
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head == None

    def insert_first(self, Node):
        if self.empty():
            self.head = Node(nodo)
            self.tail = self.head
        else:
            node = Node(nodo)
            aux = self.head
            while aux.lname[0] < nodo.lname[0]:
                if aux.next is none:
                    aux.next=node
                else:
                    aux=aux.next
    #buscar por numero
    def buscar(self,value):
        actual = self.head
        encontrado = False
            while actual.phone != None and not encontrado:
                if self.head.phone == value:
                    encontrado = True
                else:
                    actual = actual.next
            return encontrado
    def remover(self,value):
    actual = self.head
    previo = None
    encontrado = False
    while not encontrado:
        if self.head.phone == value:
            aux = self.head
            self.head=aux.next
            encontrado = True
        else:
            previo = actual
            actual = self.head.next

        if previo == None:
            head = self.head.next
        else:
            previo= self.previo.next

    def print_list(self):
        aux=self.head
        if self.empty():
             print("Lista vacia")
        else:
            while self.head:
                print (aux.name)
                print (aux.lname)
                print (aux.phone)
                print (aux.mail)
                aux=self.head.next