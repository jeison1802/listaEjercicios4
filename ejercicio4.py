
from datetime import datetime
 


class Registro:


   def __init__(self) -> None:
      self.f = open('./src/texto.txt','w')  
      self.texto = input("Ingresa un texto: ")
      

   def escribir(self):
       self.f.write(self.texto) 
     # print(data)
       self.f.close()
   
   def mostrar(self):
      with open('./src/texto.txt','r') as self.f:
         data = self.f.readlines()
         #print(data)
         print(self.f.name, "\t-",datetime.now(),"\t-", data)
         



reg = Registro()    
reg.escribir()
reg.mostrar()

