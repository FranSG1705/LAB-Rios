from typing import NamedTuple

Rio = NamedTuple("Rio", [("nombre",str),("longitud",int),("continente",str)])

rios = [Rio("Amazonas", 7062, "América del Sur"), Rio("Nilo", 6853, "África"),
        Rio("Yangtsé", 6300, "Asia"), Rio("Misisipi", 6275, "América del Norte"),
        Rio("Amarillo", 5464, "Asia"), Rio("Mekong", 4880, "Asia"),
        Rio("Congo", 4700, "África"), Rio("Danubio", 2850, "Europa")]

# EJERCICIO 1:
def carga_rios()->list[Rio]:
    res = []
    for p in rios:
        nombre = p.nombre
        longitud = int(p.longitud)
        continente = p.continente
        res.append(Rio(nombre, longitud, continente))
    return res

# EJERCICIO 2:
def filtra_rios_de_continente(rios:list[Rio], continente:str)->list[Rio]:
    res = list()
    for p in rios:
        if p.continente == continente:
            res.append(p)
    return res

