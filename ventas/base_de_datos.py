import json


class BaseDeDatos:

    def guardar_compras_de_cliente(self, cliente):
        nombre_de_archivo = f"{cliente.email}.json"
        with open(nombre_de_archivo, "w") as outfile:
            compras_a_texto = json.dumps(cliente.compras)
            outfile.write(compras_a_texto)

    def cargar_compras_de_cliente(self, cliente):
        nombre_de_archivo = f"{cliente.email}.json"
        with open(nombre_de_archivo, "r") as infile:
            compras_a_texto = infile.read()
            compras = json.loads(compras_a_texto)
        return compras