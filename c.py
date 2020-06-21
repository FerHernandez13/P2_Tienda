import socket
import pickle
import time
import Tkinter as tk
import tkMessageBox
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Tienda virtual")
root.config(bg = "lightblue")

def finaliza():
    obj = pickle.dumps(compra)

    print("Se envia compra")
    data = "Compra"
    #mi_socket.sendto(data, (socket.gethostname(), 8000))
    mi_socket.sendto(data, (socket.gethostname(), 8000))
    time.sleep(1)
    mi_socket.sendto(obj, (socket.gethostname(), 8000))
    time.sleep(1)
    ticket = mi_socket.recv(1024)
    compra.generaTicket()
    print(ticket)

class Articulo:
    def __init__(self, idd, nombre, descrip, precio, existen, promo, fecha_promo):
        self.idd = idd
        self.nombre = nombre
        self.descrip = descrip
        self.precio = precio
        self.existen = existen
        self.promo = promo
        self.fecha_promo = fecha_promo


    def describe(self):
        return "Descripcion:\n{}\n{}\n{}".format(self.nombre, self.descrip, self.promo)

    def getPrecio(self):
        return "Precio: $ {}".format(self.precio)

    def getNum(self):
        return int(self.precio)

    def getNombre(self):
        return self.nombre

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

    def generaTicket(self):
        tic = tk.Tk()
        tic.title("TICKET DE COMPRA")
        tic.config(bg = "dimgray")

        labelt0 = tk.Label(tic, text = "TICKET DE COMPRA")
        labelt0.config(bg = "dimgray", font = ("Open Sans", 20))
        labelt0.pack() 

        if self.a > 0: 
            labelt2 = tk.Label(tic, text = aguaArt.getNombre())
            labelt2.config(bg = "dimgray", font = ("Open Sans", 15))
            labelt2.place(x = 20, y = 70)

            labelt3 = tk.Label(tic, text = aguaArt.getPrecio() + " x " + str(self.a) + " = " + str(aguaArt.getNum() * self.a))
            labelt3.config(bg = "dimgray", font = ("Open Sans", 15))
            labelt3.place(x = 100, y = 70)

        if self.b > 0:
            labelt4 = tk.Label(tic, text = cocaArt.getNombre())
            labelt4.config(bg = "dimgray", font = ("Open Sans", 15))
            labelt4.place(x = 20, y = 110)

            labelt5 = tk.Label(tic, text = cocaArt.getPrecio() + " x " + str(self.b) + " = " + str(cocaArt.getNum() * self.b))
            labelt5.config(bg = "dimgray", font = ("Open Sans", 15))
            labelt5.place(x = 100, y = 110)

        if self.c > 0:
            labelt6 = tk.Label(tic, text = cheeArt.getNombre())
            labelt6.config(bg = "dimgray", font = ("Open Sans", 15))
            labelt6.place(x = 20, y = 150)

            labelt7 = tk.Label(tic, text = cheeArt.getPrecio() + "  x  " + str(self.c) + "  = " + str(cheeArt.getNum() * self.c))
            labelt7.config(bg = "dimgray", font = ("Open Sans", 15))
            labelt7.place(x = 100, y = 150)

        labelt8 = tk.Label(tic, text = "Total:")
        labelt8.config(bg = "dimgray", font = ("Open Sans", 25))
        labelt8.place(x = 20, y = 200)


        labelt9 = tk.Label(tic, text = self.muestraTotal())
        labelt9.config(bg = "dimgray", font = ("Open Sans", 25))
        labelt9.place(x = 200, y = 200)
      

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

mi_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

########Envio de catalogo
data = "Catalogo"

mi_socket.sendto(data, (socket.gethostname(), 8000)) #direccion, pto

respuesta1 = mi_socket.recv(1024) #1024 es el buffer = 1024 bytes
aguaArt = pickle.loads(respuesta1)
#print(agua)

respuesta2 = mi_socket.recv(1024) #1024 es el buffer = 1024 bytes
cocaArt = pickle.loads(respuesta2)
#print(coca)

respuesta3 = mi_socket.recv(1024) #1024 es el buffer = 1024 bytes
cheeArt = pickle.loads(respuesta3)
#print(chee)
"""
########Solicitud de imagenes

data = "Imagenes"

mi_socket.sendto(data, (socket.gethostname(), 8000)) #direccion, pto

img1 = open("agua.jpg", "wb")
for x in range (0, 18): 
    #print("en while")
    datos1 = mi_socket.recv(1024)
    img1.write(datos1)
img1.close()
print("img recibida")
time.sleep(1)

data = "Imagenes"

mi_socket.sendto(data, (socket.gethostname(), 8000)) 

img2 = open("coca.jpg", "wb")
for x in range (0, 18): 
    #print("en while")
    datos2 = mi_socket.recv(1024)
    img2.write(datos2)
img2.close()
print("img recibida")
time.sleep(1)

data = "Imagenes"

mi_socket.sendto(data, (socket.gethostname(), 8000)) 

img3 = open("papas.jpg", "wb")
for x in range (0, 18): 
    #print("en while")
    datos3 = mi_socket.recv(1024)
    img3.write(datos3)
img3.close()
print("img recibida")
time.sleep(1)
"""
####Interfaz grafica

label = tk.Label(root, text = "BIENVENIDO A LA TIENDA")
label.config(bg = "lightblue", font = ("Open Sans", 35))
label.pack() 


agua = ImageTk.PhotoImage(Image.open("agua.jpg"))
labelAgua = tk.Label(root, image = agua)
labelAgua.place(x = 80, y = 100)


coca = ImageTk.PhotoImage(Image.open("coca.jpg"))
labelCoca = tk.Label(root, image = coca)
labelCoca.place(x = 80, y = 270)


chee = ImageTk.PhotoImage(Image.open("papas.jpg"))
labelChee = tk.Label(root, image = chee)
labelChee.place(x = 80, y = 440)

labelArt1 = tk.Label(root, text = aguaArt.describe())
labelArt1.config(bg = "lightblue", font = ("Open Sans", 18))
labelArt1.place(x = 400, y = 100)

labelArt2 = tk.Label(root, text = cocaArt.describe())
labelArt2.config(bg = "lightblue", font = ("Open Sans", 18))
labelArt2.place(x = 400, y = 270)

labelArt3 = tk.Label(root, text = cheeArt.describe())
labelArt3.config(bg = "lightblue", font = ("Open Sans", 18))
labelArt3.place(x = 400, y = 440)

labelArt1p = tk.Label(root, text = aguaArt.getPrecio())
labelArt1p.config(bg = "lightblue", font = ("Open Sans", 25))
labelArt1p.place(x = 750, y = 100)

labelArt2p = tk.Label(root, text = cocaArt.getPrecio())
labelArt2p.config(bg = "lightblue", font = ("Open Sans", 25))
labelArt2p.place(x = 750, y = 270)

labelArt3p = tk.Label(root, text = cheeArt.getPrecio())
labelArt3p.config(bg = "lightblue", font = ("Open Sans", 25))
labelArt3p.place(x = 750, y = 440)

compra = Compra(0, aguaArt, cocaArt, cheeArt)

b1 = tk.Button(root, text ="Agregar al carrito", command = (lambda: compra.agregarCarrito(1)))
b1.config(bg = "tan1", font = ("Open Sans", 15))
b1.place(x = 1050, y = 150)

b2 = tk.Button(root, text ="Agregar al carrito", command = (lambda: compra.agregarCarrito(2)))
b2.config(bg = "tan1", font = ("Open Sans", 15))
b2.place(x = 1050, y = 320)

b3 = tk.Button(root, text ="Agregar al carrito", command = (lambda: compra.agregarCarrito(3)))
b3.config(bg = "tan1", font = ("Open Sans", 15))
b3.place(x = 1050, y = 490)

b4 = tk.Button(root, text ="Ver Carrito", command = (lambda: compra.verCarrito()))
b4.config(bg = "deepskyblue", font = ("Open Sans", 15))
b4.place(x = 450, y = 620) 

b5 = tk.Button(root, text ="Finalizar Compra", command = finaliza)
b5.config(bg = "springgreen2", font = ("Open Sans", 15))
b5.place(x = 750, y = 620)

root.mainloop()


#compra.muestraTotal()




mi_socket.close()