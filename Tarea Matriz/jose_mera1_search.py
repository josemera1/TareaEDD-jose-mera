print ("ingrese primero el orden de la matriz, luego los valores")
x = input () #orden de la matriz

for i in range (x):
    for j in range (x):
        array[i][j]= input()

print ("El numero es menor a:", str(i),str(x) , "? (y or n)" )

q=input()
if a==y:
    pregunta(a)
else:
print ("El numero es:", array[i][x])

def pregunta (a):
    if a==y:
           print ("El numero es menor a:", str(i),str(x-1) , "? (y or n)" )
           b=input()
           if b==y:
             pregunta(b)
           
    else :
            print ("Su numero es :" ,str(i),str(x-1), "? (y or n)")
            c=input()
            if c==y:
                print ("El numero es:", array[i][x-1])
             else:
                
              print ("El numero es menor a:", str(i+1),str(x-1) , "? (y or n)")
              pregunta(c)
            
        






