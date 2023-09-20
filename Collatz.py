
lista = []

digito = int(input("\n\nIngrese el último dígito de su código: "))
a = digito + 3

for i in range(1,a+1):
    listap = int(input(f"Ingrese el {i} numero: "))
    lista.append(listap)
    
nump = sum(lista)/a

numero = int(nump)

print("\n\tEl número promeido es:",numero)

while numero != 1:
     
    if numero %2==0: 
         numero = (numero/2)
         print("\nSe divide x2 y da: ", numero)
         
    else: 
        numero = (numero*3)+1
        print("\nSe multiplica por 3 y se le suma uno y da: ", numero)
        
print("\n\nSE HA CUMPLIDO LA SECUENCIA DE COLLATZ")



        
    
        
        
         

         
         