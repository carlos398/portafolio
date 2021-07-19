class automovil:


    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en reposo'
        self._motor = motor(cilindros=4)
    

    def aceleracion(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyectar_gasolina(10)
        else:
            self._motor.inyectar_gasolina(4)
        
        self._estado = 'en movimiento'


class motor:


    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self.temperatura = 0
    

    def inyectar_gasolina(self, cantidad):
        self.cantidad = cantidad
        