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

# EJERCICIO 3:
def obtener_continentes_y_rios(rios:list[Rio])->list[tuple[str,str]]:
    res = []
    for p in rios:
        res.append((p.continente, p.nombre))
    
    return sorted(res, key=lambda x: x[1])

# EJERCICIO 4:
def contar_diferentes_continentes(rios:list[Rio])->int:
    res = 0
    for p in rios:
        if p.longitud >= 6300:
            res += 1
    
    return res

# EJERCICIO 5:
def suma_longitudes(rios:list[Rio], continentes:set[str])->int:
    res = 0
    for p in rios:
        if p.continente in continentes:
            res += p.longitud
    return res

# EJERCICIO 6:
def rio_con_nombre_más_corto(rios:list[Rio], continentes:set[str])->str:
    res = []
    for p in rios:
        if p.continente in continentes:
            res.append(p.nombre)

    return min(res, key=len)

