from ventas.cliente import Cliente
from ventas.base_de_datos import BaseDeDatos

cliente_1 = Cliente("adolfochef2017@gmail.com")
cliente_2 = Cliente("jose1738@gmail.com")
cliente_3 = Cliente("noeruiz@gmail.com")

cliente_1.registrar_compra("guitarra", 500)
cliente_1.registrar_compra("funda", 200)
cliente_1.registrar_compra("cuerdas", 50)

cliente_2.registrar_compra("guitarra", 700)
cliente_2.registrar_compra("funda", 400)
cliente_2.registrar_compra("cuerdas", 80)
cliente_3.registrar_compra("guitarra", 200)
cliente_3.registrar_compra("funda", 80)
cliente_3.registrar_compra("cuerdas", 20)


bd = BaseDeDatos()

bd.guardar_compras_de_cliente(cliente_1)
bd.guardar_compras_de_cliente(cliente_2)
bd.guardar_compras_de_cliente(cliente_3)

print(cliente_1)
cliente_1.imprimir_compras()
print(cliente_2)
cliente_2.imprimir_compras()
print(cliente_3)
cliente_3.imprimir_compras()
