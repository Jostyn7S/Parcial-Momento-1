monto = int(input("Ingrese el monto de la compra:"))

if (monto < 50):
    D=0
    Valores=monto
elif (monto <= 50 and monto <= 100):
    descuento=monto/0.05
    Valores=monto-descuento
elif (monto>100):
    descuento=monto/10
    Valores=monto-descuento

    print(f"Descuento aplicado:${descuento:.1f}")
    print(f"Total a pagar:${monto-descuento:.1f}")