leer = input("Por favor ingrese su contraseña: ") #primer lector de variables
leer_2 = input("Por favor vuelva a ingresar su contraseña: ") #segundo lector de variables
if leer_2 == leer: 
    print("Su contraseña es: ")
    print(leer)
else: print("Su contraseña no es correcta")