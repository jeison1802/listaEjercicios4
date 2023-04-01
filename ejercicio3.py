
import requests 

url1 = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
url2 = 'https://pokeapi.co/api/v2/pokedex/1/'
url3 = 'https://pokeapi.co/api/v2/pokemon/'


data1=requests.get(url1).json()
data2=requests.get(url2).json()
data3=requests.get(url3).json()
listPokemon=data2['names']
list2Pokemon = data3['results']

print(data1)


for i,value in enumerate(listPokemon):
    name=value['language']['name']
    print(i,"=>",name)

def agregarLista(lista,n):
     lista.append(n)

def mostrar(lista1):
    
    if len(lista1)>0:
         for i in lista1:
            print(i,end = " ")

print("\n")

lista = []
for i,value in enumerate(list2Pokemon):
    name=value['name']
    print(i,"=>",name)
    agregarLista(lista,name)
print("\nLos nombres de la lista son:\n ")
mostrar(lista)

