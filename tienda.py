import Tkinter as tk
import tkMessageBox
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Tienda virtual")
root.config(bg = "lightblue")

def agregar():
    pass



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

#Variables dinamicas de texto

#texto = StringVar()
#texto.set ("Un texto dinamico")
#label.config(textvariable = texto)

#Imagenes en labels
#imagen = PhotoImage(file = "ruta") Solo acepta .gif
#label (root, image = imagen).pack

#label.grid(row = 0, column = 0)

#Botones
#Button(root, text ="Comprar", command=Comprar).pack()
"""
frame = tk.Frame(root, width = 1500, height = 700)
frame.pack(fill = 'both', expand = 1)
frame.config(bg = "lightblue")
"""
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

aguaArt = Articulo(0001, "Agua", "Embotellada 1 lt", 15, 30, "No hay promocion", "13 marzo 2020")
cocaArt = Articulo(0002, "Coca-Cola", "Lata 600 ml", 10, 40, "No hay promocion", "13 marzo 2020")
cheeArt = Articulo(0003, "Cheetos", "Bolsa individual", 9, 12, "No hay promocion", "13 marzo 2020")

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

b1 = tk.Button(root, text ="Agregar al carrito", command=agregar)
b1.config(bg = "tan1", font = ("Open Sans", 15))
b1.place(x = 1050, y = 150)

b2 = tk.Button(root, text ="Agregar al carrito", command=agregar)
b2.config(bg = "tan1", font = ("Open Sans", 15))
b2.place(x = 1050, y = 320)

b3 = tk.Button(root, text ="Agregar al carrito", command=agregar)
b3.config(bg = "tan1", font = ("Open Sans", 15))
b3.place(x = 1050, y = 490)

b4 = tk.Button(root, text ="Ver Carrito", command=agregar)
b4.config(bg = "deepskyblue", font = ("Open Sans", 15))
b4.place(x = 450, y = 620) 

b5 = tk.Button(root, text ="Finalizar Compra", command=agregar)
b5.config(bg = "springgreen2", font = ("Open Sans", 15))
b5.place(x = 750, y = 620)

root.mainloop()