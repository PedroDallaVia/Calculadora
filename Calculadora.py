
#Seleccionar que tipo de operación se quiere realizar
ope=input("que operación hay que realizar? (s:suma, r:resta, m:multiplicacion, d:division)"+"\n");

#Ingresar los valores que se van a procesar en dicha operación
num1=input("ingrese un numero "+"\n");
num2=input("ingrese otro numero "+"\n");

#Verifica que los valores ingresados sean números y no letras o símbolos
if num1.isnumeric() and num2.isnumeric():
    num1=int(num1);
    num2=int(num2);
    #Ejecuta la operación seleccionada
    if (ope == "s"):
        res=(num1+num2)
        print("resultado: ",res);
    elif (ope == "r"):
        res=(num1-num2)
        print("resultado: ",res);
    elif (ope == "m"):
        res=(num1*num2)
        print("resultado: ",res);
    elif (ope == "d"):
        res=(num1/num2)
        print("resultado: ", res);
    else:
        #Salida si no se seleccionó una operación válida
        print("error: no se ha seleccionado una operación correcta")
#salida si no se seleccionó un número
else:
    print("error: no se ha ingresado un valor numérico");