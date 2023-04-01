
import random as rd 
  
class Sorteo:

    def __init__(self): 
         self.lista = []
         self.valor_max = int(input("Ingresa el valor maximo: "))
         self.num = int(input("Ingresa el numero de terminos: "))

    def agregarDatos(self):
           i = 0
           self.lista.append(self.valor_max)

           while(i<self.num-1): 
             n = round(rd.random()*self.valor_max,2)
             self.lista.append(n)
             i +=1 
    
    def mostrarProductos(self):
       
         if len(self.lista)>0:
             for i in self.lista:
                 print(i,end = " ")

    def escogeNumero(self):
        print("\nEl valor escogido al azar de la lista es: ",rd.choice(self.lista))
                     
    
sorteo = Sorteo()
sorteo.agregarDatos()
sorteo.mostrarProductos()
sorteo.escogeNumero()


 



