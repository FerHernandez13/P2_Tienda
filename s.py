import socket
import pickle
import time

class Articulo:
    def __init__(self, idd, nombre, descrip, precio, existen, promo, fecha_promo):
        self.idd = idd
        self.nombre = nombre
        self.descrip = descrip
        self.precio = precio
        self.existen = existen
        self.promo = promo
        self.fecha_promo = fecha_promo

    def quitar_comprados(self, num):
        if num > self.existen:
            print ("No hay tantos articulos en existencia")
        else :
            self.existen = self.existen - num 

    def describe(self):
        return "Descripcion:\n{}\n{}\n{}".format(self.nombre, self.descrip, self.promo)

    def getPrecio(self):
        return "Precio:\n$ {}".format(self.precio)

    def __str__ (self):
        return "Articulo: {} \nPrecio: ${} ".format(self.nombre, self.precio)

class Compra:
    def __init__(self, total, aguaArt, cocaArt, cheeArt):
        self.total = total
        self.a = 0
        self.b = 0
        self.c = 0
        self.aguaArt = aguaArt
        self.cocaArt = cocaArt
        self.cheeArt = cheeArt

    def suma(self, n):
        self.total = self.total + n

    def getTotal(self):
        return int(self.total)

    def muestraTotal(self):
        return self.total

    def agregarCarrito(self, x): 

        if x == 1:
            if(self.a < aguaArt.existen):
                self.a = self.a + 1
                self.total = aguaArt.getNum() + self.total
            else:
                print "No hay mas en existencia de ", aguaArt.getNombre()
        if x == 2:
            if(self.b < cocaArt.existen):
                self.b = self.b + 1
                self.total = cocaArt.getNum() + self.total
            else:
                print "No hay mas en existencia de ", cocaArt.getNombre()
        if x == 3:
            if(self.c < cheeArt.existen):
                self.c = self.c + 1
                self.total = cheeArt.getNum() + self.total
            else:
                print "No hay mas en existencia de ", cheeArt.getNombre()


    def verCarrito(self):
        car = tk.Tk()
        car.title("Carrito de compras")
        car.config(bg = "AntiqueWhite2")

        label0 = tk.Label(car, text = "CARRITO DE COMPRAS")
        label0.config(bg = "AntiqueWhite2", font = ("Open Sans", 20))
        label0.pack() #command = close_window

        label1 = tk.Label(car, text = "Articulos: ")
        label1.config(bg = "AntiqueWhite2", font = ("Open Sans", 15))
        label1.pack()

        #print "\nCarrito:\n"
        if self.a > 0: 
            label2 = tk.Label(car, text = "( " + str(self.a) + " ) " + aguaArt.getNombre())
            label2.config(bg = "AntiqueWhite2", font = ("Open Sans", 15))
            label2.place(x = 20, y = 70)

            label3 = tk.Label(car, text = aguaArt.getPrecio())
            label3.config(bg = "AntiqueWhite2", font = ("Open Sans", 15))
            label3.place(x = 170, y = 70)

            #print "Del Articulo {} son {}".format(self.aguaArt.getNombre(), self.a)


        if self.b > 0:
            label4 = tk.Label(car, text = "( " + str(self.b) + " ) " + cocaArt.getNombre())
            label4.config(bg = "AntiqueWhite2", font = ("Open Sans", 15))
            label4.place(x = 20, y = 110)

            label5 = tk.Label(car, text = cocaArt.getPrecio())
            label5.config(bg = "AntiqueWhite2", font = ("Open Sans", 15))
            label5.place(x = 170, y = 110)
            
            #print "Del Articulo {} son {}".format(self.cocaArt.getNombre(), self.b)

        if self.c > 0:
            label6 = tk.Label(car, text = "( " + str(self.c) + " ) " + cheeArt.getNombre())
            label6.config(bg = "AntiqueWhite2", font = ("Open Sans", 15))
            label6.place(x = 20, y = 150)

            label7 = tk.Label(car, text = cheeArt.getPrecio())
            label7.config(bg = "AntiqueWhite2", font = ("Open Sans", 15))
            label7.place(x = 170, y = 150)
            #print "Del Articulo {} son {}".format(self.cheeArt.getNombre(), self.c)

        label8 = tk.Label(car, text = "Total ")
        label8.config(bg = "AntiqueWhite2", font = ("Open Sans", 15))
        label8.place(x = 60, y = 190)


        label9 = tk.Label(car, text = self.muestraTotal())
        label9.config(bg = "AntiqueWhite2", font = ("Open Sans", 15))
        label9.place(x = 180, y = 190)

        b6 = tk.Button(car, text ="Regresar", command = (lambda: car.destroy()))
        b6.config(bg = "AntiqueWhite2", font = ("Open Sans", 15))
        b6.place(x = 85, y = 250)

aguaArt = Articulo(0001, "Agua", "Embotellada 1 lt", 15, 30, "No hay promocion", "13 marzo 2020")
cocaArt = Articulo(0002, "Coca-Cola", "Lata 600 ml", 10, 40, "No hay promocion", "13 marzo 2020")
cheeArt = Articulo(0003, "Cheetos", "Bolsa individual", 9, 12, "No hay promocion", "13 marzo 2020")

mi_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mi_socket.bind((socket.gethostname(), 8000)) #Host y pto

obj1 = pickle.dumps(aguaArt)
obj2 = pickle.dumps(cocaArt)
obj3 = pickle.dumps(cheeArt)
aux = 0

while True:
	
	data, address = mi_socket.recvfrom(4096)
	print("Conexion establecida con cliente ", address)
	print(data) #Mensaje de peticion

	if data == "Catalogo":
		print("Se envia catalogo a  ", address)
		mi_socket.sendto(obj1, address)
		time.sleep(1)

		mi_socket.sendto(obj2, address)
		time.sleep(1)

		mi_socket.sendto(obj3, address)
		time.sleep(1)

	if data == "Compra":
		respuesta = mi_socket.recv(1024) #1024 es el buffer = 1024 bytes
		compra = pickle.loads(respuesta)
		print("Se envia ticket a ", address)
		ticket = "El total a pagar:\n " + str(compra.muestraTotal())
		mi_socket.sendto(ticket, address)
		time.sleep(1)

	if data == "Imagenes":
		print("Se envian imagenes a  ", address)

		if aux == 0:
			i1 = open("agua.jpg", "rb")
			datos1 = i1.read(1024)
			while(datos1):
				mi_socket.sendto(datos1, address)
				datos1 = i1.read(1024)
			i1.close()
			print("img enviada")
			time.sleep(3)
			aux = 1

		if aux == 1:
			i2 = open("coca.jpg", "rb")
			datos2 = i2.read(1024)
			while(datos2):
				mi_socket.sendto(datos2, address)
				datos2 = i2.read(1024)
			i2.close()
			print("img enviada")
			time.sleep(2)
			aux = 2

		if aux == 2:
			i3 = open("papas.jpg", "rb")
			datos3 = i3.read(1024)
			while(datos3):
				mi_socket.sendto(datos3, address)
				datos3 = i3.read(1024)
			i3.close()
			print("img enviada")
			time.sleep(2)
			aux = 0


	
