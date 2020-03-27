from tkinter import *


class Interfaz:
    def __init__(self, ventana):
        # Crear la ventana raiz con titulo
        self.ventana = ventana
        self.ventana.title("Calculadora")
        self.ventana.iconbitmap(
            "C:/Users/jesus/OneDrive/Escritorio/Mi Espacio/codigos/estructura de datos/proyecto_cuarentena/pruebas/calculadora.ico")
        self.ventana.resizable(False, False)
        frame = Frame(self.ventana, width=248, height=219, background="#F7F7F7", padx=5, pady=5)
        frame.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        # Tablero
        self.tablero = Text(self.ventana, state="disabled", width=27, height=3, background="gray83", foreground="black",
                            font=("Helvetica", 12))
        self.tablero.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Operacion que se mostrará en tablero
        self.operation = ""

        # Botones
        boton1 = self.Crear_Boton_Numeros(7)
        boton1.place(x=7, y=70)
        boton2 = self.Crear_Boton_Numeros(8)
        boton2.place(x=68, y=70)
        boton3 = self.Crear_Boton_Numeros(9)
        boton3.place(x=129, y=70)
        boton4 = Button(self.ventana, text=(u"\u232B"), width="7", height=2,
                        command=lambda: self.click((u"\u232B"), False), background="#FD6868")  # Borrar
        boton4.place(x=191, y=70)
        boton5 = self.Crear_Boton_Numeros(4)
        boton5.place(x=7, y=113)
        boton6 = self.Crear_Boton_Numeros(5)
        boton6.place(x=68, y=113)
        boton7 = self.Crear_Boton_Numeros(6)
        boton7.place(x=129, y=113)
        boton8 = self.Crear_Boton_Operaciones(u"\u00F7")  # Division
        boton8.place(x=191, y=113)
        boton9 = self.Crear_Boton_Numeros(1)
        boton9.place(x=7, y=156)
        boton10 = self.Crear_Boton_Numeros(2)
        boton10.place(x=68, y=156)
        boton11 = self.Crear_Boton_Numeros(3)
        boton11.place(x=129, y=156)
        boton12 = self.Crear_Boton_Operaciones("*")
        boton12.place(x=191, y=156)
        boton13 = self.Crear_Boton_Numeros(".")
        boton13.place(x=7, y=199)
        boton14 = self.Crear_Boton_Numeros(0)
        boton14.place(x=68, y=199)
        boton15 = self.Crear_Boton_Operaciones("+")
        boton15.place(x=129, y=199)
        boton16 = self.Crear_Boton_Operaciones("-")
        boton16.place(x=191, y=199)
        boton17 = Button(self.ventana, text="=", width="16", height=2, command=lambda: self.click("=", False),
                         background="#99A4A4")
        boton17.place(x=6, y=242)
        boton18 = Button(self.ventana, text="AC", width="16", height=2, command=lambda: self.click("AC", False),
                         background="#FD6868")
        boton18.place(x=129, y=242)

    def Crear_Boton_Numeros(self, valor, escribir=True, ancho=7, alto=2):
        return Button(self.ventana, text=valor, width=ancho, height=alto, command=lambda: self.click(valor, escribir),
                      background="#C6CBCB", font=("Helvetica", 9))

    def Crear_Boton_Operaciones(self, valor, escribir=True, ancho=7, alto=2):
        return Button(self.ventana, text=valor, width=ancho, height=alto, command=lambda: self.click(valor, escribir),
                      background="#FFB300", font=("Helvetica", 9))

    def click(self, texto, escribir):
        # si es uno de los botones de Borrar o Igual (no deben mostrarce por tablero)
        self.operation = re.sub(u"\u00F7", "/",self.operation)  # sub remplaza "u"\u00F7" por "/" y lo guarda en el mismo string
        if not escribir:
            if texto == "=" and self.operation != "" and not self.operation[0] == "*" and not self.operation[0] == "/":
                resultado = str(eval(self.operation))
                self.operation = resultado
                self.Limpiar()
                self.Mostrar(resultado)
            elif texto == "AC":  # si es borrar
                self.operation = ""
                self.Limpiar()
            elif texto == u"\u232b":  # si es borrar
                self.operation = self.operation[:-1]
                self.Limpiar()
                self.Mostrar(self.operation)
        # Sino, si se muestra por tablero
        else:
            if self.operation == "":
                self.Limpiar()
                self.operation += str(texto)
                self.Mostrar(texto)
            else:
                self.operation += str(texto)
                self.Mostrar(texto)

    def Limpiar(self):
        self.tablero.configure(state="normal")
        self.tablero.delete("1.0", END)
        self.tablero.configure(state="disabled")
        return

    def Mostrar(self, valor):
        self.tablero.configure(state="normal")
        self.tablero.insert(END, valor)
        self.tablero.configure(state="disabled")
        return


root = Tk()
calculo = Interfaz(root)
root.mainloop()
