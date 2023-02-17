#input 
X = int (input ("dime los minutos: "))

#proccesing

if X < 4: 
    y = 300

else:
    y = (X* 50) + 300 - 150


if y > 999:
        msj = " mil "

else:
     msj = " pesos "

#output
print ("los gastos totales son " + str(y) + msj)