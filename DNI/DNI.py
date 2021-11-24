class DNI:
    # CONTRUCTOR VACIO.
    def __init__(self):
        self.numero
        self.letra

    # CONTRUCTOR CON PARAMETROS.
    def __init__(self, numero, letra):
        self.numero = numero
        self.letra = letra

    # METODOS
    def get_dni(self, numero):
        return self.numero

    def set_dni(self, numero):
        self.numero = numero

    def leer(self):
        print("Numero del DNI: ", end='')
        numero = int(input())
        self.numero = numero

    def mostrarDNI(self):
        self.calcular()
        print("El DNI es: ", self.numero, "-", self.letra)

    def calcular(self):
        letras = tablaLetras = {0: "T", 1: "R", 2: "W", 3: "A", 4: "G", 5: "M", 6: "Y", 7: "F", 8: "P", 9: "D", 10: "X",
                                11: "B", 12: "N", 13: "J", 14: "Z", 15: "S", 16: "Q", 17: "V", 18: "H", 19: "L",
                                20: "C", 21: "K", 22: "E"}
        resto = self.numero % 23
        letra = tablaLetras[resto]
        self.letra = letra


# COMIENZO DE PRUEBAS.
dni = DNI(1, 2)
dni.leer()
dni.mostrarDNI()
