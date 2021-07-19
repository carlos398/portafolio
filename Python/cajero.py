
# El cajero bancolombia de la esquina tiene dinero en billes de nomeclatura $100.000 / $50.000 / $20.000 / $10.000
# Opciones de retiro $20.000 / $50.000 / $100.000 / $200.000 / $600.000 / $1.000.000 y otros
# Cuantos billetes debo darle al cliente dependiendo del retiro que haga de la forma mas optima

def run():
    retiro = 0
    bitelle100 = 0
    billete50 = 0
    billete20 = 0
    billete10 = 0
    monto = int(input("Ingresa el monto que quieres robar: "))
    print("Vas a robar {}".format(monto))
    neto = monto

    if monto/100 > 0:
        bitelle100 = monto/100
        retiro = bitelle100*100
        monto = monto - retiro
        print(bitelle100, retiro,"100")
    if monto/50 > 0:
        bitelle50 = monto/50
        retiro = bitelle50*50
        monto = monto - retiro
        print(bitelle50 ,retiro,"50")
    if monto/20 > 0:
        bitelle20 = monto/20
        retiro = bitelle20*20
        monto = monto - retiro
        print(bitelle20, retiro, "20")
    if monto/10 > 0:
        billete10 = monto/10
        retiro = billete10*10
        monto = monto - retiro
        print(billete10, retiro, "10")


if __name__=="__main__":
    run()

