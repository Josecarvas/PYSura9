from fileinput import close
import pandas as pd

tablaempleados = pd.read_csv('./BD/empleados.csv')

#print(tablaempleados)
#print(tablaempleados.t to_string())

# filtro 1 quiero obtener todos los datos de los analistas 1
'''
tabladeanalistas1 = tablaempleados[tablaempleados["cargo"]=="analista1"].head(50)
archivoHTML=tabladeanalistas1.to_html()
archivoTEXTO=open("datosanalistas1.html","w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()


tabladeanalistas2 = tablaempleados[tablaempleados["cargo"]=="analista2"].head(50)
archivoHTML2=tabladeanalistas2.to_html()
archivoTEXTO2=open("datosanalistas2.html","w")
archivoTEXTO2.write(archivoHTML2)
archivoTEXTO2.close()
'''

tabladefiltro = (tablaempleados[(tablaempleados["edad"]<30)&(tablaempleados["salario"]>5500000)])
archivoHTML3=tabladefiltro.to_html()
archivoTEXTO3=open("tabladefiltro.html","w")
archivoTEXTO3.write(archivoHTML3)
archivoTEXTO3.close()