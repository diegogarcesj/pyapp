def datos():
	archivo = open('/usr/home/diego/libros.txt','r')
	lineas = archivo.read()
	formated = "<pre>" + lineas + "</pre>"
	return formated
def datos2():
	archivo = open('/usr/home/diego/libros2.txt','r')
	lineas = archivo.read()
	formated = "<pre>" + lineas + "</pre>"
	return formated 
