#con esta libreria importamos todas las funciones matematicas que tiene python.
from math import *

character_name = "Link"
is_male = True 

print ("There was a boy named " + character_name)
print ("   /\ " )
print ("  /__\ " )
print (" /\  /\ " )
print ("/__\/__\ " )

#Con \n puedes hacer que pase a la siguiente linea.
print ("There was a boy named\nLINK")

#Con solo el \ damos a entender que hacemos una excepcion en el texto para dejarnos incluir caracteres que serian interpretados de forma distinta.
#variables de String
#primero podemos establecer un caso basico
phrase = "There was a boy named Link"
print(phrase)
 
#len te da la longitud del String
print(len(phrase))

#Podemos utilizar [] dentro del print para obetener un caracter en especifico partiendo de 0 como el primero. 
#Y tambien lo contrario con .index dandote la posicion de ese caracter introducido.
#Con .replace podemos cambiar una palabra con otra.

print(phrase[0])
print(phrase.index("L"))
print(phrase.replace("boy", "bitch"))

#Trabajando con numeros str nos permite darle a una variable numerica una estrustura alfabetica.

numba = "-69"
print(str(numba) + "Pussy")
#abs nos permite obtener le valor absoluto de la variable numerica.
#pow nos permite hacer exponenciales
print(pow(3, 2))
#tambien tenemos min y max que devuelven el numero mas alto y el mas bajo 
#round redondea numeros
#floor y ceil nos dan los que se conoce como floor y ceiling.
#sqrt raiz cuadrada
#input nos permite darle al usuario un punto de entrada como una contrasena o un nombre de usuario

name = input("Enter Username: ")
password = input("Enter password: ")
print("Welcome: " + name)
print("Password: " + password)

##Calculator
#float decimales y int un numero normal
num1 = input("_")
num2 = input("_") 

result = float(num1) + float(num2)

print(result)
