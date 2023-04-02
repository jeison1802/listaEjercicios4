
import re 

def telefono():
    phone_number = input("Ingresa un numero telefonico: ")

    if len(phone_number) == 9:   
       print(re.findall(r"^9\d*$", phone_number))
    else: 
        print("Ingrese otro numero")

    
telefono()    

