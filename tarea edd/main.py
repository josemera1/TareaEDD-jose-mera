def main():
    print ('elija la edd que desea ocupar')
    print ('1. Lista')
    print ('2. Arbol binario')
    print ('3. AVL')
    print ('4. Arbol 2-3')
    print ('5. Hash')

    a = imput ()
    if a==1:
        import Lista
    elif a==2:
        import abb
    elif a==3:
        import avl 
    elif a==4:
        import a23
    elif a==5:
        import hash