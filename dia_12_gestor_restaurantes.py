from tkinter import *
import re
import os 
from pathlib import Path
from tkinter import filedialog, messagebox
from random import randint as rd
from datetime import date, datetime

# iniciar tkinter
aplicacion = Tk()#Cuando creas una instancia de esta clase (Tk()), estás creando una ventana principal para tu aplicación.

# Calcula el ancho y alto de la pantalla
ancho_pantalla = aplicacion.winfo_screenwidth()#devuelve el ancho de nuestra pantalla
alto_pantalla = aplicacion.winfo_screenheight()#devuelve el alto de nuestra pantalla

# tamaño de la ventana
aplicacion.geometry('1020x630+{}+{}'.format(int((ancho_pantalla/2)-(1020/2)), int((alto_pantalla/2)-(630/2))))

# evitar maximizar ventana en eje "x" y "y"
aplicacion.resizable(0, 0) 

# titulo de la ventana
aplicacion.title("Mi Restarante - Sistema de Facturación")

# configurar el background o color de la ventana
aplicacion.config(bg="blanched almond")

# frame o marco superior
marco_superior = Frame(aplicacion, bd=2, relief=FLAT, bg="BlueViolet")#elieve es simplemente una apariencia visual que se agrega alrededor del widget para resaltar o darle una apariencia tridimensional.
marco_superior.pack(side=TOP, pady=(15, 0))

etiqueta_titulo = Label(marco_superior, text="Sistema de Facturación", fg="white", font=('Dosis', 58), bg='BlueViolet' , width=22)
etiqueta_titulo.grid(row=0, column=0)

# frame o marco izquierdo
marco_izquierdo = Frame(aplicacion, bd=2, relief=FLAT, bg="BlueViolet", padx=10, pady=10)
marco_izquierdo.pack(side=LEFT, padx=10)

# frame o marco izquierdo > superior
panel_menu = Frame(marco_izquierdo, bd=2, relief=FLAT, bg="orange", padx=10, pady=10)#elieve es simplemente una apariencia visual que se agrega alrededor del widget para resaltar o darle una apariencia tridimensional.
panel_menu.pack(side=TOP)

panel_comida = LabelFrame(panel_menu, text="Comidas", labelanchor="n", fg="white", font=('Dosis', 18, 'bold'), bd=1, relief=FLAT, bg="green", padx=5)
panel_comida.pack(side=LEFT)

panel_bebida= LabelFrame(panel_menu, text="Bebidas", labelanchor="n", fg="white", font=('Dosis', 18, 'bold'), bd=1, relief=FLAT, bg="green",  padx=5)
panel_bebida.pack(side=LEFT, padx=(10, 10))

panel_postres = LabelFrame(panel_menu, text="Postres", labelanchor="n", fg="white", font=('Dosis', 18, 'bold'), bd=1, relief=FLAT, bg="green",  padx=5)
panel_postres.pack(side=LEFT)

# frame o marco izquierdo < inferior
panel_costos = Frame(marco_izquierdo, bd=2, relief=FLAT, bg="orange", width=584, height=120, padx=54, pady=11)
panel_costos.pack(side=BOTTOM, pady=(10, 0))

# frame o marco derecho
panel_derecho = Frame(aplicacion, bd=2, relief=FLAT, bg="BlueViolet", padx=10, pady=10)#elieve es simplemente una apariencia visual que se agrega alrededor del widget para resaltar o darle una apariencia tridimensional.
panel_derecho.pack(side=LEFT)

panel_calculadora = Frame(panel_derecho, bd=1, relief=FLAT, bg="green", width=357, height=188)
panel_calculadora.pack(side=TOP)

panel_recibo = Frame(panel_derecho, bd=1, relief=FLAT, bg="green",  width=357, height=178)
panel_recibo.pack(side=TOP, pady=(10, 10))

panel_botones = Frame(panel_derecho, bd=1, relief=FLAT, bg="BlueViolet",  width=357, height=78)
panel_botones.pack(side=TOP)

# lista de productos
lista_comidas = ["Hamburguesa", "Pizza", "Tacos", "Hot Dog", "Pollo Frito", "Ensalada", "Sopa", "Sandwich"]
lista_bebidas = ["Coca Cola", "Pepsi", "Fanta", "7 Up", "Agua", "Cerveza", "Vino", "Whisky"]
lista_postres = ["Pastel", "Helado", "Gelatina", "Flan", "Cupcake", "Galletas", "Churros", "Chocolate"]

# lista de instancia de la clase IntVar que nos permitirá almacenar el estado de los Checkbutton seleccionados
lista_valores_comidas = []
cuadros_comidas = []
texto_comidas = []

def verificar_click_Checkbutton_comidas():
    for indice, valor in enumerate(lista_valores_comidas):
        if valor.get() == 1:
            cuadros_comidas[indice].config(state="normal")
            cuadros_comidas[indice].focus()
            if texto_comidas[indice].get() == "0":
                texto_comidas[indice].set("")
        else:
            cuadros_comidas[indice].config(state="disabled")
            texto_comidas[indice].set("0")

for indice, comida in enumerate(lista_comidas):
    # crear los checkbutton de comidas
    lista_valores_comidas.append("")
    lista_valores_comidas[indice] = IntVar()
    comida = Checkbutton(panel_comida, 
                         text=comida, 
                         variable=lista_valores_comidas[indice], 
                         font=('Dosis', 14), 
                         bg="green", 
                         fg="LightGrey", 
                         selectcolor="orange", 
                         onvalue=1, 
                         offvalue=0, 
                         command=verificar_click_Checkbutton_comidas,
                         activebackground="orange")
    comida.grid(row=indice, 
                column=0, 
                sticky=W)

    #crear cuadros de entrada
    cuadros_comidas.append("")
    texto_comidas.append("")
    texto_comidas[indice] = StringVar()
    cuadros_comidas[indice] = Entry(panel_comida, 
                                    font=('Dosis', 14), 
                                    width=3, 
                                    state="disabled",
                                    justify="center", 
                                    textvariable=texto_comidas[indice])
    cuadros_comidas[indice].grid(row=indice, 
                                 column=1,)
    texto_comidas[indice].set("0")



lista_valores_bebidas = []
cuadros_bebidas = []
texto_bebidas = []
def verificar_click_Checkbutton_bebidas():
    for indice, valor in enumerate(lista_valores_bebidas):
        if valor.get() == 1:
            cuadros_bebidas[indice].config(state="normal")
            cuadros_bebidas[indice].focus()
            if texto_bebidas[indice].get() == '0':
                texto_bebidas[indice].set("")
        else:
            cuadros_bebidas[indice].config(state="disabled")
            texto_bebidas[indice].set("0")

# crear los checkbutton de bebidas
for indice, bebida in enumerate(lista_bebidas):
    # crear checkbutton
    lista_valores_bebidas.append("")
    lista_valores_bebidas[indice] = IntVar()
    bebida = Checkbutton(panel_bebida, 
                         text=bebida, 
                         variable=lista_valores_bebidas[indice],
                         font=('Dosis', 14), 
                         bg="green", 
                         fg="LightGrey", 
                         selectcolor="orange", 
                         onvalue=1, 
                         offvalue=0, 
                         command=verificar_click_Checkbutton_bebidas,
                         activebackground="orange")
    bebida.grid(row=indice, 
                column=0, 
                sticky=W)

    #crear cuadros de entrada
    cuadros_bebidas.append("")
    texto_bebidas.append("")
    texto_bebidas[indice] = StringVar()
    cuadros_bebidas[indice] = Entry(panel_bebida, 
                                    font=('Dosis', 14), 
                                    width=3, 
                                    state="disabled", 
                                    justify="center",
                                    
                                    textvariable=texto_bebidas[indice])
    cuadros_bebidas[indice].grid(row=indice, 
                                 column=1)
    texto_bebidas[indice].set("0")

lista_valores_postres = []
cuadros_postres = []
texto_postres = []

def verificar_click_Checkbutton_postres():
    for indice, valor in enumerate(lista_valores_postres):
        if valor.get() == 1:
            cuadros_postres[indice].config(state="normal")
            cuadros_postres[indice].focus()
            if texto_postres[indice].get() == '0':
                texto_postres[indice].set("")
        else:
            cuadros_postres[indice].config(state="disabled")
            texto_postres[indice].set("0")

# crear los checkbutton de postres
for indice, postre in enumerate(lista_postres):
    # crear checkbutton
    lista_valores_postres.append("")
    lista_valores_postres[indice] = IntVar()
    postre = Checkbutton(panel_postres, 
                         text=postre, 
                         variable=lista_valores_postres[indice], 
                         font=('Dosis', 14), 
                         bg="green", 
                         fg="LightGrey", 
                         selectcolor="orange", 
                         onvalue=1, 
                         offvalue=0, 
                         command=verificar_click_Checkbutton_postres,
                         activebackground="orange")
    postre.grid(row=indice, 
                column=0, 
                sticky=W)

    #crear cuadros de entrada
    cuadros_postres.append("")
    texto_postres.append("")
    texto_postres[indice] = StringVar()
    cuadros_postres[indice] = Entry(panel_postres, 
                                    font=('Dosis', 14), 
                                    width=3, 
                                    state="disabled", 
                                    justify="center",
                                    # validate="key",
                                    # validatecommand=(aplicacion.register(validar_entrada), "%P"),
                                    textvariable=texto_postres[indice])
    cuadros_postres[indice].grid(row=indice, 
                                 column=1)
    texto_postres[indice].set("0")

ver_costo_comida = StringVar()
ver_costo_bebida = StringVar()
ver_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()


# etiqueta costo comida
etiqueta_costo_comida = Label(panel_costos,
                              text="Comidas:", 
                              fg="White", 
                              font=('Dosis', 18, 'bold'), 
                              bg="orange",
                              bd=1, 
                              relief=FLAT,
                              )

etiqueta_costo_comida.grid(row=0, column=0, sticky="e")

# text comida costo
texto_comida_costo = Entry(panel_costos,
                           font=('Dosis', 18, 'bold'),
                           bd=1,
                           width=6,
                           state='readonly',
                           justify="center",
                           textvariable=ver_costo_comida
                           )
texto_comida_costo.grid(row=0, column=1, padx=(5, 0))

# etiqueta costo bebida
etiqueta_costo_bebida = Label(panel_costos,
                              text="Bebidas:", 
                              fg="White", 
                              font=('Dosis', 18, 'bold'), 
                              bg="orange",
                              bd=1, 
                              relief=FLAT,
                              )

etiqueta_costo_bebida.grid(row=1, column=0, sticky="e")

# text bebida costo
texto_bebida_costo = Entry(panel_costos,
                           font=('Dosis', 18, 'bold'),
                           bd=1,
                           width=6,
                           state='readonly',
                           justify="center",
                           textvariable=ver_costo_bebida
                           )
texto_bebida_costo.grid(row=1, column=1, padx=(5, 0))

# etiqueta costo postre
etiqueta_costo_postre = Label(panel_costos,
                              text="Postres:", 
                              fg="White", 
                              font=('Dosis', 18, 'bold'), 
                              bg="orange",
                              bd=1, 
                              relief=FLAT,
                              )

etiqueta_costo_postre.grid(row=2, column=0, sticky="e")

# text postre costo
texto_postre_costo = Entry(panel_costos,
                           font=('Dosis', 18, 'bold'),
                           bd=1,
                           width=6,
                           state='readonly',
                           justify="center",
                           textvariable=ver_costo_postre
                           )
texto_postre_costo.grid(row=2, column=1, padx=(5, 0))


# etiqueta subtotal
etiqueta_subtotal = Label(panel_costos,
                              text="Sub total:", 
                              fg="White", 
                              font=('Dosis', 18, 'bold'), 
                              bg="orange",
                              bd=1, 
                              relief=FLAT,
                              )

etiqueta_subtotal.grid(row=0, column=2, padx=(60, 0), sticky="e")
# text subtotal
texto_subtotal = Entry(panel_costos,
                           font=('Dosis', 18, 'bold'),
                           bd=1,
                           width=6,
                           state='readonly',
                           justify="center",
                           textvariable=var_subtotal
                           )
texto_subtotal.grid(row=0, column=3, padx=(5, 0))

# etiqueta impuesto
etiqueta_impuesto = Label(panel_costos,
                              text="Impuesto:", 
                              fg="White", 
                              font=('Dosis', 18, 'bold'),
                              bg="orange", 
                              bd=1, 
                              relief=FLAT,
                              )

etiqueta_impuesto.grid(row=1, column=2, padx=(60, 0), sticky="e")
# text impuesto
texto_impuesto = Entry(panel_costos,
                           font=('Dosis', 18, 'bold'),
                           bd=1,
                           width=6,
                           state='readonly',
                           justify="center",
                           textvariable=var_impuesto
                           )
texto_impuesto.grid(row=1, column=3, padx=(5, 0))

# etiqueta total
etiqueta_total = Label(panel_costos,
                              text="Total:", 
                              fg="White", 
                              bg="orange",
                              font=('Dosis', 18, 'bold'), 
                              bd=1, 
                              relief=FLAT,
                              )

etiqueta_total.grid(row=2, column=2, padx=(60, 0), sticky="e")
# text total
texto_total = Entry(panel_costos,
                           font=('Dosis', 18, 'bold'),
                           bd=1,
                           width=6,
                           state='readonly',
                           justify="center",
                           textvariable=var_total
                           )
texto_total.grid(row=2, column=3, padx=(5, 0))

precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


total_comidas = 0
total_bebidas = 0
total_postres = 0
subtotal = 0
impuesto = 0
total_comprado = 0
total_alimentos_comprados = 0
def total():
    global total_comidas
    global total_bebidas
    global total_postres
    total_comidas = 0
    total_bebidas = 0
    total_postres = 0
    global subtotal
    global impuesto
    global total_comprado
    global total_alimentos_comprados

    

    #Calcular cantidades de comidas, bebidas y postres por su precio
    indice = 0
    for v_comidas, v_bebidas, v_postres in zip(lista_valores_comidas, lista_valores_bebidas, lista_valores_postres):
        if v_comidas.get() == 1:
            total_comidas += int(texto_comidas[indice].get())*precios_comida[indice]
        if v_bebidas.get() == 1:
            total_bebidas += int(texto_bebidas[indice].get())*precios_bebida[indice]
        if v_postres.get() == 1:
            total_postres += int(texto_postres[indice].get())*precios_postres[indice]
        indice += 1   

    #Mostrar precio totales individuales de comidas, bebidas y postres a comprar
    if total_comidas+total_bebidas+total_postres != 0:
        ver_costo_comida.set(str(round(total_comidas, 1)))
        ver_costo_bebida.set(str(round(total_bebidas, 1)))
        ver_costo_postre.set(str(round(total_postres, 1)))

        #Calcular y mostrar subtotal
        subtotal = round(total_comidas+total_bebidas+total_postres, 1)
        var_subtotal.set(str(subtotal))

        #Calcular y mostrar impuesto
        impuesto = round(subtotal*0.07)
        var_impuesto.set(str(impuesto))

        #calcular y mostrar total
        total_comprado = round(subtotal+impuesto, 1)
        var_total.set(str(total_comprado))



texto_recibo_actual = ""
def recibo():
    global texto_recibo_actual
    codigo = f'R#-{rd(1, 1000)}'
    fecha = date.today()
    fecha_actual = "%02d/%02d/%04d" % (fecha.day, fecha.month, fecha.year)
    hora = datetime.now().time()
    hora_actual = "%02d:%02d" % (hora.hour, hora.minute)
    texto_recibo.delete('1.0', 'end') 
    texto_recibo_actual = ""
    costos = total_comidas + total_bebidas + total_postres + subtotal + impuesto + total_comprado 
    if costos != 0:
        texto_recibo_actual = \
        f"""
        ------------------------------------------------------------
        {codigo}         fecha y hora: {fecha_actual} {hora_actual}
        ------------------------------------------------------------
                            Restaurant Rosario

        1:  Comidas               ${round(total_comidas, 1)}
        2:  Bebidas               ${round(total_bebidas, 1)}
        3:  Postres               ${round(total_postres, 1)}
        ------------------------------------------------------------
        Subtotal                  ${subtotal} 
        Impuesto                  ${impuesto} 
        TOTAL                     ${total_comprado} 
        ------------------------------------------------------------
        """
        texto_recibo.insert(END, texto_recibo_actual)

def guardar():
    # ruta_general  = os.getcwd()
    # nombre_archivo = "rosario_1.txt"
    # ruta_actual = Path(ruta_general, os.listdir()[3], nombre_archivo)
    if texto_recibo_actual != "":
        archivo = filedialog.asksaveasfile(mode="w", defaultextension='.txt')
        archivo.write(texto_recibo_actual)
        archivo.close()
        messagebox.showinfo('Information', 'Su recibo ha sido guardado')


def resetear():

    #resetear whidgets mostrados
    texto_recibo.delete('1.0', 'end') 
    ver_costo_comida.set("")
    ver_costo_bebida.set("")
    ver_costo_postre.set("")
    var_subtotal.set("")
    var_impuesto.set("")
    var_total.set("")
    indice = 0
    for v_comidas, v_bebidas, v_postres in zip(lista_valores_comidas, lista_valores_bebidas, lista_valores_postres):
        if v_comidas.get() == 1:
            cuadros_comidas[indice].config(state="disabled")
            texto_comidas[indice].set("0")
            v_comidas.set(0)
        if v_bebidas.get() == 1:
            cuadros_bebidas[indice].config(state="disabled")
            texto_bebidas[indice].set("0")
            v_bebidas.set(0)
        if v_postres.get() == 1:
            cuadros_postres[indice].config(state="disabled")
            texto_postres[indice].set("0")
            v_postres.set(0)
        indice += 1   
    print("reseteado correctamente")

def llamar_funciones(indice):
    funciones_botones[indice]()
#botones
botones = ["total", "recibo", "guardar", "resetear"]
funciones_botones = [total, recibo, guardar, resetear]


for indice, bot in enumerate(botones):
    boton = Button(panel_botones,
                   text=bot,
                   font=('Dosis', 14, 'bold'),
                   fg='White',
                   bg='green',
                   width=7,
                   command=lambda indice = indice: llamar_funciones(indice),
                   bd=1
                   )
    boton.grid(row=0, column=indice, pady=24)


#area recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=9
                    )
texto_recibo.grid(row=0, column=0)

#calculadora 
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          width=31,
                          bd=1
                          )
visor_calculadora.grid(row=0, column=0, columnspan=4)



#CALCULANDO OPERACIONES
lista_ordenada_operadores = []

#ejemplos
# / - + * => / + * => / *
# + / - * => / - * => /*
# * / + - => * / - => * /
# + -
# * /
# +
def ordenar_operadores(lis_ord_oper, indice):
    if indice < len(lis_ord_oper): 
        if lis_ord_oper[indice] == "+" or lis_ord_oper[indice] == "-":
            lista_ordenada_operadores.append(lis_ord_oper[indice])
            lis_ord_oper.pop(indice)
            ordenar_operadores(lis_ord_oper, indice)
        else:
            ordenar_operadores(lis_ord_oper, indice+1)
    lista = lis_ord_oper + lista_ordenada_operadores
    # print(f"flista_ordenada_operadores {lista_ordenada_operadores}")
    return lista
def operacion_matematica(numeros_operadores, lista_orden_oper, indice):
    if numeros_operadores[indice] == "+" and numeros_operadores[indice] == lista_orden_oper[0]:
        resultado = int(numeros_operadores[indice-1]) + int(numeros_operadores[indice+1])
        numeros_operadores[indice] = resultado
        numeros_operadores.pop(indice+1)
        numeros_operadores.pop(indice-1)
        indice = 1
        lista_orden_oper.pop(0)
        if len(numeros_operadores) == 1:
            return resultado
        return operacion_matematica(numeros_operadores, lista_orden_oper, indice)
    elif numeros_operadores[indice] == "-" and numeros_operadores[indice] == lista_orden_oper[0]:
        resultado = int(numeros_operadores[indice-1]) - int(numeros_operadores[indice+1])
        numeros_operadores[indice] = resultado
        numeros_operadores.pop(indice+1)
        numeros_operadores.pop(indice-1)
        indice = 1
        lista_orden_oper.pop(0)
        if len(numeros_operadores) == 1:
            return resultado
        return operacion_matematica(numeros_operadores, lista_orden_oper, indice)
    elif numeros_operadores[indice] == "*" and numeros_operadores[indice] == lista_orden_oper[0]:
        resultado = int(numeros_operadores[indice-1]) * int(numeros_operadores[indice+1])
        numeros_operadores[indice] = resultado
        numeros_operadores.pop(indice+1)
        numeros_operadores.pop(indice-1)
        indice = 1
        lista_orden_oper.pop(0)
        if len(numeros_operadores) == 1:
            return resultado
        return operacion_matematica(numeros_operadores, lista_orden_oper, indice)
    elif numeros_operadores[indice] == "/" and numeros_operadores[indice] == lista_orden_oper[0]:
        resultado = int(numeros_operadores[indice-1]) / int(numeros_operadores[indice+1])
        numeros_operadores[indice] = resultado
        numeros_operadores.pop(indice+1)
        numeros_operadores.pop(indice-1)
        indice = 1
        lista_orden_oper.pop(0)
        if len(numeros_operadores) == 1:
            return resultado
        return operacion_matematica(numeros_operadores, lista_orden_oper, indice)
    else:
        return operacion_matematica(numeros_operadores, lista_orden_oper, indice+2)
  

indice_operacion = -1

def insertar_valor_botones(numero):
    global indice_operacion
    global lista_ordenada_operadores
    if numero == 'R':
        indice_operacion = 0
        cadena = visor_calculadora.get()
        numeros_operadores = re.findall(r'\d+|[\+\-\*\/]', cadena)
        print(numeros_operadores)
        lis_ord_oper = [numeros_operadores[indice] for indice in range(1, len(numeros_operadores), 2)] 
        lista_orden_oper = ordenar_operadores(lis_ord_oper, indice=0)
        resultado_operacion = operacion_matematica(numeros_operadores, lista_orden_oper, indice=1)
        visor_calculadora.delete(0, END)
        visor_calculadora.insert(indice_operacion, resultado_operacion)
        lista_ordenada_operadores = []
    elif numero == "B":
        visor_calculadora.delete(0, END)
    else:
        indice_operacion+=1
        visor_calculadora.insert(indice_operacion, numero)
        print(visor_calculadora.get())
        



botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '*', 'R', 'B', '0', '/']
variable_button = []
fila = 1
columna = 0
for bot in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=bot,
                   font=('Dosis', 14, 'bold'),
                   fg='White',
                   bg='green',
                   bd=1,
                   width=7,
                   command=lambda bot = bot: insertar_valor_botones(bot),
                   )
    boton.grid(row=fila, column=columna, sticky="w")
    if (columna+1) % 4 == 0:
        fila+=1
        columna = 0
    else:
        columna += 1




# evitar que se cierre nuestra ventana bebida
aplicacion.mainloop()


