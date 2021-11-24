class DNI:
    def __init__(self, dni, letra):
        self.dni = dni
        self.letra = letra
        print(dni, letra)

    # metodo get
    def get_dni(self, dni):
        return self.dni

    # metodo set
    def set_dni(self, dni):
        self.dni = dni

    def leer(self):
        print("Numero del DNI")
        numeroDNI = int(input())
        self.dni= numeroDNI

    def mostrar(self):
        print("El DNI es ", self.dni, "-", self.letra)

    def calcular(self):
        tablaLetras = {0: "T", 1: "R", 2: "W", 3: "A", 4: "G", 5: "M", 6: "Y", 7: "F", 8: "P", 9: "D", 10: "X", 11: "B",
                       12: "N", 13: "J", 14: "Z", 15: "S", 16: "Q", 17: "V", 18: "H", 19: "L", 20: "C", 21: "K", 22: "E"}

        resto = self.dni % 23
        print(resto)
        letraTablaDNI = tablaLetras[resto]
        self.letra = letraTablaDNI

dni1 = DNI(70, 7)
dni1.leer()
dni1.calcular()
dni1.mostrar()