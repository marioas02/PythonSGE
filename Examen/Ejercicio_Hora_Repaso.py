class Hora:

    def __init__(self):
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.segundos = 0

    def __init__(self, horas, minutos, segundos):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
        self.validar()

    def leer(self):
        print("Introduce las horas: ")
        self.horas = int(input())
        print("Introduce los minutos: ")
        self.minutos = int(input())
        print("Introduce los segundos: ")
        self.segundos = int(input())
        self.validar()

    def validar(self):
        if (self.horas < 0 or self.horas > 23):
            self.horas = 0
        if (self.minutos < 0 or self.minutos > 59):
            self.minutos = 0
        if (self.segundos < 0 or self.segundos > 59):
            self.segundos = 0

    def print(self):
        if (self.horas < 10):
            print("0", end='')
        print(self.horas, ":", end='')
        if (self.minutos < 10):
            print("0", end='')
        print(self.minutos, ":", end='')
        if (self.segundos < 10):
            print("0", end='')
        print(self.segundos)

    def aSegundos(self):
        segundos = self.horas * 3600 + self.minutos * 60 + self.segundos
        return segundos

    def deSegundos(self, segundos):
        self.horas = int(segundos / 3600)
        segundos = segundos % 3600
        self.minutos = int(segundos / 60)
        segundos = segundos % 60
        self.segundos = segundos
        return segundos

    def segundosDesde(self, hora):
        segundos = self.aSegundos() - hora.aSegundos()
        return segundos

    def siguiente(self):
        self.segundos += 1
        if self.segundos == 60:
            self.segundos = 0
            self.minutos += 1
        if self.minutos == 60:
            self.minutos = 0
            self.horas += 1
        if self.horas == 24:
            self.horas = 0

    def anterior(self):
        self.segundos -= 1
        if self.segundos == -1:
            self.segundos = 59
            self.minutos -= 1
        if self.minutos == -1:
            self.minutos = 59
            self.horas -= 1
        if self.horas == -1:
            self.horas = 23

    def igualQue(self, hora):
        if hora.aSegundos() == self.aSegundos():
            return True
        else:
            return False


h1 = Hora(10, 5, 6)
h1.print()
h1.leer()
h1.print()
segundos = h1.aSegundos()
print("Segundos: ", segundos)
h1.deSegundos(25000)
h1.print()
h1 = Hora(1, 0, 0)
h2 = Hora(2, 0, 0)
print(h1.segundosDesde(h2))
h2.siguiente()
h2.print()
