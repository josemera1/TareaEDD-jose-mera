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
class Hash:
	def __init__(self):
		self.size = 6
		self.map = [None] * self.size

	def _get_hash(self, key):
		hash = 0
		for char in str(key):
			hash += ord(char)
		return hash % self.size
	
	def add(self, key, nodo):
		key_hash = self._get_hash(key)
		key_value = [key, nodo]
		
		if self.map[key_hash] is None:
			self.map[key_hash] = list([key_value])
			return True
		else:
			for pair in self.map[key_hash]:
				if pair[0] == key:
					pair[1] = nodo
					return True
			self.map[key_hash].append(key_value)
			return True
			
	def get(self, key):
		key_hash = self._get_hash(key)
		if self.map[key_hash] is not None:
			for pair in self.map[key_hash]:
				if pair[0] == key:
					return pair[1]
		return None

	def find(self,clave):
      ranuraInicio = self.funcionHash(clave,len(self.ranuras))

      dato = None
      parar = False
      encontrado = False
      posicion = ranuraInicio
      while self.ranuras[posicion] != None and  \
                           not encontrado and not parar:
         if self.ranuras[posicion] == clave:
           encontrado = True
           dato = self.datos[posicion]
         else:
           posicion=self.rehash(posicion,len(self.ranuras))
           if posicion == ranuraInicio:
               parar = True
      return dato

	def delete(self, key):
		key_hash = self._get_hash(key)
		
		if self.map[key_hash] is None:
			return False
		for i in range (0, len(self.map[key_hash])):
			if self.map[key_hash][i][0] == key:
				self.map[key_hash].pop(i)
				return True
		return False

	def imprimir(self):
		print('-------')
		for item in self.map:
			if item is not None:
				print(str(item))