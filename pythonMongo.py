import pymongo

url = "mongodb://localhost:27017"

try:
	conectar = pymongo.MongoClient(url)
	conectar.server_info()
	print ("\n-----> Conexion exitosa! <-----\n")

	#Id = int(input("\nIngrese su ID: "))
	nombre = input("Digite su nombre: ")
	#apellido = input("Digite el apellido: ")

	mydb = conectar["practica"]
	mycol = mydb["ejemplo"]
	#mycol.insert_one({"_id":Id,"nombre":nombre,"apellido":apellido})
	result = mycol.find()

	for i in result:
		if i["nombre"] == nombre:
			print ("\nNombre encontrado!")
			break
		else:
			print ("\nEl nombre no esta registrado")
	conectar.close()
except:
	print ("\nError en la conexion\n")