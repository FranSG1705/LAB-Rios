from rios import *

def test_carga_rios(rios:list[Rio])->None:
    print("\n1. Test_carga_rios")
    longitud = len(rios)
    n = 0
    while n < longitud:
        print(carga_rios()[n])
        n += 1

def test_filtra_rios_de_continente(rios, continente):
    print("\n2. Test_filtra_rios_de_continente")
    print(f'Para el continente {continente} --> {filtra_rios_de_continente(rios, continente)}')

def test_obtener_continentes_y_rios(rios):
    print('\n3. Test_obtener_continentes_y_rios')

    longitud = len(obtener_continentes_y_rios(rios))
    n = 0
    while n < longitud:
        print(obtener_continentes_y_rios(rios)[n])
        n += 1

def test_contar_diferentes_continentes(rios):
    print('\n4. test_contar_diferentes_continentes')
    print(f'Hay {contar_diferentes_continentes(rios)} continentes diferentes con rios de más de 6.300 kms')

def test_suma_longitudes(rios,continentes):
    print('\n5. test_suma_longitudes')
    print(f'La suma de las longitudes de los rios de {continentes} es {suma_longitudes(rios, continentes)}')



if __name__=='__main__':
    rios = carga_rios()
    #test_carga_rios(rios)
    #test_filtra_rios_de_continente(rios, 'Asia')
    #test_obtener_continentes_y_rios(rios)
    #test_contar_diferentes_continentes(rios)
    test_suma_longitudes(rios, {'Asia', 'Europa'})
